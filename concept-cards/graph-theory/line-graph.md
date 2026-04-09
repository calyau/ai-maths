---
concept: Line Graph
slug: line-graph

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
  - "L(G)"

prerequisites:
  - graph
  - edge
  - adjacent
extends: []
related:
  - complement
contrasts_with: []

answers_questions:
  - "What is a line graph?"
  - "What is L(G)?"
---

# Quick Definition
The line graph L(G) of G is the graph on E(G) in which two vertices (edges of G) are adjacent if and only if they are adjacent as edges in G.

# Core Definition
The line graph L(G) of G is the graph on E in which x, y in E are adjacent as vertices if and only if they are adjacent as edges in G (Diestel, p. 4).

# Prerequisites
- **Graph** — the line graph is derived from a graph
- **Edge** — edges of G become vertices of L(G)
- **Adjacent** — adjacency of edges in G determines adjacency in L(G)

# Key Properties
1. Vertices of L(G) correspond to edges of G
2. Two vertices of L(G) are adjacent iff the corresponding edges of G share an endpoint
3. |V(L(G))| = |E(G)|

# Construction / Recognition
1. Create one vertex in L(G) for each edge of G
2. Connect two vertices in L(G) if the corresponding edges of G share an endpoint

# Context & Application
Line graphs transform edge-based problems into vertex-based problems. Edge coloring of G corresponds to vertex coloring of L(G).

# Relationships
## Builds Upon
- **graph**, **edge**, **adjacent**

# Source Reference
Chapter 1: The Basics, Section 1.1, page 4 (pdf p. 14).

# Verification Notes
- Direct from p. 4
- Confidence: HIGH
