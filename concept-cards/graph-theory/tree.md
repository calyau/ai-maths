---
concept: Tree
slug: tree

category: trees-and-forests
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 23
section: "1.5 Trees and forests"

extraction_confidence: high

aliases: []

prerequisites:
  - graph
  - connected-graph
  - cycle
extends:
  - connected-graph
  - forest
related:
  - spanning-tree
  - leaf
  - rooted-tree
contrasts_with:
  - forest

answers_questions:
  - "What is a tree?"
  - "How many edges does a tree on n vertices have?"
  - "What are equivalent characterizations of trees?"
---

# Quick Definition
A tree is a connected graph containing no cycles. Equivalently, a tree is a connected graph in which any two vertices are linked by a unique path.

# Core Definition
An acyclic graph, one not containing any cycles, is called a forest. A connected forest is called a tree (Diestel, p. 13).

# Prerequisites
- **Graph** — a tree is a graph
- **Connected graph** — a tree must be connected
- **Cycle** — a tree is defined by the absence of cycles

# Key Properties (Theorem 1.5.1)
The following are equivalent for a graph T:
1. T is a tree
2. Any two vertices of T are linked by a unique path in T
3. T is minimally connected: connected, but T - e is disconnected for every edge e
4. T is maximally acyclic: contains no cycle, but T + xy does for any two non-adjacent vertices x, y

# Additional Properties
5. A connected graph with n vertices is a tree if and only if it has n - 1 edges (Corollary 1.5.3)
6. Every non-trivial tree has at least one leaf (a vertex of degree 1)
7. Removing a leaf from a tree yields another tree

# Construction / Recognition
## To Recognize a Tree
1. Check the graph is connected
2. Verify it has n - 1 edges (where n is the number of vertices)

# Context & Application
Trees are among the most fundamental structures in graph theory and computer science. They appear as spanning trees, search trees, and in many algorithms. Every connected graph contains a spanning tree.

# Examples
**Example** (p. 14): Fig. 1.5.1 shows a tree. Fig. 1.4.1 shows a spanning tree in each component.

# Relationships
## Builds Upon
- **connected-graph**, **cycle** (by its absence)

## Enables
- **spanning-tree** — a spanning subgraph that is a tree
- **rooted-tree** — a tree with a designated root
- **normal-spanning-tree** — a rooted spanning tree with special properties

## Related
- **forest** — a graph whose components are trees
- **leaf** — a vertex of degree 1 in a tree

## Contrasts With
- **forest** — a forest may be disconnected

# Common Errors
- **Error**: Forgetting that a single vertex (K^1) is a tree
  **Correction**: A single vertex is a (trivial) tree with 0 edges

# Common Confusions
- **Confusion**: Thinking trees must have leaves
  **Clarification**: K^1 is a tree with no leaves; all non-trivial trees have at least one leaf

# Source Reference
Chapter 1: The Basics, Section 1.5, pages 13-14 (pdf pp. 23-24). Theorem 1.5.1, Corollaries 1.5.2-1.5.4.

# Verification Notes
- Definition from p. 13, Theorem 1.5.1 from p. 14
- Confidence: HIGH
