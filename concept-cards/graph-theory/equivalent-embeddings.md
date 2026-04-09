---
concept: Equivalent Embeddings
slug: equivalent-embeddings
category: planar-graphs
subcategory: drawings
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.3 Drawings"
extraction_confidence: high
aliases:
  - "equivalent planar embeddings"
prerequisites:
  - planar-embedding
  - combinatorial-isomorphism
  - topological-isomorphism
extends: []
related:
  - whitney-uniqueness-theorem
contrasts_with: []
answers_questions:
  - "When are two planar embeddings considered equivalent?"
---

# Quick Definition
Two planar embeddings of a graph G are equivalent if the canonical isomorphism between their images is a topological (or, equivalently for 2-connected graphs, combinatorial) isomorphism.

# Core Definition
"Call two planar embeddings rho, rho' of G topologically (respectively, combinatorially) equivalent if rho' o rho^{-1} is a topological (respectively, combinatorial) isomorphism between rho(G) and rho'(G). If G is 2-connected, the two definitions coincide by Theorem 4.3.1, and we simply speak of equivalent embeddings" (Diestel, p. 96).

# Prerequisites
- **Planar embedding** -- Equivalence is a relation on embeddings
- **Combinatorial isomorphism** and **Topological isomorphism** -- The defining criteria

# Key Properties
1. For 2-connected graphs, topological and combinatorial equivalence coincide
2. Equivalence is indeed an equivalence relation on embeddings
3. 3-connected graphs have exactly one embedding up to equivalence (Whitney's theorem)
4. Two drawings from inequivalent embeddings may still be topologically isomorphic as plane graphs

# Context & Application
This concept provides the precise framework for asking "how many essentially different ways can a graph be drawn in the plane?" For 3-connected graphs, the answer is: exactly one way (Whitney's theorem 4.3.2).

# Relationships
## Enables
- **Whitney's uniqueness theorem** -- 3-connected graphs have unique embeddings

# Source Reference
Chapter 4, Section 4.3, page 96. Theorem 4.3.2.

# Verification Notes
- Definition quoted from p. 96
- Confidence: HIGH -- explicit definition
