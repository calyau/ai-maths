---
concept: Walk
slug: walk

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 19
section: "1.3 Paths and cycles"

extraction_confidence: high

aliases:
  - "closed walk"

prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - path
  - euler-tour
contrasts_with:
  - path

answers_questions:
  - "What is a walk?"
  - "What is a closed walk?"
---

# Quick Definition
A walk of length k in G is a non-empty alternating sequence v_0 e_0 v_1 e_1 ... e_{k-1} v_k of vertices and edges such that each e_i = {v_i, v_{i+1}}. If v_0 = v_k, the walk is closed.

# Core Definition
A walk (of length k) in a graph G is a non-empty alternating sequence v_0 e_0 v_1 e_1 ... e_{k-1} v_k of vertices and edges in G such that e_i = {v_i, v_{i+1}} for all i < k. If v_0 = v_k, the walk is closed. If the vertices in a walk are all distinct, it defines an obvious path. In general, every walk between two vertices contains a path between these vertices (Diestel, p. 10).

# Prerequisites
- **Graph**, **vertex**, **edge**

# Key Properties
1. A walk may repeat vertices and edges
2. A closed walk starts and ends at the same vertex
3. If all vertices are distinct, the walk defines a path
4. Every walk between two vertices contains a path between them

# Context & Application
Walks are more general than paths. The concept is used in defining Euler tours (closed walks traversing every edge exactly once).

# Relationships
## Builds Upon
- **graph**, **vertex**, **edge**

## Related
- **euler-tour** — a specific type of closed walk

## Contrasts With
- **path** — paths require all vertices to be distinct

# Source Reference
Chapter 1: The Basics, Section 1.3, page 10 (pdf p. 20).

# Verification Notes
- Direct from p. 10
- Confidence: HIGH
