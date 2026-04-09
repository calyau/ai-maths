---
concept: Graph Ramsey Number
slug: graph-ramsey-number
category: ramsey-theory
subcategory: graph-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 265
section: "9.2 Ramsey numbers"
extraction_confidence: high
aliases:
  - "R(H)"
  - "R(H_1, H_2)"
prerequisites:
  - ramsey-number
  - ramsey-theorem-finite
related:
  - ramsey-number-bounded-degree
  - ramsey-minimal-graph
answers_questions:
  - "What is the Ramsey number of a graph?"
---

# Quick Definition
The Ramsey number R(H) of a graph H is the least n such that every graph of order n contains H or its complement as a subgraph. R(H_1, H_2) is the least n such that H_1 subset G or H_2 subset G-bar for every G of order n.

# Core Definition
**R(H)**: the least n in N such that H subset G or H subset G-bar for every graph G of order n.
**R(H_1, H_2)**: the least n in N such that H_1 subset G or H_2 subset G-bar for every graph G of order n.

If H has few edges, R(H) should be much smaller than R(K^{|H|}). For trees T of order t: R(T, K^s) = (s-1)(t-1) + 1 (Proposition 9.2.1). (Diestel, pp. 255-256)

# Prerequisites
- **Ramsey number** — Graph Ramsey numbers specialize the general concept
- **Ramsey's theorem (finite)** — R(H) <= R(|H|) since H subset K^{|H|}

# Key Properties
1. R(H) <= R(|H|) for any H
2. For sparse H, R(H) is much smaller than R(|H|)
3. R(T, K^s) = (s-1)(t-1) + 1 for trees T of order t
4. R(H) <= c|H| for bounded-degree H (Theorem 9.2.2)

# Examples
**Example** (Proposition 9.2.1): R(T, K^s) = (s-1)(t-1) + 1 for any tree T of order t. The lower bound uses (s-1) copies of K_{t-1}; the upper bound uses chi and delta arguments.

# Relationships
## Builds Upon
- **Ramsey number** — Specialization to graphs

## Related
- **Ramsey number (bounded degree)** — Linear Ramsey numbers for bounded-degree graphs

# Source Reference
Chapter 9, Section 9.2, pages 255-256 (pdf pages 265-266). Proposition 9.2.1.

# Verification Notes
- Confidence: HIGH — explicitly defined
