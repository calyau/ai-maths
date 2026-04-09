---
concept: Planar Graphs as Unions of Forests
slug: planar-graph-union-of-forests
category: planar-graphs
subcategory: plane-graphs
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
  - edge-bound-planar
extends: []
related:
  - euler-formula
contrasts_with: []
answers_questions:
  - "Can every planar graph be decomposed into forests?"
---

# Quick Definition
Every planar graph is a union of three forests (Exercise 5). This follows from the edge bound m <= 3n - 6 and the Nash-Williams arboricity formula.

# Core Definition
"Show that every planar graph is a union of three forests" (Diestel, p. 107, Exercise 5).

# Prerequisites
- **Planar graph**, **Edge bound for planar graphs**

# Key Properties
1. The arboricity of planar graphs is at most 3
2. Follows from m <= 3(n-2) and the arboricity formula
3. Tight: some planar graphs require 3 forests

# Relationships
## Related
- **Edge bound** -- The edge density constraint enables this decomposition

# Source Reference
Chapter 4, Exercise 5, page 107.

# Verification Notes
- Exercise 5
- Confidence: MEDIUM
