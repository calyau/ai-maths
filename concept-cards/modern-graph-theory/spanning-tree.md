---
concept: Spanning Tree
slug: spanning-tree
category: paths-and-cycles
subcategory: trees-and-forests
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.2 Paths, Cycles, and Trees"
extraction_confidence: high
aliases: []
prerequisites:
  - tree
  - connected-graph
  - spanning-subgraph
extends:
  - tree
related:
  - economical-spanning-tree
  - matrix-tree-theorem
  - kirchhoffs-theorem-spanning-trees
contrasts_with: []
answers_questions:
  - "What is a spanning tree?"
  - "Does every connected graph have a spanning tree?"
---

# Quick Definition

A spanning tree of a connected graph $G$ is a tree that is a spanning subgraph of $G$ — it contains all vertices of $G$ and is connected and acyclic. Every connected graph contains a spanning tree.

# Core Definition

"**Corollary 7.** Every connected graph contains a spanning tree, that is, a tree containing every vertex of the graph. *Proof.* Take a minimal connected spanning subgraph" (Bollobás, p. 18).

A spanning tree of order $n$ has exactly $n - 1$ edges. There are two standard constructions: (1) BFS tree from a root $x$ using distance layers $V_i = \{y : d(x, y) = i\}$, and (2) incremental construction by adding edges one at a time while maintaining a tree (pp. 18-19).

# Prerequisites

- **Tree** — A spanning tree is a tree
- **Connected graph** — Only connected graphs have spanning trees
- **Spanning subgraph** — A spanning tree spans all vertices

# Key Properties

1. Contains all $n$ vertices and exactly $n - 1$ edges
2. Every connected graph has at least one spanning tree
3. A spanning tree is a minimal connected spanning subgraph (Theorem 6)
4. A spanning tree is a maximal acyclic spanning subgraph (Theorem 6)
5. Adding any non-tree edge creates exactly one cycle (the fundamental cycle)
6. Deleting any tree edge disconnects the tree into two components (the fundamental cut)

# Construction / Recognition

## BFS Construction (p. 18)
1. Pick vertex $x$; set $V_0 = \{x\}$
2. For each $y \in V_i$ ($i > 0$), choose one neighbour $y'$ in $V_{i-1}$
3. The edges $\{yy' : y \neq x\}$ form a spanning tree

## Incremental Construction (p. 18)
1. Start with a single vertex $x$
2. Repeatedly add a vertex $y$ adjacent (in $G$) to the current tree, along with the edge $yz$
3. Continue until all vertices are included

# Context & Application

Spanning trees are central to graph theory and its applications. They underpin Kirchhoff's theorem (current distribution in networks), the matrix-tree theorem (counting spanning trees), electrical network theory, and optimization (economical spanning trees). As Bollobás emphasizes in Chapter II: "virtually the only concept to be used is that of a spanning tree."

# Examples

**Example** (pp. 18-19): Two constructions of spanning trees are given, both producing trees of order $n$ and size $n - 1$.

**Example** (pp. 20-21): Four methods for finding economical (minimum-weight) spanning trees are described.

# Relationships

## Builds Upon
- **Tree** — A spanning tree is a tree
- **Connected graph** — Existence requires connectivity
- **Spanning subgraph** — A spanning tree is a spanning subgraph

## Enables
- **Economical spanning tree** — Minimum-cost spanning tree
- **Kirchhoff's theorem** — Currents expressed via spanning trees
- **Matrix-tree theorem** — Counting spanning trees
- **Fundamental cycle** — Created by adding a chord to a spanning tree
- **Fundamental cut** — Created by removing a tree edge

# Common Errors

- **Error**: Thinking a graph has a unique spanning tree
  **Correction**: A connected graph typically has many spanning trees; uniqueness holds only for trees

# Common Confusions

- **Confusion**: Confusing spanning tree with any tree subgraph
  **Clarification**: A spanning tree must include all vertices of the graph

# Source Reference

Chapter I: Fundamentals, Section I.2, Corollary 7, pages 18-19.

# Verification Notes

- Definition source: Direct from p. 18
- Confidence rationale: Explicitly defined with two constructions
- Uncertainties: None
- Cross-reference status: Verified
