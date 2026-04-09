---
concept: Regularity Graph
slug: regularity-graph
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 194
section: "7.5 Applying the regularity lemma"
extraction_confidence: high
aliases:
  - "reduced graph"
prerequisites:
  - epsilon-regular-partition
  - epsilon-regular-pair
  - density-of-pair
related:
  - regularity-lemma
  - embedding-lemma
  - erdos-stone-theorem
answers_questions:
  - "What is a regularity graph?"
  - "How do I apply Szemeredi's regularity lemma?"
---

# Quick Definition
A regularity graph R of G is the graph on partition sets {V_1, ..., V_k} where V_i and V_j are adjacent iff they form an epsilon-regular pair of density at least d.

# Core Definition
Let G be a graph with an epsilon-regular partition {V_0, V_1, ..., V_k}, with |V_1| = ... = |V_k| =: l. Given d in [0,1], the **regularity graph** R with parameters epsilon, l, d is the graph on {V_1, ..., V_k} in which two vertices V_i, V_j are adjacent iff they form an epsilon-regular pair of density >= d. Given s in N, R_s is obtained by replacing each vertex with s copies and each edge with a complete bipartite graph. (Diestel, p. 184)

# Prerequisites
- **Epsilon-regular partition** — R is built from a regular partition
- **Epsilon-regular pair** — Edges of R correspond to regular pairs
- **Density of pair** — The density threshold d determines which pairs become edges

# Key Properties
1. R has k vertices (one per non-exceptional partition set)
2. Edges correspond to epsilon-regular pairs of sufficient density
3. R_s is the "inflated" version where each vertex becomes an s-set
4. Subgraphs of R_s can be found in G (Embedding Lemma 7.5.2)
5. If G has enough edges, R has enough edges for Turan's theorem to apply

# Relationships
## Builds Upon
- **Epsilon-regular partition**

## Enables
- **Embedding lemma** — H subset R_s implies H subset G under suitable conditions
- **Erdos-Stone theorem** — K^r subset R is forced by Turan; then K_s^r subset R_s subset G

# Source Reference
Chapter 7, Section 7.5, page 184 (pdf page 194).

# Verification Notes
- Confidence: HIGH — explicitly defined with parameters
