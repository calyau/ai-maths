---
concept: Change of Basis
slug: change-of-basis
category: linear-algebra
subcategory: matrix-theory
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 418
section: "11.2 The Matrix of a Linear Transformation"
extraction_confidence: high
aliases:
  - "change of basis matrix"
  - "transition matrix"
  - "similar matrices"
prerequisites:
  - matrix-of-linear-transformation
  - basis
extends: []
related:
  - rational-canonical-form
  - jordan-canonical-form
contrasts_with: []
answers_questions:
  - "How do I change bases for a linear transformation?"
  - "When are two matrices similar?"
---

# Quick Definition
If $\mathcal{B}$ and $\mathcal{B}'$ are two bases of V and P is the change of basis matrix from $\mathcal{B}$ to $\mathcal{B}'$, then the matrix of $\varphi: V \to V$ transforms as $M_{\mathcal{B}'}(\varphi) = P^{-1} M_{\mathcal{B}}(\varphi) P$. Two matrices are similar iff they represent the same linear transformation in different bases.

# Core Definition
Let $\mathcal{B}$ and $\mathcal{B}'$ be bases of V. The change of basis matrix P has columns that are the coordinates of the new basis vectors in terms of the old basis. If A is the matrix of T with respect to $\mathcal{B}$, then $P^{-1}AP$ is the matrix with respect to $\mathcal{B}'$. Two matrices A, B are similar ($B = P^{-1}AP$ for some invertible P) iff they represent the same linear transformation (Dummit & Foote, pp. 418-422).

# Prerequisites
- **matrix-of-linear-transformation**, **basis**

# Key Properties
1. $B = P^{-1}AP$ defines an equivalence relation (similarity)
2. Similar matrices have the same characteristic polynomial, minimal polynomial, determinant, trace
3. The rational canonical form and Jordan canonical form are canonical representatives of similarity classes

# Relationships
## Builds Upon
- **matrix-of-linear-transformation**, **basis**

## Enables
- **rational-canonical-form**, **jordan-canonical-form** — Canonical representatives under similarity

# Source Reference
Chapter 11, Section 11.2, pp. 418-422.

# Verification Notes
- Confidence: HIGH — standard material
