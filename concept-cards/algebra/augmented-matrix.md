---
concept: Augmented Matrix
slug: augmented-matrix
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.2 Row Reduction"
extraction_confidence: high
aliases:
  - "[A|B]"
prerequisites:
  - matrix
  - system-of-linear-equations
extends:
  - block-matrix
related:
  - row-reduction
contrasts_with: []
answers_questions:
  - "How do I row-reduce a matrix?"
---

# Quick Definition

The augmented matrix [A|B] of a system AX = B is the block matrix formed by appending the column vector B to the right of the coefficient matrix A. Row reduction of [A|B] solves the system.

# Core Definition

Given a system AX = B, the augmented matrix is the m x (n+1) block matrix [A|B] (Artin, p. 19, formula 1.2.9). Row operations on [A|B] transform both A and B consistently, preserving solutions (Proposition 1.2.10).

# Prerequisites

- **Matrix** — The augmented matrix is a matrix
- **System of linear equations** — It represents AX = B

# Key Properties

1. Row operations on [A|B] preserve the solution set
2. [A|B] row-reduces to [A'|B'] where A'X = B' has the same solutions
3. A system is inconsistent iff a row [0...0|1] appears in echelon form

# Construction / Recognition

## To Construct:
1. Write the coefficient matrix A
2. Append the column B on the right, separated by a vertical line

## To Recognize:
1. A matrix with n+1 columns where the last column represents constants

# Context & Application

The augmented matrix is the standard tool for applying row reduction to solve systems. It keeps the coefficient and constant sides synchronized during elimination.

# Examples

**Example 1** (p. 19): For the system (1.2.11), [A|B] is row-reduced to read off solutions.

**Example 2** (pp. 20-21): To compute A^(-1), row-reduce [A|I] to [I|A^(-1)].

# Relationships

## Builds Upon
- **Block matrix** — [A|B] is a block matrix

## Enables
- **Row reduction** — Applied to augmented matrix to solve systems
- **Matrix inverse** — [A|I] -> [I|A^(-1)]

# Common Errors

- **Error**: Performing operations on A without also applying them to B
  **Correction**: Always work with the full augmented matrix

# Common Confusions

- **Confusion**: Thinking the augmented matrix is just A
  **Clarification**: The augmented matrix includes the right-hand side B

# Source Reference

Chapter 1: Matrices, Section 1.2, page 19.

# Verification Notes

- Definition source: Direct from (1.2.9), p. 19
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
