---
concept: "Halin's Theorem on Thick Ends"
slug: halins-theorem
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 218
section: "8.2 Paths, trees, and ends"
extraction_confidence: high
aliases:
  - "Halin 1965"
  - "hexagonal grid theorem"
prerequisites:
  - end-degree
  - end-of-a-graph
extends: []
related:
  - grid-theorem
contrasts_with: []
answers_questions:
  - "What structure do thick ends force?"
---

# Quick Definition
Halin's theorem (1965) states that whenever a graph contains a thick end (one with infinitely many disjoint rays), it has a subdivision of the hexagonal quarter grid whose rays belong to that end.

# Core Definition
**Theorem 8.2.6** (Halin 1965): Whenever a graph contains a thick end, it has a TH^infinity subgraph (subdivision of the hexagonal quarter grid) whose rays belong to that end (Diestel, p. 218).

# Prerequisites
- **End degree** — Thick ends have infinite vertex-degree
- **End of a graph** — The structural setting

# Key Properties
1. The hexagonal quarter grid H^infinity is used instead of the N x N grid for technical convenience
2. The N x N grid is a minor of H^infinity and vice versa
3. The proof constructs rays Q_n and path systems P_n(Q_i) simultaneously
4. This is a kind of infinite analogue of the grid theorem

# Relationships
## Related
- **Grid theorem** — The finite analogue

# Source Reference
Chapter 8, Section 8.2, pages 218-222 (Theorem 8.2.6).

# Verification Notes
- Statement from p. 218
- Confidence: HIGH — named theorem with full proof
