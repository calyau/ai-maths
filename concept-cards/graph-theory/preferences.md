---
concept: Preferences
slug: preferences
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 48
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "set of preferences"
  - "linear ordering on edges"
prerequisites:
  - graph
extends: []
related:
  - stable-matching
contrasts_with: []
answers_questions:
  - "What are preferences in matching theory?"
---

# Quick Definition
A set of preferences for a graph G is a family of linear orderings (<=_v) on E(v) for each vertex v, expressing each vertex's ranking of its incident edges.

# Core Definition
A family (<=_v)_{v in V} of linear orderings <=_v on E(v) is a **set of preferences** for G. Each vertex v ranks its incident edges from least to most preferred (Diestel, p. 48).

# Prerequisites
- **Graph** — preferences are defined on vertices of a graph

# Key Properties
1. Each vertex has a total ordering of its incident edges
2. Preferences define which matching edges are preferred
3. A matching is stable if no unmatched edge would be mutually preferred
4. Every bipartite graph with preferences has a stable matching (Theorem 2.1.4)

# Context & Application
Preferences model the situation where participants have ranked choices, as in the college admissions problem or organ donor matching.

# Examples
**Example** (p. 48): For the stable marriage theorem, preferences determine which matchings are stable.

# Relationships
## Related
- **Stable matching** — stability is defined relative to preferences

# Source Reference
Chapter 2, Section 2.1, p. 48 (pdf p. 48).

# Verification Notes
- Definition from p. 48
- Confidence: HIGH — explicitly defined
