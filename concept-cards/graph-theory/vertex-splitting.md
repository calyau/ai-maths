---
concept: Vertex Splitting
slug: vertex-splitting
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 69
section: "3.2 The structure of 3-connected graphs"
extraction_confidence: high
aliases:
  - "vertex expansion"
prerequisites:
  - three-connected-graph
extends: []
related:
  - tuttes-wheel-theorem
  - contractible-edge
contrasts_with:
  - edge-contraction
answers_questions:
  - "What is vertex splitting in the context of 3-connected graphs?"
---

# Quick Definition
Vertex splitting is the reverse of edge contraction: split a vertex v into two adjacent vertices v', v'', distributing v's neighbors between them. Used in Tutte's wheel theorem to build 3-connected graphs.

# Core Definition
In the context of Theorem 3.2.2, **vertex splitting** is the reverse of contraction. Given Gi = Gi+1/xy, the graph Gi+1 is obtained by splitting the contracted vertex v_xy into two adjacent vertices x, y with d(x), d(y) >= 3, distributing the neighbors of v_xy between x and y so that each former neighbor goes to at least one (Diestel, p. 69).

# Prerequisites
- **3-connected graph** — vertex splitting preserves 3-connectedness

# Key Properties
1. Inverse of edge contraction
2. Both new vertices must have degree >= 3
3. Every former neighbor must be adjacent to at least one new vertex
4. Preserves 3-connectedness when conditions are met
5. Starting from K4, all 3-connected graphs can be built by vertex splitting

# Context & Application
Vertex splitting is the constructive operation in Tutte's wheel theorem. It provides an explicit inductive procedure for building all 3-connected graphs from K4.

# Examples
**Example** (p. 69): Starting from K4, split one vertex v into v', v''. Each gets >= 3 edges, and every former neighbor of v gets at least one of v', v''.

# Relationships
## Related
- **Tutte's wheel theorem** — the inductive step is vertex splitting
- **Contractible edge** — contraction is the inverse of splitting

## Contrasts With
- **Edge contraction** — the inverse operation

# Source Reference
Chapter 3, Section 3.2, Theorem 3.2.2, pp. 69-70 (pdf pp. 69-70).

# Verification Notes
- From Theorem 3.2.2 discussion
- Confidence: HIGH — explicitly described
