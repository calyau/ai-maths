---
# === CORE IDENTIFICATION ===
concept: Symplectic Group
slug: symplectic-group

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
pdf_page: 15
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Sp_n
  - "Sp(\\psi)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - general-linear-group
extends: []
related:
  - orthogonal-group
contrasts_with:
  - orthogonal-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The symplectic group Sp_{2n} is the algebraic group of invertible 2n x 2n matrices A preserving the standard alternating form: A^t * J * A = J where J = (0, I; -I, 0). It is almost-simple of type C_n.

# Core Definition

The **symplectic group** Sp_{2n} consists of all invertible 2n x 2n matrices A such that A^t * J * A = J where J = (0, I; -I, 0) (p. 15). It is an affine algebraic group, defined by polynomial conditions on the matrix entries (3.9, p. 32).

More generally, Sp(psi)(R) = {alpha in GL_V(R) | psi(alpha v, alpha w) = psi(v, w)} for a nondegenerate alternating form psi (3.10, p. 32).

Sp_{2n} is almost-simple of type C_n for n >= 3 in the Killing-Cartan classification (p. 15).

# Prerequisites

- **Affine algebraic group** — Sp_{2n} is an algebraic group
- **General linear group** — Sp_{2n} is a subgroup of GL_{2n}

# Key Properties

1. Sp_{2n} is connected and almost-simple (type C_n for n >= 3)
2. Elements of Sp_{2n} automatically have determinant 1
3. Sp_{2n} preserves a nondegenerate alternating bilinear form

# Examples

**Example 1** (p. 15): Sp_{2n} consists of all invertible 2n x 2n matrices A with A^t * J * A = J.

**Example 2** (p. 32): The abstract version Sp(psi) for a nondegenerate alternating form psi on a finitely generated projective module V.

# Relationships

## Builds Upon
- **General linear group** — Sp_{2n} is a closed subgroup of GL_{2n}

## Contrasts With
- **Orthogonal group** — O_n preserves a symmetric form; Sp_n preserves an alternating form

# Source Reference

Chapter I, Section 1 (p. 15), 3.9-3.10 (p. 32).

# Verification Notes

- Definition source: Direct from p. 15 and 3.9
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
