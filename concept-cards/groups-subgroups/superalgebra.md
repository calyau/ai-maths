---
concept: Superalgebra
slug: superalgebra
category: classical-groups
subcategory: quadratic-spaces
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 207
section: "18d Super algebras"
extraction_confidence: high
aliases:
  - "graded algebra"
  - "Z/2Z-graded algebra"
prerequisites: []
extends: []
related:
  - clifford-algebra
contrasts_with: []
answers_questions:
  - "What is a Clifford algebra?"
---

# Quick Definition

A superalgebra over k is a k-algebra C with a decomposition C = C_0 + C_1 such that C_i * C_j is contained in C_{i+j mod 2}. The super tensor product uses a sign rule for commuting odd elements.

# Core Definition

A **superalgebra** (or Z/2Z-graded algebra) over k is a k-algebra C together with a decomposition C = C_0 + C_1 as k-vector spaces such that k is contained in C_0 and C_i * C_j is contained in C_{i+j mod 2} (Milne, p. 207). The **super tensor product** C hat-tensor D has multiplication (c_i tensor d_j)(c'_k tensor d'_l) = (-1)^{jk}(c_i*c'_k tensor d_j*d'_l).

# Prerequisites

This is a foundational algebraic concept within this context.

# Key Properties

1. C_0 is a k-subalgebra of C
2. The super tensor product satisfies C(c_1,...,c_{i-1}) hat-tensor C(c_i) = C(c_1,...,c_i) (Example 18.11)
3. An ordinary k-algebra can be viewed as a superalgebra with A_1 = 0 (Example 18.12)
4. The Kunneth formula for manifold cohomology uses the super tensor product (Example 18.13)

# Context & Application

Superalgebras provide the natural framework for Clifford algebras, which have a Z/2Z-grading into even and odd parts. The super tensor product is essential for understanding how Clifford algebras decompose under orthogonal direct sums.

# Examples

**Example 1** (p. 207): C(c_1,...,c_n) with generators e_i satisfying e_i^2 = c_i and e_j*e_i = -e_i*e_j, graded by parity of the number of generators in each monomial.

# Relationships

## Enables
- **Clifford algebra** -- Clifford algebras are superalgebras

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 18d, pages 207-209.

# Verification Notes

- Definition source: Direct from p. 207
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
