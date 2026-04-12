---
concept: Eigenvector
slug: eigenvector
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.4 Eigenvectors"
extraction_confidence: high
aliases:
  - "characteristic vector"
prerequisites:
  - linear-operator
  - eigenvalue
extends: []
related:
  - eigenspace
  - diagonalization
  - generalized-eigenvector
contrasts_with: []
answers_questions:
  - "What is an eigenvalue/eigenvector?"
  - "How do I compute eigenvalues and eigenvectors?"
---

# Quick Definition

An eigenvector of a linear operator T is a nonzero vector v such that T(v) = lambda*v for some scalar lambda (the eigenvalue). The operator scales v by lambda without changing its direction.

# Core Definition

An eigenvector v of a linear operator T is a nonzero vector such that T(v) = lambda*v for some scalar lambda, called the eigenvalue (Artin, p. 121, formula 4.4.5). An eigenvector is NEVER zero. A nonzero column vector X is an eigenvector of a matrix A if AX = lambda*X.

# Prerequisites

- **Linear operator** — Eigenvectors are defined for operators
- **Eigenvalue** — Each eigenvector has an associated eigenvalue

# Key Properties

1. An eigenvector must be nonzero
2. v is an eigenvector iff it is in ker(lambda*I - T) \ {0}
3. Eigenvectors with distinct eigenvalues are linearly independent (Proposition 4.6.5)
4. The span of an eigenvector is a 1-dimensional invariant subspace
5. If there is a basis of eigenvectors, the operator is diagonalizable

# Construction / Recognition

## To Construct:
1. Find an eigenvalue lambda (root of characteristic polynomial)
2. Solve (lambda*I - A)X = 0
3. Any nonzero solution is an eigenvector

## To Recognize:
1. T(v) = lambda*v for some scalar lambda and v != 0
2. Equivalently: AX is a scalar multiple of X

# Context & Application

Eigenvectors provide the basis in which a linear operator is simplest (diagonal if possible). They represent directions that are preserved by the operator. In R^n, eigenvectors of a positive matrix always include one in the first quadrant.

# Examples

**Example 1** (p. 126): For A = [[3,2],[1,4]] with eigenvalues 5 and 2: eigenvectors v_1 = (1,1)^t (for lambda=5) and v_2 = (2,-1)^t (for lambda=2).

**Example 2** (p. 122): e_1 = (1,0)^t is an eigenvector of [[3,1],[0,2]] with eigenvalue 3.

# Relationships

## Builds Upon
- **Eigenvalue** — Each eigenvector has an eigenvalue

## Enables
- **Diagonalization** — A basis of eigenvectors diagonalizes the operator
- **Eigenspace** — Set of all eigenvectors for a given eigenvalue (plus 0)

## Related
- **Generalized eigenvector** — Extends the notion when not enough eigenvectors exist

# Common Errors

- **Error**: Including 0 as an eigenvector
  **Correction**: By definition, eigenvectors must be nonzero

# Common Confusions

- **Confusion**: Thinking eigenvectors are unique
  **Clarification**: Any nonzero scalar multiple of an eigenvector is also an eigenvector with the same eigenvalue

# Source Reference

Chapter 4: Linear Operators, Sections 4.4-4.5, pages 121-126.

# Verification Notes

- Definition source: Direct from (4.4.5), p. 121
- Confidence rationale: Central concept, explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
