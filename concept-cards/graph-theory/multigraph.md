---
concept: Multigraph
slug: multigraph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 38
section: "1.10 Other notions of graphs"

extraction_confidence: high

aliases:
  - "multi-graph"
  - "pseudograph"

prerequisites:
  - graph
extends:
  - graph
related:
  - directed-graph
  - hypergraph
contrasts_with:
  - graph

answers_questions:
  - "What is a multigraph?"
  - "How does a multigraph differ from a simple graph?"
---

# Quick Definition
A multigraph is a pair (V, E) with a map assigning to every edge one or two vertices (its ends). Unlike simple graphs, multigraphs allow loops and multiple edges.

# Core Definition
A multigraph is a pair (V, E) of disjoint sets (of vertices and edges) together with a map E -> V union [V]^2 assigning to every edge either one or two vertices, its ends. Thus, multigraphs can have loops and multiple edges (Diestel, p. 29).

# Prerequisites
- **Graph** — a multigraph generalizes a graph

# Key Properties
1. Allows loops (edges from a vertex to itself)
2. Allows multiple edges between the same pair of vertices
3. A loop at a vertex contributes 2 to its degree
4. A graph is a multigraph without loops or multiple edges
5. Contraction is simpler: parallel edges and loops are kept, not deleted

# Context & Application
Some areas of graph theory (such as plane duality) require multigraphs rather than simple graphs. Authors working primarily with multigraphs often call them simply "graphs" and use "simple graph" for Diestel's graphs.

# Relationships
## Builds Upon
- **graph** — a multigraph relaxes the constraints of a simple graph

## Contrasts With
- **graph** — simple graphs have no loops or multiple edges

# Source Reference
Chapter 1: The Basics, Section 1.10, page 29 (pdf p. 39). See Fig. 1.10.1.

# Verification Notes
- Direct from p. 29
- Confidence: HIGH
