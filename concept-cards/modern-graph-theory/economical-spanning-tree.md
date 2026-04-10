---
concept: Economical Spanning Tree
slug: economical-spanning-tree
category: paths-and-cycles
subcategory: trees-and-forests
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.2 Paths, Cycles, and Trees"
extraction_confidence: high
aliases:
  - minimum spanning tree
  - MST
  - minimum-weight spanning tree
prerequisites:
  - graph
  - spanning-tree
  - tree
extends:
  - spanning-tree
related: []
contrasts_with: []
answers_questions:
  - "What is an economical spanning tree?"
  - "How can a minimum-cost spanning tree be found?"
---

# Quick Definition

An economical spanning tree of a weighted graph $(G, f)$ is a spanning tree $T$ minimizing $f(T) = \sum_{xy \in E(T)} f(xy)$. Four greedy-type algorithms find such a tree.

# Core Definition

"Given a graph $G = (V, E)$ and a positive valued cost function $f$ defined on the edges, find a connected spanning subgraph $T = (V, E')$ of $G$ for which $f(T) = \sum_{xy \in E'} f(xy)$ is minimal. We call such a spanning subgraph $T$ an economical spanning subgraph" (Bollobás, p. 19). Since the economical subgraph must be minimally connected, it is a spanning tree.

# Prerequisites

- **Graph** — Defined for weighted graphs
- **Spanning tree** — The solution is always a spanning tree
- **Tree** — Tree properties enable the greedy algorithms

# Key Properties

1. An economical spanning tree is a spanning tree minimizing total edge cost
2. If no two edges have the same cost, the economical spanning tree is unique (Theorem 10)
3. Four algorithms are described: greedy edge-addition, costly edge-removal, Prim-type growth, and distributed Boruvka-type

# Construction / Recognition

## Method 1 (Kruskal-type, p. 20)
1. Repeatedly select a cheapest available edge that does not create a cycle

## Method 2 (p. 20)
1. Repeatedly delete a costliest edge whose removal does not disconnect the graph

## Method 3 (Prim-type, p. 20)
1. Start at a vertex; repeatedly add the cheapest edge connecting the tree to a non-tree vertex

## Method 4 (Boruvka-type, p. 21)
1. Each vertex (group) builds its cheapest outgoing edge simultaneously; repeat until connected

# Context & Application

The economical spanning tree problem is one of the most practically important problems in combinatorial optimization. It models infrastructure planning (water pipes, cables) and appears in network design. Bollobás illustrates it with a village water-supply problem (p. 20).

# Examples

**Example** (p. 20): Fig. I.8 shows a graph with edge costs and Fig. I.9 shows three of its six economical spanning trees.

**Example** (p. 21): Fig. I.10 shows a graph with a unique economical spanning tree (distinct edge costs).

# Relationships

## Builds Upon
- **Spanning tree** — The solution is a spanning tree

## Enables
- Practical network design and optimization

# Common Errors

- **Error**: Applying a greedy algorithm without checking for cycles (Method 1) or connectivity (Method 2)
  **Correction**: Method 1 must avoid cycles; Method 2 must maintain connectivity

# Common Confusions

- **Confusion**: Thinking the economical spanning tree is always unique
  **Clarification**: It is unique only when no two edges have the same cost (Theorem 10)

# Source Reference

Chapter I: Fundamentals, Section I.2, pages 19-22; Theorem 10, pages 21-22.

# Verification Notes

- Definition source: Direct from pp. 19-20
- Confidence rationale: Explicitly defined with four algorithms and proof
- Uncertainties: None
- Cross-reference status: Verified
