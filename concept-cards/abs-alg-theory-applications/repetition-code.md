---
concept: Repetition Code
slug: repetition-code
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 105
section: "8.1 Error-Detecting and Correcting Codes"
extraction_confidence: high
aliases:
  - triple repetition code
prerequisites:
  - error-correcting-code
extends: []
related:
  - block-code
  - maximum-likelihood-decoding
contrasts_with: []
answers_questions:
  - "What is a repetition code?"
---

# Quick Definition

A repetition code encodes each bit by repeating it multiple times. The triple repetition code sends each $n$-tuple three times, creating a $(3n, n)$-block code that corrects single errors but is inefficient.

# Core Definition

In the triple repetition code, "the message is encoded into a binary $3n$-tuple by simply repeating the message three times: $(x_1, \ldots, x_n) \mapsto (x_1, \ldots, x_n, x_1, \ldots, x_n, x_1, \ldots, x_n)$" (Judson, Example 8.2, p. 105). Decoding uses majority voting on each bit position.

# Prerequisites

- **Error-Correcting Code** — The repetition code is a simple error-correcting code

# Key Properties

1. Corrects all single errors
2. Very inefficient: requires $2n$ extra bits for $n$ information bits
3. Decoding by majority vote: for each bit position, choose the value appearing in at least 2 of 3 copies
4. $d_{\min} = 3$ for the simplest version $\{(000), (111)\}$

# Construction / Recognition

## To Encode:
1. Take message $(x_1, \ldots, x_n)$
2. Transmit $(x_1, \ldots, x_n, x_1, \ldots, x_n, x_1, \ldots, x_n)$

## To Decode:
1. For each bit position $i$, look at the $i$th, $(n+i)$th, and $(2n+i)$th bits
2. Choose the majority value

# Context & Application

The repetition code is the simplest error-correcting code and serves as a baseline. It motivates the search for more efficient codes that add fewer redundant bits.

# Examples

**Example 1** (p. 105): Message $(0110)$ is encoded as $(0110\, 0110\, 0110)$. If an error in the 5th bit gives $(0110\, 1110\, 0110)$, majority decoding correctly recovers $(0110)$.

**Example 2** (p. 107): The simple repetition code $\{(000), (111)\}$ has $d_{\min} = 3$ and corrects single errors.

# Relationships

## Builds Upon
- **Error-Correcting Code** — A simple example

## Related
- **Block Code** — A $(3n, n)$-block code
- **Maximum-Likelihood Decoding** — Majority vote implements MLD

# Common Errors

- **Error**: Assuming repetition codes handle multiple errors well
  **Correction**: With 3 repetitions, only single errors are reliably corrected

# Common Confusions

- **Confusion**: Thinking repetition is the only way to achieve error correction
  **Clarification**: Linear codes achieve much better efficiency (fewer redundant bits per corrected error)

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, Examples 8.2 and 8.4, pages 105-107.

# Verification Notes

- Definition source: Direct from Example 8.2, p. 105
- Confidence rationale: Explicit example
- Uncertainties: None
- Cross-reference status: Verified
