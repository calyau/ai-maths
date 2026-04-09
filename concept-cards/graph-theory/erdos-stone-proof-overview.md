---
concept: "Erd\u0151s-Stone Theorem Proof Strategy"
slug: erdos-stone-proof-overview
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 197
section: "7.5 Applying the regularity lemma"
extraction_confidence: high
aliases:
  - "regularity lemma application strategy"
prerequisites:
  - regularity-lemma
  - embedding-lemma
  - turan-theorem
  - erdos-stone-theorem
related:
  - regularity-graph
  - inflated-regularity-graph
answers_questions:
  - "How do I apply Szemeredi's regularity lemma?"
  - "How is the Erdos-Stone theorem proved using the regularity lemma?"
---

# Quick Definition
The proof of the Erdos-Stone theorem via the regularity lemma follows a standard pipeline: partition G regularly, build a dense regularity graph R, find K^r in R by Turan, then find K_s^r in G via the embedding lemma.

# Core Definition
The standard regularity-lemma application strategy, as illustrated in the Erdos-Stone proof:

1. **Choose parameters**: Given d and Delta(H), Lemma 7.5.2 returns epsilon_0. Choose m > 1/gamma, epsilon small enough, and obtain M from the regularity lemma.
2. **Apply regularity lemma**: Get an epsilon-regular partition with m <= k <= M parts.
3. **Build regularity graph R**: Edges are epsilon-regular pairs of density >= d.
4. **Show R is dense**: The gamma*n^2 extra edges (above t_{r-1}(n)) force ||R|| > t_{r-1}(k), since edges in low-density pairs, irregular pairs, and exceptional edges account for less than gamma*n^2.
5. **Apply Turan**: K^r subset R.
6. **Apply embedding lemma**: K_s^r subset R_s => K_s^r subset G. (Diestel, pp. 187-190)

# Prerequisites
- **Regularity lemma**, **Embedding lemma**, **Turan's theorem**, **Erdos-Stone theorem**

# Key Properties
1. The parameter dependencies are: gamma -> d, Delta -> epsilon_0 -> epsilon, m -> M -> n
2. d must be small enough that gamma*n^2 edges overwhelm the low-density pairs
3. m must be large enough that within-partition edges are negligible
4. The bound on n grows extremely fast (tower function) due to the regularity lemma

# Context & Application
This is the template for regularity-lemma applications in dense extremal graph theory. The same approach is used in Theorem 9.2.2 (linear Ramsey numbers for bounded-degree graphs).

# Source Reference
Chapter 7, Section 7.5, pages 187-192 (pdf pages 197-202). The proof and subsequent "review" of the method.

# Verification Notes
- Confidence: HIGH — detailed proof with methodological discussion
