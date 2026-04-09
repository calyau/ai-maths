---
concept: Information Bits and Check Bits
slug: information-bits-and-check-bits
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 116
section: "8.3 Parity-Check and Generator Matrices"
extraction_confidence: high
aliases: []
prerequisites:
  - canonical-parity-check-matrix
extends: []
related:
  - standard-generator-matrix
  - block-code
contrasts_with: []
answers_questions:
  - "What are information bits and check bits?"
---

# Quick Definition

In a linear code with canonical parity-check matrix $H = (A \mid I_m)$, the first $n - m$ bits of a codeword are information bits (carrying the message) and the last $m$ bits are check bits (providing redundancy for error handling).

# Core Definition

"The first $n-m$ bits in $\mathbf{x}$ are called *information bits* and the last $m$ bits are called *check bits*" (Judson, p. 116). The information bits can be arbitrary, while the check bits are determined by the equation $H\mathbf{x} = \mathbf{0}$.

# Prerequisites

- **Canonical Parity-Check Matrix** — Determines which bits are information and which are check

# Key Properties

1. Information bits: first $n - m$ positions, can be freely chosen
2. Check bits: last $m$ positions, determined by the parity equations
3. The $i$th check bit provides an even parity check for certain information bits
4. The generator matrix $G$ computes check bits from information bits automatically

# Construction / Recognition

## To Identify:
1. In canonical form $H = (A \mid I_m)$: positions $1, \ldots, n-m$ are information; positions $n-m+1, \ldots, n$ are check
2. Check bits satisfy the parity equations from $H\mathbf{x} = \mathbf{0}$

# Context & Application

The separation of bits into information and check is fundamental to systematic codes. It allows the message to be read directly from the first $n - m$ positions of any codeword.

# Examples

**Example 1** (p. 115-116): In Example 8.23, a $(6,3)$-code has 3 information bits and 3 check bits. The message $(010)$ becomes the codeword $(010110)$.

# Relationships

## Builds Upon
- **Canonical Parity-Check Matrix** — Determines bit classification

## Related
- **Standard Generator Matrix** — Computes check bits from information bits

# Common Errors

- **Error**: Confusing which bits are information and which are check
  **Correction**: In canonical form, information bits come first, check bits last

# Common Confusions

- **Confusion**: Thinking check bits carry no information about the message
  **Clarification**: Check bits are determined by the information bits; they carry redundancy, not independent information

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.3, Theorem 8.25, page 116.

# Verification Notes

- Definition source: Direct from p. 116
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
