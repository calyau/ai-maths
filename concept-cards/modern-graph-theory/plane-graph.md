---
concept: Plane Graph
slug: plane-graph
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases:
  - planar embedding
  - plane map
prerequisites:
  - planar-graph
extends:
  - planar-graph
related:
  - face
  - eulers-formula
contrasts_with: []
answers_questions:
  - "What is a plane graph?"
  - "What is the difference between a planar graph and a plane graph?"
---

# Quick Definition

A plane graph is a specific drawing of a planar graph in the plane where no two edges cross. It is a planar graph together with a particular embedding.

# Core Definition

A representation of a graph in the plane "in which the vertices correspond to distinct points and the edges to simple Jordan curves connecting the points of its endvertices" where "every two curves are either disjoint or meet only at a common endpoint" is a plane graph (Bollobás, p. 29). A plane graph together with its faces is called a plane map.

# Prerequisites

- **Planar graph** — A plane graph is a planar graph with a chosen embedding

# Key Properties

1. Each plane graph has exactly one unbounded face
2. The faces of a plane graph are the connected components of $\mathbb{R}^2$ minus the graph
3. The boundary of a face is the set of edges in its closure
4. A plane map is a plane graph together with its faces (countries)
5. Two countries are neighbouring if they share a boundary edge

# Construction / Recognition

A plane graph is constructed by embedding a planar graph in the plane. Every planar graph has a straight-line representation (edges as straight segments).

# Context & Application

Plane graphs are needed for Euler's formula and for defining faces, the dual graph, and map colourings. The four-colour theorem concerns plane maps.

# Examples

**Example** (p. 29): The graph of any convex polyhedron drawn in the plane produces a plane graph where faces of the polyhedron correspond to faces of the plane graph.

# Relationships

## Builds Upon
- **Planar graph** — A plane graph is a planar graph with an embedding

## Enables
- **Face** — Faces are defined for plane graphs
- **Euler's formula** — Relates vertices, edges, and faces of plane graphs

# Common Errors

- **Error**: Assuming a planar graph has a unique plane embedding
  **Correction**: A planar graph may have many different plane embeddings with different face structures

# Common Confusions

- **Confusion**: Using "planar graph" and "plane graph" interchangeably
  **Clarification**: A planar graph is an abstract graph; a plane graph is a specific drawing in the plane

# Source Reference

Chapter I: Fundamentals, Section I.4, pages 29-30.

# Verification Notes

- Definition source: Direct from p. 29
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
