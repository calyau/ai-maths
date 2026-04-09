---
concept: Maximal Planar Graph
slug: maximal-planar-graph
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
  - "maximally planar graph"
prerequisites:
  - planar-graph
extends:
  - planar-graph
related:
  - plane-triangulation
  - maximal-plane-graph
  - edge-bound-planar
contrasts_with:
  - maximal-plane-graph
answers_questions:
  - "What is a maximally planar graph?"
  - "How many edges does a maximal planar graph have?"
---

# Quick Definition
A planar graph is maximally planar if adding any new edge (between existing vertices) destroys planarity.

# Core Definition
"A planar graph is maximal, or maximally planar, if it is planar but cannot be extended to a larger planar graph by adding an edge (but no vertex)" (Diestel, p. 97).

# Prerequisites
- **Planar graph** -- Must be planar to begin with

# Key Properties
1. A planar graph with n >= 3 is maximally planar iff it has 3n - 6 edges (Proposition 4.4.1)
2. Every maximal plane graph is maximally planar (Proposition 4.4.1)
3. Every maximal planar graph with >= 4 vertices is 3-connected (Corollary 4.4.7)
4. Drawings of maximal planar graphs are plane triangulations

# Context & Application
Maximal planar graphs are the "densest" planar graphs. They are important in proofs because any planar graph can be extended to a maximal one by adding edges, and properties proved for maximal planar graphs often extend to all planar graphs. The fact that maximal planar graphs with >= 4 vertices are 3-connected links planarity theory to connectivity theory.

# Relationships
## Builds Upon
- **Planar graph**

## Enables
- Inductive arguments about planar graphs (extend to triangulation, then reduce)

## Related
- **Plane triangulation** -- Drawings of maximal planar graphs
- **Edge bound** -- Characterized by having exactly 3n - 6 edges

## Contrasts With
- **Maximal plane graph** -- "Maximal plane" is a drawing property; "maximally planar" is an abstract graph property. They coincide by Proposition 4.4.1.

# Source Reference
Chapter 4, Section 4.4, page 97. Propositions 4.4.1 and Corollary 4.4.7.

# Verification Notes
- Definition from p. 97
- Confidence: HIGH -- explicit definition
