---
# === CORE IDENTIFICATION ===
concept: Ring
slug: ring

# === CLASSIFICATION ===
category: ring-theory
subcategory: basic-structures
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Definition of a Ring"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "commutative ring"
  - "commutative ring with identity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abelian-group
extends: []
related:
  - subring
  - ring-homomorphism
  - field
  - polynomial-ring
contrasts_with:
  - field
  - division-ring
  - noncommutative-ring

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a ring?"
  - "What distinguishes a ring from a field?"
---

# Quick Definition

A ring is a set with addition and multiplication satisfying the axioms of an abelian group under addition, commutativity and associativity of multiplication with identity, and the distributive law. Unlike fields, rings do not require multiplicative inverses.

# Core Definition

A ring R is a set with two laws of composition + and x, called addition and multiplication, that satisfy these axioms: (a) With the law of composition +, R is an abelian group R+, with identity 0. (b) Multiplication is commutative and associative, and has an identity denoted by 1. (c) Distributive law: For all a, b, c in R, (a + b)c = ac + bc (Artin, Definition 11.1.3, p. 339).

Artin uses "ring" to mean "commutative ring" throughout, noting that noncommutative rings (such as matrix rings) exist but are not the focus.

# Prerequisites

- **Abelian group** -- The additive structure of a ring must form an abelian group

# Key Properties

1. The additive group R+ is abelian with identity 0
2. Multiplication is commutative and associative with identity 1
3. The distributive law connects addition and multiplication
4. 0a = 0 for every element a (follows from distributive law)
5. If 1 = 0 in R, then R is the zero ring (Proposition 11.1.5)

# Construction / Recognition

## To Recognize:
1. Check that the set has two binary operations (addition and multiplication)
2. Verify the set is an abelian group under addition
3. Verify multiplication is commutative, associative, and has identity 1
4. Verify the distributive law holds

# Context & Application

Rings generalize the integers, serving as the basic algebraic structure for studying divisibility, factorization, and polynomial arithmetic. They are the central objects of commutative algebra and algebraic number theory.

# Examples

**Example 1** (p. 339): The integers Z are the basic model for a ring.

**Example 2** (p. 339): The Gauss integers Z[i] = {a + bi | a, b in Z} form a subring of C.

**Example 3** (p. 339): The ring of continuous real-valued functions forms a ring under pointwise addition and multiplication.

**Example 4** (p. 339): The zero ring {0} is a ring with 1 = 0, the only ring in which this holds.

# Relationships

## Builds Upon
- **Abelian group** -- The additive structure R+ is an abelian group

## Enables
- **Ideal** -- Ideals are special additive subgroups of rings
- **Quotient ring** -- Quotient construction for rings
- **Polynomial ring** -- Polynomials with coefficients in a ring form a ring

## Related
- **Subring** -- A subset closed under ring operations containing 1
- **Ring homomorphism** -- Structure-preserving maps between rings

## Contrasts With
- **Field** -- A ring where every nonzero element has a multiplicative inverse
- **Noncommutative ring** -- Satisfies all ring axioms except commutativity of multiplication

# Common Errors

- **Error**: Assuming the zero map between rings is a ring homomorphism
  **Correction**: The zero map does not send 1 to 1 (unless the target is the zero ring), so it is not a ring homomorphism

# Common Confusions

- **Confusion**: Thinking that "ring" always means noncommutative ring
  **Clarification**: Artin uses "ring" to mean commutative ring with identity throughout; this is common in algebraic number theory and algebraic geometry

- **Confusion**: Believing that 1 = 0 is impossible in a ring
  **Clarification**: It is possible but forces R to be the zero ring {0}

# Source Reference

Chapter 11: Rings, Section 11.1 "Definition of a Ring," pages 339-340. See Definition 11.1.3 and Proposition 11.1.5.

# Verification Notes

- Definition source: Direct from Definition 11.1.3
- Confidence rationale: Explicit, clearly stated definition with axioms
- Uncertainties: None
- Cross-reference status: Verified against planned extractions
