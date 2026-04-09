---
concept: Coset Decoding
slug: coset-decoding
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 120
section: "8.4 Efficient Decoding"
extraction_confidence: high
aliases:
  - standard decoding
prerequisites:
  - linear-code
  - left-coset
  - syndrome
extends: []
related:
  - coset-leader
  - decoding-table
  - lagranges-theorem
contrasts_with: []
answers_questions:
  - "How does coset decoding work?"
  - "How do I decode using cosets and syndromes?"
---

# Quick Definition

Coset decoding uses the cosets of a linear code $C$ in $\mathbb{Z}_2^n$ to implement maximum-likelihood decoding. The received word's coset is identified by its syndrome, and the coset leader gives the most likely error pattern.

# Core Definition

"*Coset* or *standard decoding* uses the cosets of $C$ in $\mathbb{Z}_2^n$ to implement maximum-likelihood decoding" (Judson, p. 120). By Lagrange's Theorem, there are $2^{n-m}$ cosets of an $(n, m)$-code. Two $n$-tuples are in the same coset iff they have the same syndrome (Proposition 8.43).

# Prerequisites

- **Linear Code** — The code $C$ being decoded
- **Left Coset** — Cosets of $C$ in $\mathbb{Z}_2^n$ (note: in $\mathbb{Z}_2^n$, left = right cosets)
- **Syndrome** — Identifies which coset the received word belongs to

# Key Properties

1. $\mathbb{Z}_2^n$ has $2^{n-m}$ cosets of an $(n,m)$-code $C$
2. A received word $\mathbf{r}$ is in coset $\mathbf{e} + C$ where $\mathbf{e}$ is the error
3. The coset leader (minimum weight element) gives the most likely error
4. $\mathbf{x} = \mathbf{r} + \mathbf{e}$ recovers the transmitted codeword
5. Same syndrome implies same coset (Proposition 8.43)

# Construction / Recognition

## To Decode:
1. Compute syndrome $H\mathbf{r}$
2. Look up the syndrome in the decoding table to find the coset leader $\mathbf{e}$
3. Compute $\mathbf{r} + \mathbf{e}$ to get the transmitted codeword

# Context & Application

Coset decoding connects group theory (cosets, Lagrange's theorem) to practical coding. It is efficient: a $(32, 24)$-code has only $2^8 = 256$ cosets, so the decoding table is small.

# Examples

**Example 1** (p. 120-121): For a $(5, 3)$-code with $H = \begin{pmatrix} 0 & 1 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 1 \end{pmatrix}$, there are $2^2 = 4$ codewords and $2^3 = 8$ cosets. If $\mathbf{r} = (01111)$ is received, its syndrome is $(0,1,0)^t$, the coset leader is $(00010)$, so the transmitted codeword is $(01111) + (00010) = (01101)$.

# Relationships

## Builds Upon
- **Linear Code** — Coset decoding applies to linear codes
- **Left Coset** — Uses cosets of $C$ in $\mathbb{Z}_2^n$
- **Syndrome** — Links received words to cosets
- **Lagrange's Theorem** — Determines the number of cosets

## Related
- **Coset Leader** — Minimum weight element in each coset
- **Decoding Table** — Maps syndromes to coset leaders

# Common Errors

- **Error**: Searching through all cosets for the received word
  **Correction**: Use the syndrome to directly identify the coset

# Common Confusions

- **Confusion**: Thinking each syndrome can correspond to only one error position
  **Clarification**: If the code cannot correct the error (multiple errors), the coset leader may not be the actual error

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.4, "Coset Decoding," Proposition 8.43, pages 120-122.

# Verification Notes

- Definition source: Direct from p. 120
- Confidence rationale: Explicit definition with worked examples
- Uncertainties: None
- Cross-reference status: Verified
