---
concept: Girth-Minimum Degree Lemma
slug: girth-minimum-degree-lemma
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 181
section: "7.2 Minors"
extraction_confidence: high
aliases:
  - "Lemma 7.2.3"
prerequisites:
  - graph
related:
  - girth-forcing-minors
  - kostochka-theorem
answers_questions:
  - "How does girth amplify minimum degree in minors?"
---

# Quick Definition
A graph of minimum degree delta >= d >= 3 and girth g >= 8k+3 has a minor of minimum degree at least d(d-1)^k.

# Core Definition
**Lemma 7.2.3**: Let d, k in N with d >= 3, and let G be a graph of minimum degree delta(G) >= d and girth g(G) >= 8k+3. Then G has a minor H of minimum degree delta(H) >= d(d-1)^k.

The proof partitions V(G) into trees T_x (one per x in a maximal spread-out set X), each of depth 2k. Since girth is large, these trees are induced subgraphs with at most one edge between any two. Each T_x has at least d(d-1)^{k-1} leaves, each sending at least d-1 edges to other trees. (Diestel, pp. 171-172)

# Prerequisites
- **Graph** — Requires understanding of girth and minimum degree

# Key Properties
1. Exponential amplification: minimum degree d becomes d(d-1)^k in the minor
2. The girth condition prevents short cycles from interfering with the tree structure
3. Key ingredient for Theorems 7.2.4 and 7.2.5

# Relationships
## Enables
- **Girth forcing minors** — Theorem 7.2.4 follows by combining with Kostochka's theorem

# Source Reference
Chapter 7, Section 7.2, Lemma 7.2.3, pages 171-172 (pdf pages 181-182).

# Verification Notes
- Confidence: HIGH — lemma with proof
