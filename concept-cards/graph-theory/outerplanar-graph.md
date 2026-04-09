---
concept: Outerplanar Graph
slug: outerplanar-graph
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "Exercises"
extraction_confidence: medium
aliases: []
prerequisites:
  - planar-graph
extends:
  - planar-graph
related:
  - kuratowski-theorem
contrasts_with: []
answers_questions:
  - "What is an outerplanar graph?"
---

# Quick Definition
A graph is outerplanar if it has a drawing in which every vertex lies on the boundary of the outer face. A graph is outerplanar if and only if it contains neither K^4 nor K_{2,3} as a minor.

# Core Definition
"A graph is called outerplanar if it has a drawing in which every vertex lies on the boundary of the outer face" (Diestel, p. 107, Exercise 20).

# Prerequisites
- **Planar graph** -- Every outerplanar graph is planar

# Key Properties
1. Forbidden minor characterization: no K^4 or K_{2,3} minor
2. All vertices on the outer face boundary
3. 2-colourable if bipartite; at most 3-colourable in general
4. Strictly contained in the class of planar graphs

# Relationships
## Builds Upon
- **Planar graph** -- Subclass

## Related
- **Kuratowski's theorem** -- Analogous forbidden minor characterization

# Source Reference
Chapter 4, Exercise 20, page 107.

# Verification Notes
- Definition from Exercise 20
- Confidence: MEDIUM -- exercise definition
