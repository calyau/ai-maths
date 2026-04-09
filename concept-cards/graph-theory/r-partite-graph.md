---
concept: r-Partite Graph
slug: r-partite-graph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 26
section: "1.6 Bipartite graphs"

extraction_confidence: high

aliases:
  - "multipartite graph"

prerequisites:
  - graph
  - bipartite-graph
extends:
  - graph
related:
  - complete-multipartite-graph
contrasts_with: []

answers_questions:
  - "What is an r-partite graph?"
---

# Quick Definition
A graph is r-partite if its vertex set can be partitioned into r classes such that every edge connects vertices from different classes.

# Core Definition
Let r >= 2 be an integer. A graph G = (V, E) is called r-partite if V admits a partition into r classes such that every edge has its ends in different classes: vertices in the same partition class must not be adjacent (Diestel, p. 17).

# Prerequisites
- **Graph** — r-partiteness is a graph property
- **Bipartite graph** — the case r = 2

# Key Properties
1. 2-partite = bipartite
2. An r-partite graph is also (r+1)-partite (add an empty class)
3. Each partition class is an independent set

# Relationships
## Builds Upon
- **graph**

## Related
- **bipartite-graph** — the case r = 2
- **complete-multipartite-graph** — all possible edges between different classes

# Source Reference
Chapter 1: The Basics, Section 1.6, page 17 (pdf p. 27).

# Verification Notes
- Direct from p. 17
- Confidence: HIGH
