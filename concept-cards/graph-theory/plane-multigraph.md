---
concept: Plane Multigraph
slug: plane-multigraph
category: planar-graphs
subcategory: plane-duality
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.6 Plane duality"
extraction_confidence: high
aliases: []
prerequisites:
  - plane-graph
extends:
  - plane-graph
related:
  - plane-dual
contrasts_with:
  - plane-graph
answers_questions:
  - "What is a plane multigraph?"
---

# Quick Definition
A plane multigraph extends the plane graph definition to allow loops (edges with one endpoint as a polygon containing that vertex) and multiple edges between the same pair of vertices.

# Core Definition
A plane multigraph G = (V, E) satisfies: "(i) V is a subset of R^2; (ii) every edge is either an arc between two vertices or a polygon containing exactly one vertex (its endpoint); (iii) apart from its own endpoint(s), an edge contains no vertex and no point of any other edge" (Diestel, p. 103).

# Prerequisites
- **Plane graph** -- A plane multigraph generalizes a plane graph

# Key Properties
1. Allows loops (edges that are polygons through one vertex)
2. Allows multiple edges between the same pair of vertices
3. Loops and double edges count as cycles
4. Needed for duality: the dual of a simple plane graph may have loops/multiple edges

# Context & Application
Plane multigraphs are introduced specifically for the duality theory. The dual of a bridge is a loop, and the dual of two faces sharing more than one edge requires multiple edges. Without multigraphs, duality cannot be properly defined.

# Relationships
## Builds Upon
- **Plane graph** -- Generalization allowing loops and multiple edges

## Enables
- **Plane dual** -- Duals are defined for plane multigraphs

## Contrasts With
- **Plane graph** -- Simple: no loops or multiple edges

# Source Reference
Chapter 4, Section 4.6, page 103.

# Verification Notes
- Definition quoted from p. 103
- Confidence: HIGH -- explicit definition
