---
concept: Directed Edge
slug: directed-edge
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 150
section: "6.1 Circulations"
extraction_confidence: high
aliases:
  - "edge direction"
  - "direction of an edge"
prerequisites:
  - edge
  - vertex
related:
  - circulation
  - flow-in-network
answers_questions:
  - "How are edge directions formalized for flow theory?"
---

# Quick Definition
A directed edge in a multigraph is a triple (e, x, y) specifying an edge e together with a choice of which endpoint is the tail and which is the head.

# Core Definition
For a multigraph G = (V, E), the set of directed edges is defined as:

E-arrow := { (e, x, y) | e in E; x, y in V; e = xy }.

An edge e = xy with x != y has two directions: (e, x, y) and (e, y, x). A loop e = xx has only one direction (e, x, x). For a given direction e-arrow = (e, x, y), the reverse direction is e-arrow-back = (e, y, x). (Diestel, p. 140)

# Prerequisites
- **Edge** — Directed edges refine the undirected edge concept by adding orientation
- **Vertex** — The endpoints that determine the direction

# Key Properties
1. Each non-loop edge has exactly two directions
2. A loop has exactly one direction
3. E-arrow is symmetric: E-arrow = E-arrow-back
4. For X, Y subset of V, E-arrow(X, Y) consists of directions from X to Y, excluding loops

# Context & Application
Directed edges are the technical device needed to define flows on undirected multigraphs. Since flow has a direction (from x to y or y to x), we need to formalize this choice. The triple notation (e, x, y) is necessary in multigraphs because the pair (x, y) alone does not uniquely identify an edge when parallel edges are present.

# Examples
**Example** (p. 140): If e = xy with x != y, then (e, x, y) represents flow from x to y, and (e, y, x) represents flow from y to x.

# Relationships
## Enables
- **Circulation** — Circulations are functions on directed edges
- **Flow in network** — Network flows are defined on directed edges

# Source Reference
Chapter 6: Flows, Section 6.1 "Circulations," page 140 (pdf page 150).

# Verification Notes
- Definition: Directly from p. 140
- Confidence: HIGH — formal definition explicitly stated
