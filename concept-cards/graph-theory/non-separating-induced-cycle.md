---
concept: Non-Separating Induced Cycle
slug: non-separating-induced-cycle
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
aliases: []
prerequisites:
  - plane-graph
  - face-boundary
extends: []
related:
  - facial-cycle
  - kelmans-planarity-criterion
contrasts_with: []
answers_questions:
  - "What characterizes face boundaries in 3-connected plane graphs?"
---

# Quick Definition
In a 3-connected plane graph, the face boundaries are precisely the non-separating induced cycles: induced cycles C such that G - V(C) remains connected.

# Core Definition
**Proposition 4.2.7**: "The face boundaries in a 3-connected plane graph are precisely its non-separating induced cycles" (Diestel, p. 89).

# Prerequisites
- **Plane graph** and **Face boundary** -- Applies to 3-connected plane graphs

# Key Properties
1. A non-separating induced cycle has no chords and does not disconnect the graph
2. In a 3-connected plane graph, these are exactly the face boundaries
3. Each edge lies on exactly two such cycles (in a 3-connected plane graph)
4. This characterization is purely combinatorial (no embedding needed)

# Context & Application
This characterization connects the geometric concept of face boundaries to the combinatorial concept of non-separating induced cycles. It is the foundation for the Kelmans planarity criterion (Theorem 4.5.2) and Whitney's uniqueness theorem (4.3.2).

# Relationships
## Enables
- **Kelmans planarity criterion** -- Each edge on at most two such cycles implies planarity
- **Whitney's uniqueness theorem** -- Face boundaries are combinatorially determined

# Source Reference
Chapter 4, Section 4.2, Proposition 4.2.7, page 89.

# Verification Notes
- Statement from p. 89
- Confidence: HIGH -- named proposition
