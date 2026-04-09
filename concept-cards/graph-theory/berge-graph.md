---
concept: Berge Graph
slug: berge-graph
category: graph-colouring
subcategory: perfect-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.5 Perfect graphs"
extraction_confidence: high
aliases:
  - "odd-hole-free graph"
prerequisites:
  - perfect-graph
extends: []
related:
  - strong-perfect-graph-theorem
contrasts_with: []
answers_questions:
  - "What is a Berge graph?"
  - "How are Berge graphs related to perfect graphs?"
---

# Quick Definition
A Berge graph is one that contains no odd hole (induced odd cycle of length >= 5) and no odd antihole (complement of an odd hole) as an induced subgraph. By the strong perfect graph theorem, the Berge graphs are exactly the perfect graphs.

# Core Definition
A graph G is Berge if neither G nor its complement contains an odd cycle of length >= 5 as an induced subgraph. The strong perfect graph theorem (Theorem 5.5.3) proves that Berge graphs = perfect graphs.

# Prerequisites
- **Perfect graph**

# Key Properties
1. No odd hole (C_{2k+1} with k >= 2) as induced subgraph
2. No odd antihole (complement of C_{2k+1}) as induced subgraph
3. Berge = perfect (strong perfect graph theorem)
4. Recognition in O(n^9) time

# Relationships
## Related
- **Strong perfect graph theorem** -- Berge = perfect
- **Perfect graph** -- Equivalent class

# Source Reference
Chapter 5, Section 5.5, Theorem 5.5.3, page 129.

# Verification Notes
- From Theorem 5.5.3
- Confidence: HIGH
