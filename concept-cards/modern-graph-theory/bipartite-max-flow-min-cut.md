---
concept: Bipartite Max-Flow Min-Cut Theorem
slug: bipartite-max-flow-min-cut
category: matchings
subcategory: fundamental-theorems
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "Theorem 12"
prerequisites:
  - halls-theorem
  - max-flow-min-cut-theorem
extends:
  - halls-theorem
  - max-flow-min-cut-theorem
related:
  - deficiency-version-halls-theorem
contrasts_with: []
answers_questions:
  - "What is the most general form of matching in bipartite graphs?"
---

# Quick Definition
A general theorem on bipartite graphs with degree bounds on both vertex classes, giving necessary and sufficient conditions for a subgraph with prescribed degree constraints to exist.

# Core Definition
**Theorem 12**: Let $G = G_2(m,n)$ be a bipartite graph with vertex classes $V_1 = \{x_1, \ldots, x_m\}$ and $V_2 = \{y_1, \ldots, y_n\}$. Given natural numbers $d_1, \ldots, d_m$ and $e_1, \ldots, e_n$ and $d \ge 0$, there exists a subgraph $H$ with $e(H) \ge \sum d_i - d$, $d_H(x_i) \le d_i$, and $d_H(y_j) \le e_j$ iff for every $S \subset V_1$: $\sum_{x_i \in S} d_i \le \sum_{j=1}^n \min\{S_j, e_j\} + d$, where $S_j$ counts edges from $y_j$ to $S$ (Bollobás, p. 88).

# Prerequisites
- **Hall's theorem** — Special case of this theorem
- **Max-flow min-cut theorem** — The proof uses it

# Key Properties
1. Generalizes Hall's theorem, Corollaries 9-11
2. The condition is both necessary and sufficient
3. Proved via the max-flow min-cut theorem with vertex capacities

# Construction / Recognition
1. Construct directed graph: edges from $V_1$ to $V_2$ with edge capacity 1
2. Give vertex $x_i$ capacity $d_i$ and vertex $y_j$ capacity $e_j$
3. Apply max-flow min-cut to determine feasibility

# Context & Application
This is the most general bipartite matching theorem in the chapter, subsuming all previous matching results as special cases.

# Examples
**Example** (p. 88): Setting all $d_i = 1$, $e_j = 1$, and $d = 0$ recovers Hall's theorem.

# Relationships
## Builds Upon
- **halls-theorem** — Generalized
- **max-flow-min-cut-theorem** — Used in proof

# Source Reference
Chapter III, Section III.3, pages 88-89. Theorem 12.

# Verification Notes
- Definition source: Direct from pp. 88-89
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
