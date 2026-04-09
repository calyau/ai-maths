---
concept: Single Error-Detection Condition
slug: single-error-detection-condition
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 118
section: "8.3 Parity-Check and Generator Matrices"
extraction_confidence: high
aliases: []
prerequisites:
  - canonical-parity-check-matrix
  - minimum-distance
extends: []
related:
  - single-error-correction-condition
  - linear-code
contrasts_with: []
answers_questions:
  - "When is a linear code single error-detecting?"
  - "What condition on the parity-check matrix ensures error detection?"
---

# Quick Definition

A linear code defined by matrix $H$ is single error-detecting if and only if no column of $H$ consists entirely of zeros. This ensures $d_{\min} \geq 2$.

# Core Definition

**Theorem 8.31:** "Let $H$ be an $m \times n$ binary matrix. Then the null space of $H$ is a single error-detecting code if and only if no column of $H$ consists entirely of zeros" (Judson, p. 118).

# Prerequisites

- **Canonical Parity-Check Matrix** — The matrix being analyzed
- **Minimum Distance** — Single error detection requires $d_{\min} \geq 2$

# Key Properties

1. No zero columns $\Leftrightarrow$ no weight-1 codewords $\Leftrightarrow$ $d_{\min} \geq 2$
2. $H\mathbf{e}_i$ is the $i$th column of $H$ (Proposition 8.30)
3. If the $i$th column is zero, then $\mathbf{e}_i$ (single error) is a codeword
4. Easy to verify: just check each column

# Construction / Recognition

## To Verify:
1. Examine each column of $H$
2. If all columns are nonzero, the code detects single errors
3. If any column is all zeros, the code fails to detect errors in that position

# Context & Application

This theorem connects the column structure of $H$ to the code's error-detection capability, providing a simple visual test.

# Examples

**Example 1** (p. 118): $H_1 = \begin{pmatrix} 1 & 1 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 1 \end{pmatrix}$ has no zero columns, so it defines a single error-detecting code. $H_2$ with a zero column in position 4 does not.

# Relationships

## Builds Upon
- **Canonical Parity-Check Matrix** — The condition is on the matrix columns
- **Minimum Distance** — Ensures $d_{\min} \geq 2$

## Related
- **Single Error-Correction Condition** — The stronger condition for correction

# Common Errors

- **Error**: Checking only the identity portion of the matrix
  **Correction**: All columns must be checked, including those in the $A$ portion

# Common Confusions

- **Confusion**: Thinking no zero columns implies error correction
  **Clarification**: No zero columns gives detection only; correction also requires no duplicate columns

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.3, Theorem 8.31, page 118.

# Verification Notes

- Definition source: Direct from Theorem 8.31
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
