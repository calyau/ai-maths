---
concept: Subgraph
slug: subgraph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "supergraph"
  - "proper subgraph"

prerequisites:
  - graph
extends: []
related:
  - induced-subgraph
  - spanning-subgraph
  - minor
contrasts_with:
  - induced-subgraph
  - spanning-subgraph

answers_questions:
  - "What is a subgraph?"
  - "What is a proper subgraph?"
---

# Quick Definition
A graph G' = (V', E') is a subgraph of G = (V, E) if V' is a subset of V and E' is a subset of E. We write G' is a subset of G.

# Core Definition
If V' is a subset of V and E' is a subset of E, then G' is a subgraph of G (and G a supergraph of G'), written as G' is a subset of G. Less formally, we say that G contains G'. If G' is a subset of G and G' is not equal to G, then G' is a proper subgraph of G (Diestel, p. 4).

# Prerequisites
- **Graph** — subgraphs are themselves graphs

# Key Properties
1. A subgraph must itself be a valid graph (edges must have both endpoints in V')
2. Every graph is a subgraph of itself
3. The empty graph is a subgraph of every graph
4. The subgraph relation is a partial ordering on graphs

# Construction / Recognition
G' is a subgraph of G if and only if V(G') is a subset of V(G) and E(G') is a subset of E(G).

# Context & Application
The subgraph relation is one of four fundamental containment relations between graphs discussed in Chapter 1. The others are induced subgraph, minor, and topological minor.

# Examples
**Example** (p. 4): Fig. 1.1.3 shows a graph G with subgraphs G' and G''. G' is an induced subgraph of G, but G'' is not.

# Relationships
## Builds Upon
- **graph**

## Enables
- **induced-subgraph**, **spanning-subgraph** — special types of subgraphs
- **minor** — obtained by deleting and contracting from subgraphs

## Contrasts With
- **induced-subgraph** — must include all edges between its vertices
- **spanning-subgraph** — must include all vertices of G

# Common Confusions
- **Confusion**: Thinking every subgraph is an induced subgraph
  **Clarification**: A subgraph may omit edges between its vertices; an induced subgraph cannot

# Source Reference
Chapter 1: The Basics, Section 1.1, page 4 (pdf p. 14).

# Verification Notes
- Direct from p. 4
- Confidence: HIGH
