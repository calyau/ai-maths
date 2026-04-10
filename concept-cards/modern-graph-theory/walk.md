---
concept: Walk
slug: walk
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
aliases: []
prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - path
  - trail
  - circuit
contrasts_with:
  - path
  - trail
answers_questions:
  - "What is a walk in a graph?"
---

# Quick Definition

A walk $W$ in a graph is an alternating sequence of vertices and edges $x_0, e_1, x_1, e_2, \ldots, e_l, x_l$ where $e_i = x_{i-1}x_i$. Vertices and edges may repeat.

# Core Definition

"A walk $W$ in a graph is an alternating sequence of vertices and edges, say $x_0, e_1, x_1, e_2, \ldots, e_l, x_l$ where $e_i = x_{i-1}x_i$, $0 < i \le l$. [...] $W$ is an $x_0$-$x_l$ walk and is denoted by $x_0 x_1 \cdots x_l$; the length of $W$ is $l$" (Bollobás, p. 12).

# Prerequisites

- **Graph** — Walks exist within graphs
- **Vertex** — The sequence alternates vertices
- **Edge** — The sequence alternates edges

# Key Properties

1. Both vertices and edges may be repeated
2. The length is the number of edges traversed
3. A walk with distinct vertices is a path
4. A walk with distinct edges is a trail

# Construction / Recognition

A walk is any sequence of vertices where consecutive vertices are adjacent. No distinctness requirements.

# Context & Application

Walks are the most general notion of traversal in a graph. Every path is a walk, but walks allow revisiting vertices and edges. Walks are used in connectivity proofs and in algebraic graph theory (powers of the adjacency matrix count walks).

# Examples

**Example** (p. 12): In any graph, the sequence $x_0 x_1 x_0$ is a walk of length 2, but not a path (since $x_0$ is repeated) nor a trail (since the edge $x_0 x_1$ is used twice).

# Relationships

## Builds Upon
- **Graph**, **Vertex**, **Edge**

## Enables
- **Path** — A walk with all distinct vertices
- **Trail** — A walk with all distinct edges
- **Circuit** — A closed trail

## Contrasts With
- **Path** — Paths have distinct vertices
- **Trail** — Trails have distinct edges

# Common Errors

- **Error**: Assuming a walk cannot revisit a vertex
  **Correction**: Walks may revisit vertices and edges; paths and trails have additional constraints

# Common Confusions

- **Confusion**: Using "walk" and "path" interchangeably
  **Clarification**: A path is a special case of a walk with distinct vertices

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
