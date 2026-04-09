---
concept: Bipartite Ramsey Lemma
slug: bipartite-ramsey-lemma
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
  - "Lemma 9.3.3"
prerequisites:
  - ramsey-theorem-general
related:
  - induced-ramsey-theorem
  - ramsey-graph
answers_questions:
  - "Does every bipartite graph have a bipartite Ramsey graph?"
---

# Quick Definition
For every bipartite graph P there exists a bipartite graph P' such that every 2-colouring of E(P') yields a monochromatic embedding of P in P' (preserving the bipartition).

# Core Definition
**Lemma 9.3.3**: For every bipartite graph P there exists a bipartite graph P' such that for every 2-colouring of the edges of P' there is an embedding phi: P -> P' for which all edges of phi(P) have the same colour.

The proof first embeds P into a canonical bipartite graph (X, [X]^k, E) with E = {xY | x in Y} (Lemma 9.3.2), then constructs P' using the general Ramsey theorem (9.1.3) to find a monochromatic subset of the correct structure. (Diestel, pp. 264-266)

# Prerequisites
- **Ramsey theorem (general)** — Used with parameters k', 2*C(k',k), k|X|+k-1

# Key Properties
1. Covers the bipartite case of the induced Ramsey theorem
2. Embeddings respect the bipartition
3. Uses a canonical representation of bipartite graphs via set systems
4. Central ingredient in the second proof of Theorem 9.3.1

# Relationships
## Enables
- **Induced Ramsey theorem** — The bipartite case is iterated to prove the general case

# Source Reference
Chapter 9, Section 9.3, Lemma 9.3.3, pages 264-266 (pdf pages 274-276).

# Verification Notes
- Confidence: HIGH — complete proof given
