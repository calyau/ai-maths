---
concept: Quadratic Form
slug: quadratic-form
category: classical-groups
subcategory: quadratic-spaces
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 203
section: "18a Quadratic spaces"
extraction_confidence: high
aliases:
  - "quadratic space"
prerequisites:
  - bilinear-form
extends: []
related:
  - orthogonal-group
  - clifford-algebra
  - witt-index
contrasts_with: []
answers_questions:
  - "What is a Clifford algebra?"
---

# Quick Definition

A quadratic form on a vector space V over a field k (char != 2) is a map q: V -> k such that q(x) = phi_q(x,x) for some symmetric bilinear form phi_q, which is uniquely determined by q.

# Core Definition

A **quadratic form** on a finite-dimensional k-vector space V (k not of characteristic 2) is a mapping q: V -> k such that q(x) = phi_q(x,x) for some symmetric bilinear form phi_q: V x V -> k (Milne, p. 203). The bilinear form is recovered via q(x+y) = q(x) + q(y) + 2phi_q(x,y). A **quadratic space** is a pair (V,q).

# Prerequisites

- **Bilinear form** -- Quadratic forms are defined via symmetric bilinear forms

# Key Properties

1. Every quadratic space has an orthogonal basis (Proposition 18.1)
2. The discriminant of (V,q) is det(phi(e_i,e_j)) in k/k^{*2}
3. (V,q) is regular (nondegenerate) if for all nonzero x, there exists y with phi(x,y) != 0
4. A nonzero vector x is isotropic if q(x) = 0, anisotropic if q(x) != 0
5. Over algebraically closed fields, all regular quadratic spaces of the same dimension are isomorphic

# Context & Application

Quadratic forms are the starting point for constructing orthogonal groups, Clifford algebras, and spin groups. The classification of quadratic forms over various fields (algebraically closed, real, p-adic, number fields) is a classical problem in algebra.

# Examples

**Example 1** (p. 203): With an orthogonal basis e_1,...,e_n, q(x_1,...,x_n) = c_1*x_1^2 + ... + c_n*x_n^2 where c_i = q(e_i).

# Relationships

## Enables
- **Orthogonal group** -- O(q) is the group of isometries of (V,q)
- **Clifford algebra** -- C(V,q) is constructed from (V,q)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 18a, pages 203-204.

# Verification Notes

- Definition source: Direct from p. 203
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
