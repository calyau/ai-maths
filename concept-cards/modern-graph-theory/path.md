---
concept: Path
slug: path
category: paths-and-cycles
subcategory: walks-and-trails
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
  - "$P_\\ell$"
  - "x-y path"
prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - walk
  - trail
  - cycle
  - distance
contrasts_with:
  - walk
  - trail
  - cycle
answers_questions:
  - "What is a path in a graph?"
---

# Quick Definition

A path $P$ is a graph with vertices $x_0, x_1, \ldots, x_l$ and edges $x_0 x_1, x_1 x_2, \ldots, x_{l-1} x_l$. The length of $P$ is $l = e(P)$. The symbol $P_\ell$ denotes a path of length $\ell$.

# Core Definition

"A path is a graph $P$ of the form $V(P) = \{x_0, x_1, \ldots, x_l\}$, $E(P) = \{x_0 x_1, x_1 x_2, \ldots, x_{l-1} x_l\}$. This path $P$ is usually denoted by $x_0 x_1 \cdots x_l$. The vertices $x_0$ and $x_l$ are the endvertices of $P$ and $l = e(P)$ is the length of $P$" (Bollobás, p. 12). A path is a walk with distinct vertices.

# Prerequisites

- **Graph** — A path is itself a graph
- **Vertex** — Vertices form the sequence
- **Edge** — Edges connect consecutive vertices

# Key Properties

1. All vertices are distinct
2. The length is the number of edges, not vertices
3. $P_\ell$ has $\ell + 1$ vertices and $\ell$ edges
4. A path has exactly two vertices of degree 1 (the endvertices) and all internal vertices have degree 2
5. Sometimes the initial vertex $x_0$ and terminal vertex $x_l$ are distinguished

# Construction / Recognition

## To recognize a path
1. Verify it is a connected graph
2. Verify exactly two vertices have degree 1 and all others have degree 2
3. Equivalently: verify it is a tree with maximum degree 2

# Context & Application

Paths are the fundamental notion of connectivity in graph theory. The existence of paths between vertices defines connectedness, and the length of shortest paths defines the distance function.

# Examples

**Example** (p. 12): $P_4$ is shown in Fig. I.4, having 5 vertices and 4 edges.

# Relationships

## Builds Upon
- **Graph**, **Vertex**, **Edge**

## Enables
- **Distance** — The minimum length of an $x$-$y$ path
- **Connected graph** — Connected iff every pair of vertices has a path between them
- **Tree** — A connected graph with no cycles; every pair connected by a unique path
- **Hamilton path** — A path containing all vertices

## Contrasts With
- **Walk** — A walk may repeat vertices; a path may not
- **Trail** — A trail has distinct edges but may repeat vertices
- **Cycle** — A cycle is a "closed path" returning to the start

# Common Errors

- **Error**: Confusing path length (edges) with path order (vertices)
  **Correction**: A path of length $\ell$ has $\ell$ edges and $\ell + 1$ vertices

# Common Confusions

- **Confusion**: Using "path" when "walk" is meant
  **Clarification**: A path has distinct vertices; a walk may repeat vertices

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
