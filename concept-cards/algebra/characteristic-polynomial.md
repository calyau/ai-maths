---
concept: Characteristic Polynomial
slug: characteristic-polynomial
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
aliases: []
prerequisites:
  - linear-operator
  - determinant
extends: []
related:
  - eigenvalue
  - eigenvector
  - diagonalization
  - cayley-hamilton-theorem
contrasts_with: []
answers_questions:
  - "How do eigenvalues relate to the characteristic polynomial?"
  - "How do I compute eigenvalues and eigenvectors?"
---

# Quick Definition

The characteristic polynomial of a linear operator T (or matrix A) is p(t) = det(tI - A), a polynomial of degree n whose roots are the eigenvalues of T.

# Core Definition

The characteristic polynomial of a linear operator T is p(t) = det(tI - A), where A is the matrix of T with respect to some basis (Definition 4.5.8, Artin, p. 127). It is independent of the choice of basis (Proposition 4.5.11). It has degree n with leading coefficient 1, constant term (-1)^n det(A), and second coefficient -trace(A) (Proposition 4.5.13).

# Prerequisites

- **Linear operator** — The operator whose polynomial is computed
- **Determinant** — The polynomial is a determinant

# Key Properties

1. p(t) = t^n - (trace A)t^(n-1) + ... + (-1)^n det(A)
2. Eigenvalues are the roots of p(t) (Corollary 4.5.9)
3. Independent of the choice of basis (Proposition 4.5.11)
4. Over C, p(t) has exactly n roots (counted with multiplicity)
5. det(A) = product of eigenvalues; trace(A) = sum of eigenvalues

# Construction / Recognition

## To Construct:
1. Form the matrix tI - A
2. Compute det(tI - A)

## To Recognize:
1. A degree n polynomial whose roots are the eigenvalues

# Context & Application

The characteristic polynomial is the primary tool for finding eigenvalues. Over C, it always factors completely, ensuring every complex matrix has eigenvalues. The Cayley-Hamilton theorem states that A satisfies its own characteristic polynomial: p(A) = 0.

# Examples

**Example 1** (p. 126): For A = [[3,2],[1,4]], p(t) = t^2 - 7t + 10 = (t-5)(t-2).

**Example 2** (p. 127): For [[a,b],[c,d]], p(t) = t^2 - (a+d)t + (ad-bc) = t^2 - (trace)t + det.

**Example 3** (p. 128): The rotation matrix R_theta has p(t) = t^2 - 2cos(theta)t + 1 with complex eigenvalues e^(+-i*theta).

# Relationships

## Builds Upon
- **Determinant** — p(t) = det(tI - A)

## Enables
- **Eigenvalue** — Roots of p(t)
- **Diagonalization** — Possible if p(t) has n distinct roots
- **Jordan form** — Structure determined by the characteristic polynomial

## Related
- **Cayley-Hamilton theorem** — p(A) = 0

# Common Errors

- **Error**: Computing det(A - tI) instead of det(tI - A)
  **Correction**: The conventional form is det(tI - A) to get leading coefficient +1

# Common Confusions

- **Confusion**: Thinking algebraic multiplicity equals geometric multiplicity
  **Clarification**: Algebraic multiplicity (as root of p(t)) can exceed geometric multiplicity (dim of eigenspace)

# Source Reference

Chapter 4: Linear Operators, Section 4.5, pages 126-128.

# Verification Notes

- Definition source: Direct from Definition 4.5.8, p. 127
- Confidence rationale: Central concept, explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
