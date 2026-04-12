---
# === CORE IDENTIFICATION ===
concept: Nullspace of a Form
slug: nullspace-of-a-form

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
  - "radical"
  - "null space"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonality-bilinear-forms
extends: []
related:
  - non-degenerate-form
  - orthogonal-complement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the nullspace (radical) of a bilinear form?"
---

# Quick Definition

The nullspace N of a form is the set of null vectors — vectors orthogonal to every vector in V. It equals V^perp, the orthogonal complement of the entire space. The form is nondegenerate if and only if N = {0}.

# Core Definition

A null vector v in V is a vector orthogonal to every vector in V: (v, w) = 0 for all w. The nullspace N is the set of all null vectors, which equals V^perp (Artin, p. 248). By Proposition 8.4.4, v is a null vector if and only if its coordinate vector Y solves AY = 0.

# Prerequisites

- **Orthogonality (bilinear forms)** — Null vectors are orthogonal to all of V

# Key Properties

1. N = V^perp = {v | (v, w) = 0 for all w in V}
2. N is always a subspace
3. N = {0} iff the form is nondegenerate
4. N = ker A where A is the matrix of the form
5. dim N = n - rank A

# Construction / Recognition

## To Construct:
1. Form the matrix A of the form
2. Solve AY = 0 — the solution space is the nullspace

## To Recognize:
1. A vector is in the nullspace if it gives 0 when paired with any vector

# Context & Application

The nullspace measures how "degenerate" a form is. It is the kernel of the associated linear map v -> (v, -). Quotienting by the nullspace yields a nondegenerate form on V/N.

# Examples

**Example 1** (p. 248): Dot product on R^n has nullspace {0} — it is nondegenerate.

**Example 2**: The form with matrix [[1,0],[0,0]] on R^2 has nullspace spanned by (0,1)^t.

# Relationships

## Builds Upon
- **Orthogonality (bilinear forms)** — Null vectors are defined via orthogonality

## Enables
- **Non-degenerate form** — The form is nondegenerate iff N = {0}

## Related
- **Orthogonal complement** — N = V^perp

# Common Errors

- **Error**: Confusing the nullspace of the form with the nullspace of a linear operator
  **Correction**: The nullspace of a form is V^perp; it coincides with ker A only because (v,w) = X*AY

# Common Confusions

- **Confusion**: Thinking a null vector must be the zero vector
  **Clarification**: In degenerate forms, nonzero null vectors exist

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, page 248. Proposition 8.4.4.

# Verification Notes

- Definition source: Direct from p. 248
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
