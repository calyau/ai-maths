---
concept: Ordinal
slug: ordinal

category: set-theory-foundations
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Sets"
chapter_number: null
pdf_page: 367
section: null

extraction_confidence: high

aliases:
  - "order type"
  - "omega"

prerequisites:
  - well-ordered-set
extends: []
related:
  - transfinite-induction
  - limit-element
contrasts_with: []

answers_questions:
  - "What is an ordinal?"
  - "What is the order type of a well-ordered set?"
  - "What is omega?"
---

# Quick Definition
An ordinal is a canonical representative of an order type (equivalence class of well-ordered sets under order-preserving bijection). The ordinal omega represents the order type of N.

# Core Definition
Two well-ordered sets have the same order type if there is a bijection between them which preserves their orders. When one considers properties shared by all well-ordered sets of the same order type, it is convenient to represent each order type by a specially chosen set, its ordinal. The ordinal representing the order type of N is by custom denoted as omega. Finite chains of the same cardinality always have the same order type; we choose n as the ordinal for chains of order n (Diestel, pp. 358-359).

If an ordinal beta has the same order type as a proper initial segment of another ordinal alpha, we write beta < alpha. This defines a well-ordering on every set of ordinals.

# Prerequisites
- **Well-ordered set** — ordinals represent order types of well-ordered sets

# Key Properties
1. 0 <= n < omega for every natural number n
2. The ordering < on ordinals is itself a well-ordering
3. Infinite ordinals are defined so alpha = {beta | beta < alpha}
4. The ordering < for ordinals coincides with the membership relation

# Context & Application
Ordinals provide the framework for transfinite induction and recursive definitions. They are used extensively in Chapter 8 (Infinite Graphs).

# Relationships
## Builds Upon
- **well-ordered-set**

## Enables
- **transfinite-induction** — proof and definition by ordinal induction

## Related
- **limit-element** — limit ordinals have no predecessor

# Source Reference
Appendix A: Infinite Sets, pages 358-359 (pdf pp. 368-369).

# Verification Notes
- Direct from pp. 358-359
- Confidence: HIGH
