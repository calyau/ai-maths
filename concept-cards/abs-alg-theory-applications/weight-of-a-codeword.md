---
concept: Weight of a Codeword
slug: weight-of-a-codeword
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
  - Hamming weight
prerequisites:
  - hamming-distance
extends: []
related:
  - minimum-distance
  - group-code
contrasts_with: []
answers_questions:
  - "What is the weight of a codeword?"
  - "How does weight relate to Hamming distance?"
---

# Quick Definition

The weight $w(\mathbf{x})$ of a binary codeword $\mathbf{x}$ is the number of 1s in $\mathbf{x}$. Equivalently, $w(\mathbf{x}) = d(\mathbf{x}, \mathbf{0})$.

# Core Definition

"The *weight*, $w(\mathbf{x})$, of a binary codeword $\mathbf{x}$ is the number of 1s in $\mathbf{x}$. Clearly, $w(\mathbf{x}) = d(\mathbf{x}, \mathbf{0})$" (Judson, p. 109).

# Prerequisites

- **Hamming Distance** — Weight is defined as distance from the zero word

# Key Properties

1. $w(\mathbf{x}) = d(\mathbf{x}, \mathbf{0})$
2. $w(\mathbf{x} + \mathbf{y}) = d(\mathbf{x}, \mathbf{y})$ (Lemma 8.17)
3. For group codes, $d_{\min}$ equals the minimum weight of nonzero codewords (Theorem 8.18)
4. Weights are easier to compute than all pairwise distances

# Construction / Recognition

## To Compute:
1. Count the number of 1s in the binary $n$-tuple

# Context & Application

For group codes, computing the minimum weight of nonzero codewords is much easier than computing all pairwise Hamming distances. Theorem 8.18 shows these give the same result.

# Examples

**Example 1** (p. 109): $w((10101)) = 3$, $w((11010)) = 3$, $w((00011)) = 2$.

# Relationships

## Builds Upon
- **Hamming Distance** — Weight is a special case of distance

## Enables
- **Minimum Distance** — For group codes, $d_{\min} = \min\{w(\mathbf{x}) : \mathbf{x} \neq \mathbf{0}\}$

## Related
- **Group Code** — The weight-distance theorem applies to group codes

# Common Errors

- **Error**: Using minimum weight to find $d_{\min}$ for non-group codes
  **Correction**: The theorem $d_{\min} = \min\{w(\mathbf{x})\}$ only holds for group codes

# Common Confusions

- **Confusion**: Confusing weight with distance
  **Clarification**: Weight is a property of a single word; distance is between two words

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, page 109, Lemma 8.17, Theorem 8.18.

# Verification Notes

- Definition source: Direct from p. 109
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
