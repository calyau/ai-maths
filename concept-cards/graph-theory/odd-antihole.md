---
concept: Odd Antihole
slug: odd-antihole
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
  - "complement of odd hole"
prerequisites:
  - graph
extends: []
related:
  - strong-perfect-graph-theorem
  - berge-graph
  - odd-hole
contrasts_with:
  - odd-hole
answers_questions:
  - "What is an odd antihole?"
---

# Quick Definition
An odd antihole is the complement of an induced odd cycle of length >= 5 as an induced subgraph. Odd antiholes and odd holes are the two types of forbidden subgraph for perfection.

# Core Definition
An odd antihole is an induced subgraph isomorphic to the complement of C_{2k+1} for k >= 2.

# Prerequisites
- **Graph**

# Key Properties
1. complement(C_5) = C_5 (self-complementary)
2. For k >= 3, complement(C_{2k+1}) is distinct from C_{2k+1}
3. Odd antiholes are not perfect (since their complement, the odd hole, is not perfect)
4. Forbidden induced subgraph for perfection

# Relationships
## Related
- **Strong perfect graph theorem** -- Forbidden subgraph for perfection
- **Berge graph** -- No odd holes or antiholes

## Contrasts With
- **Odd hole** -- The complement

# Source Reference
Chapter 5, Section 5.5, Theorem 5.5.3, page 129.

# Verification Notes
- From Theorem 5.5.3
- Confidence: HIGH
