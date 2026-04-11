---
concept: Radical of an Ideal
slug: radical-of-ideal
category: commutative-algebra
subcategory: ideal-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 695
section: "15.2 Radicals and Affine Varieties"
extraction_confidence: high
aliases:
  - "radical ideal"
  - "rad I"
  - "nilradical"
prerequisites:
  - ideal
  - prime-ideal
extends: []
related:
  - hilberts-nullstellensatz
  - primary-ideal
  - nilpotent-element
contrasts_with: []
answers_questions:
  - "What is the radical of an ideal?"
  - "What is a radical ideal?"
---

# Quick Definition
The radical of an ideal I, denoted rad I, is the set of elements r in R such that r^k ∈ I for some k ≥ 1. An ideal is radical if I = rad I.

# Core Definition
Let I be an ideal in a commutative ring R. The **radical of I**, denoted rad I, is {a ∈ R | a^k ∈ I for some k ≥ 1} (Definition, p. 695). The radical of the zero ideal is called the **nilradical** of R — it consists of all nilpotent elements. An ideal I is called a **radical ideal** if I = rad I. By Proposition 12 (p. 696), rad I equals the intersection of all prime ideals containing I.

# Prerequisites
- **ideal** — Radicals are defined for ideals
- **prime-ideal** — The radical is characterized as the intersection of primes containing I

# Key Properties
1. rad I is an ideal containing I (Proposition 11)
2. (rad I)/I is the nilradical of R/I
3. rad I = intersection of all prime ideals containing I (Proposition 12)
4. Prime and maximal ideals are radical (Corollary 13)
5. In a Noetherian ring, (rad I)^k ⊆ I for some k (Proposition 14)
6. I(V) is always a radical ideal for any algebraic set V

# Context & Application
Radical ideals are central to the Nullstellensatz: over algebraically closed fields, affine algebraic sets correspond bijectively to radical ideals. The concept bridges algebraic ideal theory with geometric zero sets.

# Examples
**Example** (p. 697): In Z, rad(180) = rad(2^2 · 3^2 · 5) = (2 · 3 · 5) = (30). Generally in a UFD, rad(p_1^{a_1}···p_r^{a_r}) = (p_1···p_r).

# Relationships
## Builds Upon
- **ideal** — Radicals are formed from ideals

## Enables
- **hilberts-nullstellensatz** — States I(Z(I)) = rad I over algebraically closed fields
- **primary-decomposition** — Decomposition relates to prime ideals appearing in the radical

# Source Reference
Chapter 15, Section 15.2, Definitions and Propositions 11-14, pages 695-697.

# Verification Notes
- Confidence: HIGH — explicit definitions and characterizations
