---
concept: Diagonalization
slug: diagonalization
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.6 Triangular and Diagonal Forms"
extraction_confidence: high
aliases:
  - "diagonalizable matrix"
  - "diagonalizable operator"
prerequisites:
  - linear-operator
  - eigenvector
  - eigenvalue
  - characteristic-polynomial
extends: []
related:
  - similar-matrices
  - jordan-form
contrasts_with: []
answers_questions:
  - "How do I compute eigenvalues and eigenvectors?"
---

# Quick Definition

A linear operator T is diagonalizable if there exists a basis of eigenvectors. Equivalently, its matrix is similar to a diagonal matrix. This happens when the characteristic polynomial has n distinct roots, and more generally when the eigenspaces are large enough.

# Core Definition

A matrix A is similar to a diagonal matrix if A' = P^(-1)AP is diagonal for some invertible P. This is equivalent to F^n having a basis of eigenvectors of A (Proposition 4.4.8). If the characteristic polynomial has n distinct roots, diagonalization is guaranteed (Theorem 4.6.6). The diagonal entries are the eigenvalues, and the columns of P are the eigenvectors (Artin, pp. 129-131).

# Prerequisites

- **Linear operator** — The operator being diagonalized
- **Eigenvector** — Need a basis of eigenvectors
- **Eigenvalue** — The diagonal entries
- **Characteristic polynomial** — Must factor into linear factors with enough eigenvectors

# Key Properties

1. A is diagonalizable iff F^n has a basis of eigenvectors
2. If p(t) has n distinct roots, A is diagonalizable (Theorem 4.6.6)
3. P^(-1)AP = Lambda where Lambda = diag(lambda_1,...,lambda_n)
4. A^k = P Lambda^k P^(-1) (easy to compute powers)
5. Over C, every matrix with distinct eigenvalues is diagonalizable

# Construction / Recognition

## To Construct:
1. Find all eigenvalues (roots of characteristic polynomial)
2. For each eigenvalue, find a basis of the eigenspace
3. If these bases together form a basis of F^n, form P from eigenvector columns
4. Then P^(-1)AP is diagonal

## To Recognize:
1. The characteristic polynomial has n distinct roots (sufficient but not necessary)
2. The sum of eigenspace dimensions equals n

# Context & Application

Diagonalization is one of the most powerful tools in linear algebra. It simplifies the computation of powers A^k, matrix exponentials, and the analysis of linear systems. The Jordan form handles the case when diagonalization fails.

# Examples

**Example 1** (pp. 130-131): A = [[3,2],[1,4]] has eigenvectors v_1=(1,1)^t, v_2=(2,-1)^t. With P = [[1,2],[1,-1]], P^(-1)AP = [[5,0],[0,2]].

**Example 2** (p. 131): A^k = P * diag(5^k, 2^k) * P^(-1).

# Relationships

## Builds Upon
- **Eigenvector** — Need a basis of eigenvectors
- **Characteristic polynomial** — Provides eigenvalues

## Enables
- Computing powers A^k, exponentials, etc.

## Related
- **Similar matrices** — Diagonalizable means similar to a diagonal matrix
- **Jordan form** — The generalization when diagonalization fails

# Common Errors

- **Error**: Assuming every matrix is diagonalizable
  **Correction**: Matrices with repeated eigenvalues and insufficient eigenvectors are not diagonalizable

# Common Confusions

- **Confusion**: Thinking diagonalizability depends on the field
  **Clarification**: A real matrix may not be diagonalizable over R but may be over C

# Source Reference

Chapter 4: Linear Operators, Section 4.6, pages 129-132.

# Verification Notes

- Definition source: From Proposition 4.4.8 and Theorem 4.6.6
- Confidence rationale: Central topic with detailed treatment
- Uncertainties: None
- Cross-reference status: Verified
