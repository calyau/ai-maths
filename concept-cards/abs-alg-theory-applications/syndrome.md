---
concept: Syndrome
slug: syndrome
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 119
section: "8.4 Efficient Decoding"
extraction_confidence: high
aliases: []
prerequisites:
  - canonical-parity-check-matrix
  - linear-code
extends: []
related:
  - coset-decoding
  - decoding-table
contrasts_with: []
answers_questions:
  - "What is the syndrome of a received word?"
  - "How does syndrome decoding work?"
---

# Quick Definition

The syndrome of a received word $\mathbf{x}$ is $H\mathbf{x}$, where $H$ is the parity-check matrix. A syndrome of $\mathbf{0}$ means $\mathbf{x}$ is a codeword; otherwise, the syndrome identifies the error pattern.

# Core Definition

"If $H$ is an $m \times n$ matrix and $\mathbf{x} \in \mathbb{Z}_2^n$, then we say that the *syndrome* of $\mathbf{x}$ is $H\mathbf{x}$" (Judson, p. 119). Key property: the syndrome of a received word equals the syndrome of the error (Proposition 8.36), since $H\mathbf{x} = H(\mathbf{c} + \mathbf{e}) = H\mathbf{e}$.

# Prerequisites

- **Canonical Parity-Check Matrix** — The syndrome is computed using $H$
- **Linear Code** — Syndromes are defined for linear codes

# Key Properties

1. $H\mathbf{x} = \mathbf{0}$ if and only if $\mathbf{x}$ is a codeword
2. The syndrome depends only on the error, not the transmitted codeword (Proposition 8.36)
3. If the syndrome equals the $i$th column of $H$, the error is in the $i$th bit (Theorem 8.37)
4. For single error-correcting codes, the syndrome uniquely identifies the error position
5. Two words are in the same coset iff they have the same syndrome (Proposition 8.43)

# Construction / Recognition

## To Decode Using Syndromes:
1. Compute $H\mathbf{r}$ for received word $\mathbf{r}$
2. If $H\mathbf{r} = \mathbf{0}$, no error detected
3. If $H\mathbf{r}$ equals the $i$th column of $H$, flip the $i$th bit of $\mathbf{r}$

# Context & Application

Syndrome decoding is far more efficient than comparing against all codewords. For a $(32, 24)$-block code, instead of checking $2^{24}$ codewords, one only computes a single matrix multiplication and looks up the syndrome in a table of $2^8 = 256$ entries.

# Examples

**Example 1** (p. 119): With $H = \begin{pmatrix} 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 & 1 \end{pmatrix}$, $\mathbf{x} = (11011)^t$ gives $H\mathbf{x} = (0,0,0)^t$ (codeword), while $\mathbf{y} = (01011)^t$ gives $H\mathbf{y} = (1,0,1)^t$ (error in first bit, matching column 1 of $H$).

# Relationships

## Builds Upon
- **Canonical Parity-Check Matrix** — Syndrome is $H\mathbf{x}$
- **Linear Code** — Syndromes apply to linear codes

## Enables
- **Coset Decoding** — Syndromes identify cosets
- **Decoding Table** — Maps syndromes to coset leaders

# Common Errors

- **Error**: Thinking the syndrome tells you the correct message directly
  **Correction**: The syndrome identifies the error pattern; subtract the error from the received word

# Common Confusions

- **Confusion**: Thinking a zero syndrome means no error occurred
  **Clarification**: A zero syndrome means the received word is a codeword, which could be correct or could result from undetectable multiple errors

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.4, Proposition 8.36, Theorem 8.37, pages 119-120.

# Verification Notes

- Definition source: Direct from p. 119
- Confidence rationale: Explicit definition with propositions
- Uncertainties: None
- Cross-reference status: Verified
