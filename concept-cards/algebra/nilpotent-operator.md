---
concept: Nilpotent Operator
slug: nilpotent-operator
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
aliases:
  - "nilpotent matrix"
prerequisites:
  - linear-operator
extends: []
related:
  - jordan-form
  - jordan-block
  - generalized-eigenvector
contrasts_with: []
answers_questions:
  - "What is the Jordan normal form?"
---

# Quick Definition

A linear operator T is nilpotent if T^r = 0 for some positive integer r. Equivalently, every eigenvalue is 0. The Jordan form of a nilpotent operator consists entirely of Jordan blocks J_0 with eigenvalue 0.

# Core Definition

A linear operator T on a vector space V is nilpotent if for some positive integer r, the operator T^r is zero (Artin, p. 136). Every nonzero vector is a generalized eigenvector with eigenvalue 0. The Jordan form consists of blocks J_0 of various sizes. Exercise 1.13 of Ch. 1 shows that if a matrix A is nilpotent, then I + A is invertible (its inverse is I - A + A^2 - ... + (-1)^(k-1) A^(k-1)).

# Prerequisites

- **Linear operator** — Must be a linear operator on a vector space

# Key Properties

1. T^r = 0 for some r > 0
2. All eigenvalues are 0
3. det(T) = 0; T is not invertible
4. The Jordan form has only blocks J_0
5. I + T is invertible with inverse sum_{i=0}^{r-1} (-T)^i

# Construction / Recognition

## To Construct:
1. Any strictly upper or lower triangular matrix is nilpotent

## To Recognize:
1. T^r = 0 for some r
2. Or: all eigenvalues are 0 AND T is not diagonalizable (unless T = 0)

# Context & Application

Nilpotent operators are the building blocks of Jordan form. Every operator on a complex space decomposes as T = D + N where D is diagonalizable and N is nilpotent (the Jordan decomposition can be viewed this way). The proof of the Jordan form theorem reduces to the nilpotent case.

# Examples

**Example 1** (p. 137): A = [[0,1,0],[1,0,1],[0,-1,0]] with A^3 = 0, A^2 != 0 is nilpotent.

**Example 2** (p. 137): B = [[1,-1,1],[2,-2,2],[-1,1,-1]] with B^2 = 0 is nilpotent.

# Relationships

## Builds Upon
- **Linear operator** — Nilpotent is a property of operators

## Enables
- **Jordan form** — Proof reduces to nilpotent case

## Related
- **Jordan block** — J_0 is the basic nilpotent block

# Common Errors

- **Error**: Thinking nilpotent means zero
  **Correction**: T may be nonzero; only some power T^r is zero

# Common Confusions

- **Confusion**: Confusing nilpotent operator with zero operator
  **Clarification**: The zero operator is nilpotent, but most nilpotent operators are nonzero

# Source Reference

Chapter 4: Linear Operators, Section 4.7, page 136.

# Verification Notes

- Definition source: Direct from Section 4.7, p. 136
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
