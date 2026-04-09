---
concept: Decoding Table
slug: decoding-table
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 121
section: "8.4 Efficient Decoding"
extraction_confidence: high
aliases: []
prerequisites:
  - syndrome
  - coset-leader
extends: []
related:
  - coset-decoding
contrasts_with: []
answers_questions:
  - "What is a decoding table?"
  - "How do I use a decoding table?"
---

# Quick Definition

A decoding table maps each possible syndrome to its corresponding coset leader. To decode a received word, compute its syndrome, look up the coset leader, and subtract it to obtain the corrected codeword.

# Core Definition

"We can make a table that designates a coset leader corresponding to each syndrome. Such a list is called a *decoding table*" (Judson, p. 121). The table has $2^m$ entries (one per syndrome) for a code with $m$ check bits.

# Prerequisites

- **Syndrome** — The lookup key in the table
- **Coset Leader** — The table value

# Key Properties

1. Has $2^m$ entries for $m$ check bits
2. Each syndrome maps to exactly one coset leader
3. Enables O(1) lookup decoding (after syndrome computation)
4. Precomputed once, used for all decoding

# Construction / Recognition

## To Build:
1. List all $2^{n-k}$ cosets of the code
2. For each coset, find the coset leader (minimum weight element)
3. Compute its syndrome $H\mathbf{e}$
4. Store the mapping: syndrome $\to$ coset leader

## To Use:
1. Compute $H\mathbf{r}$ for received word $\mathbf{r}$
2. Look up the syndrome in the table to find coset leader $\mathbf{e}$
3. Correct: $\mathbf{c} = \mathbf{r} + \mathbf{e}$

# Context & Application

Decoding tables make linear code decoding practical. For a $(32, 24)$-code, the table has only $2^8 = 256$ entries, far fewer than the $2^{24}$ codewords.

# Examples

**Example 1** (p. 121): Table 8.42 for the $(5,3)$-code maps syndrome $(010)$ to coset leader $(00010)$. If $\mathbf{r} = (01111)$ has syndrome $(010)$, then the error is $(00010)$ and the corrected codeword is $(01101)$.

# Relationships

## Builds Upon
- **Syndrome** — Used as the key in the table
- **Coset Leader** — The value stored in the table

## Related
- **Coset Decoding** — The decoding table implements coset decoding

# Common Errors

- **Error**: Forgetting to subtract the coset leader to get the corrected codeword
  **Correction**: The corrected word is $\mathbf{r} + \mathbf{e}$ (addition in $\mathbb{Z}_2^n$ is the same as subtraction)

# Common Confusions

- **Confusion**: Thinking the decoding table gives the message directly
  **Clarification**: The table gives the error pattern; you must add it to the received word to get the codeword, then extract the message bits

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.4, Table 8.42, pages 121-122.

# Verification Notes

- Definition source: Direct from p. 121
- Confidence rationale: Explicit definition with example table
- Uncertainties: None
- Cross-reference status: Verified
