---
concept: Adjacent
slug: adjacent

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "neighbour"
  - "neighbor"

prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - incident
  - neighborhood
  - independent-set
  - complete-graph
contrasts_with:
  - independent-set

answers_questions:
  - "What does it mean for two vertices to be adjacent?"
  - "What is a neighbour of a vertex?"
---

# Quick Definition
Two vertices x, y of a graph G are adjacent (or neighbours) if xy is an edge of G. Two edges are adjacent if they share a common end.

# Core Definition
Two vertices x, y of G are adjacent, or neighbours, if xy is an edge of G. Two edges e and f (with e not equal to f) are adjacent if they have an end in common (Diestel, p. 3).

# Prerequisites
- **Graph**, **vertex**, **edge** — adjacency is a relation defined on vertices and edges of a graph

# Key Properties
1. Adjacency of vertices is symmetric: if x is adjacent to y, then y is adjacent to x
2. No vertex is adjacent to itself (no loops in simple graphs)
3. Two edges are adjacent if they share exactly one endpoint
4. If all vertices of G are pairwise adjacent, G is complete

# Construction / Recognition
Vertices x and y are adjacent if and only if xy is in E(G).

# Context & Application
Adjacency is the fundamental relation that a graph encodes. The neighborhood N(v) of a vertex v is the set of all vertices adjacent to v.

# Examples
**Example** (p. 2-3): In the graph with edges {1,2}, {1,5}, {2,5}, {3,4}, {5,7}, vertices 1 and 2 are adjacent, but vertices 1 and 3 are not.

# Relationships
## Builds Upon
- **graph**, **vertex**, **edge**

## Enables
- **complete-graph** — all vertices pairwise adjacent
- **independent-set** — no two vertices adjacent
- **neighborhood** — set of adjacent vertices

## Contrasts With
- **independent-set** — independent vertices are pairwise non-adjacent

# Common Confusions
- **Confusion**: Confusing adjacency (vertex-vertex or edge-edge) with incidence (vertex-edge)
  **Clarification**: Adjacency relates elements of the same type; incidence relates a vertex to an edge

# Source Reference
Chapter 1: The Basics, Section 1.1, page 3 (pdf p. 13).

# Verification Notes
- Direct from p. 3
- Confidence: HIGH
