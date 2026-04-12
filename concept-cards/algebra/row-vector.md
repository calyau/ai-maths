---
concept: Row Vector
slug: row-vector
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
  - "n-dimensional row vector"
prerequisites:
  - matrix
extends: []
related:
  - column-vector
contrasts_with:
  - column-vector
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A row vector is a 1 x n matrix, written as [a_1, ..., a_n] or (a_1, ..., a_n). It is an n-dimensional row vector.

# Core Definition

A 1 x n matrix is an n-dimensional row vector. When m = 1, the row index is dropped and the vector is written as [a_1 ... a_n] or (a_1, ..., a_n), with commas optional (Artin, p. 12).

# Prerequisites

- **Matrix** — A row vector is a special case of a matrix

# Key Properties

1. Has exactly one row and n columns
2. Can be multiplied on the right by a column vector to produce a scalar
3. The transpose of a row vector is a column vector

# Construction / Recognition

## To Construct:
1. Write n numbers in a single row

## To Recognize:
1. A matrix with exactly one row

# Context & Application

Row vectors appear in the row-space analysis and in the transpose operation. In Artin's treatment, column vectors are preferred for most purposes.

# Examples

**Example 1** (p. 12): [a_1 ... a_n] is a 1 x n row vector; commas are optional.

# Relationships

## Builds Upon
- **Matrix** — Special case of a matrix

## Enables
- **Matrix multiplication** — Row-by-column product rule

## Contrasts With
- **Column vector** — An m x 1 matrix; the transpose of a row vector

# Common Errors

- **Error**: Confusing row and column vectors in multiplication
  **Correction**: In AB, rows come from A, columns from B

# Common Confusions

- **Confusion**: Assuming row and column vectors are interchangeable
  **Clarification**: They have different shapes and behave differently under multiplication

# Source Reference

Chapter 1: Matrices, Section 1.1, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
