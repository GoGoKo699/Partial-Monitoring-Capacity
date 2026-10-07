#!/usr/bin/env python3
"""Certify the fixed-example product capacity using exact rational arithmetic.

The analytical product-optimality proof is a separate dependency.  This script
certifies the resulting scalar counting optimization, the unrestricted rate,
and their difference.  No floating-point computation is a correctness premise.
It neither reads nor refreshes the protected scientific reference reports.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path


SERIES_TERMS = 40
DECIMAL_PLACES = 20
A = Fraction(1, 5)
B = Fraction(2, 25)
C = Fraction(18, 25)
Q_LO = Fraction(5583443480550842, 10**16)
Q_HI = Fraction(5583443480550843, 10**16)


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("Reversed interval")

    def __add__(self, other: Interval) -> Interval:
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def __sub__(self, other: Interval) -> Interval:
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, coefficient: Fraction) -> Interval:
        if coefficient >= 0:
            return Interval(coefficient * self.lower, coefficient * self.upper)
        return Interval(coefficient * self.upper, coefficient * self.lower)

    def shift(self, offset: int) -> Interval:
        return Interval(self.lower + offset, self.upper + offset)


def ln_reduced_bounds(value: Fraction) -> Interval:
    """Enclose ln(value) for 1 <= value <= 2 using a positive series.

    For t=(value-1)/(value+1), retain terms n=0,...,m-1 in
    ln(value)=2 sum t**(2*n+1)/(2*n+1).  The omitted tail is between
    zero and 2*t**(2*m+1)/((2*m+1)*(1-t*t)).
    """
    if not Fraction(1) <= value <= Fraction(2):
        raise ValueError("Logarithm argument was not range-reduced")
    t = (value - 1) / (value + 1)
    t_squared = t * t
    power = t
    partial = Fraction(0)
    for index in range(SERIES_TERMS):
        partial += power / (2 * index + 1)
        power *= t_squared
    lower = 2 * partial
    remainder = 2 * power / ((2 * SERIES_TERMS + 1) * (1 - t_squared))
    return Interval(lower, lower + remainder)


LN_TWO = ln_reduced_bounds(Fraction(2))


def log2_bounds(value: Fraction) -> Interval:
    """Enclose a binary logarithm using exact powers-of-two reduction."""
    if value <= 0:
        raise ValueError("Logarithms require a positive argument")
    exponent = 0
    reduced = value
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    numerator = ln_reduced_bounds(reduced)
    # Both numerator endpoints are nonnegative; both denominator endpoints
    # are positive.  These divisions therefore give outward rational bounds.
    return Interval(
        numerator.lower / LN_TWO.upper,
        numerator.upper / LN_TWO.lower,
    ).shift(exponent)


def binary_entropy_bounds(probability: Fraction) -> Interval:
    if not 0 <= probability <= 1:
        raise ValueError("Entropy argument must be a probability")
    if probability in (0, 1):
        return Interval(Fraction(0), Fraction(0))
    return log2_bounds(probability).scale(-probability) + log2_bounds(
        1 - probability
    ).scale(probability - 1)


def counting_rate_bounds(q: Fraction) -> Interval:
    """F(q), with the common detected-jump entropy term cancelled."""
    u = 1 - (1 - B) * q
    v = 1 - (1 - A) * q
    return (
        log2_bounds(u).scale(-u)
        + log2_bounds(A * q).scale(-A * q)
        + log2_bounds(v).scale(v)
        + log2_bounds(B * q).scale(B * q)
    )


def counting_derivative_bounds(q: Fraction) -> Interval:
    u = 1 - (1 - B) * q
    v = 1 - (1 - A) * q
    return (
        log2_bounds(u).scale(1 - B)
        + log2_bounds(v).scale(-(1 - A))
        + log2_bounds(A * q).scale(-A)
        + log2_bounds(B * q).scale(B)
    )


def derivative_sign(q: Fraction) -> int:
    """Exact sign of F'(q), after exponentiating 25*F'(q).

    F'(q)>0 iff 20*(1-23*q/25)**23 > q**3*(1-4*q/5)**20.
    All factors removed in obtaining this comparison are strictly positive.
    """
    if not 0 < q < 1:
        raise ValueError("Derivative sign is used only in the open unit interval")
    polynomial = 20 * (1 - Fraction(23, 25) * q) ** 23 - q**3 * (
        1 - Fraction(4, 5) * q
    ) ** 20
    return (polynomial > 0) - (polynomial < 0)


def outward_decimal(value: Fraction, *, upward: bool) -> str:
    """Round a rational outward to a fixed decimal grid, without floats."""
    scale = 10**DECIMAL_PLACES
    numerator = value.numerator * scale
    denominator = value.denominator
    integer = (
        -((-numerator) // denominator)
        if upward
        else numerator // denominator
    )
    sign = "-" if integer < 0 else ""
    integer = abs(integer)
    whole, fractional = divmod(integer, scale)
    return f"{sign}{whole}.{fractional:0{DECIMAL_PLACES}d}"


def display_interval(interval: Interval) -> dict[str, str]:
    return {
        "lower": outward_decimal(interval.lower, upward=False),
        "upper": outward_decimal(interval.upper, upward=True),
    }


def certificate() -> dict[str, object]:
    if not (A > B > 0 and C > 0 and A + B + C == 1):
        raise ArithmeticError("The fixed channel assumptions failed")
    if not 0 < Q_LO < Q_HI < 1:
        raise ArithmeticError("Invalid root bracket")
    signs = [derivative_sign(Q_LO), derivative_sign(Q_HI)]
    if signs != [1, -1]:
        raise ArithmeticError("The exact derivative signs do not bracket the root")

    at_lower = counting_rate_bounds(Q_LO)
    derivative = counting_derivative_bounds(Q_LO)
    if derivative.lower <= 0:
        raise ArithmeticError("The logarithm enclosure did not resolve F'(q_lo)>0")
    # F''(q)<0 throughout (0,1), so the root is the unique maximum.  Its
    # value lies above F(q_lo) and below the tangent there evaluated at q_hi.
    tangent_at_upper = at_lower + derivative.scale(Q_HI - Q_LO)
    product = Interval(at_lower.lower, tangent_at_upper.upper)
    collective = binary_entropy_bounds(Fraction(5, 28)) - binary_entropy_bounds(
        Fraction(1, 14)
    )
    gap = collective - product
    checks = {
        "root_bracket_has_exact_opposite_derivative_signs": signs == [1, -1],
        "lower_endpoint_derivative_interval_is_positive": derivative.lower > 0,
        "product_rate_lower_bound_is_positive": product.lower > 0,
        "product_rate_upper_bound_is_below_collective_lower_bound": (
            product.upper < collective.lower
        ),
        "gap_lower_bound_is_positive": gap.lower > 0,
    }
    if not all(checks.values()):
        raise ArithmeticError("A rational certificate inequality failed")

    return {
        "status": "PASS",
        "example": {"a": str(A), "b": str(B), "c": str(C)},
        "scope": (
            "Exact rational evaluation of the scalar counting capacity, "
            "the unrestricted capacity, and their gap for this fixed example."
        ),
        "analytical_dependency": (
            "The separate analytical theorem proves Q_prod=max_q F(q) for all "
            "predetermined product helper POVMs, arbitrary input coherences, "
            "and sender/receiver block codes. This script does not prove that "
            "POVM reduction or extend it to adaptive helper strategies."
        ),
        "scalar_proof": {
            "objective": (
                "F(q)=(1-c*q)*[h2(a*q/(1-c*q))-h2(b*q/(1-c*q))]"
            ),
            "second_derivative": (
                "F''(q)=-(a-b)/[ln(2)*q*(1-(1-b)*q)*(1-(1-a)*q)]<0 "
                "for 0<q<1; F(0)=F(1)=0."
            ),
            "maximum_lower_bound": "F(q_lo)",
            "maximum_upper_bound": "F(q_lo)+(q_hi-q_lo)*F'(q_lo)",
            "collective_rate": "h2(5/28)-h2(1/14)",
        },
        "optimizer_bracket": {"lower": str(Q_LO), "upper": str(Q_HI)},
        "exact_derivative_signs": {
            "lower": signs[0],
            "upper": signs[1],
            "comparison": (
                "sign[20*(1-23*q/25)^23-q^3*(1-4*q/5)^20]"
            ),
        },
        "product_capacity_bits_per_use": display_interval(product),
        "collective_capacity_bits_per_use": display_interval(collective),
        "collective_minus_product_bits_per_use": display_interval(gap),
        "arithmetic": {
            "type": "Python standard-library Fraction; integer/rational only",
            "logarithm_range_reduction": "x=2^k*y with 1<=y<2",
            "series_parameter": "t=(y-1)/(y+1), so 0<=t<1/3",
            "ln2_parameter": "t=1/3",
            "retained_terms": SERIES_TERMS,
            "ln_lower_bound": "2*sum(t^(2*n+1)/(2*n+1), n=0,...,m-1)",
            "ln_tail_upper_bound": "2*t^(2*m+1)/[(2*m+1)*(1-t^2)]",
            "display_rounding": "lower=floor, upper=ceiling on the decimal grid",
            "display_decimal_places": DECIMAL_PLACES,
        },
        "checks": checks,
        "certificate_source_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional JSON destination, created exclusively; existing files fail.",
    )
    args = parser.parse_args()
    result = json.dumps(certificate(), indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(result)
    print(result, end="")


if __name__ == "__main__":
    main()
