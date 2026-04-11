---
concept: Rank of a Free Module
slug: rank-of-free-module
category: module-theory
subcategory: generation
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 356
section: "10.3 Generation of Modules, Direct Sums, and Free Modules"
extraction_confidence: high
aliases:
  - "rank"
prerequisites:
  - free-module
extends: []
related:
  - dimension
contrasts_with: []
answers_questions:
  - "What is the rank of a free module?"
---

# Quick Definition
The rank of a free module over a commutative ring R is the cardinality of any basis. For commutative rings, this is well-defined: $R^n \cong R^m$ if and only if $n = m$.

# Core Definition
If R is a commutative ring and F is a free R-module with basis A, the cardinality of A is called the *rank* of F. For commutative rings, the rank is well-defined: two free R-modules of finite rank are isomorphic if and only if they have the same rank (Dummit & Foote, p. 356, Exercise 2 p. 360).

# Prerequisites
- **free-module** — Rank is defined for free modules

# Key Properties
1. For commutative rings, rank is well-defined (unique)
2. For noncommutative rings, rank may not be unique (Exercise 27 gives an example where $R \cong R^2$)
3. When R is a field, rank equals dimension

# Relationships
## Builds Upon
- **free-module**

## Related
- **dimension** — Rank for free modules over fields

# Source Reference
Chapter 10, Section 10.3, p. 356 and Exercise 2, p. 360.

# Verification Notes
- Confidence: HIGH — explicit definition, uniqueness proved in exercises
