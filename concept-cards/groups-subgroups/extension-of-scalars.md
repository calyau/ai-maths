---
# === CORE IDENTIFICATION ===
concept: Extension of Scalars
slug: extension-of-scalars

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 35
section: "Some basic constructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - base change
  - extension of the base ring

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-group
extends: []
related:
  - weil-restriction-of-scalars
contrasts_with:
  - weil-restriction-of-scalars

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

For a k-algebra k', the base change G_{k'} of an affine group G over k is the affine group over k' obtained by restricting the functor G to k'-algebras. Its coordinate ring is O(G_{k'}) = k' tensor_k O(G).

# Core Definition

Let k' be a k-algebra. A k'-algebra R can be regarded as a k-algebra through k -> k' -> R, and so a functor G of k-algebras "restricts" to a functor G_{k'}: R -> G(R) of k'-algebras. If G is an affine group, then G_{k'} is an affine group with coordinate ring O(G_{k'}) = k' tensor_k O(G) (Section 4c, p. 35).

The affine group G_{k'} is said to have been obtained from G by **extension of the base ring** (or by **extension of scalars**). The functor G -> G_{k'} has a right adjoint: restriction of scalars (Section 4d).

# Prerequisites

- **Affine group** — Base change is applied to affine groups

# Key Properties

1. O(G_{k'}) = k' tensor_k O(G)
2. If G is algebraic, so is G_{k'}
3. G -> G_{k'} is a functor
4. Has a right adjoint: Weil restriction of scalars (when k'/k is finitely generated projective)

# Examples

**Example 1** (p. 36): For the unitary group G defined by K/k, G_{k^{al}} is isomorphic to GL_n.

# Relationships

## Related
- **Weil restriction of scalars** — The right adjoint to extension of scalars

## Contrasts With
- **Weil restriction of scalars** — Extension goes up (k -> k'); restriction goes down (k' -> k)

# Source Reference

Chapter I, Section 4c (p. 35-36).

# Verification Notes

- Definition source: Direct from Section 4c
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
