---
concept: Whitney's Uniqueness Theorem
slug: whitney-uniqueness-theorem
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
extraction_confidence: high
aliases:
  - "Theorem 4.3.2"
  - "Whitney 1932"
  - "uniqueness of embeddings"
prerequisites:
  - equivalent-embeddings
  - planar-graph
extends: []
related:
  - jordan-schoenflies-theorem
  - kuratowski-theorem
contrasts_with: []
answers_questions:
  - "How many essentially different planar embeddings does a 3-connected graph have?"
  - "Are planar embeddings of 3-connected graphs unique?"
---

# Quick Definition
Whitney's uniqueness theorem states that any two planar embeddings of a 3-connected graph are equivalent. That is, a 3-connected planar graph can be drawn in the plane in essentially only one way.

# Core Definition
**Theorem 4.3.2** (Whitney 1932): "Any two planar embeddings of a 3-connected graph are equivalent" (Diestel, p. 96).

# Prerequisites
- **Equivalent embeddings** -- The theorem asserts equivalence
- **Planar graph** -- The graph must be planar (and 3-connected)

# Key Properties
1. 3-connected planar graphs have unique embeddings up to equivalence
2. The proof uses Proposition 4.2.7 (face boundaries = non-separating induced cycles)
3. 2-connected graphs may have multiple inequivalent embeddings
4. The theorem justifies speaking of "the" embedding of a 3-connected planar graph

# Context & Application
This is one of the fundamental structural results about planar graphs. It means that for 3-connected graphs, the face structure is determined by the abstract graph structure alone, not by the choice of embedding. This makes many properties of 3-connected planar graphs (such as their duals) well-defined without specifying an embedding.

# Examples
**Example** (p. 96): Any two drawings of the cube graph (3-connected, planar) produce equivalent embeddings with the same face structure.

# Relationships
## Builds Upon
- **Equivalent embeddings**, **Proposition 4.2.7** (face boundaries are non-separating induced cycles)

## Enables
- **Plane duality** -- For 3-connected graphs, the dual is uniquely determined

# Source Reference
Chapter 4, Section 4.3, Theorem 4.3.2, page 96.

# Verification Notes
- Theorem statement directly quoted
- Confidence: HIGH -- named classical theorem
