---
concept: Greedy Clique-Finding Algorithm
slug: greedy-clique-finding
category: extremal-graph-theory
subcategory: algorithms
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
  - "Theorem 6"
prerequisites:
  - turan-graph
  - turan-number
extends: []
related:
  - turans-theorem
contrasts_with: []
answers_questions:
  - "How do you find a complete subgraph algorithmically?"
---

# Quick Definition
Given a graph with at least $t_r(n)$ edges, repeatedly picking a vertex of maximum degree and restricting to its neighbourhood either finds $K_{r+1}$ or shows the graph is $T_r(n)$.

# Core Definition
**Theorem 6**: Let $G$ have $n$ vertices and at least $t_r(n)$ edges. Pick $x_1$ of max degree in $G_1 = G$, then $x_2$ of max degree in $G_2 = G_1[\Gamma(x_1)]$, and so on. Either $G \cong T_r(n)$, or the procedure finds $x_1, \ldots, x_{r+1}$ spanning a $K_{r+1}$ (Bollobás, pp. 117-118).

# Prerequisites
- **Turán graph** — The only graph where the algorithm terminates without finding $K_{r+1}$
- **Turán number** — The edge threshold

# Key Properties
1. The algorithm is greedy: always picks max degree
2. Proof uses induction on $r$ and Theorem 5
3. If $e(G_2) > t_{r-1}(n-k)$, the induction applies; otherwise $G \cong T_r(n)$

# Construction / Recognition
1. Pick vertex $x_1$ of maximum degree in $G$
2. Restrict to $G[\Gamma(x_1)]$, pick $x_2$ of max degree
3. Repeat; stop when isolated vertex found
4. If $r+1$ vertices found: they form $K_{r+1}$

# Context & Application
This provides a constructive proof of Turán's theorem and gives an efficient algorithm.

# Examples
**Example** (p. 118): For $r = 2$, pick max degree vertex $x_1$, then in $\Gamma(x_1)$ pick max degree $x_2$; if they share a neighbour $x_3$, we have $K_3$.

# Relationships
## Builds Upon
- **turan-graph** — The extremal case

## Enables
- **turans-theorem** — Proved constructively

# Source Reference
Chapter IV, Section IV.2, pages 117-118. Theorem 6.

# Verification Notes
- Definition source: Direct from pp. 117-118
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
