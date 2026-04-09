---
# === CORE IDENTIFICATION ===
concept: Opposite Algebra
slug: opposite-algebra

# === CLASSIFICATION ===
category: module-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 100
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "A^opp"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
extends: []
related:
  - centralizer-of-a-module
  - endomorphism-algebra-of-a-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the opposite of an F-algebra?"
  - "How does reversing multiplication affect an algebra?"
---

# Quick Definition

The opposite A^opp of an F-algebra A is the same F-vector space as A but with multiplication reversed: a *' b = ba.

# Core Definition

The **opposite** A^opp of an F-algebra A is defined as (A, +, *') where a *' b = ba. There is a one-to-one correspondence a <-> a': A <-> A^opp which is an isomorphism of F-vector spaces and satisfies a'b' = (ba)'. (Milne, Chapter 7, p. 100)

# Prerequisites

- **F-algebra** — the opposite is defined for F-algebras

# Key Properties

1. Same underlying F-vector space as A
2. Same addition as A
3. Multiplication is reversed: a *' b = ba
4. (A^opp)^opp = A
5. If A is commutative, then A^opp = A

# Construction / Recognition

1. Take an F-algebra A
2. Keep the same set and addition
3. Define new multiplication by reversing the order of factors
4. The result is A^opp

# Context & Application

The opposite algebra arises naturally when studying endomorphism algebras. For an F-algebra A, End_A(_A A) is isomorphic to A^opp (via right multiplication). This relationship is fundamental to the Wedderburn structure theorems and the double centralizer theorem.

# Examples

**Example 1** (p. 107): End_A(_A A) is isomorphic to A^opp as F-algebras, where the isomorphism sends the endomorphism "right multiplication by a" to a.

# Relationships

## Builds Upon
- **f-algebra** — defined for any F-algebra

## Enables
- **endomorphism-algebra-of-a-module** — End_A(_A A) = A^opp
- **wedderburn-theorem** — A = M_n(D^opp) in the structure theorem

## Related
- **centralizer-of-a-module** — centralizers relate to opposite algebras

## Contrasts With
- The original algebra A when A is noncommutative

# Common Errors

- **Error**: Forgetting that composition of right multiplications reverses order
  **Correction**: (phi_a o phi_{a'})(1) = a'a, not aa', which is why End_A(_A A) = A^opp

# Common Confusions

- **Confusion**: Thinking A^opp is always different from A
  **Clarification**: When A is commutative, A^opp = A

# Source Reference

Chapter 7: Representations of Finite Groups, p. 100 and p. 107 (7.16).

# Verification Notes

- Definition source: Direct from p. 100
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
