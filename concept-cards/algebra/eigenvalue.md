---
concept: Eigenvalue
slug: eigenvalue
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
  - "characteristic value"
  - "lambda"
prerequisites:
  - linear-operator
  - characteristic-polynomial
extends: []
related:
  - eigenvector
  - eigenspace
  - diagonalization
contrasts_with: []
answers_questions:
  - "What is an eigenvalue/eigenvector?"
  - "How do eigenvalues relate to the characteristic polynomial?"
  - "How do I compute eigenvalues and eigenvectors?"
  - "What must I know before learning about eigenvalues?"
---

# Quick Definition

An eigenvalue of a linear operator T (or matrix A) is a scalar lambda such that T(v) = lambda*v for some nonzero vector v. Eigenvalues are the roots of the characteristic polynomial det(tI - A).

# Core Definition

The scalar lambda in (4.4.5) T(v) = lambda*v is the eigenvalue associated to the eigenvector v. An eigenvalue of a linear operator T or matrix A is a scalar lambda that is the eigenvalue for some eigenvector. Eigenvalues may be any element of F, including zero (Artin, pp. 121-122). The eigenvalues are precisely the roots of the characteristic polynomial det(tI - A) (Corollary 4.5.9).

# Prerequisites

- **Linear operator** — Eigenvalues are defined for operators on a space
- **Characteristic polynomial** — Eigenvalues are its roots

# Key Properties

1. lambda is an eigenvalue iff det(lambda*I - A) = 0
2. An n x n matrix has at most n eigenvalues
3. Over C, every operator on a nonzero space has at least one eigenvalue (Proposition 4.5.14)
4. Similar matrices have the same eigenvalues
5. det(A) = product of eigenvalues; trace(A) = sum of eigenvalues (Corollary 4.5.15)

# Construction / Recognition

## To Construct:
1. Compute the characteristic polynomial p(t) = det(tI - A)
2. Find its roots — those are the eigenvalues

## To Recognize:
1. A scalar lambda such that (lambda*I - A)X = 0 has a nonzero solution

# Context & Application

Eigenvalues are the key to understanding the behavior of a linear operator. They determine diagonalizability, stability of dynamical systems, and the structure of the Jordan form. Computing eigenvalues first, then eigenvectors, is the standard approach.

# Examples

**Example 1** (p. 126): For A = [[3,2],[1,4]], p(t) = t^2 - 7t + 10 = (t-5)(t-2), so eigenvalues are 5 and 2.

**Example 2** (p. 127): The rotation matrix R_theta has characteristic polynomial t^2 - 2cos(theta)t + 1, with no real roots when theta != 0, pi.

# Relationships

## Builds Upon
- **Characteristic polynomial** — Eigenvalues are its roots

## Enables
- **Eigenvector** — Found by solving (lambda*I - A)X = 0
- **Diagonalization** — Possible when there are enough eigenvectors

## Related
- **Eigenspace** — The set of eigenvectors for a given eigenvalue, plus 0

# Common Errors

- **Error**: Forgetting that 0 can be an eigenvalue
  **Correction**: lambda = 0 means T(v) = 0, i.e., v is in the null space

# Common Confusions

- **Confusion**: Confusing eigenvalue multiplicity with the number of eigenvectors
  **Clarification**: Algebraic multiplicity (root multiplicity) may exceed geometric multiplicity (dimension of eigenspace)

# Source Reference

Chapter 4: Linear Operators, Sections 4.4-4.5, pages 121-128.

# Verification Notes

- Definition source: Direct from (4.4.5), p. 122, and Corollary 4.5.9
- Confidence rationale: Central concept with extensive treatment
- Uncertainties: None
- Cross-reference status: Verified
