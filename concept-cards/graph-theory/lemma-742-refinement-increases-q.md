---
concept: Refinement Never Decreases q
slug: lemma-742-refinement-increases-q
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
  - "Lemma 7.4.2"
prerequisites:
  - energy-increment-argument
  - density-of-pair
related:
  - regularity-lemma
answers_questions:
  - "Why does refinement increase the energy function q?"
---

# Quick Definition
Lemma 7.4.2: (i) Partitioning both sets in a pair never decreases q(C,D). (ii) If P' refines P, then q(P') >= q(P). This follows from the Cauchy-Schwarz inequality.

# Core Definition
**Lemma 7.4.2**: (i) Let C, D be disjoint vertex sets. If C is a partition of C and D of D, then q(C, D) >= q(C, D). (ii) If P' refines P, then q(P') >= q(P).

The proof uses the inequality sum(e_i^2/mu_i) >= (sum e_i)^2 / (sum mu_i), which follows from Cauchy-Schwarz. (Diestel, pp. 178-179)

# Prerequisites
- **Energy increment argument** — This lemma is part of the energy argument
- **Density of pair** — q is defined via pair densities

# Key Properties
1. Monotonicity: refinement can only increase q
2. Combined with the upper bound q <= 1, limits the number of refinements
3. The Cauchy-Schwarz inequality is the key analytical tool

# Source Reference
Chapter 7, Section 7.4, Lemma 7.4.2, pages 178-179 (pdf pages 188-189).

# Verification Notes
- Confidence: HIGH — lemma with proof
