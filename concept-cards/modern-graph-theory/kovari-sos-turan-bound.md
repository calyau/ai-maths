---
concept: "Kővári-Sós-Turán Bound"
slug: kovari-sos-turan-bound
category: extremal-graph-theory
subcategory: bipartite-extremal
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: high
aliases:
  - "Theorem 10"
  - "Lemma 9"
  - "double counting bound"
prerequisites:
  - zarankiewicz-problem
extends: []
related:
  - turans-theorem
contrasts_with: []
answers_questions:
  - "What is the best upper bound for the Zarankiewicz function?"
---

# Quick Definition
$z(m,n;s,t) \le (s-1)^{1/t}(n-t+1)m^{1-1/t} + (t-1)m$, bounding the maximum edges in a $K_{s,t}$-free bipartite graph.

# Core Definition
**Theorem 10**: For all natural numbers $m,n,s,t$: $z(m,n;s,t) \le (s-1)^{1/t}(n-t+1)m^{1-1/t} + (t-1)m$. The proof uses the double counting lemma (Lemma 9): count $t$-sets in $V_2$ covered by vertices of $V_1$ using convexity of $\binom{u}{t}$ (Bollobás, pp. 122-123).

# Prerequisites
- **Zarankiewicz problem** — The problem being bounded

# Key Properties
1. Proved via double counting and convexity
2. For $t = 2$: $z(n,n;s,2) \le \frac{n}{2}(1+\sqrt{4(s-1)(n-1)+1})$
3. Best possible for $K_{2,2} = C_4$ (Theorem 12) and $K_{3,3}$
4. Applies to general graphs via the duplication trick (Theorem 11)

# Construction / Recognition
1. Each $t$-set of $V_2$ is covered by at most $s-1$ vertices
2. Sum $\binom{d(x)}{t}$ over $x \in V_1$, apply convexity
3. Get the upper bound

# Context & Application
The double counting argument is "perhaps the most basic combinatorial argument" (p. 122). It is the fundamental technique for bipartite Turán problems.

# Examples
**Example** (p. 123): For $s = t = 2$: $z(n,n;2,2) \le \frac{n}{2}(1+\sqrt{4n-3})$, tight for $n = q^2+q+1$.

# Relationships
## Builds Upon
- **zarankiewicz-problem** — The problem being bounded

## Related
- **turans-theorem** — Analogous technique for non-bipartite case

# Source Reference
Chapter IV, Section IV.2, pages 122-123. Lemma 9, Theorem 10.

# Verification Notes
- Definition source: Direct from pp. 122-123
- Confidence rationale: Explicitly proved
- Uncertainties: None
- Cross-reference status: Verified
