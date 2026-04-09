---
concept: Face Boundary
slug: face-boundary
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
  - "boundary of a face"
  - "G[f]"
prerequisites:
  - face
  - plane-graph
extends: []
related:
  - facial-cycle
  - euler-formula
  - plane-duality
contrasts_with:
  - frontier
answers_questions:
  - "What is the boundary of a face in a plane graph?"
  - "What subgraph bounds a given face?"
---

# Quick Definition
The face boundary (or boundary) of a face f in a plane graph G is the subgraph G[f] whose point set is the frontier of f. In a 2-connected plane graph, every face boundary is a cycle.

# Core Definition
"The subgraph of G whose point set is the frontier of a face f is said to bound f and is called its boundary; we denote it by G[f]" (Diestel, p. 88). A face is incident with the vertices and edges of its boundary.

# Prerequisites
- **Face** -- Face boundaries are defined for faces
- **Plane graph** -- The boundary is a subgraph of the plane graph

# Key Properties
1. The frontier of a face is always the point set of a subgraph (Corollary 4.2.3)
2. In a 2-connected plane graph, every face boundary is a cycle (Proposition 4.2.6)
3. In a 3-connected plane graph, face boundaries are precisely the non-separating induced cycles (Proposition 4.2.7)
4. Different faces have different boundaries unless the graph is a cycle (Lemma 4.2.5)
5. An edge on a cycle bounds exactly two faces; an edge on no cycle bounds exactly one face (Lemma 4.2.2)
6. Every face is a face of its own boundary

# Construction / Recognition
## To Find the Boundary of a Face f
1. Identify the frontier of f (points where f meets G)
2. The subgraph on this point set is G[f]
3. In a 2-connected graph, this will be a cycle

# Context & Application
Face boundaries are fundamental to planarity theory. The facial cycles of a 2-connected plane graph generate its entire cycle space and form a simple basis (MacLane's theorem). The duality between cycles and bonds is mediated through face boundaries. In a 3-connected graph, face boundaries can be characterized purely combinatorially as non-separating induced cycles.

# Examples
**Example** (p. 89): In a 2-connected plane graph, Proposition 4.2.6 guarantees every face boundary is a cycle.

**Example** (p. 89): In a 3-connected plane graph, the face boundaries are exactly the non-separating induced cycles (Proposition 4.2.7).

# Relationships
## Builds Upon
- **Face** -- Boundaries are defined for faces

## Enables
- **Euler's formula** -- The proof uses face boundary properties
- **Plane duality** -- Cycles in G correspond to cuts in G*
- **MacLane's theorem** -- Facial cycles form a simple basis of the cycle space

## Related
- **Facial cycle** -- In 2-connected plane graphs, face boundaries are facial cycles

## Contrasts With
- **Frontier** -- The frontier is the topological concept; the boundary is the graph-theoretic subgraph

# Common Errors
- **Error**: Assuming every face boundary is a cycle
  **Correction**: This holds only for 2-connected plane graphs; bridges can appear on the boundary of just one face

# Source Reference
Chapter 4: Planar Graphs, Section 4.2 "Plane graphs," pages 88-89. Corollary 4.2.3, Lemma 4.2.5, Propositions 4.2.6 and 4.2.7.

# Verification Notes
- Definition directly quoted from p. 88
- Confidence: HIGH -- explicit definition with supporting propositions
