---
concept: Linear Transformation
slug: linear-transformation
category: linear-algebra
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 408
section: "11.1 Definitions and Basic Theory"
extraction_confidence: high
aliases:
  - "linear map"
  - "F-linear map"
prerequisites:
  - vector-space
extends:
  - module-homomorphism
related:
  - matrix-of-linear-transformation
  - nullity
  - rank-of-linear-transformation
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition
A linear transformation $\varphi: V \to W$ between vector spaces over F is an F-module homomorphism: $\varphi(\alpha v + w) = \alpha\varphi(v) + \varphi(w)$ for all $\alpha \in F$ and $v, w \in V$.

# Core Definition
A linear transformation is a module homomorphism when the ring is a field. The kernel (null space) and image are subspaces. The nullity is $\dim\ker\varphi$ and the rank is $\dim\varphi(V)$. The fundamental relation is $\dim V = \text{nullity} + \text{rank}$ (Corollary 8). If $\ker\varphi = 0$, the transformation is nonsingular (Dummit & Foote, pp. 408, 413).

# Prerequisites
- **vector-space** — Linear transformations map between vector spaces

# Key Properties
1. $\dim V = \dim\ker\varphi + \dim\text{image}(\varphi)$ (rank-nullity theorem)
2. For equal dimensions: injective $\iff$ surjective $\iff$ isomorphism (Corollary 9)
3. Determined by values on a basis
4. $\text{Hom}_F(V, W) \cong M_{m \times n}(F)$ as vector spaces (Theorem 10)

# Context & Application
Linear transformations are the morphisms in the category of vector spaces. Their study via matrices is the heart of linear algebra.

# Relationships
## Builds Upon
- **vector-space**, **module-homomorphism**

## Enables
- **matrix-of-linear-transformation** — Matrix representation with respect to bases

# Source Reference
Chapter 11, Section 11.1, pp. 408-414; Section 11.2, pp. 414-425.

# Verification Notes
- Confidence: HIGH — standard definitions
