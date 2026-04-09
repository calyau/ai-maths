---
concept: Maximum-Likelihood Decoding
slug: maximum-likelihood-decoding
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 107
section: "8.1 Error-Detecting and Correcting Codes"
extraction_confidence: high
aliases: []
prerequisites:
  - hamming-distance
  - minimum-distance
extends: []
related:
  - error-correcting-code
  - coset-decoding
contrasts_with: []
answers_questions:
  - "What is maximum-likelihood decoding?"
---

# Quick Definition

Maximum-likelihood decoding decodes a received $n$-tuple into the codeword that is closest to it in Hamming distance. It assumes that fewer errors are more likely than many errors.

# Core Definition

"We will also assume that a received $n$-tuple is decoded into a codeword that is closest to it; that is, we assume that the receiver uses *maximum-likelihood decoding*" (Judson, p. 108). This strategy minimizes the probability of incorrect decoding under the assumption that transmission errors are rare and independent.

# Prerequisites

- **Hamming Distance** — "Closest" is measured by Hamming distance
- **Minimum Distance** — Determines when decoding is unambiguous

# Key Properties

1. Decodes to the nearest codeword in Hamming distance
2. Optimal when errors are independent and each bit has the same error probability
3. Unambiguous when the number of errors is at most $\lfloor(d_{\min}-1)/2\rfloor$
4. Can be implemented via coset decoding for linear codes

# Construction / Recognition

## To Decode:
1. Receive word $\mathbf{r}$
2. Compute $d(\mathbf{r}, \mathbf{c})$ for each codeword $\mathbf{c}$
3. Decode as the codeword with minimum distance

# Context & Application

Maximum-likelihood decoding is the theoretically optimal strategy, but brute-force comparison is impractical for large codes. Syndrome decoding and coset decoding provide efficient alternatives for linear codes.

# Examples

**Example 1** (p. 107): If codewords are $(000)$ and $(111)$ and $(101)$ is received, then $d((101),(000)) = 2$ and $d((101),(111)) = 1$, so decode as $(111)$.

# Relationships

## Builds Upon
- **Hamming Distance** — Distance metric for decoding
- **Minimum Distance** — Determines unambiguous decoding radius

## Related
- **Coset Decoding** — An efficient implementation for linear codes

# Common Errors

- **Error**: Attempting maximum-likelihood decoding by comparing to every possible $n$-tuple
  **Correction**: Only compare to codewords, not all possible $n$-tuples

# Common Confusions

- **Confusion**: Thinking maximum-likelihood always gives the correct original message
  **Clarification**: If more errors occur than the code can correct, maximum-likelihood may decode to the wrong codeword

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, "Maximum-Likelihood Decoding," pages 107-108.

# Verification Notes

- Definition source: Direct from p. 108
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
