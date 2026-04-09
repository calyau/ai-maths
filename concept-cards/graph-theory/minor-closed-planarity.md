---
concept: Planarity is Minor-Closed
slug: minor-closed-planarity
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
extraction_confidence: high
aliases:
  - "Exercise 13"
prerequisites:
  - planar-graph
  - kuratowski-theorem
extends: []
related:
  - kuratowski-theorem
contrasts_with: []
answers_questions:
  - "Is the minor of a planar graph always planar?"
  - "Is planarity closed under taking minors?"
---

# Quick Definition
Any minor of a planar graph is planar (Exercise 13). Equivalently, a graph is planar if and only if it is a minor of a grid.

# Core Definition
"Show that any minor of a planar graph is planar. Deduce that a graph is planar if and only if it is the minor of a grid" (Diestel, p. 107, Exercise 13).

# Prerequisites
- **Planar graph**, **Kuratowski's theorem**

# Key Properties
1. Planarity is closed under edge deletion, vertex deletion, and contraction
2. Hence closed under the minor relation
3. Equivalently: planar graphs are exactly the minors of grids
4. This is immediate from the forbidden-minor characterization (Kuratowski)

# Context & Application
The minor-closed property of planarity makes it the prototypical example for the Robertson-Seymour graph minor theorem, which states that every minor-closed property has a finite forbidden-minor characterization.

# Relationships
## Related
- **Kuratowski's theorem** -- The forbidden-minor characterization

# Source Reference
Chapter 4, Exercise 13, page 107.

# Verification Notes
- Exercise 13
- Confidence: HIGH
