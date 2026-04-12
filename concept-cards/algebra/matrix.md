---
# === CORE IDENTIFICATION ===
concept: Matrix
slug: matrix

# === CLASSIFICATION ===
category: matrices
subcategory: null
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
aliases:
  - "rectangular array"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - matrix-entry
  - row-vector
  - column-vector
  - square-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a matrix?"
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A matrix is a rectangular array of numbers (or elements of a field) arranged in rows and columns. An m x n matrix has m rows and n columns.

# Core Definition

An m x n matrix is a collection of mn numbers arranged in a rectangular array with m rows and n columns. The entry in the ith row and jth column is denoted a_ij, where i is the row index and j is the column index. The matrix may be denoted by A or (a_ij) (Artin, p. 12).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An m x n matrix has m rows and n columns
2. Entries are indexed by pairs (i, j) with 1 <= i <= m and 1 <= j <= n
3. An n x n matrix is called a square matrix
4. A 1 x 1 matrix [a] is identified with its single entry a
5. A 1 x n matrix is a row vector; an m x 1 matrix is a column vector

# Construction / Recognition

## To Construct:
1. Choose dimensions m (rows) and n (columns)
2. Specify the entry a_ij for each position (i, j)

## To Recognize:
1. A rectangular array of numbers
2. The shape m x n is determined by counting rows and columns

# Context & Application

Matrices provide a compact notation for systems of linear equations, linear transformations, and many algebraic structures. Artin opens the book with matrices as a concrete gateway to abstract algebra, emphasizing their computational utility before introducing groups and vector spaces.

# Examples

**Example 1** (p. 12): A 2 x 3 matrix with entries a_11 = 2, a_13 = 0, a_23 = 5.

**Example 2** (p. 12): The system of equations 2x_1 + x_2 = 1, x_1 + 3x_2 + 5x_3 = 18 can be written in matrix notation as AX = B.

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Matrix addition** — Defined for matrices of the same shape
- **Matrix multiplication** — The central operation on matrices
- **Determinant** — A function on square matrices
- **Linear transformation** — Every linear transformation corresponds to a matrix

## Related
- **Row vector** — Special case: 1 x n matrix
- **Column vector** — Special case: m x 1 matrix

# Common Errors

- **Error**: Confusing the order of indices (writing a_ji instead of a_ij)
  **Correction**: The first index is always the row, the second is the column

# Common Confusions

- **Confusion**: Assuming all matrices are square
  **Clarification**: Matrices can be any m x n shape; square matrices are the special case m = n

# Source Reference

Chapter 1: Matrices, Section 1.1, pages 12-13.

# Verification Notes

- Definition source: Direct from opening of Section 1.1, p. 12
- Confidence rationale: Explicitly defined with notation and examples
- Uncertainties: None
- Cross-reference status: All slugs verified
