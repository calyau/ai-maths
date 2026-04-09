---
concept: Single Error-Correction Condition
slug: single-error-correction-condition
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
  - single-error-detection-condition
  - canonical-parity-check-matrix
extends:
  - single-error-detection-condition
related:
  - syndrome
  - hamming-code
contrasts_with: []
answers_questions:
  - "When is a linear code single error-correcting?"
  - "What condition on the parity-check matrix ensures error correction?"
---

# Quick Definition

A linear code defined by matrix $H$ is single error-correcting if and only if $H$ has no zero columns and no two columns are identical. This ensures $d_{\min} \geq 3$.

# Core Definition

**Theorem 8.34:** "Let $H$ be a binary matrix. The null space of $H$ is a single error-correcting code if and only if $H$ does not contain any zero columns and no two columns of $H$ are identical" (Judson, p. 118).

# Prerequisites

- **Single Error-Detection Condition** — Error correction strengthens error detection
- **Canonical Parity-Check Matrix** — The condition applies to the matrix columns

# Key Properties

1. No zero columns AND no duplicate columns $\Leftrightarrow$ $d_{\min} \geq 3$
2. Ensures every single error produces a unique syndrome
3. For an $m$-row matrix, at most $2^m - 1$ nonzero distinct columns are possible
4. Subtracting the $m$ columns of $I_m$ leaves $2^m - 1 - m$ possible information columns

# Construction / Recognition

## To Verify:
1. Check that no column of $H$ is all zeros
2. Check that all columns are distinct
3. If both conditions hold, the code corrects single errors

# Context & Application

This theorem provides the key design criterion for constructing single error-correcting codes. It directly motivates Hamming codes, which use all possible nonzero columns.

# Examples

**Example 1** (p. 118): $H = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 1 & 1 & 0 & 0 \end{pmatrix}$ has no zero columns and all columns are distinct, so it defines a single error-correcting code.

# Relationships

## Builds Upon
- **Single Error-Detection Condition** — Adds the no-duplicate-columns requirement

## Enables
- **Hamming Code** — Uses all possible distinct nonzero columns
- **Syndrome** — Unique syndromes for each single-error pattern

# Common Errors

- **Error**: Checking only that columns are nonzero
  **Correction**: Must also check that no two columns are identical

# Common Confusions

- **Confusion**: Thinking this guarantees correction of multiple errors
  **Clarification**: Only single errors are corrected; multiple errors may be misidentified

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.3, Theorem 8.34, page 118.

# Verification Notes

- Definition source: Direct from Theorem 8.34
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
