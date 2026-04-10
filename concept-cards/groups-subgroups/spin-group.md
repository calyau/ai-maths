---
concept: Spin Group
slug: spin-group
category: classical-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 213
section: "18g The Spin group"
extraction_confidence: high
aliases:
  - "Spin(q)"
prerequisites:
  - clifford-algebra
  - orthogonal-group
extends: []
related:
  - clifford-group
  - classical-semisimple-groups
contrasts_with: []
answers_questions:
  - "What is a spin group?"
---

# Quick Definition

The spin group Spin(q) is the subgroup of the even Clifford algebra C_0(V,q) consisting of elements t with t*t = 1 and tVt^{-1} = V. It is a 2-fold covering of the special orthogonal group SO(q).

# Core Definition

The group **Spin(q)** consists of the elements t of C_0(V,q) such that (a) t*t = 1, (b) tVt^{-1} = V, and (c) the map x -> txt^{-1}: V -> V has determinant 1 (Milne, Definition 18.22). Condition (c) is actually superfluous -- it follows from (a) and (b) (Corollary 18.27).

# Prerequisites

- **Clifford algebra** -- Spin(q) lives inside C_0(V,q)
- **Orthogonal group** -- Spin(q) is a covering of SO(q)

# Key Properties

1. Spin(q) -> SO(q) has kernel of order 2 (Theorem 18.24)
2. Over algebraically closed fields, Spin(q) -> SO(q) is surjective
3. In general, the image may be a proper subgroup of SO(q) (e.g., the identity component for indefinite forms over R)
4. Spin(q) is an algebraic group: Spin(q)(K) = Spin(q_K) for all extensions K/k (Theorem 18.29)
5. The action of O(q) on C(V,q) preserves Spin(q) (Theorem 18.29)

# Construction / Recognition

## To Construct:
1. Start with a regular quadratic space (V,q)
2. Form the Clifford algebra C(V,q) = C_0 + C_1
3. Spin(q) = {t in C_0 | t*t = 1 and tVt^{-1} = V}

## To Recognize:
1. An element t of C_0 such that t*t = 1 and conjugation by t preserves V

# Context & Application

The spin group was historically introduced because not all representations of the orthogonal Lie algebra arise from the orthogonal group. As Chevalley explained, Cartan discovered "spinor" representations of so_n that come from Spin(q) but not from SO(q). This is why the simply connected cover of SO(q) is needed.

# Examples

**Example 1** (p. 213): The map Spin(q) -> SO(q) sends t to the isometry x -> txt^{-1}. The kernel is {+1, -1}.

**Example 2** (p. 214): For anisotropic a,b in V with q(a)q(b) = 1, the product ab lies in Spin(q) and maps to the composition of reflections R_a * R_b in SO(q).

# Relationships

## Builds Upon
- **Clifford algebra** -- Spin(q) is a subgroup of C_0(V,q)^x
- **Orthogonal group** -- Spin(q) is a double cover of SO(q)

## Enables
- **Spinor representations** -- Representations of Spin(q) not factoring through SO(q)

## Related
- **Clifford group** -- Gamma(q) is a larger group in C(V,q); Spin(q) is related to its even part

# Common Errors

- **Error**: Assuming Spin(q) -> SO(q) is always surjective
  **Correction**: It is surjective over algebraically closed fields but may not be in general

# Common Confusions

- **Confusion**: Confusing the Clifford group Gamma(q) with the spin group
  **Clarification**: Gamma(q) maps onto O(q) with kernel k^x; Spin(q) is a subgroup of C_0 that maps onto SO(q) with kernel {+/-1}

# Source Reference

Chapter I: Basic Theory of Affine Groups, Sections 18g-18j, pages 213-216.

# Verification Notes

- Definition source: Direct from Definition 18.22
- Confidence rationale: Explicit definition with proof of properties
- Uncertainties: None
- Cross-reference status: Verified
