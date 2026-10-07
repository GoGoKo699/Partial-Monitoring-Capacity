# How much loss can remain unobserved?

**Reading guide, 7 October 2026.** This explains the existing theorem, its algebraic consequences and the subsequent product-measurement separation. It adds no implementation claim.

A quantum signal leaks into two places outside the receiver: a field we can collect and a field we cannot access. A helper measures the collected field and sends the receiver a classical record. The question is how much unknown quantum information can be transmitted reliably when some loss is still hidden.

For the qubit-decay and vacuum optical models here, **the receiver must receive more than the environment permanently hides**. Write the received, unobserved and collected fractions as $a,b,c$, with $a+b+c=1$. At positive optical signal-energy budget, the exact positive-capacity boundary is

```math
a>b.
```

The receiver can therefore receive less than half the original signal and still transmit quantum information with assistance. At fixed $a$, collecting more of the existing loss reduces $b$ and increases $c$; it does not increase the fraction sent directly to the receiver.

## One physical example

Use the existing split $(a,b,c)=(0.2,0.08,0.72)$:

| Destination | Fraction of incident signal | Available resource |
|---|---:|---|
| Receiver $B$ | 20% | Quantum output |
| Inaccessible environment $E$ | 8% | No access |
| Helper $D$ | 72% | Quantum processing, followed by a classical message to the receiver |

The helper collects 90% of the field lost by the receiver. Without its record the receiver's channel has zero quantum capacity; with the stipulated assistance it has positive capacity. These are asymptotic coding statements, not the probability of recovering one lost photon.

In optics, an average incident budget of one photon per mode gives about $0.369$ qubits per mode for this split. The exact rate is

```math
Q(N)=g(aN)-g(bN),\qquad
g(x)=(x+1)\log_2(x+1)-x\log_2x,
```

on the positive side $a>b$. At fixed $0<b<a$, increasing signal energy approaches the ceiling

```math
\lim_{N\to\infty}Q(N)=\log_2(a/b).
```

Here that ceiling is $\log_2(2.5)\simeq1.322$ qubits per mode. Additional signal power cannot remove it. Better collection can: lowering $b$ raises the ceiling, and at $b=0$ the rate $g(aN)$ is unbounded as $N$ grows for $a>0$. The input constraint counts average incident signal photons, not the helper's apparatus energy.

## Collection and signal power are different resources

Let $\eta$ be the fraction of the lost field collected by the helper, so $b=(1-\eta)(1-a)$. For $0<a<1/2$, the positive-rate condition becomes

```math
\eta>1-\frac{a}{1-a}.
```

More quantitatively, for $0<a<1$ and a target optical rate $R>0$, that target is attainable at some finite signal-energy budget with the theorem's ideal resources exactly when

```math
b<a\,2^{-R}
\quad\Longleftrightarrow\quad
\eta>1-\frac{a}{2^R(1-a)}.
```

This follows directly from the continuous increasing rate and its ceiling. When $b>0$, equality only approaches $R$ at infinite energy. At $b=0$, every finite target is reachable with some finite energy. For $a=0.2$, positivity requires collection above 75%, while one qubit per mode requires collection above 87.5%. These conditions permit choosing the energy; they do not guarantee the target at a prescribed budget or specify a realizable detector. In the high-loss limit, the uncollected fraction must shrink proportionally to survival to maintain a fixed target. This is an interpretation of the existing law, not a separate novelty claim.

## Why the theorem can make an exact statement

The general result applies when the receiver can simulate the inaccessible output while preserving every correlation with the helper. That **joint-register** requirement is stronger than reproducing the inaccessible marginal alone. It gives two upper bounds for the same input: $S(B)-S(E)$, which remains valid after classical helper assistance, and $S(BD)-S(E)$, obtained by hypothetically giving the receiver the collected field coherently. A known assistance construction attains their minimum asymptotically. The proposed contribution is the matching converse and resulting exact optimization under this condition.

The helper resources include quantum storage, phase references and arbitrary joint measurements. Photon counting reaches the positive-rate boundary in the qubit example but gives about $0.1862$ qubits per use, below the unrestricted value $0.3057$. That comparison alone does not bound other single-use measurements.

[A separate analytical proof](PRODUCT_HELPER_GAP_2026-10-07.md) now shows a strict gap for **every predetermined product helper POVM**, even when the sender and receiver use arbitrary block codes. Measuring each collected output separately according to a schedule fixed in advance cannot approach the unrestricted optimum. The proof does not give the gap's size or settle measurements chosen adaptively from earlier outcomes. Collective gains in assistance have known precedents; the result here includes residual inaccessible loss and optimizes the entire stated product class. No efficient measurement attaining the general optimum is supplied.

Environment-assisted communication, partial environmental access and the assistance lower bound have established predecessors. Read [the model](MODEL_AND_CLAIMS.md) for exact resources, [the theorem](THEOREM.md) for the proof and evaluations, and [the targeted comparison](../literature/PRIORITY_CHECK_2026-10-07.md) for the inherited ingredients and precise proposed contribution. Independent scrutiny and exhaustive priority remain open.
