---
concept: Localization
slug: localization
category: commutative-algebra
subcategory: ring-constructions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 706
section: "15.4 Localization"
extraction_confidence: high
aliases:
  - "ring of fractions"
  - "D^{-1}R"
  - "localization at a prime"
prerequisites:
  - ring
  - prime-ideal
extends: []
related:
  - local-ring
  - prime-spectrum
contrasts_with: []
answers_questions:
  - "What is localization of a ring?"
  - "How does localization relate to the prime spectrum?"
---

# Quick Definition
Localization D^{-1}R inverts the elements of a multiplicatively closed set D ⊆ R, creating a ring of fractions r/d. Localizing at a prime P means inverting elements outside P, giving a local ring R_P.

# Core Definition
Let D be a multiplicatively closed subset of R containing 1. The **localization** (or ring of fractions) D^{-1}R is the ring of equivalence classes r/d where r ∈ R, d ∈ D, with (r,d) ~ (s,e) iff x(er-ds) = 0 for some x ∈ D (Theorem 36, p. 706). The map π: R → D^{-1}R sending r to r/1 satisfies a universal property. **Localizing at a prime** P means taking D = R - P; the result R_P is a local ring.

# Prerequisites
- **ring** — The base ring
- **prime-ideal** — The most important case is localization at a prime

# Key Properties
1. D^{-1}R = 0 iff 0 ∈ D (Corollary 37(2))
2. π is injective iff D has no zero divisors (Corollary 37(1))
3. Prime ideals of D^{-1}R correspond bijectively to primes of R disjoint from D (Proposition 38(3))
4. If R is Noetherian/Artinian, so is D^{-1}R (Proposition 38(4))
5. Localization is exact: preserves exactness of sequences

# Examples
**Example** (p. 707): Z_(p) = {a/b ∈ Q | p ∤ b} is the localization of Z at (p).

**Example** (p. 707): For f ∈ R, R_f = D^{-1}R where D = {f^n | n ≥ 0}. Then R_f ≅ R[x]/(xf-1).

# Relationships
## Enables
- **local-ring** — R_P is always a local ring
- **prime-spectrum** — Localization is the algebraic analogue of "looking near a point"
- **discrete-valuation-ring** — DVRs are localizations of Dedekind domains at primes

# Source Reference
Chapter 15, Section 15.4, Theorem 36 and Propositions 38-40, pages 706-713.

# Verification Notes
- Confidence: HIGH — thorough treatment with universal property
