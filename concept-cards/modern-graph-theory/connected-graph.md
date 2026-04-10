---
concept: Connected Graph
slug: connected-graph
category: graph-fundamentals
subcategory: connectivity
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases:
  - connectivity
prerequisites:
  - graph
  - path
extends: []
related:
  - component
  - cutvertex
  - bridge
  - tree
contrasts_with: []
answers_questions:
  - "What is a connected graph?"
---

# Quick Definition

A graph is connected if for every pair of distinct vertices there is a path between them. A maximal connected subgraph is called a component.

# Core Definition

"A graph is connected if for every pair $\{x, y\}$ of distinct vertices there is a path from $x$ to $y$. Note that a connected graph of order at least 2 cannot contain an isolated vertex. A maximal connected subgraph is a component of the graph" (Bollobás, p. 14).

# Prerequisites

- **Graph** — Connectivity is a property of graphs
- **Path** — Connectivity is defined via the existence of paths

# Key Properties

1. A connected graph has exactly one component
2. A connected graph of order $\ge 2$ has no isolated vertices
3. Every graph is the vertex-disjoint union of its components (Theorem 3)
4. A graph is connected iff $d(x, y) < \infty$ for all vertex pairs

# Construction / Recognition

## To verify connectivity
1. Pick any vertex $x$
2. Determine all vertices reachable from $x$ via paths
3. If all vertices are reached, the graph is connected

# Context & Application

Connectivity is one of the most fundamental properties of graphs. Most interesting graph theory concerns connected graphs. The concept extends to higher connectivity: $k$-connected graphs cannot be disconnected by removing fewer than $k$ vertices.

# Examples

**Example** (p. 14): The graph in Fig. I.1 is connected. The forest in Fig. I.5 is disconnected with multiple components.

# Relationships

## Builds Upon
- **Graph**, **Path**

## Enables
- **Tree** — A connected acyclic graph
- **Spanning tree** — Every connected graph contains one
- **Cutvertex** — A vertex whose removal disconnects a connected graph
- **Bridge** — An edge whose removal disconnects a connected graph

# Common Errors

- **Error**: Assuming a graph with many edges must be connected
  **Correction**: A graph can have many edges but still be disconnected (e.g., a disjoint union of complete graphs)

# Common Confusions

- **Confusion**: Confusing connected graph with complete graph
  **Clarification**: Connected means a path exists between every pair; complete means an edge exists between every pair

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 14.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
