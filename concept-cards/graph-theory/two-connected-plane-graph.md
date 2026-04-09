---
concept: Face Boundaries in 2-Connected Plane Graphs
slug: two-connected-plane-graph
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
  - "Proposition 4.2.6"
prerequisites:
  - plane-graph
  - face-boundary
extends: []
related:
  - facial-cycle
  - non-separating-induced-cycle
contrasts_with: []
answers_questions:
  - "What are face boundaries in a 2-connected plane graph?"
---

# Quick Definition
In a 2-connected plane graph, every face is bounded by a cycle (Proposition 4.2.6). This is a key structural result enabling many arguments about plane graphs.

# Core Definition
**Proposition 4.2.6**: "In a 2-connected plane graph, every face is bounded by a cycle" (Diestel, p. 89).

# Prerequisites
- **Plane graph**, **Face boundary**

# Key Properties
1. Every face boundary is a cycle (not just a subgraph)
2. Requires 2-connectedness: in graphs with bridges, face boundaries may contain bridges
3. For 3-connected graphs, face boundaries are precisely non-separating induced cycles

# Context & Application
This proposition is used throughout Chapter 4 as a foundational structural result. It ensures that face boundaries have the nice cycle structure needed for Euler's formula, MacLane's theorem, and duality arguments.

# Relationships
## Enables
- **Facial cycle** -- Facial cycles are these cycle boundaries
- **Euler's formula** -- Proof relies on face boundary structure

# Source Reference
Chapter 4, Section 4.2, Proposition 4.2.6, page 89.

# Verification Notes
- Proposition from p. 89
- Confidence: HIGH
