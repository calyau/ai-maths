---
concept: c-Colouring (Ramsey)
slug: c-colouring
category: ramsey-theory
subcategory: classical-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 263
section: "9.1 Ramsey's original theorems"
extraction_confidence: high
aliases:
  - "partition into colours"
  - "edge colouring (Ramsey)"
prerequisites:
  - graph
  - edge
related:
  - monochromatic-subgraph
  - ramsey-theorem-finite
contrasts_with: []
answers_questions:
  - "What does colouring mean in Ramsey theory?"
---

# Quick Definition
In Ramsey theory, a c-colouring of a set X (or its k-subsets) is a partition of X (or [X]^k) into c classes (colours), without any adjacency constraints.

# Core Definition
A **c-colouring** of (the elements of) a set X with c colours is simply a partition of X into c classes (indexed by the "colours"). In particular, these colourings need not satisfy any non-adjacency requirements as in Chapter 5 (chromatic colouring). Given a c-colouring of [X]^k, the set of all k-subsets of X, a set Y subset X is called monochromatic if all elements of [Y]^k have the same colour. (Diestel, p. 253)

# Prerequisites
- **Graph**, **Edge** — Colourings are often applied to edges of graphs

# Key Properties
1. No adjacency constraint: any partition of edges into c classes is a c-colouring
2. Different from chromatic colouring (Ch 5), which requires adjacent vertices to have different colours
3. The goal is to find monochromatic substructures, not to avoid them

# Relationships
## Enables
- **Monochromatic subgraph** — The objects sought in Ramsey theory
- **Ramsey's theorem** — Stated in terms of 2-colourings

## Contrasts With
- Chromatic colouring — In Chapter 5, colourings must be proper (no monochromatic edges)

# Source Reference
Chapter 9, Section 9.1, page 253 (pdf page 263).

# Verification Notes
- Confidence: HIGH — explicitly defined with distinction from chromatic colouring
