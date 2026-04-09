---
# === CORE IDENTIFICATION ===
concept: Graph
slug: graph

# === CLASSIFICATION ===
category: graph-fundamentals
tier: foundational

# === PROVENANCE ===
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "simple graph"
  - "undirected graph"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - vertex
  - edge
  - graph-isomorphism
  - multigraph
  - directed-graph
  - hypergraph
contrasts_with:
  - multigraph
  - directed-graph
  - hypergraph

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a graph?"
  - "How is a graph formally defined?"
---

# Quick Definition
A graph is a pair G = (V, E) of sets where E consists of 2-element subsets of V. The elements of V are called vertices and the elements of E are called edges.

# Core Definition
A graph is a pair G = (V, E) of sets such that E is a subset of [V]^2, the set of all 2-element subsets of V. It is tacitly assumed that V and E are disjoint. The elements of V are the vertices (or nodes, or points) of the graph G, and the elements of E are its edges (or lines) (Diestel, p. 2, Section 1.1).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. A graph consists of exactly two sets: a vertex set V and an edge set E
2. Every edge is a 2-element subset of V (i.e., edges connect exactly two distinct vertices)
3. There are no loops (edges from a vertex to itself) or multiple edges between the same pair of vertices
4. The graph is undirected: the edge {x, y} is the same as {y, x}
5. Graphs are finite, infinite, countable, etc., according to their order (number of vertices)

# Construction / Recognition
## To Specify a Graph
1. Define a vertex set V
2. Define an edge set E where each element of E is a 2-element subset of V
3. Verify V and E are disjoint

## To Draw a Graph
1. Draw a dot for each vertex
2. Join two dots by a line if the corresponding vertices form an edge
3. The exact placement of dots and lines is irrelevant; only adjacency information matters

# Context & Application
The graph is the central object of study in graph theory. Diestel's definition is the standard modern definition of a simple undirected graph. Except in Chapter 8 (Infinite Graphs), graphs in this text are finite unless otherwise stated.

The notation G = (V, E) is standard. The vertex set of G is referred to as V(G) and its edge set as E(G), regardless of the actual names of the sets.

# Examples
**Example 1** (p. 2): The graph on V = {1, ..., 7} with edge set E = {{1,2}, {1,5}, {2,5}, {3,4}, {5,7}} is depicted in Fig. 1.1.1.

# Relationships
## Builds Upon
- No prerequisites; this is the foundational concept of graph theory

## Enables
- **vertex** and **edge** — components of a graph
- **subgraph**, **induced-subgraph**, **spanning-subgraph** — containment relations
- **graph-isomorphism** — equivalence of graphs
- All further graph-theoretic concepts

## Contrasts With
- **multigraph** — allows loops and multiple edges
- **directed-graph** — edges have direction
- **hypergraph** — edges can connect more than two vertices

# Common Errors
- **Error**: Including loops (edges from a vertex to itself) in a graph
  **Correction**: In Diestel's definition, edges are 2-element subsets of V, so loops are excluded by definition

- **Error**: Treating the edge {x, y} as different from {y, x}
  **Correction**: Graphs are undirected; edge xy is the same as edge yx

# Common Confusions
- **Confusion**: Believing that a graph must be connected
  **Clarification**: A graph may be disconnected, consisting of multiple components, or even be the empty graph

- **Confusion**: Confusing a graph with its drawing
  **Clarification**: A graph is a combinatorial object; its visual representation is irrelevant as long as adjacency information is preserved

# Source Reference
Chapter 1: The Basics, Section 1.1 "Graphs," page 2 (pdf p. 12). See Fig. 1.1.1 for illustration.

# Verification Notes
- Definition directly quoted from p. 2
- Notation V(G), E(G) conventions from same page
- Confidence: HIGH — this is the opening definition of the text, explicitly stated
