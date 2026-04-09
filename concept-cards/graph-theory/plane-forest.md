---
concept: Plane Forest
slug: plane-forest
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
  - "plane tree"
  - "Proposition 4.2.4"
prerequisites:
  - plane-graph
  - face
extends: []
related:
  - euler-formula
contrasts_with: []
answers_questions:
  - "How many faces does a plane forest have?"
---

# Quick Definition
A plane forest has exactly one face (Proposition 4.2.4). This is because arcs do not separate the plane: removing a tree from R^2 leaves one connected region.

# Core Definition
**Proposition 4.2.4**: "A plane forest has exactly one face" (Diestel, p. 88).

# Prerequisites
- **Plane graph**, **Face**

# Key Properties
1. Exactly one face (the entire complement R^2 \ T)
2. This face is unbounded
3. Follows from Lemma 4.1.3 (arcs don't separate) by induction on edges
4. Base case for Euler's formula proof: n - (n-1) + 1 = 2

# Relationships
## Enables
- **Euler's formula** -- Base case of the proof

# Source Reference
Chapter 4, Section 4.2, Proposition 4.2.4, page 88.

# Verification Notes
- Proposition from p. 88
- Confidence: HIGH
