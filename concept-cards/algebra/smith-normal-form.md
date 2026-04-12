---
concept: Smith Normal Form
slug: smith-normal-form
category: module-theory
subcategory: computational-methods
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.4 Diagonalizing Integer Matrices"
extraction_confidence: high
aliases:
  - "diagonal form"
  - "diagonalization of integer matrices"
prerequisites:
  - free-module
  - integer-matrix
extends: []
related:
  - structure-theorem-finitely-generated-modules-pid
  - elementary-divisors
  - invariant-factors
contrasts_with: []
answers_questions:
  - "How do I compute the Smith normal form?"
  - "What is the Smith normal form?"
---

# Quick Definition

The Smith normal form is a diagonal matrix obtained from an integer (or polynomial) matrix by invertible row and column operations, where each diagonal entry divides the next. It is the key computational tool for classifying finitely generated modules over PIDs.

# Core Definition

Let A be an integer matrix. There exist products Q and P of elementary integer matrices of appropriate sizes so that A' = Q^{-1}AP is diagonal, with positive diagonal entries d_1, ..., d_k where d_1 | d_2 | ... | d_k (Artin, Theorem 14.4.6). The allowed operations are: adding an integer multiple of one row/column to another, interchanging two rows/columns, and multiplying a row/column by -1.

# Prerequisites

- **Free module** -- Smith normal form applies to maps between free modules
- **Integer matrix** -- The matrix entries must be in a PID (like Z or F[x])

# Key Properties

1. The diagonal entries d_i are positive and each divides the next: d_1 | d_2 | ... | d_k
2. d_1 is the greatest common divisor of all entries of A
3. The form is achieved by elementary row and column operations (14.4.2)
4. The procedure works over any PID, not just Z (Theorem 14.8.1 for F[t])
5. The diagonal entries (invariant factors) are uniquely determined by the matrix

# Construction / Recognition

## To Construct:
1. Move a nonzero entry with smallest absolute value to the upper left corner (make it positive)
2. Use division with remainder to clear the first column via row operations
3. Similarly clear the first row via column operations
4. Ensure the upper left entry divides all entries of the remaining submatrix
5. Repeat on the remaining submatrix

## To Recognize:
1. The matrix is diagonal
2. All diagonal entries are positive
3. Each entry divides the next

# Context & Application

Smith normal form is the computational engine behind the structure theorem for finitely generated abelian groups and modules over PIDs. It solves integer linear systems AX = B, determines the kernel and image of integer matrix multiplication, and classifies finitely generated modules.

# Examples

**Example 1** (p. 437): The matrix A = [[1,2,3],[4,6,6]] reduces to A' = [[1,0,0],[0,2,0]] via row and column operations. The invertible integer matrices Q^{-1} and P are computed by tracking the operations.

**Example 2** (p. 439): The 3x4 matrix (14.5.4) reduces through operations to show it presents the abelian group Z/4Z.

# Relationships

## Builds Upon
- **Free module** -- Diagonalizes maps between free modules

## Enables
- **Structure theorem for finitely generated modules over a PID** -- The normal form proves the decomposition
- **Structure theorem for abelian groups** -- The integer case
- **Rational canonical form** -- The polynomial case

## Related
- **Invariant factors** -- The diagonal entries d_i
- **Elementary divisors** -- Prime power factors of the invariant factors

# Common Errors

- **Error**: Forgetting to ensure each diagonal entry divides the next (Step 3 of the algorithm)
  **Correction**: After clearing the first row and column, check divisibility; if some entry of M is not divisible by a_{11}, add its column to column 1 and repeat.

- **Error**: Confusing row operations (which change Q) with column operations (which change P)
  **Correction**: Row operations multiply on the left (in reverse order for Q^{-1}); column operations multiply on the right (in forward order for P).

# Common Confusions

- **Confusion**: Thinking Smith normal form is the same as row echelon form
  **Clarification**: Smith normal form uses both row AND column operations to achieve a diagonal matrix; row echelon form uses only row operations.

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.4, pages 436-440. Theorem 14.4.6, Proposition 14.4.9.

# Verification Notes

- Definition source: Direct from Artin, Theorem 14.4.6
- Confidence rationale: Complete algorithm and theorem statement given
- Uncertainties: None
- Cross-reference status: Verified
