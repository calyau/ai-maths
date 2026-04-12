---
concept: Sign of a Permutation
slug: sign-of-a-permutation
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.5 Permutations"
extraction_confidence: high
aliases:
  - "parity of a permutation"
  - "even permutation"
  - "odd permutation"
prerequisites:
  - permutation
  - permutation-matrix
  - determinant
extends: []
related:
  - transposition
  - alternating-group
contrasts_with: []
answers_questions:
  - "What is a permutation?"
---

# Quick Definition

The sign of a permutation p is the determinant of its associated permutation matrix: sign(p) = det(P) = +1 or -1. A permutation is even (sign +1) or odd (sign -1). If p is a product of k transpositions, sign(p) = (-1)^k.

# Core Definition

The sign of a permutation p is defined as sign(p) = det(P) = +/-1, where P is the associated permutation matrix (Artin, p. 33, formula 1.5.11). A permutation is even if its sign is +1 and odd if its sign is -1. Every permutation can be written as a product of transpositions; the number of transpositions is always even for even permutations and always odd for odd permutations.

# Prerequisites

- **Permutation** — The object whose sign is being computed
- **Permutation matrix** — The sign is the determinant of this matrix
- **Determinant** — Used to define the sign

# Key Properties

1. sign(p) = +1 or -1
2. sign(qp) = sign(q) * sign(p)
3. Any transposition has sign -1
4. A k-cycle has sign (-1)^(k-1)
5. The sign is well-defined regardless of how p is written as a product of transpositions

# Construction / Recognition

## To Construct:
1. Write p as a product of transpositions
2. Count the number k of transpositions
3. sign(p) = (-1)^k

## To Recognize:
1. Even: an even number of transpositions; sign = +1
2. Odd: an odd number of transpositions; sign = -1

# Context & Application

The sign appears in the complete expansion of the determinant: det(A) = sum over permutations p of (sign p) * a_1,p(1) * ... * a_n,p(n). It also defines the alternating group A_n (even permutations).

# Examples

**Example 1** (p. 33): The permutation (123) has sign +1 (even). Any transposition (12) has sign -1 (odd).

# Relationships

## Builds Upon
- **Permutation** — The object classified
- **Determinant** — Sign = det of permutation matrix

## Enables
- **Alternating group** — The group of even permutations
- **Determinant** — Complete expansion formula uses sign

## Related
- **Transposition** — Always has sign -1

# Common Errors

- **Error**: Thinking a 3-cycle is odd
  **Correction**: A 3-cycle is even (sign +1); it is a product of 2 transpositions

# Common Confusions

- **Confusion**: Confusing the sign of a permutation with the sign of a number
  **Clarification**: The sign is a group homomorphism S_n -> {+1, -1}

# Source Reference

Chapter 1: Matrices, Section 1.5, page 33.

# Verification Notes

- Definition source: Direct from (1.5.11), p. 33
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
