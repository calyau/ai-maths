---
# === CORE IDENTIFICATION ===
concept: Conjugacy Classes and the Centre of F[G]
slug: conjugacy-classes-and-centre-of-f-g

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 113
section: "The representations of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-algebra
extends: []
related:
  - class-function
  - number-of-irreducible-representations
  - decomposition-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the dimension of the centre of F[G]?"
  - "How do conjugacy classes relate to the group algebra?"
---

# Quick Definition

The dimension of the centre of F[G] as an F-vector space equals the number of conjugacy classes in G. A basis for the centre is given by the class sums c_i = sum_{a in C_i} a.

# Core Definition

**Proposition 7.38.** The dimension of the centre of F[G] as an F-vector space is the number of conjugacy classes in G. Specifically, if C_1, ..., C_t are the conjugacy classes and c_i = sum_{a in C_i} a, then centre(F[G]) = Fc_1 + ... + Fc_t. (Milne, Proposition 7.38, p. 113)

# Prerequisites

- **Group algebra** — the centre of F[G] is being computed

# Key Properties

1. dim_F(centre(F[G])) = number of conjugacy classes = t
2. The class sums c_i form a basis for the centre
3. An element sum m_a a lies in the centre iff the function a -> m_a is constant on conjugacy classes
4. This connects the algebraic structure of F[G] to the combinatorics of conjugacy classes

# Construction / Recognition

1. List the conjugacy classes C_1, ..., C_t of G
2. Form the class sums c_i = sum_{a in C_i} a
3. These are linearly independent and span the centre of F[G]

# Context & Application

This proposition connects the number of conjugacy classes to the number of irreducible representations. Since F[G] = M_{f_1}(F) x ... x M_{f_t}(F), the centre has dimension t (one copy of F per factor), and t equals the number of conjugacy classes.

# Examples

**Example 1** (p. 113): For S_3 with conjugacy classes {(1)}, {(12), (13), (23)}, {(123), (132)}: the centre has dimension 3.

# Relationships

## Builds Upon
- **group-algebra** — centre of F[G]

## Enables
- **number-of-irreducible-representations** — equals dim of centre = number of conjugacy classes
- **class-function** — central elements correspond to class functions

## Related
- **decomposition-of-f-g** — the number of factors equals the dimension of the centre

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.38, p. 113.

# Verification Notes

- Definition source: Direct from Proposition 7.38
- Confidence rationale: HIGH — explicit proposition
- Uncertainties: None
