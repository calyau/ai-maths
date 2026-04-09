---
concept: Irregular Pair q Increment
slug: lemma-743-irregular-pair-increment
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 189
section: "7.4 Szemeredi's regularity lemma"
extraction_confidence: high
aliases:
  - "Lemma 7.4.3"
prerequisites:
  - energy-increment-argument
  - epsilon-regular-pair
related:
  - regularity-lemma
answers_questions:
  - "By how much does q increase when an irregular pair is split?"
---

# Quick Definition
Lemma 7.4.3: If (C, D) is not epsilon-regular, then splitting it into two parts each increases q by at least epsilon^4 * |C||D|/n^2.

# Core Definition
**Lemma 7.4.3**: Let epsilon > 0, and let C, D be disjoint vertex sets. If (C, D) is not epsilon-regular, then there are partitions C = {C_1, C_2} of C and D = {D_1, D_2} of D such that q(C, D) >= q(C, D) + epsilon^4 * |C||D|/n^2.

The witnesses X subset C, Y subset D to irregularity (with |d(X,Y) - d(C,D)| > epsilon) become the partition sets. (Diestel, pp. 179-180)

# Prerequisites
- **Energy increment argument** — Part of the energy argument
- **Epsilon-regular pair** — Applies to pairs that fail regularity

# Key Properties
1. Each irregular pair contributes a positive increment to q
2. The increment depends on pair sizes and epsilon
3. Accumulating over > epsilon*k^2 irregular pairs gives a total increase of >= epsilon^5/2

# Source Reference
Chapter 7, Section 7.4, Lemma 7.4.3, pages 179-180 (pdf pages 189-190).

# Verification Notes
- Confidence: HIGH — lemma with proof
