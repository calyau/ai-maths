---
concept: Edge
slug: edge
category: graph-fundamentals
subcategory: basic-definitions
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
  - link
prerequisites: []
extends: []
related:
  - graph
  - vertex
  - adjacency
contrasts_with: []
answers_questions:
  - "What is an edge in a graph?"
---

# Quick Definition

An edge is an unordered pair $\{x, y\}$ of vertices in a graph, denoted $xy$. It represents a connection between vertices $x$ and $y$.

# Core Definition

In a graph $G = (V, E)$, the set $E$ is a subset of $V^{(2)}$, the set of unordered pairs of $V$. "An edge $\{x, y\}$ is said to join the vertices $x$ and $y$ and is denoted by $xy$. Thus $xy$ and $yx$ mean exactly the same edge; the vertices $x$ and $y$ are the endvertices of this edge" (Bollobás, p. 9). Two edges are adjacent if they share exactly one common endvertex.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An edge is an unordered pair, so $xy = yx$
2. Each edge has exactly two distinct endvertices
3. Two edges are adjacent if they share exactly one endvertex
4. The number of edges in $G$ is the size of $G$, denoted $e(G)$
5. A graph of order $n$ has at most $\binom{n}{2}$ edges

# Construction / Recognition

An edge $xy$ exists in $G$ if and only if $\{x, y\} \in E(G)$.

# Context & Application

Edges represent the pairwise relationships in the modelled system. The number and arrangement of edges determine the graph's structure and properties.

# Examples

**Example** (p. 9): In the graph of Fig. I.1, $12, 23, 34, 45, 56, 61$ are among the 18 edges.

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Adjacency** — Two vertices are adjacent iff joined by an edge
- **Path** — A sequence of edges forming a route
- **Bridge** — An edge whose removal disconnects a component

## Related
- **Graph** — Edges form one of the two defining sets
- **Vertex** — Each edge connects exactly two vertices

# Common Errors

- **Error**: Treating $xy$ and $yx$ as different edges
  **Correction**: In an undirected graph, $xy = yx$; they are the same edge

# Common Confusions

- **Confusion**: Thinking edges can connect a vertex to itself
  **Clarification**: In a simple graph, edges join distinct vertices; self-loops require a multigraph

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 9.

# Verification Notes

- Definition source: Direct from p. 9
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
