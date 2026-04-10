---
# === CORE IDENTIFICATION ===
concept: Graph
slug: graph

# === CLASSIFICATION ===
category: graph-fundamentals
subcategory: basic-definitions
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - simple graph

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - vertex
  - edge
  - multigraph
  - directed-graph
contrasts_with:
  - multigraph
  - hypergraph
  - directed-graph

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a graph (in the formal sense)?"
  - "What are the components of a graph's formal definition?"
---

# Quick Definition

A graph $G$ is an ordered pair $(V, E)$ of disjoint sets where $E$ is a subset of the set $V^{(2)}$ of unordered pairs of $V$. The set $V$ is the set of vertices and $E$ is the set of edges.

# Core Definition

"A graph $G$ is an ordered pair of disjoint sets $(V, E)$ such that $E$ is a subset of the set $V^{(2)}$ of unordered pairs of $V$. Unless it is explicitly stated otherwise, we consider only finite graphs, that is, $V$ and $E$ are always finite. The set $V$ is the set of vertices and $E$ is the set of edges" (Bollobás, p. 9). An edge $\{x, y\}$ is denoted $xy$, and the vertices $x$ and $y$ are the endvertices of this edge.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A graph consists of two sets: a vertex set $V(G)$ and an edge set $E(G)$
2. Edges are unordered pairs of vertices, so $xy$ and $yx$ denote the same edge
3. By default, only finite graphs are considered
4. A graph contains no loops (edges joining a vertex to itself) and no multiple edges
5. When there is danger of confusion, graphs are called "simple graphs"

# Construction / Recognition

## To Verify a Graph
1. Check that $V$ and $E$ are finite sets
2. Verify every element of $E$ is an unordered pair of distinct vertices from $V$
3. Confirm no two elements of $E$ join the same pair of vertices (no multiple edges)
4. Confirm no element of $E$ has both endpoints equal (no loops)

# Context & Application

The graph is the fundamental object of study in graph theory. As Bollobás notes, "the basic concepts of graph theory are extraordinarily simple and can be used to express problems from many different subjects." Graphs model pairwise relationships and can represent networks, social connections, molecular structures, and many other real-world structures.

# Examples

**Example 1** (p. 9): The graph with vertices $1, 2, \ldots, 9$ and edges $12, 23, 34, 45, 56, 61, 17, 72, 29, 95, 57, 74, 48, 83, 39, 96, 68$, and $81$ is illustrated in Fig. I.1.

**Example 2** (p. 10): Fig. I.3 shows all graphs (up to isomorphism) of order at most 4 and size 3.

# Relationships

## Builds Upon
- No prerequisites — this is the foundational object of graph theory

## Enables
- **Subgraph** — Defined in terms of a graph
- **Path** — A special type of graph
- **Tree** — A connected acyclic graph
- **Planar graph** — A graph with a special embedding property

## Related
- **Vertex** — The elements of $V(G)$
- **Edge** — The elements of $E(G)$

## Contrasts With
- **Multigraph** — Allows loops and multiple edges
- **Directed graph** — Edges are ordered pairs
- **Hypergraph** — Edges can join any number of vertices

# Common Errors

- **Error**: Including loops or multiple edges in a graph
  **Correction**: By definition, a graph (simple graph) has neither loops nor multiple edges; use multigraph if these are needed

# Common Confusions

- **Confusion**: Thinking a graph must be connected
  **Clarification**: A graph may have multiple components or isolated vertices; connectedness is a separate property
- **Confusion**: Confusing "graph" with "multigraph"
  **Clarification**: A graph forbids loops and multiple edges; a multigraph allows both

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, pages 9-10.

# Verification Notes

- Definition source: Direct quote from p. 9
- Confidence rationale: Explicit formal definition provided
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extractions
