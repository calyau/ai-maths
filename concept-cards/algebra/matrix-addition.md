---
# === CORE IDENTIFICATION ===
concept: Matrix Addition
slug: matrix-addition

# === CLASSIFICATION ===
category: matrices
subcategory: matrix-operations
tier: foundational

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.1 The Basic Operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - matrix
extends: []
related:
  - scalar-multiplication
  - matrix-multiplication
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

Matrix addition is the entry-wise sum of two matrices of the same shape. If A = (a_ij) and B = (b_ij) are m x n matrices, their sum S = A + B has entries s_ij = a_ij + b_ij.

# Core Definition

Let A = (a_ij) and B = (b_ij) be two m x n matrices. Their sum A + B is the m x n matrix S = (s_ij) defined by s_ij = a_ij + b_ij. Addition is defined only when the matrices have the same shape (Artin, p. 13).

# Prerequisites

- **Matrix** — Must know what a matrix is and its entry notation

# Key Properties

1. Only defined for matrices of the same dimensions
2. Performed entry by entry
3. Commutative: A + B = B + A
4. Associative: (A + B) + C = A + (B + C)
5. The zero matrix O serves as the additive identity

# Construction / Recognition

## To Construct:
1. Verify both matrices have the same dimensions m x n
2. Add corresponding entries: s_ij = a_ij + b_ij

## To Recognize:
1. An operation combining two matrices of the same shape into a third of the same shape
2. Each entry of the result is the sum of the corresponding entries

# Context & Application

Matrix addition, together with scalar multiplication, gives the set of m x n matrices the structure of a vector space. It satisfies the distributive laws with matrix multiplication.

# Examples

**Example 1** (p. 13): [[2,1,0],[1,3,5]] + [[1,0,3],[4,-3,1]] = [[3,1,3],[5,0,6]].

# Relationships

## Builds Upon
- **Matrix** — Operates on matrices

## Enables
- **Vector space** — Matrices form a vector space under addition and scalar multiplication
- **Linear combination** — Combines addition with scalar multiplication

## Related
- **Scalar multiplication** — The other vector space operation on matrices

# Common Errors

- **Error**: Attempting to add matrices of different dimensions
  **Correction**: Addition requires both matrices to be m x n with the same m and n

# Common Confusions

- **Confusion**: Thinking matrix addition has the same complexity as matrix multiplication
  **Clarification**: Addition is trivial (entry-wise) while multiplication is more involved

# Source Reference

Chapter 1: Matrices, Section 1.1, page 13.

# Verification Notes

- Definition source: Direct from p. 13
- Confidence rationale: Explicitly defined with formula and example
- Uncertainties: None
- Cross-reference status: Verified
