---
# === CORE IDENTIFICATION ===
concept: Orthogonal Projection
slug: orthogonal-projection

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-complement
  - non-degenerate-form
extends: []
related:
  - gram-schmidt-process
  - orthogonal-basis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the orthogonal projection formula?"
---

# Quick Definition

The orthogonal projection from V to a subspace W (when the form is nondegenerate on W) is the linear map pi: V -> W that decomposes v = w + u with w in W and u in W^perp. It is given by the projection formula using an orthogonal basis of W.

# Core Definition

Suppose the form is nondegenerate on a subspace W, so V = W direct-sum W^perp. The orthogonal projection pi: V -> W is defined by pi(v) = w where v = w + u with w in W and u in W^perp. The Projection Formula (Theorem 8.4.11): if (w_1, ..., w_k) is an orthogonal basis for W, then pi(v) = w_1 c_1 + ... + w_k c_k where c_i = (w_i, v)/(w_i, w_i).

# Prerequisites

- **Orthogonal complement** — The decomposition V = W + W^perp is needed
- **Non-degenerate form** — Required for the projection to exist

# Key Properties

1. pi(w) = w for w in W; pi(u) = 0 for u in W^perp
2. pi is a linear transformation
3. The projection formula requires an orthogonal basis (Warning: not correct for non-orthogonal bases)
4. When the basis is orthonormal, the formula simplifies to c_i = (w_i, v) (denominators become 1)
5. If the form is nondegenerate on all of V, the projection formula gives coordinates with respect to an orthogonal basis (Corollary 8.4.13)

# Construction / Recognition

## To Compute:
1. Find an orthogonal basis (w_1, ..., w_k) for W
2. Compute c_i = (w_i, v) / (w_i, w_i) for each i
3. pi(v) = w_1 c_1 + ... + w_k c_k

# Context & Application

Orthogonal projection is the workhorse of computational linear algebra. It underlies least squares fitting, the Gram-Schmidt process, and Fourier analysis. The formula extends to infinite-dimensional Hilbert spaces.

# Examples

**Example 1** (p. 252): Let W = span(1, 1, 1)^t in R^3. Then pi(v) = w_1 c_1 where c_1 = (x_1 + x_2 + x_3)/3.

**Example 2** (p. 252): With orthogonal basis (1,1,1)^t, (1,-1,0)^t, (1,1,-2)^t of R^3, the coordinates are c_1 = (x_1+x_2+x_3)/3, c_2 = (x_1-x_2)/2, c_3 = (x_1+x_2-2x_3)/6.

# Relationships

## Builds Upon
- **Orthogonal complement** — Projection decomposes along W and W^perp
- **Non-degenerate form** — Required for the decomposition to exist

## Enables
- **Gram-Schmidt process** — Uses iterated projections to orthogonalize

## Related
- **Orthogonal basis** — Required for the projection formula

# Common Errors

- **Error**: Using the projection formula with a non-orthogonal basis
  **Correction**: The projection formula is only correct for orthogonal bases (Artin, p. 252)

# Common Confusions

- **Confusion**: Thinking orthogonal projection exists whenever W is a subspace
  **Clarification**: The form must be nondegenerate on W; otherwise W intersect W^perp is nonzero and the projection is undefined

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, pages 251-253. Theorem 8.4.11.

# Verification Notes

- Definition source: Direct from Theorem 8.4.11
- Confidence rationale: Explicitly stated with formula and examples
- Uncertainties: None
- Cross-reference status: Verified
