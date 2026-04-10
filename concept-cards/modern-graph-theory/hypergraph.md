---
concept: Hypergraph
slug: hypergraph
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
aliases: []
prerequisites:
  - graph
extends: []
related:
  - bipartite-graph
contrasts_with:
  - graph
answers_questions:
  - "What is a hypergraph?"
---

# Quick Definition

A hypergraph is a pair $(V, E)$ where $E$ is a subset of $\mathcal{P}(V)$, the power set of $V$. Edges (hyperedges) can connect any number of vertices, not just two.

# Core Definition

"A hypergraph is a pair $(V, E)$ such that $V \cap E = \emptyset$ and $E$ is a subset of $\mathcal{P}(V)$, the power set of $V$, that is the set of all subsets of $V$" (Bollobás, p. 15). There is a 1-to-1 correspondence between hypergraphs and certain bipartite graphs via the incidence graph construction.

# Prerequisites

- **Graph** — Hypergraphs generalize graphs

# Key Properties

1. Edges can have any number of vertices (not restricted to pairs)
2. Every graph is a hypergraph where all edges have exactly 2 elements
3. Each hypergraph has an associated bipartite incidence graph

# Construction / Recognition

Given a hypergraph $H = (V, E)$, its incidence graph is the bipartite graph with vertex classes $V$ and $E$, where $x \in V$ is joined to $S \in E$ iff $x \in S$.

# Context & Application

Hypergraphs model multi-way relationships (e.g., committees, reactions). The Fano plane is a classic hypergraph example (Fig. I.6).

# Examples

**Example** (p. 15): The Fano plane, $PG(2, 2)$, is a hypergraph with 7 points and 7 lines, each line containing 3 points (Fig. I.6). Its incidence graph is the Heawood graph (Fig. I.7).

# Relationships

## Builds Upon
- **Graph** — Generalization

## Related
- **Bipartite graph** — The incidence graph of a hypergraph is bipartite

## Contrasts With
- **Graph** — Graph edges have exactly 2 endpoints; hyperedges can have any number

# Common Errors

- **Error**: Assuming hyperedges must contain at least 2 vertices
  **Correction**: A hyperedge can be any subset of $V$, including singletons or the empty set

# Common Confusions

- **Confusion**: Thinking hypergraphs are rare in practice
  **Clarification**: Many combinatorial structures (designs, set systems) are naturally hypergraphs

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, pages 15-16.

# Verification Notes

- Definition source: Direct from p. 15
- Confidence rationale: Explicitly defined with example
- Uncertainties: None
- Cross-reference status: Verified
