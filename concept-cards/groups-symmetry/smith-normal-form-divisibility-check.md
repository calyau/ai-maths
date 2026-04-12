---
# === CORE IDENTIFICATION ===
concept: Smith Normal Form Divisibility Check
slug: smith-normal-form-divisibility-check

# === CLASSIFICATION ===
category: structure-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Row and Column Operations"
chapter_number: 22
pdf_page: 132
section: "Outline Proof for (22.1)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "divisibility check in Smith normal form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - smith-normal-form
  - row-column-operations
extends: []
related:
  - divisibility-chain
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why can't you just diagonalise the matrix without checking divisibility?"
  - "What happens if the diagonal entries don't divide subsequent submatrix entries?"
---

# Quick Definition

In the Smith normal form algorithm, after achieving a matrix with $c_{11}$ in the corner and zeros in the rest of row 1 and column 1, one must check that $c_{11}$ divides every entry of the remaining submatrix $C_1$. If not, adding an offending row to row 1 and restarting reduces $c_{11}$, eventually forcing divisibility.

# Core Definition

Armstrong warns (p. 134): "At this point we may be tempted to work with the smaller matrix $C_1$... This does give a diagonal matrix, but unfortunately its diagonal elements may not successively divide one another." Instead, one must check whether every entry of $C_1$ is a multiple of $c_{11}$. If $c_{11}$ does not divide some entry $c_{ij}$, one adds row $i$ to row 1 and restarts from the beginning. This produces a new leading entry smaller than $c_{11}$, and the process terminates.

# Prerequisites

- **Smith normal form** -- this is a critical step in the algorithm
- **Row and column operations** -- the tools used

# Key Properties

1. A diagonal matrix is NOT necessarily in Smith normal form
2. The divisibility check ensures $d_1 \mid d_2 \mid \cdots \mid d_k$
3. Each restart strictly reduces the leading entry, guaranteeing termination
4. Only after the divisibility check passes does the leading entry become a genuine diagonal entry $d_{ii}$

# Context & Application

This subtlety is the most commonly overlooked step in the Smith normal form algorithm. Armstrong explicitly addresses it to prevent students from producing diagonal but non-canonical results.

# Examples

**Example (ii)** (p. 135): The matrix $\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$ is diagonal but NOT in Smith normal form since $2 \nmid 3$. After operations: $\begin{bmatrix} 1 & 0 \\ 0 & 6 \end{bmatrix}$, which is in Smith normal form with $1 \mid 6$.

# Relationships

## Builds Upon
- **Smith normal form** -- this is part of the algorithm
- **Row and column operations** -- the restart procedure uses these

## Related
- **Divisibility chain** -- what the check enforces

# Common Errors

- **Error**: Stopping at a diagonal matrix and reading off the group.
  **Correction**: Always verify the divisibility chain. A diagonal entry that does not divide the next one means more work is needed.

# Source Reference

Chapter 22: Row and Column Operations, Outline Proof for (22.1), pages 134--135.

# Verification Notes

- Warning and procedure: Direct from pp. 134--135
- Example: Verified from p. 135
- Confidence: HIGH -- Armstrong explicitly addresses this pitfall
