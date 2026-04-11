---
concept: Algebraic Integer
slug: algebraic-integer
category: commutative-algebra
subcategory: number-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 722
section: "15.3 Integral Extensions and Hilbert's Nullstellensatz"
extraction_confidence: high
aliases:
  - "ring of integers"
  - "O_K"
prerequisites:
  - integral-extension
extends: []
related:
  - dedekind-domain
  - integral-closure
contrasts_with: []
answers_questions:
  - "What is an algebraic integer?"
  - "What is the ring of integers in a number field?"
---

# Quick Definition
An algebraic integer is an element of a field extension of Q that is integral over Z (i.e., a root of a monic polynomial with integer coefficients). The ring of integers O_K of a number field K is the integral closure of Z in K.

# Core Definition
An element α in an extension field of Q is an **algebraic integer** if α is integral over Z, i.e., α is the root of some monic polynomial with coefficients in Z (Definition, p. 722). The integral closure of Z in K is the **ring of integers** O_K (Definition, p. 722). By Proposition 28, α is an algebraic integer iff its minimal polynomial over Q has integer coefficients.

# Prerequisites
- **integral-extension** — Algebraic integers are integral over Z

# Key Properties
1. α is an algebraic integer iff its minimal polynomial over Q has Z-coefficients (Proposition 28)
2. The algebraic integers in Q are exactly Z
3. O_K is a Noetherian ring and a free Z-module of rank [K:Q] (Theorem 29)
4. Nonzero prime ideals in O_K are maximal
5. O_K is a Dedekind domain (Proposition 14 of Section 16.3)

# Examples
**Example** (p. 723): For K = Q(√D) with D squarefree, O_K = Z[ω] where ω = √D if D ≡ 2,3 (mod 4) and ω = (1+√D)/2 if D ≡ 1 (mod 4).

# Relationships
## Builds Upon
- **integral-extension** — Algebraic integers are integral over Z

## Enables
- **dedekind-domain** — Rings of integers are Dedekind domains

# Source Reference
Chapter 15, Section 15.3, Definitions, Propositions 28-29, pages 722-726.

# Verification Notes
- Confidence: HIGH — explicit definitions and characterizations
