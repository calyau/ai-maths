---
concept: Hamming Distance
slug: hamming-distance
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
  - distance
prerequisites: []
extends: []
related:
  - weight-of-a-codeword
  - minimum-distance
contrasts_with: []
answers_questions:
  - "What is Hamming distance?"
  - "How do I compute the distance between two codewords?"
---

# Quick Definition

The Hamming distance $d(\mathbf{x}, \mathbf{y})$ between two binary $n$-tuples is the number of positions in which they differ. It measures the minimum number of bit changes needed to transform one word into another.

# Core Definition

"Let $\mathbf{x} = (x_1, \ldots, x_n)$ and $\mathbf{y} = (y_1, \ldots, y_n)$ be binary $n$-tuples. The *Hamming distance* or *distance*, $d(\mathbf{x}, \mathbf{y})$, between $\mathbf{x}$ and $\mathbf{y}$ is the number of bits in which $\mathbf{x}$ and $\mathbf{y}$ differ" (Judson, p. 109).

# Prerequisites

This is a foundational concept in coding theory with no prerequisites.

# Key Properties

1. $d(\mathbf{x}, \mathbf{y}) \geq 0$ (non-negativity)
2. $d(\mathbf{x}, \mathbf{y}) = 0$ if and only if $\mathbf{x} = \mathbf{y}$
3. $d(\mathbf{x}, \mathbf{y}) = d(\mathbf{y}, \mathbf{x})$ (symmetry)
4. $d(\mathbf{x}, \mathbf{y}) \leq d(\mathbf{x}, \mathbf{z}) + d(\mathbf{z}, \mathbf{y})$ (triangle inequality)
5. $d(\mathbf{x}, \mathbf{y}) = w(\mathbf{x} + \mathbf{y})$ for group codes (Lemma 8.17)
6. Hamming distance is a metric on $\mathbb{Z}_2^n$ (Proposition 8.11)

# Construction / Recognition

## To Compute:
1. Compare the two $n$-tuples position by position
2. Count the number of positions where they differ

# Context & Application

Hamming distance is the fundamental measure in coding theory. The error-detecting and error-correcting capabilities of a code are entirely determined by the minimum Hamming distance between its codewords.

# Examples

**Example 1** (p. 109): $d((10101), (11010)) = 4$, $d((10101), (00011)) = 3$, $d((11010), (00011)) = 3$.

# Relationships

## Enables
- **Minimum Distance** — The minimum over all pairs of codewords
- **Error-Correcting Code** — Correction capability depends on Hamming distance

## Related
- **Weight of a Codeword** — $w(\mathbf{x}) = d(\mathbf{x}, \mathbf{0})$

# Common Errors

- **Error**: Confusing Hamming distance with weight
  **Correction**: Distance is between two words; weight is the distance from the zero word

# Common Confusions

- **Confusion**: Thinking Hamming distance measures "how similar" two words are
  **Clarification**: It measures *differences*; larger distance means more different

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, Proposition 8.11, page 109.

# Verification Notes

- Definition source: Direct from p. 109
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
