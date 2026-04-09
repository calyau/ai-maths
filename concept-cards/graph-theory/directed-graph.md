---
concept: Directed Graph
slug: directed-graph

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
  - "digraph"
  - "oriented graph"
  - "orientation"

prerequisites:
  - graph
extends: []
related:
  - multigraph
  - graph
contrasts_with:
  - graph

answers_questions:
  - "What is a directed graph?"
  - "What is an orientation of a graph?"
---

# Quick Definition
A directed graph (digraph) is a pair (V, E) with maps init and ter assigning to each edge an initial and terminal vertex. An oriented graph is a digraph without loops or multiple edges, arising from directing the edges of a simple graph.

# Core Definition
A directed graph (or digraph) is a pair (V, E) of disjoint sets together with two maps init: E -> V and ter: E -> V assigning to every edge e an initial vertex init(e) and a terminal vertex ter(e). The edge e is directed from init(e) to ter(e). A directed graph D is an orientation of an (undirected) graph G if V(D) = V(G) and E(D) = E(G), and {init(e), ter(e)} = {x, y} for every edge e = xy. Oriented graphs are directed graphs without loops or multiple edges (Diestel, pp. 28-29).

# Prerequisites
- **Graph** — a directed graph adds direction to edges

# Key Properties
1. Each edge has an initial vertex and a terminal vertex
2. Multiple edges (same direction) are called parallel
3. If init(e) = ter(e), the edge is a loop
4. An orientation of a graph assigns a direction to each edge
5. Oriented graphs have no loops or multiple edges

# Relationships
## Builds Upon
- **graph**

## Contrasts With
- **graph** — undirected; no initial/terminal distinction

# Source Reference
Chapter 1: The Basics, Section 1.10, pages 28-29 (pdf pp. 38-39).

# Verification Notes
- Direct from pp. 28-29
- Confidence: HIGH
