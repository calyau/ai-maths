---
concept: "Tutte's 1-Factor Theorem"
slug: tuttes-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 49
section: "2.2 Matching in general graphs"
extraction_confidence: high
aliases:
  - "Tutte's theorem"
  - "Tutte 1947"
  - "1-factor theorem"
prerequisites:
  - tuttes-condition
  - one-factor
  - odd-component
extends:
  - halls-marriage-theorem
related:
  - tutte-berge-formula
  - factor-critical-graph
  - petersens-theorem-1-factor
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "When does a graph have a 1-factor?"
  - "What is Tutte's theorem?"
---

# Quick Definition
A graph G has a 1-factor if and only if q(G-S) <= |S| for every set S of vertices, where q counts odd components.

# Core Definition
**Theorem 2.2.1 (Tutte 1947).** A graph G has a 1-factor if and only if q(G-S) <= |S| for all S contained in V(G) (Diestel, p. 49).

# Prerequisites
- **Tutte's condition** — the condition q(G-S) <= |S|
- **One-factor** — a perfect matching; the object whose existence is characterized
- **Odd component** — the condition counts odd components

# Key Properties
1. The forward direction is obvious: each odd component of G-S sends a factor edge to S
2. The reverse direction is the deep result
3. The proof assumes G is edge-maximal without a 1-factor and derives a contradiction
4. In the edge-maximal case, all components of G-S are complete and every vertex of S is adjacent to all of G-S
5. Implies Petersen's theorem: every bridgeless cubic graph has a 1-factor (Corollary 2.2.2)

# Construction / Recognition
## Proof Strategy (First Proof)
1. Assume G has no 1-factor but is edge-maximal with this property
2. Show that all components of G-S must be complete graphs
3. Show every vertex s in S is adjacent to all vertices outside S
4. Derive a contradiction using alternating paths in M1 and M2

## Proof Strategy (Second Proof, Theorem 2.2.3)
1. Find a set S satisfying properties (i) matchable to components and (ii) all components factor-critical
2. Deduce Tutte's theorem from this structural result

# Context & Application
Tutte's theorem is the definitive generalization of Hall's theorem to non-bipartite graphs. While Hall's theorem characterizes matchings of one side in bipartite graphs, Tutte's theorem characterizes perfect matchings in arbitrary graphs. It is one of the most important results in matching theory. The theorem can also be derived from Mader's theorem (Exercise 21, Ch. 3).

# Examples
**Example** (p. 50): A graph with bad set S where q(G-S) = 3 and |S| = 3, so Tutte's condition is satisfied (q = 3 <= 3 = |S|). The contracted graph G_S shows the structure.

# Relationships
## Builds Upon
- **Tutte's condition**, **one-factor**, **odd component**

## Enables
- **Petersen's theorem (1-factor)** — bridgeless cubic graphs have 1-factors
- **Tutte-Berge formula** — extension to maximum matching size
- **Gallai-Edmonds structure theorem** — deeper structural result (Theorem 2.2.3)

## Related
- **Hall's marriage theorem** — bipartite special case
- **Menger's theorem** — Tutte's theorem can be derived from Mader's theorem

# Common Errors
- **Error**: Applying Tutte's condition only for S = empty set
  **Correction**: The condition must hold for all subsets S of V(G)

# Common Confusions
- **Confusion**: Confusing Tutte's theorem with the Tutte-Berge formula
  **Clarification**: Tutte's theorem characterizes 1-factor existence; the Tutte-Berge formula gives the maximum matching size

# Source Reference
Chapter 2, Section 2.2, Theorem 2.2.1, pp. 49-51 (pdf pp. 49-51). Two proofs given.

# Verification Notes
- Theorem statement from p. 49
- Two proofs spanning pp. 49-52
- Confidence: HIGH — major named theorem with full proofs
