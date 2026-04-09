---
concept: Bipartite Embedding
slug: bipartite-embedding
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
  - "bipartition-respecting embedding"
prerequisites:
  - graph
related:
  - bipartite-ramsey-lemma
  - induced-ramsey-theorem
answers_questions:
  - "What is a bipartite embedding?"
---

# Quick Definition
An embedding of a bipartite graph P = (V_1, V_2, E) into P' = (V'_1, V'_2, E') is an injective map phi respecting the bipartition (phi(V_i) subset V'_i) such that edges and non-edges are preserved (induced embedding).

# Core Definition
Given bipartite graphs P = (V_1, V_2, E) and P' = (V'_1, V'_2, E'), an injective map phi: V_1 union V_2 -> V'_1 union V'_2 is an **embedding** of P in P' if phi(V_i) subset V'_i for i = 1,2 and phi(v_1)phi(v_2) is an edge of P' if and only if v_1v_2 is an edge of P. (Diestel, p. 264)

# Prerequisites
- **Graph** — Bipartite graphs with specified partitions

# Key Properties
1. Respects the bipartition
2. "Induced" by default: preserves both edges and non-edges
3. Used in the second proof of the induced Ramsey theorem

# Relationships
## Enables
- **Bipartite Ramsey lemma** — Seeks monochromatic bipartite embeddings

# Source Reference
Chapter 9, Section 9.3, page 264 (pdf page 274).

# Verification Notes
- Confidence: HIGH — formally defined
