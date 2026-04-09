---
concept: Determinant as Homomorphism
slug: determinant-as-homomorphism
category: morphisms
subcategory: concrete-homomorphisms
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 156
section: "Some Facts from Linear Algebra"
extraction_confidence: high
aliases: []
prerequisites:
  - group-homomorphism
  - general-linear-group
extends:
  - group-homomorphism
related:
  - special-linear-group
  - kernel-of-homomorphism
contrasts_with: []
answers_questions:
  - "How is the determinant a group homomorphism?"
  - "What is the kernel of the determinant map?"
---

# Quick Definition

The determinant map $\det: GL_n(\mathbb{R}) \to \mathbb{R}^*$ is a surjective group homomorphism since $\det(AB) = \det(A)\det(B)$. Its kernel is the special linear group $SL_n(\mathbb{R})$.

# Core Definition

"The determinant is a homomorphism into the multiplicative group of real numbers; that is, $\det(AB) = (\det A)(\det B)$" (Judson, p. 156). This makes $\det: GL_n(\mathbb{R}) \to \mathbb{R}^*$ a group homomorphism with $\ker(\det) = SL_n(\mathbb{R})$.

# Prerequisites

- **Group homomorphism** — The determinant is an example
- **General linear group** — The domain

# Key Properties

1. $\det(AB) = \det(A)\det(B)$ (homomorphism property)
2. $\det(A^{-1}) = 1/\det(A)$
3. $\det(A^t) = \det(A)$
4. $\ker(\det) = SL_n(\mathbb{R})$
5. By the First Isomorphism Theorem: $GL_n(\mathbb{R})/SL_n(\mathbb{R}) \cong \mathbb{R}^*$

# Examples

**Example 1** (p. 148): $\phi: GL_2(\mathbb{R}) \to \mathbb{R}^*$ by $A \mapsto \det(A)$. The kernel is $SL_2(\mathbb{R})$.

# Relationships

## Builds Upon
- **Group homomorphism** — The determinant is a concrete homomorphism

## Enables
- **Special linear group** — Defined as $\ker(\det)$

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.1, p. 156. Also Chapter 11, Example 11.2, 11.6.

# Verification Notes

- Definition source: p. 156 and Example 11.2
- Confidence: HIGH
