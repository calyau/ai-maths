---
concept: Bramble
slug: bramble
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 332
section: "12.3 Tree-decompositions"
extraction_confidence: high
aliases:
  - "screen"
prerequisites:
  - tree-width
  - tree-decomposition
extends: []
related:
  - bramble-order
  - tree-width-duality-theorem
contrasts_with: []
answers_questions:
  - "What is a bramble?"
  - "How do brambles relate to tree-width?"
---

# Quick Definition
A bramble in G is a set of mutually touching connected vertex sets, where two sets "touch" if they share a vertex or G has an edge between them. The order of a bramble is the minimum number of vertices needed to cover (hit) every set in it.

# Core Definition
Two subsets of V(G) *touch* if they have a vertex in common or G contains an edge between them. A set of mutually touching connected vertex sets in G is a *bramble*. A subset of V(G) *covers* a bramble B if it meets every element of B. The least number of vertices covering a bramble is its *order* (Diestel, p. 332).

# Prerequisites
- **Tree-width** — Brambles characterize tree-width
- **Tree-decomposition** — Brambles obstruct small tree-decompositions

# Key Properties
1. Every part of a tree-decomposition that covers a bramble has order at least the bramble's order
2. tw(G) = k iff the largest bramble order in G is k+1 (Theorem 12.3.9)
3. Any set separating two covers of a bramble also covers it (Lemma 12.3.8)
4. The crosses of the k x k grid form a bramble of order k

# Context & Application
Brambles are the dual obstruction to small tree-width, just as cuts are dual to flows. The tree-width duality theorem (Seymour-Thomas, 1993) says tree-width equals one less than the maximum bramble order.

# Examples
**Example 1** (p. 332): The crosses C_{ij} of the k x k grid (union of ith column and jth row) form a bramble of order k. They are covered by any row or column, but k-1 vertices miss some cross.

# Relationships
## Enables
- **Tree-width duality theorem** — tw(G) = max bramble order - 1

## Related
- **Tree-width** — Brambles provide lower bounds

# Source Reference
Chapter 12, Section 12.3, pages 332-334 (Theorem 12.3.9).

# Verification Notes
- Definition from p. 332
- Confidence: HIGH — explicit definition with concrete example
