---
concept: "Kirchhoff's Law"
slug: kirchhoffs-law
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
  - "conservation law"
  - "flow conservation"
prerequisites:
  - vertex
  - edge
  - directed-edge
related:
  - circulation
  - flow-in-network
answers_questions:
  - "What is Kirchhoff's law in graph theory?"
  - "What conservation principle governs flows?"
---

# Quick Definition
Kirchhoff's law states that at any vertex x, the total net flow out of x is zero: the sum of f(x, y) over all neighbours y equals zero.

# Core Definition
For a function f: V^2 -> Z (or more generally, f: E-arrow -> H for an abelian group H) and a vertex x, Kirchhoff's law requires:

sum_{y in N(x)} f(x, y) = 0.

Equivalently, in the directed-edge formalism: f(v, V) = 0 for all v in V. This is condition (F2) in Diestel's definition of a circulation. (Diestel, p. 139-140)

# Prerequisites
- **Vertex** and **Edge** — The law applies at vertices of a graph
- **Directed edge** — Flow values are assigned to directed edges

# Key Properties
1. Expresses conservation: everything flowing into a vertex also flows out
2. Holds at every vertex in a circulation
3. Holds at every vertex except source and sink in a network flow
4. Together with antisymmetry (F1), implies f(X, X-bar) = 0 for all vertex subsets X

# Context & Application
Kirchhoff's law is the graph-theoretic analogue of conservation of flow in physics and electrical networks. It is the key structural condition that distinguishes circulations from arbitrary antisymmetric functions on directed edges.

# Examples
**Example** (p. 139): In a physical network carrying water, Kirchhoff's law says that at most internal nodes, the water flowing in equals the water flowing out.

# Relationships
## Enables
- **Circulation** — Kirchhoff's law is condition (F2) in the definition
- **Flow in network** — Modified form (F2') requires the law at all vertices except source and sink

# Source Reference
Chapter 6: Flows, pages 139-140 (pdf page 150). The law appears as condition (F2) in the circulation definition.

# Verification Notes
- Definition: From the chapter introduction (p. 139) and formalized as (F2) on p. 140
- Confidence: HIGH — explicitly named and defined
