---
concept: Coset Leader
slug: coset-leader
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
  - coset-decoding
extends: []
related:
  - decoding-table
  - weight-of-a-codeword
contrasts_with: []
answers_questions:
  - "What is a coset leader?"
---

# Quick Definition

A coset leader is an $n$-tuple of least weight in a coset of a linear code $C$. It represents the most likely error pattern for any received word in that coset.

# Core Definition

"An $n$-tuple of least weight in a coset is called a *coset leader*" (Judson, p. 121). In maximum-likelihood decoding, the coset leader represents the error $\mathbf{e}$ with the fewest bit flips, making it the most probable error pattern.

# Prerequisites

- **Coset Decoding** — Coset leaders are used in coset decoding

# Key Properties

1. Minimum weight element in the coset
2. Represents the most likely error pattern
3. May not be unique (ties are possible)
4. For single error-correcting codes, coset leaders have weight 0 or 1
5. The coset leader of $C$ itself is $\mathbf{0}$ (the zero word)

# Construction / Recognition

## To Find:
1. List all elements in a coset
2. Select the one(s) with minimum weight

# Context & Application

Coset leaders are precomputed and stored in a decoding table, enabling fast decoding by syndrome lookup.

# Examples

**Example 1** (p. 121): In Table 8.40, the coset leaders for the $(5,3)$-code are $(00000)$, $(10000)$, $(01000)$, $(00100)$, $(00010)$, $(00001)$, $(10100)$, $(00110)$.

# Relationships

## Builds Upon
- **Coset Decoding** — Coset leaders are the key to the decoding procedure

## Related
- **Decoding Table** — Maps syndromes to coset leaders
- **Weight of a Codeword** — Coset leaders have minimum weight in their coset

# Common Errors

- **Error**: Assuming the coset leader is always unique
  **Correction**: Multiple elements may share the minimum weight; any can be chosen

# Common Confusions

- **Confusion**: Thinking the coset leader is a codeword
  **Clarification**: The coset leader is only a codeword for the coset $C$ itself (where it is $\mathbf{0}$)

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.4, page 121.

# Verification Notes

- Definition source: Direct from p. 121
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
