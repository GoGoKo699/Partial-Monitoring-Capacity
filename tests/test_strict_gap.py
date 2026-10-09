"""Finite safeguards for the analytical strict-gap corollary, not its proof."""
import unittest

import mpmath as mp


def phi(t):
    return mp.mpf(0) if t == 0 else t * mp.log(t, 2)


def entropy(t):
    return -phi(t) - phi(1 - t)


def objectives(a, b, q):
    c = 1 - a - b
    weight = 1 - c * q
    product = weight * (entropy(a * q / weight) - entropy(b * q / weight))
    return entropy(a * q) - entropy(b * q), entropy((1 - b) * q) - entropy(b * q), product


def mixed_difference(x, y, z):
    return phi(x + y + z) - phi(x + y) - phi(x + z) + phi(x)


class StrictGapChecks(unittest.TestCase):
    def assert_close(self, actual, expected):
        self.assertTrue(
            mp.almosteq(actual, expected, rel_eps=mp.mpf("1e-45"), abs_eps=mp.mpf("1e-110")),
            f"{mp.nstr(actual, 60)} != {mp.nstr(expected, 60)}",
        )

    def test_entropy_identities_and_gap_bounds(self):
        # Decimal construction avoids importing binary float errors. The tiny
        # parameters make double precision unsuitable for these subtractions.
        with mp.workdps(120):
            tiny = mp.mpf("1e-30")
            cases = [
                ("certificate split", mp.mpf(".2"), mp.mpf(".08"), mp.mpf(".5583443480550842")),
                ("first cut", mp.mpf(".6"), mp.mpf(".1"), mp.mpf(".25")),
                ("second cut", mp.mpf(".6"), mp.mpf(".1"), mp.mpf(".9")),
                ("small collection", mp.mpf(".6"), mp.mpf(".4") - tiny, mp.mpf(".37")),
                ("nearly equal fractions", mp.mpf(".2") + tiny, mp.mpf(".2"), mp.mpf(".37")),
                ("small inaccessible fraction", mp.mpf(".3"), tiny, mp.mpf(".61")),
                ("near vacuum input", mp.mpf(".2"), mp.mpf(".08"), tiny),
                ("near excited input", mp.mpf(".2"), mp.mpf(".08"), 1 - tiny),
            ]
            for name, a, b, q in cases:
                with self.subTest(case=name):
                    c = 1 - a - b
                    self.assertTrue(a > b > 0 and c > 0 and 0 < q < 1)
                    d1, d2, product = objectives(a, b, q)
                    triples = ((1 - (1 - b) * q, (a - b) * q, c * q),
                               (a * q, 1 - q, c * q))
                    for direct, (x, y, z) in zip((d1 - product, d2 - product), triples):
                        self.assertTrue(x > 0 and y > 0 and z > 0)
                        self.assert_close(x + y + z, 1 - b * q)
                        self.assert_close(direct, mixed_difference(x, y, z))
                        self.assertGreater(direct, 0)
                        self.assertGreaterEqual(direct, y * z / ((x + y + z) * mp.log(2)))
                    bound = c * q * min((a - b) * q, 1 - q) / ((1 - b * q) * mp.log(2))
                    self.assertGreater(bound, 0)
                    self.assertGreaterEqual(min(d1, d2) - product, bound)

    def test_concavity_and_common_product_optimum(self):
        with mp.workdps(120):
            a, b = mp.mpf(".2"), mp.mpf(".08")
            product = lambda q: objectives(a, b, q)[2]
            for q in map(mp.mpf, (".1", ".5", ".9")):
                with self.subTest(q=str(q)):
                    second = -(a - b) / (mp.log(2) * q * (1 - (1 - b) * q) * (1 - (1 - a) * q))
                    self.assert_close(mp.diff(product, q, 2), second)
                    self.assertLess(second, 0)
            q_star = mp.findroot(lambda q: mp.diff(product, q), (mp.mpf(".5"), mp.mpf(".6")))
            self.assertTrue(mp.mpf(".5583443480550842") < q_star < mp.mpf(".5583443480550843"))
            d1, d2, optimum = objectives(a, b, q_star)
            self.assertGreater(optimum, 0)
            self.assertGreater(min(d1, d2), optimum)
            c = 1 - a - b
            bound = c * q_star * min((a - b) * q_star, 1 - q_star) / ((1 - b * q_star) * mp.log(2))
            self.assertGreaterEqual(min(d1, d2) - optimum, bound)

    def test_boundary_consistency(self):
        with mp.workdps(120):
            for q in map(mp.mpf, ("0", ".37", "1")):
                with self.subTest(boundary="no collection", q=str(q)):
                    d1, d2, product = objectives(mp.mpf(".7"), mp.mpf(".3"), q)
                    self.assert_close(d1, product)
                    self.assert_close(d2, product)
                with self.subTest(boundary="equal fractions", q=str(q)):
                    d1, d2, product = objectives(mp.mpf(".2"), mp.mpf(".2"), q)
                    self.assert_close(product, 0)
                    self.assert_close(min(d1, d2), 0)
            for q in (mp.mpf(0), mp.mpf(1)):
                with self.subTest(boundary="pure input", q=str(q)):
                    d1, d2, product = objectives(mp.mpf(".2"), mp.mpf(".08"), q)
                    self.assert_close(product, 0)
                    self.assert_close(min(d1, d2), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
