---
concept: Scalar Matrix
slug: scalar-matrix
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 239
section: "7.2 Examples: Polynomial Rings, Matrix Rings, and Group Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - matrix-ring
extends: []
related:
  - center-of-a-ring
  - matrix-ring
contrasts_with: []
answers_questions:
  - "What is a scalar matrix?"
---

# Quick Definition
A scalar matrix is a diagonal matrix $aI_n$ with a single element $a \in R$ on all diagonal entries. Scalar matrices form a subring of $M_n(R)$ isomorphic to R and constitute the center when R is commutative.

# Core Definition
An element $(a_{ij})$ of $M_n(R)$ is a *scalar matrix* if $a_{ii} = a$ for all i and $a_{ij} = 0$ for $i \neq j$, for some $a \in R$. The scalar matrices form a subring isomorphic to R. If R is commutative, they commute with all elements and form the center of $M_n(R)$ (Dummit & Foote, p. 239).

# Prerequisites
- **Matrix ring** — Scalar matrices are elements of $M_n(R)$

# Key Properties
1. The map $a \mapsto aI_n$ is an injective ring homomorphism $R \to M_n(R)$
2. If R is commutative, scalar matrices = center of $M_n(R)$
3. The identity matrix is the scalar matrix with $a = 1$

# Source Reference
Chapter 7, Section 7.2, page 239.

# Verification Notes
- Definition: Direct from p. 239
- Confidence: HIGH — explicit definition
