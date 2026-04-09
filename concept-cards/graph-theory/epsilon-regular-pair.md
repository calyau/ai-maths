---
concept: Epsilon-Regular Pair
slug: epsilon-regular-pair
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
  - "regular pair"
  - "eps-regular pair"
prerequisites:
  - density-of-pair
related:
  - epsilon-regular-partition
  - regularity-lemma
  - embedding-lemma
answers_questions:
  - "What is an epsilon-regular pair?"
  - "What must I know before understanding the regularity lemma?"
---

# Quick Definition
A pair (A, B) of disjoint vertex sets is epsilon-regular if for all subsets X of A and Y of B with |X| >= epsilon*|A| and |Y| >= epsilon*|B|, the density d(X, Y) deviates from d(A, B) by at most epsilon.

# Core Definition
Given epsilon > 0, a pair (A, B) of disjoint sets A, B subset of V is **epsilon-regular** if all X subset of A and Y subset of B with |X| >= epsilon*|A| and |Y| >= epsilon*|B| satisfy |d(X, Y) - d(A, B)| <= epsilon. The edges in an epsilon-regular pair are thus distributed fairly uniformly, the more so the smaller epsilon. (Diestel, p. 176)

# Prerequisites
- **Density of pair** — Regularity is defined via deviations in density

# Key Properties
1. Captures "pseudo-randomness": edges distributed uniformly between A and B
2. Smaller epsilon means more uniform distribution
3. Trivial when |A| and |B| are singletons; powerful when they are large
4. An epsilon-regular pair in G is also epsilon-regular in the complement G-bar (Exercise 38)
5. Most vertices in A have about the expected number of neighbours in large subsets of B (Lemma 7.5.1)

# Construction / Recognition
## To Check Epsilon-Regularity of (A, B)
1. Compute d(A, B)
2. For all subsets X of A with |X| >= epsilon*|A| and Y of B with |Y| >= epsilon*|B|:
3. Check that |d(X, Y) - d(A, B)| <= epsilon
4. If any such X, Y violate this, the pair is NOT epsilon-regular

# Context & Application
Epsilon-regular pairs are the building blocks of the regularity lemma. They model "pseudo-random" bipartite graphs where edge distribution is nearly uniform. This pseudo-randomness enables subgraph embedding via the embedding lemma (Lemma 7.5.2).

# Relationships
## Builds Upon
- **Density of pair** — Regularity constrains density deviations

## Enables
- **Epsilon-regular partition** — Partitions made of mostly regular pairs
- **Regularity lemma** — Guarantees existence of regular partitions
- **Embedding lemma** — Subgraphs can be found in regular pairs

# Common Confusions
- **Confusion**: Thinking epsilon-regular means density approximately epsilon
  **Clarification**: Epsilon-regularity means the density is APPROXIMATELY CONSTANT (whatever that constant is); epsilon bounds the deviation, not the density itself

# Source Reference
Chapter 7, Section 7.4, page 176 (pdf page 186).

# Verification Notes
- Confidence: HIGH — formal definition with clear notation
