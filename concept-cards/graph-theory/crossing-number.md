---
concept: Crossing Number
slug: crossing-number
category: planar-graphs
subcategory: drawings
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.3 Drawings"
extraction_confidence: medium
aliases:
  - "cr(G)"
prerequisites:
  - planar-graph
  - plane-graph
extends: []
related:
  - planar-embedding
  - straight-line-drawing
contrasts_with: []
answers_questions:
  - "What is the crossing number of a graph?"
  - "How many crossings are unavoidable when drawing a non-planar graph?"
---

# Quick Definition
The crossing number cr(G) of a graph G is the minimum number of edge crossings in any drawing of G in the plane. A graph is planar if and only if cr(G) = 0.

# Core Definition
The crossing number is the minimum number of edge crossings over all possible drawings of G in the plane. Planar graphs have cr(G) = 0.

# Prerequisites
- **Planar graph** and **Plane graph**

# Key Properties
1. cr(G) = 0 iff G is planar
2. cr(G) measures "how far" G is from being planar
3. Computing cr(G) is NP-hard in general
4. The crossing lemma gives lower bounds: cr(G) >= m^3/(64n^2) for m >= 4n

# Context & Application
The crossing number quantifies non-planarity. It is important in graph drawing and VLSI circuit layout. The crossing lemma (due to Ajtai, Chvatal, Newborn, Szemeredi, and independently Leighton) provides useful lower bounds.

# Relationships
## Related
- **Planar graph** -- cr(G) = 0 characterizes planarity

# Source Reference
Chapter 4, Section 4.3, pages 92-96. Also Chapter 7.

# Verification Notes
- Concept implicit in Ch. 4 discussion
- Confidence: MEDIUM -- not formally defined in Ch. 4 (more in Ch. 7)
