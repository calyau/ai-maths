---
concept: Hamming Code
slug: hamming-code
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 125
section: "8.6 Exercises"
extraction_confidence: medium
aliases: []
prerequisites:
  - canonical-parity-check-matrix
  - single-error-correction-condition
extends:
  - linear-code
related:
  - syndrome
contrasts_with: []
answers_questions:
  - "What is a Hamming code?"
---

# Quick Definition

A Hamming code is a linear code whose parity-check matrix $H$ has columns that are the binary representations of the integers $1, 2, \ldots, 2^m - 1$. It is a single error-correcting code where the syndrome directly indicates the error position.

# Core Definition

"Let $H$ be an $m \times n$ matrix over $\mathbb{Z}_2$, where the $i$th column is the number $i$ written in binary with $m$ bits. The null space of such a matrix is called a *Hamming code*" (Judson, Exercise 26, p. 125). The syndrome of a received word with a single error in position $i$ equals the $i$th column -- that is, the binary representation of $i$ -- directly identifying the error position.

# Prerequisites

- **Canonical Parity-Check Matrix** — Hamming codes are defined by specific parity-check matrices
- **Single Error-Correction Condition** — All columns are distinct and nonzero

# Key Properties

1. All $2^m - 1$ possible nonzero $m$-bit columns are used
2. Parameters: $(2^m - 1, 2^m - 1 - m)$-block code with $m$ check bits
3. The syndrome directly gives the position of a single error in binary
4. Single error-correcting
5. Hamming codes with maximum information bits are called *perfect*

# Construction / Recognition

## To Construct:
1. Choose $m$ (number of check bits)
2. Form an $m \times (2^m - 1)$ matrix whose columns are $1, 2, \ldots, 2^m - 1$ in binary
3. The null space is the Hamming code

## To Decode:
1. Compute syndrome $H\mathbf{r}$
2. The syndrome, read as a binary number, gives the position of the error
3. Flip that bit to correct

# Context & Application

Hamming codes are among the most fundamental error-correcting codes. They were invented by Richard Hamming at Bell Labs in the late 1940s, motivated by frustration with programs failing due to single-bit errors.

# Examples

**Example 1** (p. 125): The matrix $H = \begin{pmatrix} 0 & 0 & 0 & 1 & 1 & 1 \\ 0 & 1 & 1 & 0 & 0 & 1 \\ 1 & 0 & 1 & 0 & 1 & 0 \end{pmatrix}$ defines a $(6, 3)$ Hamming code (columns are 1-6 in binary, omitting column for 7 which would be all 1s for a $(7,4)$ code).

# Relationships

## Builds Upon
- **Canonical Parity-Check Matrix** — Hamming codes use a specific $H$
- **Single Error-Correction Condition** — All columns distinct and nonzero

## Related
- **Syndrome** — Binary interpretation of syndrome gives error position

# Common Errors

- **Error**: Numbering columns starting from 0 instead of 1
  **Correction**: Columns represent $1, 2, \ldots, 2^m - 1$ (no zero column)

# Common Confusions

- **Confusion**: Thinking Hamming codes correct multiple errors
  **Clarification**: Hamming codes correct only single errors (they have $d_{\min} = 3$)

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.6, Exercise 26, pages 125-126.

# Verification Notes

- Definition source: From Exercise 26, p. 125
- Confidence rationale: Medium - defined in exercises but clearly described
- Uncertainties: None
- Cross-reference status: Verified
