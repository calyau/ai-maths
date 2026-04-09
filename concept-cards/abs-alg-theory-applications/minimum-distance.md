---
concept: Minimum Distance
slug: minimum-distance
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 109
section: "8.1 Error-Detecting and Correcting Codes"
extraction_confidence: high
aliases:
  - "$d_{\\min}$"
prerequisites:
  - hamming-distance
extends: []
related:
  - error-detecting-code
  - error-correcting-code
  - weight-of-a-codeword
contrasts_with: []
answers_questions:
  - "What is the minimum distance of a code?"
  - "How does minimum distance determine error capabilities?"
---

# Quick Definition

The minimum distance $d_{\min}$ of a code is the smallest Hamming distance between any two distinct codewords. It determines the code's error-detecting ($d_{\min} - 1$ errors) and error-correcting ($\lfloor(d_{\min} - 1)/2\rfloor$ errors) capabilities.

# Core Definition

"The *minimum distance* for a code, $d_{\min}$, is the minimum of all distances $d(\mathbf{x}, \mathbf{y})$, where $\mathbf{x}$ and $\mathbf{y}$ are distinct codewords" (Judson, p. 109). For group codes, $d_{\min} = \min\{w(\mathbf{x}) : \mathbf{x} \neq \mathbf{0}\}$ (Theorem 8.18).

# Prerequisites

- **Hamming Distance** — Minimum distance is defined using Hamming distance

# Key Properties

1. A code with $d_{\min} = 2n + 1$ corrects $n$ errors and detects $2n$ errors (Theorem 8.13)
2. $d_{\min} \geq 2$ gives single error detection
3. $d_{\min} \geq 3$ gives single error correction
4. For group codes, $d_{\min}$ equals the minimum nonzero weight (Theorem 8.18)

# Construction / Recognition

## To Compute:
1. For general codes: compute $d(\mathbf{x}, \mathbf{y})$ for all pairs of codewords and take the minimum
2. For group codes: find the minimum weight of nonzero codewords

# Context & Application

The minimum distance is the single most important parameter of a code, as it completely determines the error-detection and error-correction capabilities.

# Examples

**Example 1** (p. 109): Code $C = \{(10101), (11010), (00011)\}$ has $d_{\min} = 3$, so it can correct 1 error and detect 2 errors.

**Example 2** (p. 110): The even parity code on 4 bits has $d_{\min} = 2$ (Table 8.12), so it detects single errors but cannot correct them.

# Relationships

## Builds Upon
- **Hamming Distance** — $d_{\min}$ is defined using Hamming distance

## Enables
- **Error-Detecting Code** — Detection capability: $d_{\min} - 1$ errors
- **Error-Correcting Code** — Correction capability: $\lfloor(d_{\min}-1)/2\rfloor$ errors

## Related
- **Weight of a Codeword** — For group codes, minimum weight = minimum distance

# Common Errors

- **Error**: Confusing detection and correction capability
  **Correction**: $d_{\min} = 2n+1$ detects $2n$ errors but corrects only $n$

# Common Confusions

- **Confusion**: Thinking $d_{\min} = 3$ means the code corrects 3 errors
  **Clarification**: $d_{\min} = 3$ corrects 1 error ($\lfloor 2/2 \rfloor = 1$) and detects 2 errors

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, Theorem 8.13, pages 109-111.

# Verification Notes

- Definition source: Direct from p. 109
- Confidence rationale: Explicit definition with theorem
- Uncertainties: None
- Cross-reference status: Verified
