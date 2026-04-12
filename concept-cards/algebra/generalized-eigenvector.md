---
concept: Generalized Eigenvector
slug: generalized-eigenvector
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.7 Jordan Form"
extraction_confidence: high
aliases: []
prerequisites:
  - eigenvector
  - eigenvalue
  - linear-operator
extends:
  - eigenvector
related:
  - jordan-form
  - jordan-block
contrasts_with:
  - eigenvector
answers_questions:
  - "What is the Jordan normal form?"
---

# Quick Definition

A generalized eigenvector of T with eigenvalue lambda is a nonzero vector x such that (T - lambda)^k x = 0 for some k > 0. Its exponent d is the smallest such k. An ordinary eigenvector has exponent 1.

# Core Definition

A generalized eigenvector with eigenvalue lambda of a linear operator T is a nonzero vector x such that (T - lambda)^k x = 0 for some k > 0. Its exponent is the smallest integer d such that (T - lambda)^d x = 0 (Artin, p. 133). The chain u_j = (T - lambda)^j x for j = 0, ..., d-1 forms a basis for a T-invariant subspace with Jordan block matrix (Proposition 4.7.1).

# Prerequisites

- **Eigenvector** — Generalized eigenvectors extend the concept
- **Eigenvalue** — lambda must be an eigenvalue
- **Linear operator** — Operates on a vector space

# Key Properties

1. An ordinary eigenvector is a generalized eigenvector with exponent 1
2. Every generalized eigenvector's eigenvalue is an actual eigenvalue (Corollary 4.7.4)
3. The chain u_0, u_1, ..., u_{d-1} is a basis for a d-dimensional invariant subspace
4. The matrix of T on this subspace is a d x d Jordan block J_lambda
5. T is diagonalizable iff every generalized eigenvector is an eigenvector (Corollary 4.7.13)

# Construction / Recognition

## To Construct:
1. Choose an eigenvalue lambda
2. Find vectors in ker(T - lambda*I)^k for increasing k
3. Pick x with maximal exponent

## To Recognize:
1. (T - lambda)^k x = 0 for some k, but x != 0

# Context & Application

Generalized eigenvectors are needed when ordinary eigenvectors don't form a basis (non-diagonalizable case). They provide the Jordan basis: a basis in which the matrix has Jordan form.

# Examples

**Example 1** (p. 137): For A = [[0,1,0],[1,0,1],[0,-1,0]] with A^3 = 0 and A^2 != 0: taking v = e_1, the chain v, Av, A^2 v gives a Jordan basis.

# Relationships

## Builds Upon
- **Eigenvector** — Generalized eigenvectors extend eigenvectors

## Enables
- **Jordan form** — The Jordan basis consists of generalized eigenvector chains

## Contrasts With
- **Eigenvector** — An eigenvector has exponent 1; generalized allows higher exponents

# Common Errors

- **Error**: Confusing generalized eigenvectors with ordinary eigenvectors
  **Correction**: A generalized eigenvector satisfies (T-lambda)^k x = 0 for some k >= 1; an ordinary eigenvector satisfies it for k = 1

# Common Confusions

- **Confusion**: Thinking generalized eigenvectors are only needed for defective eigenvalues
  **Clarification**: Non-defective eigenvalues only need ordinary eigenvectors; generalized eigenvectors appear when geometric < algebraic multiplicity

# Source Reference

Chapter 4: Linear Operators, Section 4.7, pages 133-134.

# Verification Notes

- Definition source: Direct from Section 4.7, p. 133
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
