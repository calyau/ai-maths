---
concept: Triangle-Free Planar Edge Bound
slug: triangle-free-edge-bound
category: planar-graphs
subcategory: plane-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.2 Plane graphs"
extraction_confidence: high
aliases:
  - "m <= 2n - 4"
prerequisites:
  - euler-formula
  - edge-bound-planar
extends:
  - edge-bound-planar
related:
  - kuratowski-graphs
contrasts_with: []
answers_questions:
  - "How many edges can a triangle-free planar graph have?"
---

# Quick Definition
A triangle-free planar graph with n >= 3 vertices has at most 2n - 4 edges. This tighter bound follows from the constraint that face boundaries have length >= 4 in triangle-free graphs.

# Core Definition
In a 2-connected triangle-free plane graph, every face boundary is a cycle of length >= 4 (Proposition 4.2.6). The double-counting argument then gives 2m >= 4l, yielding m <= 2n - 4 via Euler's formula (Diestel, p. 92).

# Prerequisites
- **Euler's formula**, **Edge bound for planar graphs**

# Key Properties
1. m <= 2n - 4 for triangle-free planar graphs with n >= 3
2. Used to prove K_{3,3} is non-planar: 9 > 2(6) - 4 = 8
3. Generalizes: for girth g, m <= g/(g-2) * (n-2) (Exercise 4)

# Relationships
## Builds Upon
- **Edge bound** (general), **Euler's formula**

## Enables
- Non-planarity of K_{3,3}

# Source Reference
Chapter 4, Section 4.2, page 92. Exercise 4.

# Verification Notes
- Derivation on p. 92
- Confidence: HIGH
