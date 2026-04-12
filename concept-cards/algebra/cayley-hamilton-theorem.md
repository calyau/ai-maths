---
# === CORE IDENTIFICATION ===
concept: Cayley-Hamilton Theorem
slug: cayley-hamilton-theorem

# === CLASSIFICATION ===
category: applications-of-linear-algebra
subcategory: matrix-theory
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Applications of Linear Operators"
chapter_number: 5
pdf_page: 143
section: "5.2 Using Continuity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - system-of-differential-equations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the Cayley-Hamilton Theorem state?"
  - "How is continuity used to prove the Cayley-Hamilton Theorem?"
---

# Quick Definition

The Cayley-Hamilton Theorem states that every square matrix satisfies its own characteristic polynomial: if p(t) is the characteristic polynomial of A, then p(A) = 0.

# Core Definition

Let p(t) = t^n + c_{n-1}t^{n-1} + ... + c_1 t + c_0 be the characteristic polynomial of an n x n complex matrix A. Then p(A) = A^n + c_{n-1}A^{n-1} + ... + c_1 A + c_0 I is the zero matrix (Artin, Theorem 5.2.3, p. 150).

# Prerequisites

- **Characteristic polynomial** — The theorem is about the characteristic polynomial of a matrix
- **Diagonalization** — The proof strategy uses diagonalization and continuity

# Key Properties

1. Every matrix satisfies its own characteristic polynomial
2. The proof uses continuity of eigenvalues (Proposition 5.2.1)
3. For diagonal matrices, verification is immediate
4. General case follows by approximating any matrix by diagonalizable ones

# Construction / Recognition

## To Verify (2x2 case):
1. Compute the characteristic polynomial p(t) = t^2 - (a+d)t + (ad-bc)
2. Substitute the matrix A for t: A^2 - (a+d)A + (ad-bc)I = 0

# Context & Application

The Cayley-Hamilton Theorem has important theoretical consequences: it shows that A^{-1} can be expressed as a polynomial in A, and it bounds the minimal polynomial. Artin's proof via continuity is a beautiful application of the technique of approximating matrices by diagonalizable ones.

# Examples

**Example 1** (p. 150): For a 2x2 matrix A with entries a, b, c, d, the theorem asserts A^2 - (a+d)A + (ad-bc)I = 0, which can be verified directly.

# Relationships

## Builds Upon
- **Characteristic polynomial** — The matrix satisfies this polynomial
- **Diagonalization** — Used in the proof

## Enables
- **Matrix polynomial identities** — Allows expressing high powers of A in terms of lower powers

# Common Errors

- **Error**: Substituting the matrix into det(A - tI) by replacing t with A incorrectly
  **Correction**: Replace t with A and the constant 1 with I throughout

# Common Confusions

- **Confusion**: Thinking the theorem is trivially true because det(A - AI) = 0
  **Clarification**: The eigenvalue equation det(A - lambda I) = 0 holds for scalar lambda; the theorem states p(A) = 0 where A is substituted as a matrix, which is nontrivial

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.2, Theorem 5.2.3, pages 150-151.

# Verification Notes

- Definition source: Direct from Theorem 5.2.3
- Confidence rationale: Named theorem, explicitly stated and proved
- Uncertainties: None
- Cross-reference status: Verified
