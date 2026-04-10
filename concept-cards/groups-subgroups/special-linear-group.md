---
# === CORE IDENTIFICATION ===
concept: Special Linear Group
slug: special-linear-group

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
  - SL_n
  - SL(V)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - general-linear-group
extends: []
related:
  - general-linear-group
  - almost-simple-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The special linear group SL_n is the algebraic group of n x n matrices with determinant 1. Its coordinate ring is k[X_11,...,X_nn]/(det(X_ij) - 1).

# Core Definition

The **special linear group** SL_n is the affine algebraic group with functor R -> SL_n(R) = {n x n matrices with entries in R and determinant 1}. Its coordinate ring is O(SL_n) = k[X_11,...,X_nn]/(det(X_ij) - 1) (3.7, p. 31).

The entries of the product of two matrices are polynomials in the entries of the two matrices, and Cramer's rule realizes the inverse entries as polynomials when det = 1 (p. 14).

SL_n is almost-simple for n > 1, with finite centre Z = {diag(zeta,...,zeta) | zeta^n = 1} and simple quotient PSL_n = SL_n/Z (p. 15).

# Prerequisites

- **Affine algebraic group** — SL_n is a foundational example
- **General linear group** — SL_n is the kernel of det: GL_n -> G_m

# Key Properties

1. O(SL_n) = k[X_11,...,X_nn]/(det(X_ij) - 1)
2. SL_n is almost-simple for n > 1 (type A_{n-1} in the Killing-Cartan classification)
3. SL_n = Ker(det: GL_n -> G_m) (Example 7.17, p. 77)
4. dim(SL_n) = n^2 - 1
5. SL_n is smooth and connected

# Examples

**Example 1** (p. 14): SL_n(k) is the subset of M_n(k) = k^{n^2} defined by the polynomial condition det(a_ij) = 1.

**Example 2** (p. 34): The homomorphism G_a -> SL_2 sends a to the matrix (1, a; 0, 1).

# Relationships

## Builds Upon
- **General linear group** — SL_n is the kernel of the determinant map on GL_n

## Related
- **Almost-simple algebraic group** — SL_n is the prototypical almost-simple group (type A_{n-1})

# Source Reference

Chapter I, Section 1 (p. 14), 3.7 (p. 31), Example 7.17 (p. 77).

# Verification Notes

- Definition source: Direct from p. 14 and 3.7
- Confidence rationale: First example given in the book
- Uncertainties: None
- Cross-reference status: Verified
