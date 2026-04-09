---
concept: Wave
slug: wave
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 228
section: "8.4 Connectivity and matching"
extraction_confidence: high
aliases:
  - "A-to-B wave"
prerequisites:
  - infinite-graph
  - infinite-mengers-theorem
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is a wave in infinite graph theory?"
---

# Quick Definition
An A-to-B wave in G is a family W = (W_a | a in A) of disjoint paths starting at a in A such that the set Z of final vertices of paths in W separates A from B in G.

# Core Definition
Given sets A, B of vertices, let W = (W_a | a in A) be a family of disjoint paths such that every W_a starts in a. W is an *A -> B wave* in G if the set Z of final vertices of paths in W separates A from B in G. The boundary X of the wave is the set of vertices in Z that either lie in B or have a neighbour in the component towards B. A wave is *large* if all paths are finite and X = Z; otherwise it is *small* (Diestel, p. 228).

# Prerequisites
- **Infinite graph** — Waves are a tool for infinite Menger's theorem
- **Infinite Menger's theorem** — Waves are central to its proof

# Key Properties
1. Waves may contain infinite paths (rays)
2. A wave is large if all paths are finite and the boundary equals the separator
3. A maximal wave always exists (by Zorn's lemma on the ordering W <= W' iff each path in W is an initial segment of the corresponding path in W')
4. Waves can be composed: if U is an A->B wave with boundary X, and V is an X->B wave, then U+V is an A->B wave

# Context & Application
Waves are the key technical tool in proving the infinite Menger's theorem for countable graphs. The proof strategy: find a maximal wave, then show that a maximal wave can be extended to a system of disjoint A-B paths.

# Relationships
## Enables
- Proof of the infinite Menger's theorem (Theorem 8.4.2)

# Source Reference
Chapter 8, Section 8.4, pages 228-229.

# Verification Notes
- Definition from pp. 228-229
- Confidence: HIGH — explicit definition
