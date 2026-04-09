---
concept: Complement
slug: complement

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
  - "complement graph"
  - "G-bar"

prerequisites:
  - graph
  - edge
extends: []
related:
  - complete-graph
  - independent-set
contrasts_with: []

answers_questions:
  - "What is the complement of a graph?"
---

# Quick Definition
The complement of a graph G = (V, E) is the graph on V whose edge set consists of all pairs of vertices that are not edges in G.

# Core Definition
The complement G-bar of G is the graph on V with edge set [V]^2 minus E (Diestel, p. 4).

# Prerequisites
- **Graph** — the complement is defined relative to a graph
- **Edge** — the complement swaps edges and non-edges

# Key Properties
1. The complement has the same vertex set as G
2. An edge is in G-bar if and only if it is not in G
3. The complement of the complement is the original graph
4. G union G-bar = K^n (where n = |G|)
5. The complement of K^n is the edgeless graph; the complement of the edgeless graph is K^n

# Construction / Recognition
To construct G-bar, keep all vertices of G and include exactly those edges that are absent from G.

# Examples
**Example** (p. 4): Fig. 1.1.4 shows a graph isomorphic to its complement (a self-complementary graph).

# Relationships
## Builds Upon
- **graph**

## Related
- **complete-graph** — complement of the empty graph
- **independent-set** — an independent set in G is a clique in G-bar

# Source Reference
Chapter 1: The Basics, Section 1.1, page 4 (pdf p. 14). See Fig. 1.1.4.

# Verification Notes
- Direct from p. 4
- Confidence: HIGH
