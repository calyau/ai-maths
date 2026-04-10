---
concept: Cycle
slug: cycle
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
  - "$C_\\ell$"
  - l-cycle
  - triangle ($C_3$)
  - quadrilateral ($C_4$)
prerequisites:
  - graph
  - path
  - walk
extends: []
related:
  - circuit
  - hamilton-cycle
  - euler-circuit
  - forest
contrasts_with:
  - circuit
  - path
answers_questions:
  - "What is a cycle in a graph?"
---

# Quick Definition

A cycle is a closed walk $x_1 x_2 \cdots x_l$ of length $l \ge 3$ where the vertices $x_1, \ldots, x_l$ are all distinct. The symbol $C_l$ denotes a cycle of length $l$.

# Core Definition

"If a walk $W = x_0 x_1 \cdots x_l$ is such that $l \ge 3$, $x_0 = x_l$, and the vertices $x_i$, $0 < i < l$, are distinct from each other and $x_0$, then $W$ is said to be a cycle. For simplicity this cycle is denoted by $x_1 x_2 \cdots x_l$" (Bollobás, p. 12). A cycle has neither a starting vertex nor a direction, so various rotations and reflections denote the same cycle. $C_3$ is a triangle, $C_4$ a quadrilateral, $C_5$ a pentagon. A cycle is even (odd) if its length is even (odd).

# Prerequisites

- **Graph** — Cycles exist within graphs
- **Path** — A cycle is essentially a "closed path"
- **Walk** — A cycle is defined as a special walk

# Key Properties

1. Length $l \ge 3$
2. All internal vertices are distinct from each other and from the start/end vertex
3. A cycle has no distinguished starting vertex or direction
4. $C_l$ has $l$ vertices and $l$ edges
5. The edge set of a graph can be partitioned into cycles iff every vertex has even degree (Theorem 1)

# Construction / Recognition

## To recognize a cycle
1. Verify it is a connected graph where every vertex has degree exactly 2
2. Verify it has at least 3 vertices

# Context & Application

Cycles are fundamental structures in graph theory. Their presence or absence determines key properties: a graph without cycles is a forest/tree, bipartite graphs are exactly those with no odd cycles (Theorem 4), and Euler's formula for planar graphs relies on cycle structure.

# Examples

**Example** (p. 12): $C_4$ and $C_5$ are shown in Fig. I.4.

**Example** (Theorem 1, p. 12): The edge set of a graph can be partitioned into cycles iff every vertex has even degree.

# Relationships

## Builds Upon
- **Graph**, **Path**, **Walk**

## Enables
- **Forest** — A graph with no cycles
- **Tree** — A connected graph with no cycles
- **Bipartite graph** — Characterized by the absence of odd cycles
- **Hamilton cycle** — A cycle through all vertices
- **Girth** — Length of a shortest cycle

## Contrasts With
- **Circuit** — A circuit is a closed trail; a cycle requires distinct vertices
- **Path** — A path is open-ended; a cycle is closed

# Common Errors

- **Error**: Including cycles of length 1 or 2 in simple graphs
  **Correction**: In simple graphs, cycles have length $\ge 3$; length-1 (loops) and length-2 cycles require multigraphs

# Common Confusions

- **Confusion**: Confusing cycle and circuit
  **Clarification**: A cycle has distinct vertices; a circuit has distinct edges but may repeat vertices

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, pages 12-13.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
