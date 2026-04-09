---
concept: Connected Graph
slug: connected-graph

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 20
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "connected"
  - "disconnected"

prerequisites:
  - graph
  - path
extends: []
related:
  - component
  - k-connected
  - separator
contrasts_with: []

answers_questions:
  - "What is a connected graph?"
  - "When is a graph connected?"
---

# Quick Definition
A non-empty graph G is connected if any two of its vertices are linked by a path in G. A graph that is not connected is disconnected.

# Core Definition
A non-empty graph G is called connected if any two of its vertices are linked by a path in G. If U is a subset of V(G) and G[U] is connected, we also call U itself connected (in G). Instead of 'not connected' we usually say 'disconnected' (Diestel, p. 10).

# Prerequisites
- **Graph** — connectivity is a graph property
- **Path** — defined via existence of paths

# Key Properties
1. A connected graph is non-empty by definition
2. The vertices of a connected graph can be enumerated v_1, ..., v_n so that G[v_1, ..., v_i] is connected for every i (Proposition 1.4.1)
3. Every connected graph contains a spanning tree

# Context & Application
Connectivity is one of the most basic graph properties. Most graph algorithms assume or exploit connectivity.

# Examples
**Example** (p. 11): Fig. 1.4.1 shows a graph with three components.

# Relationships
## Builds Upon
- **graph**, **path**

## Enables
- **component** — maximal connected subgraphs
- **k-connected** — higher connectivity
- **spanning-tree** — exists in every connected graph

# Common Confusions
- **Confusion**: Thinking the empty graph is connected
  **Clarification**: By Diestel's definition, a connected graph must be non-empty

# Source Reference
Chapter 1: The Basics, Section 1.4, page 10 (pdf p. 20).

# Verification Notes
- Direct from p. 10
- Confidence: HIGH
