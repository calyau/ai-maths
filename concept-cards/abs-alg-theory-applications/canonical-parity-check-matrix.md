---
concept: Canonical Parity-Check Matrix
slug: canonical-parity-check-matrix
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 114
section: "8.3 Parity-Check and Generator Matrices"
extraction_confidence: high
aliases:
  - parity-check matrix
prerequisites:
  - linear-code
extends: []
related:
  - standard-generator-matrix
  - syndrome
contrasts_with: []
answers_questions:
  - "What is a canonical parity-check matrix?"
  - "How does the parity-check matrix relate to the generator matrix?"
---

# Quick Definition

A canonical parity-check matrix has the form $H = (A \mid I_m)$, where $A$ is an $m \times (n-m)$ matrix and $I_m$ is the $m \times m$ identity. It defines a linear code and determines error-detection/correction capabilities through its column structure.

# Core Definition

"If the last $m$ columns of the matrix form the $m \times m$ identity matrix, $I_m$, then the matrix is a *canonical parity-check matrix*. More specifically, $H = (A \mid I_m)$" (Judson, p. 114). The null space of $H$ gives an $(n, n-m)$-block code where the first $n-m$ bits are information bits and the last $m$ are check bits (Theorem 8.25).

# Prerequisites

- **Linear Code** — The canonical parity-check matrix defines a linear code

# Key Properties

1. Form: $H = (A \mid I_m)$ where $A$ is $m \times (n-m)$ and $I_m$ is $m \times m$ identity
2. Defines an $(n, n-m)$-block code
3. First $n - m$ bits are information bits; last $m$ are check bits
4. No zero columns implies single error detection (Theorem 8.31)
5. No identical columns implies single error correction (Theorem 8.34)
6. $HG = \mathbf{0}$ where $G$ is the standard generator matrix (Lemma 8.27)

# Construction / Recognition

## To Construct:
1. Choose an $m \times (n-m)$ matrix $A$ with entries in $\mathbb{Z}_2$
2. Form $H = (A \mid I_m)$
3. For single error correction: ensure all columns of $A$ are distinct and nonzero, and distinct from columns of $I_m$

# Context & Application

The canonical form provides a systematic way to generate linear codes with desired properties. The identity matrix portion ensures the check bits directly enforce parity conditions.

# Examples

**Example 1** (p. 114-115): With $A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$, $H = \begin{pmatrix} 0 & 1 & 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 & 0 & 1 \end{pmatrix}$. This gives a $(6, 3)$-block code with 8 codewords.

# Relationships

## Builds Upon
- **Linear Code** — Defines a linear code

## Enables
- **Standard Generator Matrix** — Derived from the parity-check matrix
- **Syndrome** — $H\mathbf{x}$ gives the syndrome for error detection

# Common Errors

- **Error**: Placing the identity matrix on the left instead of the right
  **Correction**: In canonical form, $H = (A \mid I_m)$ with identity on the right

# Common Confusions

- **Confusion**: Thinking any matrix can be a parity-check matrix
  **Clarification**: Any binary matrix defines a linear code, but canonical form requires $I_m$ in the last $m$ columns

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.3, Theorem 8.25, pages 114-117.

# Verification Notes

- Definition source: Direct from p. 114
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
