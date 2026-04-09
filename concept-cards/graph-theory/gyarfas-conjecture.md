---
concept: "Gy\u00E1rf\u00E1s's Conjecture"
slug: gyarfas-conjecture
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 179
section: "7.1 Subgraphs"
extraction_confidence: medium
aliases:
  - "Gyarfas conjecture"
prerequisites:
  - graph
related:
  - turan-theorem
  - hadwiger-conjecture
answers_questions:
  - "Can large chromatic number force induced trees?"
---

# Quick Definition
Gyarfas's conjecture (1975) asserts that for every r and every tree T, there exists k such that every graph G with chi(G) >= k and omega(G) < r contains T as an induced subgraph.

# Core Definition
According to a conjecture of **Gyarfas** (1975), there exists for every r in N and every tree T an integer k = k(T, r) such that every graph G with chi(G) >= k and omega(G) < r contains T as an induced subgraph. (Diestel, p. 169)

The conjecture addresses whether large chromatic number (with bounded clique number) forces induced copies of trees. Note that large average degree alone does not suffice (complete bipartite graphs are counterexamples).

# Prerequisites
- **Graph** — Requires understanding of chromatic number and clique number

# Key Properties
1. Requires bounded clique number: omega(G) < r
2. Large average degree alone is insufficient (K_{n,n} has large d(G) but no induced P^3)
3. If true, would significantly extend the understanding of how chi forces substructures

# Source Reference
Chapter 7, Section 7.1, page 169 (pdf page 179).

# Verification Notes
- Confidence: MEDIUM — mentioned as a conjecture without detailed discussion
