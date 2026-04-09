---
concept: Path
slug: path

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 16
section: "1.3 Paths and cycles"

extraction_confidence: high

aliases:
  - "P^k"

prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - cycle
  - walk
  - connected-graph
  - distance
contrasts_with:
  - cycle
  - walk

answers_questions:
  - "What is a path?"
  - "What is the length of a path?"
  - "What are the ends of a path?"
---

# Quick Definition
A path is a non-empty graph P = (V, E) with V = {x_0, ..., x_k} and E = {x_0x_1, x_1x_2, ..., x_{k-1}x_k} where all vertices are distinct. Its length is k (the number of edges).

# Core Definition
A path is a non-empty graph P = (V, E) of the form V = {x_0, x_1, ..., x_k}, E = {x_0x_1, x_1x_2, ..., x_{k-1}x_k}, where the x_i are all distinct. The vertices x_0 and x_k are linked by P and are called its ends; the vertices x_1, ..., x_{k-1} are the inner vertices of P. The number of edges of a path is its length, and the path of length k is denoted by P^k. Note that k is allowed to be zero; thus, P^0 = K^1 (Diestel, p. 6).

# Prerequisites
- **Graph**, **vertex**, **edge** — a path is a specific type of graph

# Key Properties
1. All vertices in a path are distinct
2. The length is the number of edges (not vertices)
3. P^k has k + 1 vertices and k edges
4. P^0 = K^1 (a single vertex is a path of length 0)
5. Vertices x_0 and x_k are the ends; the rest are inner vertices
6. A path is often written as x_0 x_1 ... x_k

# Construction / Recognition
## To Recognize a Path
1. Verify the graph is connected
2. Verify all vertices are distinct
3. Verify exactly two vertices have degree 1 (the ends) and all others have degree 2 (unless the path has length 0)

# Context & Application
Paths are fundamental in graph theory. They define connectivity, distance, and many structural properties. The notation xPy denotes the subpath from x to y.

An A-B path has its first vertex in A and last vertex in B, with no other vertex in A or B. Two or more paths are independent if none contains an inner vertex of another.

# Examples
**Example** (p. 7): Fig. 1.3.1 shows a path P = P^6 in a graph G.

# Relationships
## Builds Upon
- **graph**, **vertex**, **edge**

## Enables
- **connected-graph** — defined via existence of paths
- **distance** — length of shortest path
- **cycle** — a path plus one edge

## Contrasts With
- **cycle** — a cycle closes a path into a loop
- **walk** — a walk allows repeated vertices

# Common Confusions
- **Confusion**: Thinking a path can revisit vertices
  **Clarification**: In a path, all vertices must be distinct; a sequence that revisits vertices is a walk

# Source Reference
Chapter 1: The Basics, Section 1.3, pages 6-7 (pdf pp. 16-17). See Fig. 1.3.1.

# Verification Notes
- Direct from p. 6-7
- Confidence: HIGH
