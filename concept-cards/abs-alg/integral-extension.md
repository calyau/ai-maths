---
concept: Integral Extension
slug: integral-extension
category: commutative-algebra
subcategory: ring-extensions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 715
section: "15.3 Integral Extensions and Hilbert's Nullstellensatz"
extraction_confidence: high
aliases:
  - "integral element"
  - "integral over R"
prerequisites:
  - ring
  - module
extends: []
related:
  - algebraic-integer
  - integral-closure
  - going-up-theorem
  - going-down-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for an element to be integral over a ring?"
  - "What is an integral extension?"
---

# Quick Definition
An element s of a commutative ring S is integral over a subring R if s is a root of a monic polynomial in R[x]. The ring S is an integral extension of R if every element of S is integral over R.

# Core Definition
Let R be a subring of S with 1 ∈ R. An element s ∈ S is **integral** over R if s is the root of a monic polynomial in R[x] (Definition, p. 715). Equivalently (Proposition 23): (1) s is integral over R, (2) R[s] is a finitely generated R-module, (3) s ∈ T for some subring T with R ⊆ T ⊆ S that is finitely generated as an R-module. The set of elements integral over R forms a subring — the **integral closure** of R in S (Corollary 24).

# Prerequisites
- **ring** — The base ring R and extension S
- **module** — Characterization uses R-module structure

# Key Properties
1. Integral elements form a subring (Corollary 24(2))
2. Integrality is transitive (Corollary 24(3))
3. Every UFD is integrally closed in its fraction field
4. If S/R is integral and S is a domain, then R is a field iff S is a field (Theorem 26(1))

# Examples
**Example** (p. 717): If R, S are fields then S integral over R iff S is algebraic over R.

**Example** (p. 717): k[x,y]/(x^2-y^3) is NOT integrally closed: x̄/ȳ satisfies (x̄/ȳ)^3 = x̄.

# Relationships
## Enables
- **going-up-theorem** — About lifting chains of primes in integral extensions
- **algebraic-integer** — Integers in number fields are integral over Z

# Source Reference
Chapter 15, Section 15.3, Definition and Propositions 23-25, pages 715-717.

# Verification Notes
- Confidence: HIGH — explicit definition with three equivalent characterizations
