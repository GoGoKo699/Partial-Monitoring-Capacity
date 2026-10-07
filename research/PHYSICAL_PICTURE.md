# Collecting loss and choosing how to measure it

**Reading guide, 7 October 2026.** This explains the existing theorem, its algebraic consequences and the exact product-measurement comparison. It adds no implementation claim.

A quantum signal leaks into two places outside the receiver: a field we can collect and a field we cannot access. A helper measures the collected field and sends the receiver a classical record. The question is how much unknown quantum information can be transmitted reliably when some loss is still hidden.

**The best predetermined individual measurements can still leave capacity unused.** In the positive-rate qubit regime with both kinds of loss present, photon counting maximizes the rate over every helper POVM applied separately to each collected output according to a schedule fixed in advance. Allowing unrestricted joint helper measurements can nevertheless increase the rate. The helper-to-receiver message remains classical in both cases.

## Collecting enough loss makes transmission possible

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

## A better individual detector cannot close the example's rate gap

For the same qubit split, [the exact product-capacity proof](EXACT_PRODUCT_CAPACITY_2026-10-07.md) optimizes over all predetermined product helper POVMs and all inputs, including coherent inputs. Photon counting attains that maximum. The sender and receiver may use arbitrary block codes in both rows below.

| Helper measurement resource | Capacity, qubits/use |
|---|---:|
| Best predetermined product measurements, attained by counting | $0.18621044$ |
| Unrestricted collective measurements | $0.30570954$ |

The exact difference is certified at about $0.11949910$ qubits/use. Counting already reaches the positive-capacity boundary $a>b$; the additional collective benefit demonstrated here is a higher rate. No choice of a better predetermined single-use detector closes this example's gap. The approximately 64% increase illustrates that comparison; the theorem's content is optimization over the entire stated product class.

The product class includes every single-use POVM and schedules fixed in advance. It excludes measurements chosen adaptively from earlier helper outcomes and general separable block POVMs. Thus this result does not establish that coherent helper memory is necessary against all local strategies. Counting optimality is global after input optimization, rather than a claim for each fixed coherent input. No efficient measurement attaining the unrestricted optimum is supplied, and product optimality has not been established for the optical model.

## Inaccessible optical loss also imposes an energy ceiling

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

The general result applies when the receiver can simulate the inaccessible output while preserving every correlation with the helper. That **joint-register** requirement is stronger than reproducing the inaccessible marginal alone. It gives two upper bounds for the same input: $S(B)-S(E)$, which remains valid after classical helper assistance, and $S(BD)-S(E)$, obtained by hypothetically giving the receiver the collected field coherently. Both finite-dimensional cuts follow from the established degradable-state distillation theorem after regrouping registers. A known assistance construction attains their minimum asymptotically. The exact capacity is a consequence of these ingredients under the stated resource condition; [the dependency record](PROOF_DEPENDENCIES.md) gives the reduction.

The unrestricted helper resources include quantum storage, phase references and arbitrary joint measurements. The separate product-optimality proof bounds every single-use measurement and coherent input by the counting capacity. These two proofs give both sides of the qubit rate comparison above. The numerical certificate encloses the resulting scalar values; it does not prove either operational capacity theorem.

Environment-assisted communication, partial environmental access and collective assistance gains have established predecessors. The contribution here combines a capacity consequence of known converse and assistance results with a separate exact product benchmark. Read [the model](MODEL_AND_CLAIMS.md) for resources and claim IDs, [the theorem](THEOREM.md) for the unrestricted capacity, [the exact product proof](EXACT_PRODUCT_CAPACITY_2026-10-07.md) for the measurement comparison, and [the contribution assessment](CONTRIBUTION_ASSESSMENT_2026-10-07.md) for the closest precedents and significance limits. Independent scrutiny and exhaustive priority remain open.
