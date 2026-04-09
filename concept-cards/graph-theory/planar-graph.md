---
concept: Planar Graph
slug: planar-graph
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.4 Planar graphs: Kuratowski's theorem"
extraction_confidence: high
aliases:
  - "planar"
prerequisites:
  - graph
  - plane-graph
extends:
  - graph
related:
  - kuratowski-theorem
  - euler-formula
  - four-colour-theorem
  - chromatic-number
contrasts_with:
  - plane-graph
  - non-planar-graph
answers_questions:
  - "What is a planar graph?"
  - "How do I test whether a graph is planar?"
  - "What must I know before studying planar graphs?"
---

# Quick Definition
A graph is planar if it can be embedded in the plane, i.e., if it is isomorphic to some plane graph. Equivalently, it can be drawn with no edge crossings.

# Core Definition
"A graph is called planar if it can be embedded in the plane: if it is isomorphic to a plane graph" (Diestel, p. 97). By Kuratowski's theorem (4.4.6), a graph is planar if and only if it contains neither K^5 nor K_{3,3} as a (topological) minor.

# Prerequisites
- **Graph** -- A planar graph is a graph with a special property
- **Plane graph** -- Planarity means admitting a plane drawing

# Key Properties
1. Equivalently characterized by forbidden minors: no K^5 or K_{3,3} minor (Kuratowski/Wagner)
2. Has at most 3n - 6 edges for n >= 3
3. Average degree < 6; minimum degree <= 5
4. 4-colourable (four colour theorem)
5. 5-choosable (Thomassen's theorem)
6. Closed under taking minors and subgraphs
7. A planar graph with n >= 4 vertices is maximal iff it has 3n - 6 edges

# Construction / Recognition
## To Test Planarity
1. Check if the graph contains K^5 or K_{3,3} as a topological minor
2. If neither is present, the graph is planar (Kuratowski's theorem)
3. Alternatively, check if the cycle space has a simple basis (MacLane's theorem)
4. For 3-connected graphs, check if every edge lies on exactly two non-separating induced cycles (Theorem 4.5.2)

# Context & Application
Planarity is one of the most important graph properties, with deep connections to topology, algebra, and combinatorics. Planar graphs arise naturally in cartography (map colouring), circuit design, and network layout. The four colour theorem -- that every planar graph is 4-colourable -- was one of the most famous open problems in mathematics for over a century.

# Examples
**Example** (p. 97): K^4 is planar (draw it as a triangle with one interior vertex).

**Example** (p. 92): K^5 is NOT planar (10 > 3(5) - 6 = 9 edges).

**Example** (p. 92): K_{3,3} is NOT planar (9 > 2(6) - 4 = 8 edges, triangle-free bound).

# Relationships
## Builds Upon
- **Graph** -- Planarity is a property of graphs
- **Plane graph** -- Definition requires plane graph concept

## Enables
- **Four colour theorem** -- Every planar graph is 4-colourable
- **Five colour theorem** -- Every planar graph is 5-colourable (with elementary proof)
- **Plane duality** -- Only planar graphs have abstract duals (Whitney's theorem 4.6.3)
- **Chromatic number** -- chi(G) <= 4 for planar G

## Related
- **Kuratowski's theorem** -- Characterizes planarity by forbidden minors
- **Euler's formula** -- Holds for plane graphs (which represent planar graphs)

## Contrasts With
- **Plane graph** -- "Planar" = CAN be drawn; "plane" = IS drawn
- **Non-planar graph** -- Contains K^5 or K_{3,3} as minor

# Common Errors
- **Error**: Claiming a graph is non-planar because a particular drawing has crossings
  **Correction**: A graph is non-planar only if ALL drawings have crossings; finding one crossing-free drawing suffices for planarity

# Common Confusions
- **Confusion**: Confusing "planar" with "plane"
  **Clarification**: A planar graph is an abstract graph with the property of being embeddable; a plane graph is a concrete realization in R^2

- **Confusion**: Thinking planarity depends on the drawing
  **Clarification**: Planarity is an intrinsic property of the abstract graph; it does not depend on any specific drawing

# Source Reference
Chapter 4: Planar Graphs, Section 4.4 "Planar graphs: Kuratowski's theorem," page 97. Also Section 4.2 for plane graph foundations.

# Verification Notes
- Definition directly quoted from p. 97
- Equivalence via Kuratowski's theorem (4.4.6)
- Confidence: HIGH -- central concept of the chapter with explicit definition
