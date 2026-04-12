---
# === CORE IDENTIFICATION ===
concept: Gram-Schmidt Process
slug: gram-schmidt-process

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
  - "Gram-Schmidt orthogonalization"
  - "Gram-Schmidt procedure"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-projection
  - positive-definite-form
extends: []
related:
  - orthonormal-basis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct an orthonormal basis?"
---

# Quick Definition

The Gram-Schmidt process is an inductive procedure that converts an arbitrary basis of a positive definite space into an orthonormal basis, by repeatedly projecting and normalizing.

# Core Definition

Given a positive definite symmetric or Hermitian form and an arbitrary basis (v_1, ..., v_n), the Gram-Schmidt procedure produces an orthonormal basis (w_1, ..., w_n) as follows: Let V_k = span(v_1, ..., v_k). Suppose (w_1, ..., w_{k-1}) is an orthonormal basis for V_{k-1}. Let pi be the orthogonal projection from V to V_{k-1}. Then W_k = v_k - pi(v_k) is orthogonal to V_{k-1}. Normalize W_k to get w_k (Artin, p. 255).

# Prerequisites

- **Orthogonal projection** — Used at each step to remove the component in the previously constructed subspace
- **Positive definite form** — Required for normalization (dividing by the length)

# Key Properties

1. Input: any basis (v_1, ..., v_n) and a positive definite form
2. Output: an orthonormal basis (w_1, ..., w_n)
3. span(w_1, ..., w_k) = span(v_1, ..., v_k) for each k
4. Each step subtracts the projection onto the previously constructed space and normalizes
5. The process is constructive and algorithmic

# Construction / Recognition

## To Apply:
1. Set w_1 = v_1 / |v_1|
2. For k = 2, ..., n:
   a. Compute pi(v_k) = sum_{i=1}^{k-1} (w_i, v_k) w_i
   b. Set W_k = v_k - pi(v_k)
   c. Normalize: w_k = W_k / |W_k|

# Context & Application

The Gram-Schmidt process is the standard constructive method for producing orthonormal bases. It is used in numerical linear algebra (QR factorization), in proofs of spectral theorems, and in constructing orthogonal polynomials. The process requires positive definiteness because one must divide by lengths.

# Examples

**Example 1** (Exercise 4.7, p. 262): Apply Gram-Schmidt to the basis (1,1,0)^t, (1,0,1)^t, (0,1,1)^t of R^3 with dot product.

# Relationships

## Builds Upon
- **Orthogonal projection** — Used at each step
- **Positive definite form** — Required for normalization

## Enables
- **Orthonormal basis** — The output of the process

# Common Errors

- **Error**: Forgetting to normalize at each step
  **Correction**: After subtracting the projection, the resulting vector must be divided by its length

# Common Confusions

- **Confusion**: Thinking Gram-Schmidt works for indefinite forms
  **Clarification**: The normalization step requires (v, v) > 0, which is guaranteed only for positive definite forms

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, page 255.

# Verification Notes

- Definition source: Direct from p. 255
- Confidence rationale: Explicitly described as a procedure
- Uncertainties: None
- Cross-reference status: Verified
