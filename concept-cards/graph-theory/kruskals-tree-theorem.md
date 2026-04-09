---
concept: "Kruskal's Tree Theorem"
slug: kruskals-tree-theorem
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 328
section: "12.2 The graph minor theorem for trees"
extraction_confidence: high
aliases:
  - "Kruskal 1960"
prerequisites:
  - well-quasi-ordering
  - higmans-lemma
extends: []
related:
  - graph-minor-theorem
contrasts_with: []
answers_questions:
  - "Are finite trees well-quasi-ordered?"
---

# Quick Definition
Kruskal's tree theorem (1960) states that the finite trees are well-quasi-ordered by the topological minor relation. The proof uses the minimal bad sequence technique and Higman's lemma.

# Core Definition
**Theorem 12.2.1** (Kruskal 1960): The finite trees are well-quasi-ordered by the topological minor relation (Diestel, p. 328).

# Prerequisites
- **Well-quasi-ordering** — The theorem asserts WQO
- **Higman's lemma** — Used in the proof via Lemma 12.1.3

# Key Properties
1. The proof works with rooted trees and an embedding relation T <= T' preserving tree-order
2. Uses the minimal bad sequence technique: choose T_n of minimum order
3. The components of T_n - r_n (made into rooted trees) form a WQO set A
4. By Higman's lemma, (A_n) has a good pair, yielding a contradiction
5. Stronger than WQO by the minor relation (topological minor is stronger)

# Context & Application
Kruskal's tree theorem is the first major step towards the graph minor theorem. It proves WQO for the simplest class of graphs (trees) and introduces the proof techniques that will be generalized. The Nash-Williams proof technique of "minimal bad sequences" was introduced here.

# Examples
**Example 1** (pp. 328-329, Fig. 12.2.1): An embedding of T in T' showing T <= T'.

# Relationships
## Builds Upon
- **Higman's lemma** — Finite subsets of a WQO are WQO

## Enables
- **Theorem 12.3.7** — Graphs of bounded tree-width are WQO by minors
- **Graph minor theorem** — Kruskal's theorem is the tree case

# Source Reference
Chapter 12, Section 12.2, pages 328-329 (Theorem 12.2.1).

# Verification Notes
- Statement and proof from pp. 328-329
- Confidence: HIGH — named theorem with full proof
