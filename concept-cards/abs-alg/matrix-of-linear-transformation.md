---
concept: Matrix of a Linear Transformation
slug: matrix-of-linear-transformation
category: linear-algebra
subcategory: matrix-theory
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 414
section: "11.2 The Matrix of a Linear Transformation"
extraction_confidence: high
aliases:
  - "matrix representation"
prerequisites:
  - linear-transformation
  - basis
extends: []
related:
  - change-of-basis
  - similar-matrices
contrasts_with: []
answers_questions:
  - "How do I find the matrix of a linear transformation?"
---

# Quick Definition
Given bases $\mathcal{B}$ of V and $\mathcal{E}$ of W, the matrix $M_{\mathcal{B}}^{\mathcal{E}}(\varphi)$ of a linear transformation $\varphi: V \to W$ has columns given by the coordinates of $\varphi(v_j)$ with respect to $\mathcal{E}$.

# Core Definition
Let $\mathcal{B} = \{v_1, \ldots, v_n\}$ be a basis of V and $\mathcal{E} = \{w_1, \ldots, w_m\}$ a basis of W. For $\varphi \in \text{Hom}_F(V, W)$, write $\varphi(v_j) = \sum_{i=1}^m \alpha_{ij} w_i$. The $m \times n$ matrix $M_{\mathcal{B}}^{\mathcal{E}}(\varphi) = (\alpha_{ij})$ is the matrix of $\varphi$ with respect to bases $\mathcal{B}$, $\mathcal{E}$. The map $\varphi \mapsto M_{\mathcal{B}}^{\mathcal{E}}(\varphi)$ is a vector space isomorphism $\text{Hom}_F(V, W) \cong M_{m \times n}(F)$ (Dummit & Foote, pp. 414-415, Theorem 10).

# Prerequisites
- **linear-transformation** — We represent linear transformations as matrices
- **basis** — Matrices depend on choice of bases

# Key Properties
1. The correspondence $\varphi \mapsto M_{\mathcal{B}}^{\mathcal{E}}(\varphi)$ is a vector space isomorphism
2. $M(\varphi \circ \psi) = M(\varphi) \cdot M(\psi)$ (composition corresponds to matrix multiplication)
3. Changing basis by invertible matrix P gives $M_{\mathcal{B}'}^{\mathcal{E}'}(\varphi) = Q^{-1} M_{\mathcal{B}}^{\mathcal{E}}(\varphi) P$

# Relationships
## Builds Upon
- **linear-transformation**, **basis**

## Enables
- **change-of-basis**, **similar-matrices**
- **rational-canonical-form**, **jordan-canonical-form**

# Source Reference
Chapter 11, Section 11.2, pp. 414-425.

# Verification Notes
- Confidence: HIGH — explicit construction with isomorphism theorem
