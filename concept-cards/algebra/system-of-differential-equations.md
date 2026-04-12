---
# === CORE IDENTIFICATION ===
concept: System of Differential Equations
slug: system-of-differential-equations

# === CLASSIFICATION ===
category: applications-of-linear-algebra
subcategory: differential-equations
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Applications of Linear Operators"
chapter_number: 5
pdf_page: 143
section: "5.3 Systems of Differential Equations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "linear ODE system"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - matrix-exponential
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you solve a system of linear differential equations using eigenvalues?"
  - "What role does diagonalization play in solving dX/dt = AX?"
---

# Quick Definition

A system of homogeneous linear, first-order, constant-coefficient differential equations has the form dX/dt = AX, where A is a constant n x n matrix and X(t) is a vector-valued function. It is solved by diagonalization or the matrix exponential.

# Core Definition

A system of homogeneous linear, first-order, constant-coefficient differential equations is a matrix equation dX/dt = AX, where A is a constant n x n matrix and X(t) is an n-dimensional vector-valued function (Artin, (5.3.7), p. 152). If V is an eigenvector for A with eigenvalue lambda, then X = e^{lambda t} V is a particular solution.

# Prerequisites

- **Eigenvalues and eigenvectors** — Solutions built from eigenvectors
- **Diagonalization** — Used to reduce to decoupled equations

# Key Properties

1. If A is diagonalizable, the general solution is X = P * X_tilde, where X_tilde has entries c_i * e^{lambda_i t}
2. Each eigenvector produces an independent solution e^{lambda t} V
3. Complex eigenvalues yield real solutions via real and imaginary parts (Lemma 5.3.23)
4. Initial conditions determine the arbitrary constants

# Construction / Recognition

## To Solve (diagonalizable case):
1. Find eigenvalues lambda_1, ..., lambda_n and diagonalizing matrix P
2. The general solution is X = P * (c_1 e^{lambda_1 t}, ..., c_n e^{lambda_n t})^t
3. Use initial conditions to determine c_i

# Context & Application

Systems of linear ODEs arise throughout science and engineering. The algebraic approach via diagonalization connects linear algebra directly to analysis, showing how the eigenstructure of A determines the qualitative behavior of solutions (exponential growth, oscillation, decay).

# Examples

**Example 1** (p. 152): For A = [[3,2],[1,4]], eigenvectors [[1],[1]] and [[2],[-1]] with eigenvalues 5 and 2 give solutions [[e^{5t}],[e^{5t}]] and [[2e^{2t}],[-e^{2t}]].

**Example 2** (p. 154): For A = [[1,1],[-1,1]] with complex eigenvalues 1+i, 1-i, real solutions involve e^t cos t and e^t sin t.

# Relationships

## Builds Upon
- **Eigenvalues** — Each eigenvalue contributes an exponential solution
- **Diagonalization** — Reduces the system to decoupled equations

## Enables
- **Matrix exponential** — Provides a general solution e^{tA}

# Common Errors

- **Error**: Forgetting to take real parts when A is real but has complex eigenvalues
  **Correction**: Use Lemma 5.3.23: real and imaginary parts of complex solutions are also solutions

# Common Confusions

- **Confusion**: Thinking diagonalizable matrices are required
  **Clarification**: Non-diagonalizable matrices can be handled via Jordan form or the matrix exponential

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.3, pages 151-155.

# Verification Notes

- Definition source: Direct from (5.3.7)
- Confidence rationale: Extensively developed with examples
- Uncertainties: None
- Cross-reference status: Verified
