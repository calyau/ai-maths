---
concept: Alternating Map
slug: alternating-map
category: linear-algebra
subcategory: determinants
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 432
section: "11.4 Determinants"
extraction_confidence: high
aliases:
  - "alternating multilinear function"
  - "skew-symmetric"
prerequisites:
  - multilinear-map
extends:
  - multilinear-map
related:
  - determinant
  - exterior-algebra
contrasts_with:
  - symmetric-map
answers_questions:
  - "What is an alternating map?"
---

# Quick Definition
An n-multilinear function $\varphi$ on V is alternating if $\varphi(v_1, \ldots, v_n) = 0$ whenever two consecutive arguments are equal. Swapping two arguments negates the value.

# Core Definition
An n-multilinear function $\varphi$ on V is called alternating if $\varphi(v_1, \ldots, v_n) = 0$ whenever $v_i = v_{i+1}$ for some i. It is called symmetric if interchanging any $v_i$ and $v_j$ does not change the value (Dummit & Foote, p. 432).

# Prerequisites
- **multilinear-map** — Alternating maps are special multilinear maps

# Key Properties
1. Swapping two adjacent arguments negates the value (Proposition 22)
2. For any $\sigma \in S_n$: $\varphi(v_{\sigma(1)}, \ldots, v_{\sigma(n)}) = \epsilon(\sigma)\varphi(v_1, \ldots, v_n)$
3. If any two arguments are equal, the value is 0
4. Adding a multiple of one argument to another does not change the value

# Relationships
## Builds Upon
- **multilinear-map**

## Enables
- **determinant** — The determinant is an alternating multilinear form
- **exterior-algebra** — Quotient of tensor algebra by alternating relations

## Contrasts With
- **symmetric-map** — Symmetric maps are unchanged by swapping; alternating maps change sign

# Source Reference
Chapter 11, Section 11.4, pp. 432-433, Proposition 22.

# Verification Notes
- Confidence: HIGH — explicit definition
