---
concept: Epsilon-Regular Partition
slug: epsilon-regular-partition
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 186
section: "7.4 Szemeredi's regularity lemma"
extraction_confidence: high
aliases:
  - "regular partition"
  - "equitable partition"
prerequisites:
  - epsilon-regular-pair
  - density-of-pair
related:
  - regularity-lemma
  - regularity-graph
  - exceptional-set
answers_questions:
  - "What is an epsilon-regular partition?"
  - "What must I know before understanding the regularity lemma?"
---

# Quick Definition
An epsilon-regular partition of G is a partition {V_0, V_1, ..., V_k} where V_0 is a small exceptional set, V_1 through V_k have equal size, and all but at most epsilon*k^2 pairs (V_i, V_j) are epsilon-regular.

# Core Definition
A partition {V_0, V_1, ..., V_k} of V is an **epsilon-regular partition** of G if:
(i) |V_0| <= epsilon*|V| (small exceptional set);
(ii) |V_1| = ... = |V_k| (equal-sized non-exceptional parts);
(iii) all but at most epsilon*k^2 of the pairs (V_i, V_j) with 1 <= i < j <= k are epsilon-regular.

The exceptional set V_0 may be empty; its role is convenience, allowing equal-sized parts. (Diestel, p. 176-177)

# Prerequisites
- **Epsilon-regular pair** — Most pairs in the partition must be epsilon-regular
- **Density of pair** — Regularity is defined via density

# Key Properties
1. At most epsilon-fraction of V is exceptional
2. Non-exceptional parts have exactly equal size
3. At most epsilon*k^2 pairs may fail to be epsilon-regular
4. Useful only for dense graphs; for sparse graphs, all densities tend to zero trivially
5. The number of partition sets k is bounded (regularity lemma)

# Relationships
## Builds Upon
- **Epsilon-regular pair** — The partition is defined via regular pairs

## Enables
- **Regularity lemma** — Guarantees existence of epsilon-regular partitions
- **Regularity graph** — Constructed from the regular partition

# Source Reference
Chapter 7, Section 7.4, pages 176-177 (pdf pages 186-187).

# Verification Notes
- Confidence: HIGH — formal definition with numbered conditions
