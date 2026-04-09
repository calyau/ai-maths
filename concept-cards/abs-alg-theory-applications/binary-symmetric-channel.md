---
concept: Binary Symmetric Channel
slug: binary-symmetric-channel
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 108
section: "8.1 Error-Detecting and Correcting Codes"
extraction_confidence: high
aliases:
  - BSC
prerequisites: []
extends: []
related:
  - maximum-likelihood-decoding
  - error-correcting-code
contrasts_with: []
answers_questions:
  - "What is a binary symmetric channel?"
---

# Quick Definition

A binary symmetric channel is a communication model where each bit is correctly transmitted with probability $p$ and flipped with probability $q = 1 - p$, independently of other bits.

# Core Definition

"A *binary symmetric channel* is a model that consists of a transmitter capable of sending a binary signal, either a 0 or a 1, together with a receiver. Let $p$ be the probability that the signal is correctly received. Then $q = 1 - p$ is the probability of an incorrect reception" (Judson, p. 108).

# Prerequisites

This is an introductory concept requiring basic probability.

# Key Properties

1. Each bit has independent error probability $q = 1 - p$
2. The probability of exactly $k$ errors in $n$ bits is $\binom{n}{k}q^k p^{n-k}$ (Theorem 8.7)
3. Symmetric: $P(\text{0 received} | \text{1 sent}) = P(\text{1 received} | \text{0 sent}) = q$
4. Maximum-likelihood decoding is optimal for this channel

# Construction / Recognition

## To Model:
1. Specify the bit-flip probability $q$ (typically small, e.g., 0.001)
2. Each bit is independently transmitted
3. No correlation between errors in different bit positions

# Context & Application

The binary symmetric channel is the standard theoretical model for analyzing code performance. It justifies maximum-likelihood decoding and allows precise calculation of error probabilities.

# Examples

**Example 1** (p. 108): With $p = 0.999$ and $n = 10000$ bits, the probability of error-free transmission is $(0.999)^{10000} \approx 0.00005$.

**Example 2** (p. 108-109): With $p = 0.995$ and $n = 500$: $P(\text{no errors}) \approx 0.082$, $P(\text{1 error}) \approx 0.204$, $P(\text{2 errors}) \approx 0.257$.

# Relationships

## Enables
- **Maximum-Likelihood Decoding** — Optimal for this channel model

## Related
- **Error-Correcting Code** — Designed to handle BSC errors

# Common Errors

- **Error**: Assuming errors are correlated across bits
  **Correction**: In a BSC, errors are independent

# Common Confusions

- **Confusion**: Thinking $p$ is the error probability
  **Clarification**: $p$ is the probability of *correct* transmission; $q = 1 - p$ is the error probability

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, Theorem 8.7, pages 108-109.

# Verification Notes

- Definition source: Direct from p. 108
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
