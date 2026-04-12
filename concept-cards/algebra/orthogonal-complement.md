---
# === CORE IDENTIFICATION ===
concept: Orthogonal Complement
slug: orthogonal-complement

# === CLASSIFICATION ===
category: bilinear-forms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.4 Orthogonality"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "orthogonal space"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonality-bilinear-forms
extends: []
related:
  - non-degenerate-form
  - nullspace-of-a-form
  - orthogonal-projection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the orthogonal complement of a subspace?"
---

# Quick Definition

The orthogonal complement W^perp of a subspace W is the set of all vectors orthogonal to every vector in W. If the form is nondegenerate on W, then V = W direct-sum W^perp.

# Core Definition

The orthogonal space to a subspace W of V is W^perp = {v in V | (v, w) = 0 for all w in W} (Artin, (8.4.1), p. 247). Theorem 8.4.5 states: the form is nondegenerate on W if and only if V = W direct-sum W^perp. When V is the orthogonal sum of W and W^perp and both carry nondegenerate restrictions, the form is also nondegenerate on W^perp.

# Prerequisites

- **Orthogonality (bilinear forms)** — Orthogonal complement is built from the orthogonality relation

# Key Properties

1. W^perp is always a subspace of V
2. The form is nondegenerate on W iff W intersect W^perp = {0} (Lemma 8.4.2)
3. If nondegenerate on W, then V = W direct-sum W^perp (Theorem 8.4.5)
4. The nullspace N of V equals V^perp
5. If the form is nondegenerate on V and on W, it is nondegenerate on W^perp

# Construction / Recognition

## To Construct:
1. Given W with basis (w_1, ..., w_k) and a matrix A for the form
2. Solve the system A Y = 0 restricted to the coordinates paired with W
3. The solution space gives W^perp

## To Recognize:
1. A subspace of V consisting of all vectors orthogonal to W

# Context & Application

Orthogonal complements decompose a vector space into independent components with respect to a form. This is fundamental to the spectral theorem, the Gram-Schmidt process, and projection formulas. In positive definite spaces, orthogonal complements always give a direct sum decomposition.

# Examples

**Example 1** (p. 247): In R^3 with dot product, the orthogonal complement of the span of (1, 1, 1)^t is the plane x_1 + x_2 + x_3 = 0.

# Relationships

## Builds Upon
- **Orthogonality (bilinear forms)** — The complement collects all orthogonal vectors

## Enables
- **Orthogonal projection** — Projects onto W along W^perp
- **Spectral theorem** — Eigenspaces decompose V as orthogonal complements

## Related
- **Non-degenerate form** — Needed for V = W direct-sum W^perp
- **Nullspace of a form** — N = V^perp

# Common Errors

- **Error**: Assuming V = W direct-sum W^perp without checking nondegeneracy on W
  **Correction**: V = W direct-sum W^perp holds if and only if the form is nondegenerate on W (Theorem 8.4.5)

# Common Confusions

- **Confusion**: Thinking W^perp is always a complement (W intersect W^perp = {0})
  **Clarification**: If the form is degenerate on W, then W intersect W^perp is nonzero

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, pages 247-249. Theorem 8.4.5.

# Verification Notes

- Definition source: Direct from (8.4.1), p. 247
- Confidence rationale: Explicitly defined with full theorem
- Uncertainties: None
- Cross-reference status: Verified
