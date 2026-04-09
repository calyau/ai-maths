---
# === CORE IDENTIFICATION ===
concept: Orthogonal Group
slug: orthogonal-group

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
pdf_page: 9
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Aut(φ) for symmetric φ"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - general-linear-group
extends:
  - general-linear-group
related:
  - symplectic-group
contrasts_with:
  - symplectic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the orthogonal group?"
  - "What group preserves a symmetric bilinear form?"
---

# Quick Definition

The orthogonal group of a nondegenerate symmetric bilinear form phi is the group of linear automorphisms preserving phi, i.e., those invertible linear maps alpha satisfying phi(alpha v, alpha w) = phi(v, w) for all v, w.

# Core Definition

Let V be a finite-dimensional vector space over a field F with a bilinear form phi: V x V -> F. An automorphism of phi is an isomorphism alpha: V -> V such that phi(alpha v, alpha w) = phi(v, w) for all v, w in V. The automorphisms form a group Aut(phi). When phi is symmetric (phi(v, w) = phi(w, v)) and nondegenerate, Aut(phi) is called the **orthogonal group** of phi. In matrix terms, choosing a basis with matrix P = (phi(e_i, e_j)), the orthogonal group consists of invertible matrices A such that A^T P A = P (1.8, pp. 9-10).

# Prerequisites

- **Group** — the orthogonal group is a group
- **General linear group** — the orthogonal group is a subgroup of GL(V)

# Key Properties

1. Preserves a nondegenerate symmetric bilinear form
2. In matrix form: {A in GL_n(F) | A^T P A = P}
3. When P = I_n (standard inner product), gives the classical orthogonal group O_n

# Construction / Recognition

## To Construct:
1. Start with a finite-dimensional vector space V and a nondegenerate symmetric bilinear form phi
2. Find all invertible linear maps alpha: V -> V satisfying phi(alpha v, alpha w) = phi(v, w)
3. These form the orthogonal group

# Context & Application

The orthogonal group is one of the classical groups arising from bilinear forms. It captures the symmetries that preserve lengths and angles. Together with the symplectic group (for skew-symmetric forms), it exemplifies how geometric structure constrains the symmetry group.

# Examples

**Example 1** (pp. 9-10, 1.8): For a symmetric nondegenerate bilinear form with matrix P, the orthogonal group consists of matrices A satisfying A^T P A = P.

# Relationships

## Builds Upon
- **general-linear-group** — the orthogonal group is a subgroup of GL(V)

## Related
- **symplectic-group** — analogous construction for skew-symmetric forms

## Contrasts With
- **symplectic-group** — orthogonal preserves symmetric forms; symplectic preserves skew-symmetric forms

# Common Errors

- **Error**: Assuming the orthogonal group always consists of matrices with A^T A = I
  **Correction**: That is the special case P = I; in general the condition is A^T P A = P

# Common Confusions

- **Confusion**: Confusing orthogonal group with special orthogonal group
  **Clarification**: The special orthogonal group SO_n additionally requires det(A) = 1

# Source Reference

Chapter 1: Basic Definitions and Results, Example 1.8, pages 9-10.

# Verification Notes

- Definition source: Direct from 1.8, pp. 9-10
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
