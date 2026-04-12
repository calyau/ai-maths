---
concept: Column Vector
slug: column-vector
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.1 The Basic Operations"
extraction_confidence: high
aliases:
  - "m-dimensional column vector"
prerequisites:
  - matrix
extends: []
related:
  - row-vector
  - standard-basis
contrasts_with:
  - row-vector
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A column vector is an m x 1 matrix, written as a vertical array of m numbers. In Artin's book, column vectors are identified with points in m-dimensional space.

# Core Definition

An m x 1 matrix is an m-dimensional column vector, written as [b_1, ..., b_m]^t. In most of the book, no distinction is made between an n-dimensional column vector and the point of R^n with the same coordinates (Artin, p. 12).

# Prerequisites

- **Matrix** — A column vector is a special case of a matrix

# Key Properties

1. Has exactly one column and m rows
2. The transpose of a column vector is a row vector
3. Can be expressed using the standard basis: X = x_1 e_1 + ... + x_n e_n

# Construction / Recognition

## To Construct:
1. Write m numbers in a single column

## To Recognize:
1. A matrix with exactly one column

# Context & Application

Column vectors are the primary working objects in Artin's linear algebra. They represent solutions of linear equations, elements of vector spaces, and are the natural inputs for left multiplication by a matrix.

# Examples

**Example 1** (p. 14): X = [x_1, x_2, x_3]^t is a column vector of unknowns in AX = B.

# Relationships

## Builds Upon
- **Matrix** — Special case

## Enables
- **System of linear equations** — Unknowns written as column vectors
- **Vector space** — F^n is the space of column vectors

## Contrasts With
- **Row vector** — A 1 x n matrix; the transpose of a column vector

# Common Errors

- **Error**: Writing column vectors as rows without the transpose notation
  **Correction**: Use (a_1, ..., a_n)^t to write a column vector on one line

# Common Confusions

- **Confusion**: Confusing the column vector with its scalar entries
  **Clarification**: The vector is the matrix; the entries are scalars

# Source Reference

Chapter 1: Matrices, Section 1.1, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
