---
concept: Strong Perfect Graph Theorem
slug: strong-perfect-graph-theorem
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
extraction_confidence: medium
aliases:
  - "Theorem 5.5.3"
  - "SPGT"
  - "Chudnovsky-Robertson-Seymour-Thomas 2002"
  - "Berge's strong conjecture"
prerequisites:
  - perfect-graph
extends: []
related:
  - perfect-graph-theorem
contrasts_with: []
answers_questions:
  - "How are perfect graphs characterized by forbidden subgraphs?"
---

# Quick Definition
A graph G is perfect if and only if neither G nor its complement contains an odd cycle of length >= 5 as an induced subgraph. Odd holes and odd antiholes are the only obstructions to perfection.

# Core Definition
**Theorem 5.5.3** (Chudnovsky, Robertson, Seymour & Thomas 2002): "A graph G is perfect if and only if neither G nor G-bar contains an odd cycle of length at least 5 as an induced subgraph" (Diestel, p. 129).

# Prerequisites
- **Perfect graph** -- The theorem characterizes perfect graphs

# Key Properties
1. Two types of forbidden induced subgraphs: odd holes (C_{2k+1} for k >= 2) and odd antiholes (complements of C_{2k+1})
2. The proof is long and technical (not given in Diestel)
3. Formerly the "strong perfect graph conjecture" of Berge (1963)
4. An O(n^9) recognition algorithm exists

# Context & Application
The strong perfect graph theorem is one of the deepest results in graph theory, confirming a conjecture that stood for nearly 40 years. It provides a complete forbidden-subgraph characterization of perfect graphs, analogous to Kuratowski's theorem for planar graphs.

# Relationships
## Builds Upon
- **Perfect graph**

## Related
- **Perfect graph theorem** -- The weaker result that perfection is self-complementary

# Source Reference
Chapter 5, Section 5.5, Theorem 5.5.3, page 129. Notes pp. 138-139.

# Verification Notes
- Theorem stated without proof
- Confidence: MEDIUM -- proof not given (extremely long and technical)
