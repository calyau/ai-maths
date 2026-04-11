---
concept: Basis
slug: basis
category: linear-algebra
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 409
section: "11.1 Definitions and Basic Theory"
extraction_confidence: high
aliases:
  - "ordered basis"
  - "set of free generators"
prerequisites:
  - vector-space
extends: []
related:
  - dimension
  - linear-independence
  - spanning-set
contrasts_with: []
answers_questions:
  - "What is a basis of a vector space?"
---

# Quick Definition
A basis of a vector space V is an ordered set of linearly independent vectors that span V. Every finite dimensional vector space has a basis, and any two bases have the same number of elements.

# Core Definition
A subset S of V is linearly independent if $\alpha_1 v_1 + \cdots + \alpha_n v_n = 0$ with $v_i \in S$ implies all $\alpha_i = 0$. A basis of V is an ordered set of linearly independent vectors which span V (Dummit & Foote, p. 409).

# Prerequisites
- **vector-space** — Bases exist in vector spaces

# Key Properties
1. Any spanning set contains a basis (Corollary 2)
2. Any linearly independent set extends to a basis (Building-Up Lemma, Corollary 5)
3. All bases have the same cardinality (Corollary 4)
4. Replacement Theorem (Theorem 3): independent vectors can replace basis vectors
5. A finite set spanning V with no proper spanning subset is a basis (Proposition 1)

# Examples
**Example** (p. 410): $F[x]/(f(x))$ with $\deg f = n$ has basis $\{1, \bar{x}, \bar{x}^2, \ldots, \bar{x}^{n-1}\}$.

# Relationships
## Builds Upon
- **vector-space**

## Enables
- **dimension** — Defined as the cardinality of a basis
- **matrix-of-linear-transformation** — Requires choice of bases

# Source Reference
Chapter 11, Section 11.1, pp. 409-413.

# Verification Notes
- Confidence: HIGH — explicit definitions and theorems
