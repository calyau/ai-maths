---
concept: Empty Graph
slug: empty-graph
category: graph-fundamentals
subcategory: special-graphs
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
  - "$\\overline{K}_n$"
  - "$E_n$"
  - edgeless graph
prerequisites:
  - graph
extends:
  - graph
related:
  - complete-graph
  - graph-complement
  - independent-set
contrasts_with:
  - complete-graph
answers_questions:
  - "What is an empty graph?"
---

# Quick Definition

The empty graph $E_n = \overline{K}_n$ is the graph of order $n$ with no edges. No two vertices are adjacent.

# Core Definition

"An empty $n$-graph $E_n$ has order $n$ and no edges. [...] In $E_n$ no two vertices are adjacent" (Bollobás, p. 11). The notation $\overline{K}_n$ is frequently used since the empty graph is the complement of the complete graph.

# Prerequisites

- **Graph** — The empty graph is a graph

# Key Properties

1. $E_n$ has order $n$ and size 0
2. Every vertex is isolated (degree 0)
3. $E_n = \overline{K}_n$ — it is the complement of $K_n$
4. $K_1 = E_1$ — the trivial graph

# Construction / Recognition

Take $n$ vertices with no edges.

# Context & Application

The empty graph represents the extreme case of no connections. It appears in the definition of independent sets: $W \subset V(G)$ consists of independent vertices iff $G[W]$ is an empty graph.

# Examples

**Example** (p. 12): $E_3$ is shown in Fig. I.4.

# Relationships

## Builds Upon
- **Graph**

## Enables
- **Independent set** — An independent vertex set induces an empty subgraph

## Contrasts With
- **Complete graph** — $K_n$ has all possible edges; $E_n$ has none

# Common Errors

- **Error**: Confusing the empty graph $E_n$ with the edge set notation $E(G)$
  **Correction**: Context disambiguates; $\overline{K}_n$ notation avoids confusion

# Common Confusions

- **Confusion**: Thinking an empty graph has no vertices
  **Clarification**: An empty graph has $n$ vertices but no edges

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 11.

# Verification Notes

- Definition source: Direct from p. 11
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
