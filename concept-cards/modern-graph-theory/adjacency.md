---
concept: Adjacency
slug: adjacency
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
  - neighbouring
  - adjacent vertices
  - incidence
prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - neighbourhood
  - vertex-degree
contrasts_with: []
answers_questions:
  - "When are two vertices adjacent in a graph?"
  - "What does it mean for vertices to be incident with an edge?"
---

# Quick Definition

Two vertices $x$ and $y$ are adjacent (or neighbouring) if $xy \in E(G)$. Two edges are adjacent if they share exactly one common endvertex.

# Core Definition

"If $xy \in E(G)$, then $x$ and $y$ are adjacent, or neighbouring, vertices of $G$, and the vertices $x$ and $y$ are incident with the edge $xy$. Two edges are adjacent if they have exactly one common endvertex" (Bollobás, p. 9). The notation $x \sim y$ means that vertex $x$ is adjacent to vertex $y$.

# Prerequisites

- **Graph** — Adjacency is defined within the context of a graph
- **Vertex** — Adjacency is a relation between vertices
- **Edge** — Adjacency holds when an edge connects two vertices

# Key Properties

1. Adjacency of vertices is symmetric: if $x \sim y$ then $y \sim x$
2. $y \in \Gamma(x)$, $x \in \Gamma(y)$, $x \sim y$, $y \sim x$ are all equivalent — each means $xy$ is an edge
3. Vertex adjacency and edge incidence are the two fundamental relations in a graph
4. Adjacency of edges requires exactly one shared endvertex, not two

# Construction / Recognition

To check adjacency of vertices $x$ and $y$: verify that $\{x, y\} \in E(G)$.

# Context & Application

Adjacency is the most basic relation in graph theory. It determines the entire structure of the graph and is the basis for defining paths, connectivity, colourings, and virtually all graph-theoretic properties.

# Examples

**Example** (p. 9): In the graph of Fig. I.1, vertices 1 and 2 are adjacent since $12 \in E(G)$.

# Relationships

## Builds Upon
- **Graph**, **Vertex**, **Edge**

## Enables
- **Neighbourhood** — The set of vertices adjacent to a given vertex
- **Vertex degree** — Count of adjacent vertices
- **Connected graph** — Defined via paths, which are sequences of adjacent vertices

## Related
- **Graph isomorphism** — Preserves adjacency

# Common Errors

- **Error**: Saying two edges are adjacent when they share both endvertices
  **Correction**: Two edges are adjacent only if they share exactly one endvertex

# Common Confusions

- **Confusion**: Confusing vertex adjacency with edge adjacency
  **Clarification**: Vertex adjacency means joined by an edge; edge adjacency means sharing one endvertex

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 9.

# Verification Notes

- Definition source: Direct quote from p. 9
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
