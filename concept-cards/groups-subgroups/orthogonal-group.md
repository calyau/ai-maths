---
# === CORE IDENTIFICATION ===
concept: Orthogonal Group
slug: orthogonal-group

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
pdf_page: 16
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - O_n
  - "O(\\phi)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - general-linear-group
extends: []
related:
  - special-orthogonal-group
  - symplectic-group
contrasts_with:
  - symplectic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The orthogonal group O_n is the algebraic group of n x n matrices A such that A^t * A = I. More generally, O(phi) is the group preserving a nondegenerate symmetric bilinear form phi.

# Core Definition

For an invertible n x n matrix C with entries in k, the algebraic group G with G(R) = {T in GL_n(R) | T^t * C * T = C} is an affine algebraic group, represented by a quotient of k[X_11,...,X_nn, Y] by the polynomial conditions. When C = I, this is the **orthogonal group** O_n (3.9, p. 32).

O_n is not connected: det(A)^2 = 1 for all A in O_n, and diag(-1, 1,...) has determinant -1. The **special orthogonal group** SO_n = Ker(O_n -> {+/- 1}) is the connected component of the identity, a normal subgroup of index 2 (p. 16).

# Prerequisites

- **Affine algebraic group** — O_n is an algebraic group
- **General linear group** — O_n is a closed subgroup of GL_n

# Key Properties

1. O_n is not connected; it has two connected components
2. SO_{2n+1} is almost-simple of type B_n (p. 15)
3. SO_{2n} is almost-simple of type D_n (p. 15)
4. The abstract version O(phi) preserves a nondegenerate symmetric bilinear form phi: V x V -> k (3.10, p. 32)

# Examples

**Example 1** (p. 16): O_n(k) = {A in M_n(k) | A^t A = I}, with det(A) in {+/- 1}.

# Relationships

## Builds Upon
- **General linear group** — O_n is a subgroup of GL_n

## Related
- **Special orthogonal group** — SO_n is the identity component of O_n
- **Symplectic group** — Another classical group preserving a bilinear form (alternating instead of symmetric)

# Source Reference

Chapter I, Section 1 (p. 16), 3.9-3.10 (p. 32).

# Verification Notes

- Definition source: Direct from p. 16 and 3.9
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
