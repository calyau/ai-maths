---
concept: Energy Increment Argument
slug: energy-increment-argument
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 188
section: "7.4 Szemeredi's regularity lemma"
extraction_confidence: high
aliases:
  - "index function q"
  - "energy function"
prerequisites:
  - epsilon-regular-partition
  - density-of-pair
related:
  - regularity-lemma
answers_questions:
  - "How is the regularity lemma proved?"
---

# Quick Definition
The energy increment argument proves the regularity lemma by showing that a "potential function" q(P) increases by at least epsilon^5/2 at each refinement step, and since q(P) <= 1, only finitely many refinements are needed.

# Core Definition
For a partition P = {C_1, ..., C_k} of V, define q(P) := sum_{i<j} q(C_i, C_j) where q(A,B) = (|A||B|/n^2) * d^2(A,B). Key properties:
- q(P) <= 1 (upper bound)
- Refining a partition never decreases q (Lemma 7.4.2)
- If P is not epsilon-regular, refinement increases q by >= epsilon^5/2 (Lemma 7.4.4)

Since q can increase at most 2/epsilon^5 times, the partition becomes regular after bounded refinements. (Diestel, pp. 178-183)

# Prerequisites
- **Epsilon-regular partition** — The argument proves these exist
- **Density of pair** — The index q is built from pair densities

# Key Properties
1. q(P) is bounded: 0 <= q(P) <= 1
2. Refinement never decreases q (Lemma 7.4.2)
3. Splitting irregular pairs increases q by a constant (Lemma 7.4.3)
4. At most 2/epsilon^5 iterations needed
5. The Cauchy-Schwarz inequality is used to prove q increases under refinement

# Relationships
## Enables
- **Regularity lemma** — This is the proof technique

# Source Reference
Chapter 7, Section 7.4, pages 178-183 (pdf pages 188-192). Lemmas 7.4.2, 7.4.3, 7.4.4.

# Verification Notes
- Confidence: HIGH — central proof technique, fully detailed
