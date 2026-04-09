---
# === CORE IDENTIFICATION ===
concept: Quaternion Algebra
slug: quaternion-algebra

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
pdf_page: 108
section: "Simple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "H(a,b)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
  - division-algebra
extends:
  - simple-f-algebra
related:
  - matrix-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a quaternion algebra?"
  - "When is a quaternion algebra a division algebra?"
---

# Quick Definition

For a, b in F^x, the quaternion algebra H(a,b) is the 4-dimensional F-algebra with basis {1, i, j, k} and multiplication i^2 = a, j^2 = b, ij = k = -ji. It is either a division algebra or isomorphic to M_2(F).

# Core Definition

For a, b in F^x, let **H(a,b)** be the F-algebra with basis {1, i, j, k} (as an F-vector space) and with multiplication determined by i^2 = a, j^2 = b, ij = k = -ji. Then H(a,b) is a **quaternion algebra** over F. It is either a division algebra or isomorphic to M_2(F). In particular, it is always simple. (Milne, Example 7.20, p. 108)

# Prerequisites

- **F-algebra** — quaternion algebras are F-algebras
- **Division algebra** — they may be division algebras

# Key Properties

1. Dimension 4 over F
2. Always simple
3. Either a division algebra or M_2(F) -- no other options
4. For F = R: H(-1,-1) is the classical Hamilton quaternions (a division algebra)
5. Over an algebraically closed field F, H(a,b) = M_2(F) for all a, b

# Construction / Recognition

1. Choose a, b in F^x
2. Define the 4-dimensional algebra with basis {1, i, j, k}
3. Multiplication rules: i^2 = a, j^2 = b, ij = k = -ji
4. Derive: ik = iij = aj, ki = -iij = -aj, jk = jij = -j^2 i = -bi, kj = iji = bi, k^2 = ijk = -ab

# Context & Application

Quaternion algebras are the simplest examples of non-commutative division algebras and simple algebras beyond matrix algebras over fields. Over R, the quaternion algebra H(-1,-1) is the only non-trivial division algebra (up to isomorphism), showing that the Brauer group of R has order 2.

# Examples

**Example 1** (p. 108, 7.20): H(-1,-1) over R is the classical quaternion algebra, a division algebra.

**Example 2** (p. 108): Over an algebraically closed field, every quaternion algebra is isomorphic to M_2(F).

# Relationships

## Builds Upon
- **f-algebra** — quaternion algebras are F-algebras
- **division-algebra** — may be division algebras

## Enables
- Understanding the Brauer group (via division algebra classification)

## Related
- **matrix-algebra** — quaternion algebras that are not division algebras are M_2(F)
- **simple-f-algebra** — quaternion algebras are simple

# Source Reference

Chapter 7: Representations of Finite Groups, Example 7.20, p. 108.

# Verification Notes

- Definition source: Direct from Example 7.20
- Confidence rationale: HIGH — explicit construction
- Uncertainties: None
