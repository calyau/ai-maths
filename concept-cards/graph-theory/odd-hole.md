---
concept: Odd Hole
slug: odd-hole
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
  - "induced odd cycle"
prerequisites:
  - graph
extends: []
related:
  - strong-perfect-graph-theorem
  - berge-graph
  - perfect-graph
contrasts_with:
  - odd-antihole
answers_questions:
  - "What is an odd hole?"
---

# Quick Definition
An odd hole is an induced cycle of odd length >= 5 (i.e., C_{2k+1} for k >= 2 as an induced subgraph). Odd holes and their complements (odd antiholes) are the only obstructions to perfection.

# Core Definition
An odd hole is an induced odd cycle C_{2k+1} with k >= 2. Note: C_3 (triangle) is not an odd hole, since "hole" requires length >= 5.

# Prerequisites
- **Graph**

# Key Properties
1. C_5 is the smallest odd hole
2. Odd holes are not perfect: chi(C_{2k+1}) = 3 but omega = 2
3. Forbidden induced subgraph for perfect graphs (with odd antiholes)

# Relationships
## Related
- **Strong perfect graph theorem** -- Odd holes and antiholes are the forbidden subgraphs
- **Berge graph** -- No odd holes or antiholes

## Contrasts With
- **Odd antihole** -- Complement of an odd hole

# Source Reference
Chapter 5, Section 5.5, Theorem 5.5.3, page 129.

# Verification Notes
- From Theorem 5.5.3
- Confidence: HIGH
