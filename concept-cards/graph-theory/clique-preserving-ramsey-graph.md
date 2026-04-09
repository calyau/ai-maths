---
concept: Clique-Preserving Ramsey Graph
slug: clique-preserving-ramsey-graph
category: ramsey-theory
subcategory: induced-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 276
section: "9.3 Induced Ramsey theorems"
extraction_confidence: high
aliases:
  - "omega-preserving Ramsey graph"
prerequisites:
  - induced-ramsey-theorem
  - ramsey-graph
related:
  - bipartite-ramsey-lemma
answers_questions:
  - "Can Ramsey graphs be constructed with controlled clique number?"
---

# Quick Definition
The second proof of the induced Ramsey theorem constructs a Ramsey graph G for H with omega(G) = omega(H), i.e., the construction preserves the clique number.

# Core Definition
The second proof of Theorem 9.3.1 (Nesetril-Rodl) constructs G with omega(G) = omega(H). The construction uses:
1. A graph G^0 consisting of C(n,r) disjoint copies of H arranged in rows (where n = R(r))
2. Iterative application of the bipartite Ramsey lemma (Lemma 9.3.3) to pairs of rows
3. The final graph G = G^m satisfies: any 2-colouring projects to a colouring of K^n, yielding a monochromatic K^r, inside which a monochromatic induced H exists. (Diestel, pp. 266-268)

# Prerequisites
- **Induced Ramsey theorem** — This is the stronger version
- **Ramsey graph** — G is a Ramsey graph with the extra clique-number property

# Key Properties
1. omega(G) = omega(H): no unnecessary cliques
2. Uses bipartite Ramsey iteration over all edge pairs
3. The construction is explicit but the resulting G is enormous

# Source Reference
Chapter 9, Section 9.3, second proof of Theorem 9.3.1, pages 266-268 (pdf pages 276-278).

# Verification Notes
- Confidence: HIGH — complete proof given
