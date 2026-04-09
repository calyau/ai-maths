---
concept: Linear Ramsey Number Proof Strategy
slug: ramsey-theorem-92-proof-strategy
category: ramsey-theory
subcategory: graph-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 266
section: "9.2 Ramsey numbers"
extraction_confidence: high
aliases:
  - "proof strategy for Theorem 9.2.2"
prerequisites:
  - ramsey-number-bounded-degree
  - regularity-lemma
  - embedding-lemma
  - turan-theorem
related:
  - erdos-stone-proof-overview
answers_questions:
  - "How is the regularity lemma used in Ramsey theory?"
---

# Quick Definition
The proof of Theorem 9.2.2 (R(H) <= c|H| for bounded-degree H) applies the regularity lemma to a 2-coloured graph: either enough regular pairs are dense (find H) or most are sparse (find H in the complement).

# Core Definition
Given a 2-edge-colouring of G with |G| >= c|H|:
1. Apply the regularity lemma to get an epsilon-regular partition
2. Build the regularity graph R (edges = regular pairs of ANY density)
3. R is dense (||R|| >= t_{m-1}(k) by Turan's estimate), so K^m subset R for m = R(Delta+1)
4. 2-colour R's edges: red if pair density >= 1/2, green otherwise
5. By Ramsey (for m), K contains a monochromatic K^{Delta+1}: either in R' (dense) or R'' (sparse)
6. Correspondingly, H subset R'_s or H subset R''_s (since chi(H) <= Delta+1)
7. Apply embedding lemma: H subset G or H subset G-bar. (Diestel, pp. 256-258)

# Prerequisites
- **Ramsey number (bounded degree)** — The theorem being proved
- **Regularity lemma**, **Embedding lemma**, **Turan's theorem**

# Key Properties
1. Key insight: the regularity graph R is dense enough for Turan
2. The 2-colouring of R matches the edge-colouring of G
3. R'' is a regularity graph of G-bar (since epsilon-regular pairs are also regular for the complement)
4. c depends only on Delta (not on the structure of H)

# Source Reference
Chapter 9, Section 9.2, Theorem 9.2.2, pages 256-258 (pdf pages 266-268).

# Verification Notes
- Confidence: HIGH — complete proof summarized
