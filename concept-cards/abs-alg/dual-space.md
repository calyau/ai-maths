---
concept: Dual Space
slug: dual-space
category: linear-algebra
subcategory: dual-spaces
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 425
section: "11.3 Dual Vector Spaces"
extraction_confidence: high
aliases:
  - "algebraic dual"
  - "dual vector space"
prerequisites:
  - vector-space
  - linear-transformation
extends: []
related:
  - dual-basis
  - double-dual
  - annihilator-dual-space
  - transpose
contrasts_with: []
answers_questions:
  - "What is the dual space of a vector space?"
---

# Quick Definition
The dual space $V^* = \text{Hom}_F(V, F)$ is the space of all linear functionals on V (linear maps from V to the base field F). For finite dimensional V, $\dim V^* = \dim V$.

# Core Definition
For V any vector space over F, let $V^* = \text{Hom}_F(V, F)$ be the space of linear transformations from V to F, called the dual space of V. Elements of $V^*$ are called linear functionals. If $\dim V = n$ (finite), then $\dim V^* = n$ (Dummit & Foote, p. 425, Proposition 18).

# Prerequisites
- **vector-space** — The dual is defined for vector spaces
- **linear-transformation** — Elements of $V^*$ are linear maps to F

# Key Properties
1. $\dim V^* = \dim V$ when V is finite dimensional
2. If V is infinite dimensional, $\dim V < \dim V^*$
3. There is a natural (basis-independent) isomorphism $V \cong V^{**}$ for finite dimensional V (Theorem 19)
4. The matrix of $\varphi^*: W^* \to V^*$ is the transpose of the matrix of $\varphi: V \to W$

# Relationships
## Builds Upon
- **vector-space**, **linear-transformation**

## Enables
- **dual-basis** — Basis of the dual space
- **double-dual** — $V^{**}$, naturally isomorphic to V (finite dim)
- **annihilator-dual-space** — Annihilator of a subspace

# Source Reference
Chapter 11, Section 11.3, pp. 425-432.

# Verification Notes
- Confidence: HIGH — explicit definition with dimension result
