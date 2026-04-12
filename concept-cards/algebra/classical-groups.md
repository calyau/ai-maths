---
# === CORE IDENTIFICATION ===
concept: Classical Groups
slug: classical-groups

# === CLASSIFICATION ===
category: linear-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.1 The Classical Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "matrix groups"
  - "linear groups"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bilinear-form
  - hermitian-form
  - skew-symmetric-form
extends: []
related:
  - general-linear-group
  - special-linear-group
  - orthogonal-group
  - unitary-group
  - symplectic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the classical groups?"
---

# Quick Definition

The classical groups are the most important subgroups of the general linear group: the special linear, orthogonal, unitary, and symplectic groups. They are defined as groups of matrices preserving various forms (dot product, Hermitian product, or symplectic form) or having determinant 1.

# Core Definition

Subgroups of the general linear group GL_n are called linear groups or matrix groups. The most important ones are the classical groups: the special linear group SL_n, orthogonal group O_n, special orthogonal group SO_n, unitary group U_n, special unitary group SU_n, and symplectic group Sp_{2n} (Artin, p. 264). They are defined by conditions on the matrix: determinant 1 (SL), P^t P = I (O), P*P = I (U), P^t S P = S (Sp), and intersections thereof.

# Prerequisites

- **Bilinear form** — Orthogonal and symplectic groups preserve forms
- **Hermitian form** — The unitary group preserves the Hermitian form
- **Skew-symmetric form** — The symplectic group preserves it

# Key Properties

1. All are subgroups of GL_n
2. O_n preserves dot product, U_n preserves Hermitian product, Sp_{2n} preserves symplectic form
3. SL_n is defined by det P = 1
4. "Special" means the subgroup of matrices with determinant 1
5. Symplectic matrices automatically have determinant 1
6. All classical groups are manifolds (closed subgroups of GL_n, Theorem 9.7.4)
7. They have complex analogues defined by the same relations

# Construction / Recognition

## To Recognize:
1. Check the defining relation (P^t P = I, P*P = I, det P = 1, etc.)

# Context & Application

The classical groups are the foundation of Lie theory, differential geometry, and physics. They appear as symmetry groups of physical systems. Artin's distinctive approach is to study them through concrete matrix groups rather than abstract axioms.

# Examples

**Example 1** (p. 264): The circle group U_1 = SO_2, the simplest nonabelian classical group has dimension 1.

**Example 2** (p. 265): SL_2 has dimension 3 (4 entries minus 1 determinant equation).

# Relationships

## Enables
- **General linear group** — GL_n contains all classical groups
- **Special linear group** — det P = 1
- **Orthogonal group** — P^t P = I
- **Unitary group** — P*P = I
- **Symplectic group** — P^t S P = S

# Common Errors

- **Error**: Confusing the complex orthogonal group with the unitary group
  **Correction**: Complex orthogonal is P^t P = I; unitary is P*P = I. These are different conditions.

# Common Confusions

- **Confusion**: Thinking "homeomorphism" and "homomorphism" are the same
  **Clarification**: Artin notes (p. 265) that homeomorphism (topological equivalence) differs from homomorphism (group map) by just one letter

# Source Reference

Chapter 9: Linear Groups, Section 9.1, pages 264-266.

# Verification Notes

- Definition source: Direct from p. 264
- Confidence rationale: Explicitly defined with all groups listed
- Uncertainties: None
- Cross-reference status: Verified
