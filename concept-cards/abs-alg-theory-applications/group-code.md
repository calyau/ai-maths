---
concept: Group Code
slug: group-code
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 111
section: "8.2 Linear Codes"
extraction_confidence: high
aliases: []
prerequisites:
  - block-code
extends:
  - block-code
related:
  - linear-code
  - weight-of-a-codeword
contrasts_with: []
answers_questions:
  - "What is a group code?"
  - "Why is it useful for a code to be a group?"
---

# Quick Definition

A group code is a code that is also a subgroup of $\mathbb{Z}_2^n$. This algebraic structure allows the minimum distance to be computed as the minimum weight, greatly simplifying analysis.

# Core Definition

"A *group code* is a code that is also a subgroup of $\mathbb{Z}_2^n$" (Judson, p. 111). To verify, one need only check closure under addition: if any two codewords are added, the result must be a codeword. Inverses and identity are automatic since every element of $\mathbb{Z}_2^n$ is its own inverse.

# Prerequisites

- **Block Code** — A group code is a block code with additional structure

# Key Properties

1. Closed under addition in $\mathbb{Z}_2^n$
2. Contains the zero codeword $\mathbf{0}$
3. $d_{\min} = \min\{w(\mathbf{x}) : \mathbf{x} \neq \mathbf{0}\}$ (Theorem 8.18)
4. Every element is its own inverse
5. Only need to check closure to verify the group property

# Construction / Recognition

## To Verify a Code is a Group Code:
1. Check that adding any two codewords produces another codeword
2. The zero word and inverses are automatic in $\mathbb{Z}_2^n$

# Context & Application

Group codes allow efficient computation of minimum distance via minimum weight. This property motivates the development of linear codes, which are group codes with additional matrix structure.

# Examples

**Example 1** (p. 111-112): The code in Example 8.16 with 16 codewords of length 7 is a group code. Its minimum nonzero weight is 3, so $d_{\min} = 3$.

# Relationships

## Builds Upon
- **Block Code** — A group code is a block code that is also a group

## Enables
- **Linear Code** — Linear codes are group codes defined by matrices

## Related
- **Weight of a Codeword** — Minimum weight = minimum distance for group codes

# Common Errors

- **Error**: Forgetting to check that $\mathbf{0}$ is a codeword
  **Correction**: Every group code must contain the zero word (it's the identity)

# Common Confusions

- **Confusion**: Thinking the minimum weight result holds for all codes
  **Clarification**: $d_{\min} = \min\{w(\mathbf{x})\}$ holds only for group codes, not arbitrary codes

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.2, Lemma 8.17, Theorem 8.18, pages 111-112.

# Verification Notes

- Definition source: Direct from p. 111
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
