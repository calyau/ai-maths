---
concept: Vertex
slug: vertex
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
  - node
  - point
prerequisites: []
extends: []
related:
  - graph
  - edge
  - neighbourhood
  - vertex-degree
contrasts_with: []
answers_questions:
  - "What is a vertex in a graph?"
---

# Quick Definition

A vertex is a fundamental element of a graph; vertices are the objects that may be connected by edges. The set of all vertices of a graph $G$ is denoted $V(G)$.

# Core Definition

In the definition of a graph $G = (V, E)$, the set $V$ is the set of vertices (Bollobás, p. 9). An edge $\{x, y\}$ is said to join the vertices $x$ and $y$, and these are called the endvertices of the edge. If $xy \in E(G)$, then $x$ and $y$ are adjacent or neighbouring vertices, and they are incident with the edge $xy$.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Each vertex belongs to exactly one component of a graph
2. The notation $x \in G$ is sometimes used as shorthand for $x \in V(G)$
3. Two vertices are adjacent if joined by an edge
4. A vertex is incident with each edge that has it as an endvertex
5. A vertex of degree 0 is called an isolated vertex

# Construction / Recognition

Vertices are the primitive elements of a graph; they are given, not constructed.

# Context & Application

Vertices represent the objects in the system being modelled. In network contexts, vertices might represent cities, people, molecules, or any discrete entities with pairwise relationships.

# Examples

**Example** (p. 9): In the graph of Fig. I.1, the vertices are $1, 2, \ldots, 9$.

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Edge** — Edges connect pairs of vertices
- **Neighbourhood** — Defined as the set of vertices adjacent to a given vertex
- **Vertex degree** — The number of neighbours of a vertex

## Related
- **Graph** — A vertex is a fundamental component of a graph

# Common Errors

- **Error**: Confusing a vertex with an edge
  **Correction**: Vertices are the points; edges are the connections between them

# Common Confusions

- **Confusion**: Assuming vertices must have at least one edge
  **Clarification**: A vertex may be isolated (degree 0)

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 9.

# Verification Notes

- Definition source: Direct from p. 9
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
