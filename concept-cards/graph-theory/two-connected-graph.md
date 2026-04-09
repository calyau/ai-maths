---
concept: 2-Connected Graph
slug: two-connected-graph
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 65
section: "3.1 2-Connected graphs and subgraphs"
extraction_confidence: high
aliases:
  - "biconnected graph"
  - "2-connected"
prerequisites:
  - graph
  - connectivity
  - cutvertex
extends:
  - connectivity
related:
  - block
  - ear-decomposition
  - three-connected-graph
contrasts_with:
  - three-connected-graph
answers_questions:
  - "What is a 2-connected graph?"
---

# Quick Definition
A graph is 2-connected if it has at least 3 vertices and remains connected after the removal of any single vertex (equivalently, kappa(G) >= 2).

# Core Definition
A graph G is **2-connected** if |G| >= 3 and G has no cutvertex, i.e., kappa(G) >= 2. Equivalently, any two vertices lie on a common cycle.

# Prerequisites
- **Graph** — 2-connectedness is a property of graphs
- **Connectivity** — kappa(G) >= 2
- **Cutvertex** — absence of cutvertices characterizes 2-connectedness

# Key Properties
1. |G| >= 3 and no cutvertex
2. Any two vertices lie on a common cycle (Exercise 7)
3. Can be constructed from a cycle by successively adding H-paths (Proposition 3.1.3)
4. Every 2-connected graph is the union of its ears in an ear decomposition
5. 2-connected graphs are the building blocks: every connected graph decomposes into blocks

# Construction / Recognition
## Ear Decomposition Construction (Proposition 3.1.3)
1. Start with a cycle C
2. At each step, add an H-path to the graph H already constructed
3. The graph is 2-connected at every stage
4. Every 2-connected graph can be built this way

# Context & Application
2-connected graphs are the fundamental building blocks of graph connectivity. They have no cutvertex, meaning the graph cannot be disconnected by removing a single vertex. Section 3.1 provides both the canonical decomposition of connected graphs into 2-connected blocks and the constructive characterization of 2-connected graphs via ear decomposition.

# Examples
**Example** (p. 67, Fig. 3.1.2): The construction of 2-connected graphs by adding H-paths to an existing 2-connected subgraph.

# Relationships
## Builds Upon
- **Connectivity**, **cutvertex**

## Enables
- **Block** — maximal 2-connected subgraphs are blocks
- **Ear decomposition** — constructive characterization
- **Three-connected graph** — higher connectivity

## Related
- **H-path** — used in the ear decomposition construction

## Contrasts With
- **Three-connected graph** — stronger connectivity requirement

# Common Errors
- **Error**: Calling K2 (a single edge) 2-connected
  **Correction**: 2-connected requires |G| >= 3; K2 has only 2 vertices

# Common Confusions
- **Confusion**: Confusing 2-connected with 2-edge-connected
  **Clarification**: 2-connected means no vertex removal disconnects (kappa >= 2); 2-edge-connected means no edge removal disconnects (lambda >= 2). 2-connected implies 2-edge-connected but not vice versa.

# Source Reference
Chapter 3, Section 3.1, pp. 65-67 (pdf pp. 65-67).

# Verification Notes
- Definition from Ch. 1.4, elaborated in Section 3.1
- Confidence: HIGH — extensively treated
