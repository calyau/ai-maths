---
concept: Embedding Lemma
slug: embedding-lemma
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
  - "Lemma 7.5.2"
  - "key lemma for regularity"
prerequisites:
  - regularity-graph
  - epsilon-regular-pair
  - regularity-lemma
related:
  - erdos-stone-theorem
  - counting-lemma
answers_questions:
  - "How do I apply Szemeredi's regularity lemma?"
---

# Quick Definition
The embedding lemma states that if H has bounded maximum degree and H is a subgraph of the inflated regularity graph R_s, then H is also a subgraph of G, provided epsilon is small enough and partition sets are large enough.

# Core Definition
**Lemma 7.5.2**: For all d in (0,1] and Delta >= 1 there exists an epsilon_0 > 0 with the following property: if G is any graph, H is a graph with Delta(H) <= Delta, s in N, and R is any regularity graph of G with parameters epsilon <= epsilon_0, l >= 2s/d^Delta and d, then

H subset R_s => H subset G.

The proof embeds vertices of H one by one, maintaining "target sets" that shrink by a factor of at most (d - epsilon) at each step. The bounded degree ensures at most Delta shrinkages per target set. (Diestel, pp. 184-187)

# Prerequisites
- **Regularity graph** — H must be a subgraph of R_s
- **Epsilon-regular pair** — Regularity ensures target sets remain large
- **Regularity lemma** — Provides the regular partition

# Key Properties
1. epsilon_0 depends only on d and Delta, not on G or H
2. Partition sets must be large: l >= 2s/d^Delta
3. The proof uses Lemma 7.5.1: in a regular pair, most vertices have many neighbours in large subsets
4. Works for any graph H of bounded maximum degree

# Construction / Recognition
## How to Apply the Embedding Lemma
1. Obtain an epsilon-regular partition of G via the regularity lemma
2. Build the regularity graph R with appropriate parameters epsilon, l, d
3. Show that R contains K^r (or another target structure) using Turan's theorem or similar
4. Conclude H subset R_s subset G

# Context & Application
The embedding lemma is the key tool for converting regularity-lemma partitions into concrete subgraph results. It is the step that makes the abstract partition information useful.

# Relationships
## Builds Upon
- **Regularity graph**, **Regularity lemma**, **Epsilon-regular pair**

## Enables
- **Erdos-Stone theorem** — The proof uses the embedding lemma to find K_s^r in G
- **Theorem 9.2.2** — Ramsey numbers of bounded-degree graphs

# Source Reference
Chapter 7, Section 7.5, Lemma 7.5.2, pages 184-187 (pdf pages 194-197).

# Verification Notes
- Confidence: HIGH — central lemma with full proof
