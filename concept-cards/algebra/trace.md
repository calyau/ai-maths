---
concept: Trace
slug: trace
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.5 The Characteristic Polynomial"
extraction_confidence: high
aliases:
  - "trace A"
prerequisites:
  - matrix
  - square-matrix
extends: []
related:
  - characteristic-polynomial
  - eigenvalue
  - determinant
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

The trace of a square matrix A is the sum of its diagonal entries: trace(A) = a_11 + a_22 + ... + a_nn. It equals the sum of eigenvalues and is the coefficient of -t^(n-1) in the characteristic polynomial.

# Core Definition

The trace of an n x n matrix A is trace(A) = a_11 + a_22 + ... + a_nn (Artin, p. 128, Proposition 4.5.13). It is invariant under similarity: trace(P^(-1)AP) = trace(A). It equals the sum of eigenvalues (Corollary 4.5.15). Properties: trace(A+B) = trace(A) + trace(B), trace(AB) = trace(BA) (Exercise M.3, Ch. 1).

# Prerequisites

- **Matrix** — Must be a square matrix
- **Square matrix** — Trace is defined for square matrices

# Key Properties

1. trace(A) = sum of diagonal entries
2. trace(A) = sum of eigenvalues
3. trace(P^(-1)AP) = trace(A) (invariant under similarity)
4. trace(AB) = trace(BA)
5. Appears as coefficient of -t^(n-1) in characteristic polynomial

# Construction / Recognition

## To Construct:
1. Sum the diagonal entries a_11 + ... + a_nn

## To Recognize:
1. A single scalar computed from the diagonal of a square matrix

# Context & Application

The trace, together with the determinant, provides the most important numerical invariants of a matrix. For the characteristic polynomial p(t) = t^n - (trace A)t^(n-1) + ... + (-1)^n det A, the trace and determinant are the extreme coefficients.

# Examples

**Example 1** (p. 128): For a 2x2 matrix [[a,b],[c,d]], trace = a + d, and p(t) = t^2 - (a+d)t + (ad-bc).

# Relationships

## Builds Upon
- **Square matrix** — Trace is a property of square matrices

## Related
- **Characteristic polynomial** — trace appears as a coefficient
- **Eigenvalue** — trace = sum of eigenvalues
- **Determinant** — determinant = product of eigenvalues

# Common Errors

- **Error**: Thinking trace(AB) = trace(A) * trace(B)
  **Correction**: trace(AB) = trace(BA), but trace is NOT multiplicative

# Common Confusions

- **Confusion**: Thinking trace depends on the basis
  **Clarification**: trace(P^(-1)AP) = trace(A), so trace is basis-independent

# Source Reference

Chapter 4: Linear Operators, Section 4.5, page 128.

# Verification Notes

- Definition source: Direct from Proposition 4.5.13
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
