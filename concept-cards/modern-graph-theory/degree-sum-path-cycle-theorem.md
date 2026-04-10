---
concept: Degree-Sum Path and Cycle Theorem
slug: degree-sum-path-cycle-theorem
category: extremal-graph-theory
subcategory: hamilton-theory
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
  - "Theorem 2"
  - "Pósa-Dirac theorem"
prerequisites:
  - girth
  - circumference
extends: []
related:
  - diracs-theorem
  - hamilton-cycle
contrasts_with: []
answers_questions:
  - "How many edges guarantee a long path or cycle?"
---

# Quick Definition
If every pair of nonadjacent vertices in a connected graph of order $n \ge 3$ satisfies $d(x) + d(y) \ge k$, then: if $k = n$, $G$ is Hamiltonian; if $k < n$, $G$ has a path of length $k$ and a cycle of length at least $(k+2)/2$.

# Core Definition
**Theorem 2**: Let $G$ be a connected graph of order $n \ge 3$ such that $d(x) + d(y) \ge k$ for any two nonadjacent vertices. If $k = n$ then $G$ is Hamiltonian, and if $k < n$ then $G$ contains a path of length $k$ and a cycle of length at least $(k+2)/2$ (Bollobás, pp. 113-114).

# Prerequisites
- **Girth** and **Circumference** — Related cycle parameters

# Key Properties
1. Contains Dirac's theorem as the special case $k = n$
2. The path bound $k$ is tight: graphs with max path length $k$ exist
3. The cycle bound $(k+2)/2$ comes from the larger-degree endpoint of a longest path
4. The proof uses the "rotation" argument: neighbors of endpoints on longest paths

# Construction / Recognition
1. Check $d(x) + d(y) \ge k$ for all nonadjacent pairs
2. If $k = n$: graph is Hamiltonian
3. If $k < n$: find path of length $\ge k$ and cycle of length $\ge (k+2)/2$

# Context & Application
This theorem unifies several results about long paths and cycles. The degree-sum condition is weaker than requiring high minimum degree.

# Examples
**Example** (p. 114, Fig. IV.2): The proof constructs a cycle of length $\ell$ from a longest path by connecting $x_\ell$ to $x_i$ where $x_1$ is adjacent to $x_{i+1}$.

# Relationships
## Enables
- **diracs-theorem** — Special case $k = n$
- **extremal-bound-for-paths** — Theorem 3

# Source Reference
Chapter IV, Section IV.1, pages 113-115. Theorem 2.

# Verification Notes
- Definition source: Direct theorem statement from pp. 113-114
- Confidence rationale: Major theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
