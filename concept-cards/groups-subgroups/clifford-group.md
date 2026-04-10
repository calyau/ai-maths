---
concept: Clifford Group
slug: clifford-group
category: classical-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 214
section: "18h The Clifford group"
extraction_confidence: high
aliases:
  - "Gamma(q)"
prerequisites:
  - clifford-algebra
  - orthogonal-group
extends: []
related:
  - spin-group
contrasts_with:
  - spin-group
answers_questions:
  - "What is a spin group?"
---

# Quick Definition

The Clifford group Gamma(q) consists of invertible elements t of the Clifford algebra C(V,q) such that gamma(t)Vt^{-1} = V, where gamma is the grading automorphism. It maps surjectively onto O(q) with kernel k^x.

# Core Definition

The **Clifford group** is Gamma(q) = {t in C(V,q) | t invertible and gamma(t)Vt^{-1} = V}, where gamma is the automorphism acting as 1 on C_0 and -1 on C_1 (Milne, Definition 18.25). The map alpha(t)(x) = gamma(t)xt^{-1} gives an isometry of V.

# Prerequisites

- **Clifford algebra** -- Gamma(q) lives in C(V,q)
- **Orthogonal group** -- alpha maps Gamma(q) onto O(q)

# Key Properties

1. The sequence 1 -> k^x -> Gamma(q) -> O(q) -> 1 is exact (Proposition 18.26)
2. For t in Gamma(q), alpha(t) is an isometry (Proposition 18.26)
3. Every element of Gamma(q) is of the form c*a_1...a_m with c in k^x and a_i anisotropic in V
4. An invertible element of C_0 with tVt^{-1} = V automatically has det(x -> txt^{-1}) = 1 (Corollary 18.27)

# Context & Application

The Clifford group is a larger group than Spin(q) that maps onto the full orthogonal group O(q) rather than just SO(q). It provides the natural framework for understanding the relationship between the Clifford algebra and the orthogonal group.

# Examples

**Example 1** (p. 214): For an anisotropic a in V, a is in Gamma(q) and alpha(a) = -R_a (the negative of the reflection).

# Relationships

## Builds Upon
- **Clifford algebra** -- Gamma(q) is a subgroup of C(V,q)^x

## Related
- **Spin group** -- Spin(q) is related to the even part of Gamma(q)

## Contrasts With
- **Spin group** -- Gamma(q) maps onto O(q); Spin(q) maps onto SO(q)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 18h, pages 214-215.

# Verification Notes

- Definition source: Direct from Definition 18.25
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
