---
concept: Canonical Bipartite Representation
slug: canonical-bipartite-representation
category: ramsey-theory
subcategory: induced-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 274
section: "9.3 Induced Ramsey theorems"
extraction_confidence: high
aliases:
  - "Lemma 9.3.2"
prerequisites:
  - graph
related:
  - bipartite-ramsey-lemma
  - bipartite-embedding
answers_questions:
  - "How can bipartite graphs be represented canonically?"
---

# Quick Definition
Every bipartite graph can be embedded in a bipartite graph of the form (X, [X]^k, E) where E = {xY | x in Y}, providing a canonical representation.

# Core Definition
**Lemma 9.3.2**: Every bipartite graph can be embedded in a bipartite graph of the form (X, [X]^k, E) with E = {xY | x in Y}. The proof takes a bipartite graph with classes {a_1,...,a_n} and {b_1,...,b_m}, sets X with 2n+m elements, maps a_i -> x_i, and maps each b_i to an (n+1)-set Y subset X chosen so that Y intersect {x_1,...,x_n} = images of N(b_i). (Diestel, pp. 264-265)

# Prerequisites
- **Graph** — The representation concerns bipartite graphs

# Key Properties
1. One vertex class is X, the other is [X]^k (k-subsets of X)
2. The edge relation is membership: x is adjacent to Y iff x in Y
3. Index elements ensure injectivity: different vertices get different images
4. Used to reduce the bipartite Ramsey lemma to a set-system problem

# Relationships
## Enables
- **Bipartite Ramsey lemma** — Uses this canonical form

# Source Reference
Chapter 9, Section 9.3, Lemma 9.3.2, pages 264-265 (pdf pages 274-275).

# Verification Notes
- Confidence: HIGH — lemma with proof
