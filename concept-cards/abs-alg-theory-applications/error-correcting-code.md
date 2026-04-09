---
# === CORE IDENTIFICATION ===
concept: Error-Correcting Code
slug: error-correcting-code

# === CLASSIFICATION ===
category: applications-coding
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 107
section: "8.1 Error-Detecting and Correcting Codes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - minimum-distance
extends:
  - error-detecting-code
related:
  - hamming-distance
  - maximum-likelihood-decoding
contrasts_with:
  - error-detecting-code

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an error-correcting code?"
  - "How many errors can a code correct?"
---

# Quick Definition

An error-correcting code can not only detect but also correct transmission errors. A code with minimum distance $d_{\min} = 2n + 1$ can correct up to $n$ errors.

# Core Definition

**Theorem 8.13:** "Let $C$ be a code with $d_{\min} = 2n + 1$. Then $C$ can correct any $n$ or fewer errors. Furthermore, any $2n$ or fewer errors can be detected in $C$" (Judson, p. 110). Error correction works by decoding a received word to the nearest codeword.

# Prerequisites

- **Minimum Distance** — Determines the correction capability

# Key Properties

1. Requires $d_{\min} \geq 3$ for single error correction
2. $d_{\min} = 2n + 1$ allows correction of up to $n$ errors
3. Uses maximum-likelihood decoding: decode to the nearest codeword
4. More redundancy (more check bits) enables more error correction

# Construction / Recognition

## To Correct:
1. Receive a word $\mathbf{y}$
2. Find the codeword $\mathbf{x}$ closest to $\mathbf{y}$ (in Hamming distance)
3. Decode $\mathbf{y}$ as $\mathbf{x}$

# Context & Application

Error correction is crucial when retransmission is impractical (e.g., deep-space communication, data storage). Linear codes with suitable minimum distance provide efficient error correction.

# Examples

**Example 1** (p. 107): The repetition code $\{(000), (111)\}$ has $d_{\min} = 3$ and can correct single errors. If $(101)$ is received, the nearest codeword is $(111)$.

**Example 2** (p. 111): The code with codewords $(00000)$, $(00111)$, $(11100)$, $(11011)$ has $d_{\min} = 3$ and corrects single errors.

# Relationships

## Builds Upon
- **Minimum Distance** — Determines correction capability
- **Error-Detecting Code** — Error correction extends detection

## Related
- **Maximum-Likelihood Decoding** — The decoding strategy
- **Hamming Distance** — Measures distance between words

## Contrasts With
- **Error-Detecting Code** — Detection without correction

# Common Errors

- **Error**: Assuming a code can correct as many errors as it can detect
  **Correction**: Detection capability is roughly double correction capability: $d_{\min} = 2n+1$ detects $2n$ but corrects only $n$

# Common Confusions

- **Confusion**: Thinking error correction always gives the right answer
  **Clarification**: If more errors occur than the code can correct, decoding may produce the wrong codeword

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, Theorem 8.13, pages 107-111.

# Verification Notes

- Definition source: Direct from Theorem 8.13
- Confidence rationale: Explicit theorem with examples
- Uncertainties: None
- Cross-reference status: Verified
