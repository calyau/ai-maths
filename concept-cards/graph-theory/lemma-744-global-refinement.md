---
concept: Global Refinement Lemma
slug: lemma-744-global-refinement
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 190
section: "7.4 Szemeredi's regularity lemma"
extraction_confidence: high
aliases:
  - "Lemma 7.4.4"
prerequisites:
  - lemma-743-irregular-pair-increment
  - lemma-742-refinement-increases-q
related:
  - regularity-lemma
answers_questions:
  - "How does the regularity lemma proof handle all irregular pairs simultaneously?"
---

# Quick Definition
Lemma 7.4.4: If a partition P is not epsilon-regular, it can be refined into P' with k <= |P'| <= k*4^k parts such that q(P') >= q(P) + epsilon^5/2.

# Core Definition
**Lemma 7.4.4**: Let 0 < epsilon <= 1/4, and P = {C_0, C_1, ..., C_k} be a partition with exceptional set |C_0| <= epsilon*n and equal-sized parts. If P is not epsilon-regular, then there is a refined partition P' = {C'_0, C'_1, ..., C'_l} with k <= l <= k*4^k, |C'_0| <= |C_0| + n/2^k, equal-sized non-exceptional parts, and q(P') >= q(P) + epsilon^5/2. (Diestel, pp. 180-182)

# Prerequisites
- **Lemma 7.4.3** — Individual pair increments sum up
- **Lemma 7.4.2** — Refinement monotonicity

# Key Properties
1. Handles ALL irregular pairs simultaneously
2. The number of parts can grow to k*4^k per step
3. Exceptional set grows by at most n/2^k per step
4. The increase epsilon^5/2 is the key constant bounding iterations

# Source Reference
Chapter 7, Section 7.4, Lemma 7.4.4, pages 180-182 (pdf pages 190-192).

# Verification Notes
- Confidence: HIGH — lemma with proof
