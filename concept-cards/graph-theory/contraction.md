---
concept: Contraction
slug: contraction

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 28
section: "1.7 Contraction and minors"

extraction_confidence: high

aliases:
  - "G/e"
  - "edge contraction"

prerequisites:
  - graph
  - edge
  - adjacent
extends: []
related:
  - minor
  - topological-minor
  - subdivision
contrasts_with: []

answers_questions:
  - "What is an edge contraction?"
  - "What does G/e mean?"
---

# Quick Definition
Contracting an edge e = xy in G means merging x and y into a new vertex v_e that is adjacent to all former neighbours of x and y. The resulting graph is denoted G/e.

# Core Definition
Let e = xy be an edge of a graph G = (V, E). By G/e we denote the graph obtained from G by contracting the edge e into a new vertex v_e, which becomes adjacent to all the former neighbours of x and of y. Formally, G/e is a graph (V', E') with vertex set V' := (V minus {x, y}) union {v_e} and edges preserving all adjacencies except those involving x and y, which are redirected to v_e (Diestel, p. 19).

# Prerequisites
- **Graph**, **edge**, **adjacent** — contraction merges adjacent vertices

# Key Properties
1. Contraction reduces the number of vertices by 1
2. The contracted vertex v_e is adjacent to all former neighbors of both x and y
3. Parallel edges and loops that might arise are deleted (in simple graphs)
4. G is an MX if and only if X can be obtained from G by a series of edge contractions (Proposition 1.7.1)

# Construction / Recognition
## To Contract Edge e = xy
1. Remove vertices x and y and all their incident edges
2. Add a new vertex v_e
3. Connect v_e to all vertices that were neighbors of x or y (excluding x and y themselves)

# Context & Application
Contraction is one of the fundamental graph operations. Together with deletion, it defines the minor relation.

# Examples
**Example** (p. 19): Fig. 1.7.1 shows the contraction of edge e = xy.

# Relationships
## Builds Upon
- **graph**, **edge**, **adjacent**

## Enables
- **minor** — obtained by deletions and contractions
- **topological-minor** — related but uses subdivision instead

# Source Reference
Chapter 1: The Basics, Section 1.7, page 19 (pdf p. 29). See Fig. 1.7.1.

# Verification Notes
- Direct from p. 19
- Confidence: HIGH
