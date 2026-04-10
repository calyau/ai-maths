---
concept: Edge Set Between Vertex Sets
slug: edge-set-between-vertex-sets
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
  - "$E(U, W)$"
  - "$e(U, W)$"
  - cross-edges
prerequisites:
  - graph
  - edge
extends: []
related:
  - cut-space
  - bipartite-graph
contrasts_with: []
answers_questions:
  - "How are edges between vertex subsets counted?"
---

# Quick Definition

For disjoint subsets $U, W \subset V(G)$, $E(U, W)$ denotes the set of edges joining a vertex in $U$ to a vertex in $W$, and $e(U, W) = |E(U, W)|$ is their count.

# Core Definition

"Given disjoint subsets $U$ and $W$ of the vertex set of a graph, we write $E(U, W)$ for the set of $U$-$W$ edges, that is, for the set of edges joining a vertex in $U$ to a vertex in $W$. Also, $e(U, W) = |E(U, W)|$ is the number of $U$-$W$ edges" (Bollobás, p. 10). Subscript notation $E_G(U, W)$ and $e_G(U, W)$ emphasizes the underlying graph.

# Prerequisites

- **Graph** — Defined within graphs
- **Edge** — Counts edges

# Key Properties

1. $E(U, W)$ is defined for disjoint subsets $U, W$
2. $e(U, W) = |E(U, W)|$ counts the cross-edges
3. In a bipartite graph with partition $(V_1, V_2)$: all edges are in $E(V_1, V_2)$
4. For the cut space: cuts are exactly the sets $E(V_1, V_2)$ for partitions $V = V_1 \cup V_2$

# Construction / Recognition

Count all edges with one endpoint in $U$ and the other in $W$.

# Context & Application

This notation is used throughout the text for bipartite structure, cuts, and extremal counting arguments.

# Examples

**Example** (p. 10): In a bipartite graph with vertex classes $V_1$ and $V_2$, $e(V_1, V_2) = e(G)$.

# Relationships

## Builds Upon
- **Graph**, **Edge**

## Enables
- **Cut space** — Cuts are edge sets $E(V_1, V_2)$
- Extremal counting arguments

# Common Errors

- **Error**: Applying $E(U, W)$ when $U$ and $W$ overlap
  **Correction**: The definition requires $U$ and $W$ to be disjoint

# Common Confusions

- **Confusion**: Confusing $E(U, W)$ with the edge set $E(G)$
  **Clarification**: $E(U, W)$ is the set of cross-edges between two specific subsets

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 10.

# Verification Notes

- Definition source: Direct from p. 10
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
