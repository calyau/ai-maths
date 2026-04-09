---
concept: Graph Minor Theorem
slug: graph-minor-theorem
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 352
section: "12.5 The graph minor theorem"
extraction_confidence: high
aliases:
  - "Robertson-Seymour theorem"
  - "Wagner's conjecture"
prerequisites:
  - well-quasi-ordering
  - graph-minor
  - tree-width
  - tree-decomposition
  - kruskals-tree-theorem
extends: []
related:
  - kuratowski-set
  - finite-basis-theorem
  - forbidden-minor
contrasts_with: []
answers_questions:
  - "What is the graph minor theorem?"
  - "What must I know before understanding the graph minor theorem?"
---

# Quick Definition
The graph minor theorem (Robertson-Seymour, 1986-2004) states that the finite graphs are well-quasi-ordered by the minor relation. Equivalently, in every infinite set of graphs, some graph is a minor of another. Its proof spans over 500 pages.

# Core Definition
**Theorem 12.5.1** (Robertson & Seymour 1986-2004): The finite graphs are well-quasi-ordered by the minor relation <= (Diestel, p. 352). This means that for every infinite sequence G_0, G_1, G_2, ... of finite graphs, there exist indices i < j such that G_i <= G_j.

# Prerequisites
- **Well-quasi-ordering** — The theorem asserts WQO
- **Graph minor** — The ordering relation
- **Tree-width** — Central to the proof structure
- **Tree-decomposition** — The graphs in Forb(K^n) have structured tree-decompositions
- **Kruskal's tree theorem** — The tree case, proved first

# Key Properties
1. The proof is over 500 pages, published in a series of 20+ papers (Graph Minors I-XX)
2. Implies every minor-closed property has finitely many forbidden minors (Corollary 12.5.2)
3. For every surface S, embeddability in S is characterized by finitely many forbidden minors (Corollary 12.5.3)
4. Every minor-closed property can be tested in polynomial (cubic) time
5. The theorem does not extend to uncountable graphs (Thomas 1988)
6. Whether it extends to countable graphs is open

# Context & Application
The graph minor theorem is one of the deepest results in all of mathematics. It implies, non-constructively, that countless natural graph properties have finite forbidden minor characterizations and polynomial-time algorithms. For example, before the theorem, it was unknown whether knotlessness (embeddability in R^3 without knotted cycles) was even decidable; the theorem implies it can be decided in cubic time, though no explicit algorithm is known.

# Examples
**Example 1** (p. 352): Kuratowski's theorem (K^5 and K_{3,3} for planarity) is a special case.

**Example 2** (p. 337): Forb(K^3) = forests; Forb(K^4) = graphs of tree-width < 3.

# Relationships
## Builds Upon
- **Kruskal's tree theorem** — The tree case
- **Theorem 12.3.7** — WQO for bounded tree-width
- **Theorem 12.4.11** — Structure of Forb(K^n)

## Enables
- **Finite basis theorem** — Every minor-closed property has finitely many forbidden minors
- Polynomial-time algorithms for all minor-closed properties

## Related
- **Kuratowski set** — The unique smallest forbidden minor set

# Common Confusions
- **Confusion**: Thinking the theorem provides explicit forbidden minors
  **Clarification**: The theorem is non-constructive; finding the actual forbidden minors requires additional work

- **Confusion**: Thinking the theorem gives efficient algorithms directly
  **Clarification**: It guarantees existence of cubic algorithms, but with potentially enormous constants depending on the property

# Source Reference
Chapter 12, Section 12.5, pages 352-359.

# Verification Notes
- Statement from p. 352
- Proof sketch from pp. 357-359
- Confidence: HIGH — the central theorem of the chapter
