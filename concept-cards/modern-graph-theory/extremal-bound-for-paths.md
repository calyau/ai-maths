---
concept: Extremal Bound for Paths
slug: extremal-bound-for-paths
category: extremal-graph-theory
subcategory: forbidden-subgraphs
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.1 Paths and Cycles"
extraction_confidence: high
aliases:
  - "Theorem 3"
  - "ex(n; P_ℓ)"
prerequisites:
  - extremal-function
  - degree-sum-path-cycle-theorem
extends: []
related:
  - extremal-bound-for-cycles
contrasts_with: []
answers_questions:
  - "How many edges guarantee a path of given length?"
---

# Quick Definition
A graph of order $n$ without a path of length $k$ has at most $(k-1)n/2$ edges, with equality iff all components are $K_k$.

# Core Definition
**Theorem 3**: Let $G$ be a graph of order $n$ without a path of length $k \ge 1$. Then $e(G) \le \frac{k-1}{2}n$. Equality holds iff all components of $G$ are complete graphs of order $k$ (Bollobás, p. 115).

# Prerequisites
- **Extremal function** — This determines $ex(n; P_k)$
- **Degree-sum path and cycle theorem** — Used in the proof

# Key Properties
1. $ex(n; P_k) = (k-1)n/2$ (when $k | n$)
2. Extremal graphs are disjoint unions of $K_k$
3. Proof uses induction on $n$ and Theorem 2

# Construction / Recognition
1. Check that $G$ has no path of length $k$
2. Count edges; at most $(k-1)n/2$
3. Equality iff $G = (n/k) \cdot K_k$

# Context & Application
One of the cleanest forbidden subgraph results: the extremal function for paths is linear in $n$.

# Examples
**Example** (p. 115): If $G$ is connected with no $K_k$, Theorem 2 gives a vertex of degree $\le (k-1)/2$, and induction completes the argument.

# Relationships
## Builds Upon
- **degree-sum-path-cycle-theorem** — Key tool in the proof
- **extremal-function** — This computes $ex(n; P_k)$

## Related
- **extremal-bound-for-cycles** — Theorem 4

# Source Reference
Chapter IV, Section IV.1, page 115. Theorem 3.

# Verification Notes
- Definition source: Direct from p. 115
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
