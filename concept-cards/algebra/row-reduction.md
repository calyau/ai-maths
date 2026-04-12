---
concept: Row Reduction
slug: row-reduction
category: matrices
subcategory: matrix-operations
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
  - "Gaussian elimination"
  - "row echelon reduction"
prerequisites:
  - matrix
  - elementary-row-operations
  - elementary-matrix
extends: []
related:
  - row-echelon-form
  - system-of-linear-equations
  - invertible-matrix
contrasts_with: []
answers_questions:
  - "How do I row-reduce a matrix?"
  - "How do row operations relate to matrix invertibility?"
---

# Quick Definition

Row reduction is the process of simplifying a matrix by a sequence of elementary row operations to obtain a row echelon matrix. It is the fundamental computational tool for solving systems of linear equations.

# Core Definition

Row reduction is the procedure of performing a sequence of elementary row operations on a matrix M to produce a simpler matrix M'. Since each operation is multiplication by an elementary matrix, the result is M' = E_k ... E_2 E_1 M (Artin, p. 19, formula 1.2.7). The goal is to reach row echelon form.

# Prerequisites

- **Matrix** — The object being reduced
- **Elementary row operations** — The three types of operations used
- **Elementary matrix** — Each operation corresponds to multiplication by an elementary matrix

# Key Properties

1. Row reduction preserves the solution set of AX = B (Proposition 1.2.10)
2. Every matrix can be reduced to row echelon form
3. The row echelon form is unique (though the sequence of operations is not)
4. A square matrix is invertible iff it reduces to I (Theorem 1.2.16)

# Construction / Recognition

## To Construct:
1. Find the leftmost nonzero column
2. Interchange rows to put a nonzero entry at the top
3. Normalize the pivot to 1
4. Clear entries below the pivot using Type (i) operations
5. Repeat for the submatrix below and to the right
6. Clear entries above pivots (for reduced row echelon form)

## To Recognize:
1. A systematic process of applying elementary row operations to simplify a matrix

# Context & Application

Row reduction is the primary algorithm for solving systems of linear equations, computing inverses, determining rank, and testing invertibility. Artin presents it early as the workhorse computational method.

# Examples

**Example 1** (p. 19, formula 1.2.8): The matrix [[1,1,2,1,5],[1,1,2,6,10],[1,2,5,2,7]] is reduced step by step to [[1,0,-1,0,3],[0,1,3,0,1],[0,0,0,1,1]].

**Example 2** (pp. 20-21): Inverting [[1,5],[2,6]] by row-reducing [A|I] to [I|A^(-1)].

# Relationships

## Builds Upon
- **Elementary row operations** — The individual steps
- **Elementary matrix** — Each step is multiplication by an elementary matrix

## Enables
- **Row echelon form** — The end result of reduction
- **Matrix inverse** — Computed by row-reducing [A|I]
- **Rank** — Determined by the number of pivots

## Related
- **System of linear equations** — Solved by row-reducing [A|B]

# Common Errors

- **Error**: Not normalizing pivots to 1
  **Correction**: Divide each pivot row to make the pivot entry 1

- **Error**: Forgetting to clear entries above pivots
  **Correction**: For reduced row echelon form, clear both above and below

# Common Confusions

- **Confusion**: Thinking row reduction changes the solution set
  **Clarification**: Row reduction preserves solutions (Proposition 1.2.10)

# Source Reference

Chapter 1: Matrices, Section 1.2, pages 18-22.

# Verification Notes

- Definition source: Direct from Section 1.2
- Confidence rationale: Extensively described with examples and algorithm
- Uncertainties: None
- Cross-reference status: Verified
