---
concept: Bridge
slug: bridge
category: graph-fundamentals
subcategory: connectivity
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
  - bridge edge
  - isthmus
prerequisites:
  - graph
  - connected-graph
  - component
extends: []
related:
  - cutvertex
  - tree
contrasts_with:
  - cutvertex
answers_questions:
  - "What is a bridge in a graph?"
---

# Quick Definition

A bridge is an edge whose deletion increases the number of components. In a connected graph, a bridge is an edge whose deletion disconnects the graph.

# Core Definition

"An edge is a bridge if its deletion increases the number of components. Thus an edge of a connected graph is a bridge if its deletion disconnects the graph" (Bollobás, p. 14). Theorem 3 implies that "an edge is a bridge iff it is not contained in a cycle" (p. 16).

# Prerequisites

- **Graph** — Bridges are edges of graphs
- **Connected graph** — Bridges disconnect connected graphs
- **Component** — Bridge deletion increases component count

# Key Properties

1. An edge is a bridge iff it is not contained in any cycle
2. Every edge of a tree is a bridge (Theorem 6)
3. A connected graph is a tree iff every edge is a bridge (Theorem 6)
4. A regular bipartite graph of degree $\ge 2$ has no bridge

# Construction / Recognition

To identify bridges: check each edge $e$; it is a bridge iff $G - e$ has more components than $G$, equivalently iff $e$ lies in no cycle.

# Context & Application

Bridges represent critical connections in a network — their removal disconnects parts of the network. In a tree, every edge is a bridge, which characterizes trees as minimally connected graphs.

# Examples

**Example** (p. 17): In the tree characterization (Theorem 6), a connected graph $G$ is a tree iff every edge is a bridge — $G$ is a minimal connected graph.

# Relationships

## Builds Upon
- **Graph**, **Connected graph**, **Component**

## Enables
- **Tree** — Characterized as connected graphs where every edge is a bridge

## Contrasts With
- **Cutvertex** — A cutvertex is a vertex; a bridge is an edge

# Common Errors

- **Error**: Assuming a bridge must connect two large subgraphs
  **Correction**: A bridge can connect a single vertex to the rest (a pendant edge)

# Common Confusions

- **Confusion**: Thinking removing a bridge only separates one vertex
  **Clarification**: A bridge can separate the graph into components of any size

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 14; Theorem 3, page 16.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
