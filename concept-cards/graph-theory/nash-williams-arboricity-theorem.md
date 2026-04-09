---
concept: Nash-Williams Arboricity Theorem
slug: nash-williams-arboricity-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 59
section: "2.4 Tree-packing and arboricity"
extraction_confidence: high
aliases:
  - "Nash-Williams 1964"
  - "forest partition theorem"
prerequisites:
  - arboricity
  - forest
extends: []
related:
  - nash-williams-tutte-theorem
contrasts_with: []
answers_questions:
  - "When can a graph be partitioned into at most k forests?"
---

# Quick Definition
A multigraph G can be partitioned into at most k forests if and only if ||G[U]|| <= k(|U|-1) for every non-empty vertex set U.

# Core Definition
**Theorem 2.4.4 (Nash-Williams 1964).** A multigraph G = (V, E) can be partitioned into at most k forests if and only if ||G[U]|| <= k(|U|-1) for every non-empty set U contained in V (Diestel, p. 59).

# Prerequisites
- **Arboricity** — the theorem characterizes arboricity
- **Forest** — the edge set is partitioned into forests

# Key Properties
1. The condition bounds the edge density of every induced subgraph
2. Each forest on U has at most |U|-1 edges, so k forests have at most k(|U|-1) edges
3. The proof reuses Lemma 2.4.3 from the spanning tree packing theorem
4. Provides an exact characterization of arboricity

# Construction / Recognition
## Proof Strategy
1. Use the same edge-replacement framework as Theorem 2.4.1
2. If some edge e is not in any forest of an optimal k-tuple
3. Lemma 2.4.3 gives a set U connected in all forests, containing the ends of e
4. Then ||G[U]|| > k(|U|-1), contradicting the assumption

# Context & Application
This theorem is the covering dual of the spanning tree packing theorem. While Theorem 2.4.1 characterizes how many edge-disjoint spanning trees can be packed, Theorem 2.4.4 characterizes how few forests suffice to cover all edges.

# Examples
**Example**: For a graph where every induced subgraph on U vertices has at most 2(|U|-1) edges, the edges can be partitioned into 2 forests.

# Relationships
## Builds Upon
- **Arboricity**, **forest**

## Related
- **Nash-Williams-Tutte theorem** — the packing dual

# Common Errors
- **Error**: Checking the condition only for V
  **Correction**: The condition must hold for all non-empty subsets U of V

# Common Confusions
- **Confusion**: Confusing with the spanning tree packing theorem
  **Clarification**: Spanning tree packing uses spanning trees and partitions of V; arboricity uses forests and subsets U

# Source Reference
Chapter 2, Section 2.4, Theorem 2.4.4, p. 59 (pdf p. 59).

# Verification Notes
- Theorem from p. 59
- Confidence: HIGH — explicitly stated theorem
