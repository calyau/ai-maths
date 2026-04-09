---
concept: Chromatic Polynomial
slug: chromatic-polynomial
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.2 Colouring vertices"
extraction_confidence: medium
aliases:
  - "P_G(k)"
prerequisites:
  - chromatic-number
extends: []
related:
  - vertex-colouring
contrasts_with: []
answers_questions:
  - "What is the chromatic polynomial?"
  - "How many colourings does a graph have?"
---

# Quick Definition
The chromatic polynomial P_G(k) counts the number of proper vertex colourings of G using at most k colours. It is a polynomial of degree n = |G| with leading coefficient 1.

# Core Definition
"Given a graph G and k in N, let P_G(k) denote the number of vertex colourings V(G) -> {1,...,k}. P_G is a polynomial in k of degree n := |G|, in which the coefficient of k^n is 1 and the coefficient of k^{n-1} is -||G||" (Diestel, p. 134, Exercise 17).

# Prerequisites
- **Chromatic number** -- chi(G) = min{k : P_G(k) > 0}

# Key Properties
1. P_G is a polynomial in k of degree n
2. Leading coefficient is 1; coefficient of k^{n-1} is -m
3. chi(G) = smallest positive integer k with P_G(k) > 0
4. Computed by deletion-contraction: P_G(k) = P_{G-e}(k) - P_{G/e}(k)
5. For trees: P_T(k) = k(k-1)^{n-1}

# Relationships
## Builds Upon
- **Chromatic number**

# Source Reference
Chapter 5, Exercise 17, page 134.

# Verification Notes
- Defined in exercises
- Confidence: MEDIUM -- exercise definition, not main text
