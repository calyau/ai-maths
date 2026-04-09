---
# === CORE IDENTIFICATION ===
concept: Symplectic Group
slug: symplectic-group

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 10
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Sp₂ₘ"
  - "Aut(φ) for skew-symmetric φ"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - general-linear-group
extends:
  - general-linear-group
related:
  - orthogonal-group
contrasts_with:
  - orthogonal-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the symplectic group?"
  - "What group preserves a skew-symmetric bilinear form?"
---

# Quick Definition

The symplectic group Sp_{2m} is the group of linear automorphisms preserving a nondegenerate skew-symmetric bilinear form. In matrix terms, it consists of invertible matrices A satisfying A^T J_{2m} A = J_{2m}.

# Core Definition

When the bilinear form phi is skew-symmetric (phi(v, w) = -phi(w, v)) and nondegenerate, Aut(phi) is called the **symplectic group** of phi. There exists a basis for V for which the matrix of phi is J_{2m} = ((0, I_m), (-I_m, 0)) where 2m = n, and the group of invertible matrices A such that A^T J_{2m} A = J_{2m} is called the symplectic group Sp_{2m} (p. 10).

# Prerequisites

- **Group** — the symplectic group is a group
- **General linear group** — the symplectic group is a subgroup of GL_{2m}(F)

# Key Properties

1. Preserves a nondegenerate skew-symmetric bilinear form
2. The dimension of the underlying space must be even (2m)
3. In standard form: {A in GL_{2m}(F) | A^T J_{2m} A = J_{2m}}
4. J_{2m} = ((0, I_m), (-I_m, 0)) is the standard symplectic matrix

# Construction / Recognition

## To Construct:
1. Start with a 2m-dimensional vector space V and a nondegenerate skew-symmetric bilinear form phi
2. Choose a basis putting phi in standard form J_{2m}
3. Find all invertible matrices A satisfying A^T J_{2m} A = J_{2m}

# Context & Application

The symplectic group is one of the classical groups, arising naturally from skew-symmetric bilinear forms. It plays a fundamental role in Hamiltonian mechanics and symplectic geometry.

# Examples

**Example 1** (p. 10, 1.8): Sp_{2m} is the group of 2m x 2m matrices A satisfying A^T J_{2m} A = J_{2m}.

# Relationships

## Builds Upon
- **general-linear-group** — Sp_{2m} is a subgroup of GL_{2m}(F)

## Related
- **orthogonal-group** — analogous construction for symmetric forms

## Contrasts With
- **orthogonal-group** — symplectic preserves skew-symmetric forms; orthogonal preserves symmetric forms

# Common Confusions

- **Confusion**: Thinking a symplectic group can exist in odd dimensions
  **Clarification**: A nondegenerate skew-symmetric form requires even-dimensional space

# Source Reference

Chapter 1: Basic Definitions and Results, Example 1.8, page 10.

# Verification Notes

- Definition source: Direct from 1.8, p. 10
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
