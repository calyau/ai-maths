---
concept: General Linear Group over a Ring
slug: general-linear-group-ring
category: module-theory
subcategory: matrix-groups
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.2 Free Modules"
extraction_confidence: high
aliases:
  - "GL_n(R)"
prerequisites:
  - ring
  - invertible-matrix
extends:
  - general-linear-group
related:
  - free-module
contrasts_with: []
answers_questions:
  - "What is the general linear group over a ring?"
---

# Quick Definition

GL_n(R) is the group of n x n invertible R-matrices -- those whose determinant is a unit in R. Over Z, this means det = +/-1.

# Core Definition

The n x n invertible R-matrices form a group called the general linear group over R, denoted GL_n(R) (Artin, p. 434, equation 14.2.1). An R-matrix A is invertible iff its determinant is a unit of R (Lemma 14.2.3(a)). An invertible R-matrix is necessarily square (14.2.3(b)).

# Prerequisites

- **Ring** -- Matrix entries come from a ring
- **Invertible matrix** -- The group elements

# Key Properties

1. A is invertible iff det(A) is a unit in R (14.2.3(a))
2. Over Z, det(A) must be +/-1 for A to be in GL_n(Z)
3. Elementary R-matrices (I + ae_{ij} with i != j) are invertible and generate a large subgroup
4. Cramer's Rule gives the inverse: A^{-1} = (det A)^{-1} * cof(A)

# Context & Application

GL_n(R) captures the symmetries of free R-modules. It is much smaller than GL_n over a field when R has few units (e.g., GL_n(Z) requires det = +/-1).

# Examples

**Example 1** (p. 434): Over Z, most integer matrices that are invertible as real matrices are NOT in GL_n(Z) unless det = +/-1.

# Relationships

## Builds Upon
- **Ring** -- Matrix entries from a ring

## Related
- **Free module** -- GL_n(R) acts on R^n

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.2, pages 434-435. Lemma 14.2.3.

# Verification Notes

- Definition source: Direct from Artin (14.2.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
