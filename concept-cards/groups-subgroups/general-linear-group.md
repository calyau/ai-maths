---
# === CORE IDENTIFICATION ===
concept: General Linear Group
slug: general-linear-group

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 14
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - GL_n
  - GL(V)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - special-linear-group
  - multiplicative-group
  - coordinate-ring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The general linear group GL_n is the algebraic group of invertible n x n matrices. Its functor sends a k-algebra R to GL_n(R) = {A in M_n(R) | det(A) is a unit in R}, and its coordinate ring is k[X_11,...,X_nn]_{det(X_ij)}.

# Core Definition

The **general linear group** GL_n is the affine algebraic group with functor R -> GL_n(R) = {invertible n x n matrices with entries in R}. It has coordinate ring O(GL_n) = k[X_11,...,X_nn, Y]/(det(X_ij)Y - 1), equivalently the localization k[X_11,...,X_nn]_{det(X_ij)} (3.8, p. 31).

More generally, for a finitely generated projective k-module V, GL_V(R) = {R-linear automorphisms of R tensor V} defines an algebraic group (3.10, p. 32).

The Hopf algebra structure is (5.22, p. 49):
- Delta(x_{ik}) = sum_j x_{ij} tensor x_{jk} (matrix multiplication)
- Delta(y) = y tensor y
- epsilon(x_{ii}) = 1, epsilon(x_{ij}) = 0 for i != j, epsilon(y) = 1
- S(x_{ij}) = y * a_{ji} where a_{ji} is the cofactor (Cramer's rule)

# Prerequisites

- **Affine algebraic group** — GL_n is a key example

# Key Properties

1. GL_n is a reductive group (p. 16)
2. dim(GL_n) = n^2
3. Every affine algebraic group embeds as a closed subgroup of GL_n for some n (p. 15)
4. Z(GL_n) = G_m (scalar matrices) (Example 7.48, p. 84)
5. The determinant defines a surjective homomorphism det: GL_n -> G_m with kernel SL_n

# Examples

**Example 1** (p. 14): GL_n(k) is identified with the (n^2 + 1)-tuples ((a_ij), d) such that det(a_ij) * d = 1. This makes it an algebraic group.

**Example 2** (p. 16): GL_n is an extension of PGL_n by G_m: 1 -> G_m -> GL_n -> PGL_n -> 1.

# Relationships

## Enables
- **Special linear group** — SL_n = Ker(det: GL_n -> G_m)
- **Affine subgroup** — Every algebraic group embeds in some GL_n

## Related
- **Multiplicative group** — G_m = GL_1
- **Orthogonal group** — O_n and Sp_n are subgroups of GL_n

# Source Reference

Chapter I, Section 1 (p. 14), 3.8 (p. 31), 5.22 (p. 49).

# Verification Notes

- Definition source: Direct from 3.8 and 5.22
- Confidence rationale: Explicit definition with full Hopf algebra structure
- Uncertainties: None
- Cross-reference status: Verified
