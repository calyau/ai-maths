---
# === CORE IDENTIFICATION ===
concept: Orthogonality (Bilinear Forms)
slug: orthogonality-bilinear-forms

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
  - "orthogonality"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bilinear-form
  - symmetric-bilinear-form
extends: []
related:
  - orthogonal-complement
  - non-degenerate-form
  - orthogonal-basis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does orthogonal mean for a general bilinear form?"
---

# Quick Definition

Two vectors v and w are orthogonal (written v _|_ w) with respect to a symmetric or Hermitian form if (v, w) = 0. This generalizes the familiar notion from dot product to arbitrary forms.

# Core Definition

Given a symmetric or Hermitian form on V, two vectors v and w are orthogonal (written v _|_ w) if (v, w) = 0 (Artin, p. 247). Note v _|_ w if and only if w _|_ v. When the form is indefinite, a nonzero vector may be self-orthogonal: (v, v) = 0.

# Prerequisites

- **Bilinear form** — Orthogonality is defined in terms of a form
- **Symmetric bilinear form** — The form must be symmetric or Hermitian for orthogonality to be symmetric

# Key Properties

1. v _|_ w if and only if (v, w) = 0
2. Orthogonality is symmetric: v _|_ w iff w _|_ v
3. In indefinite forms, nonzero vectors can be self-orthogonal
4. It is best to work algebraically with the definition rather than seek geometric intuition for indefinite forms (Artin, p. 247)

# Construction / Recognition

## To Recognize:
1. Compute (v, w) using the form
2. v and w are orthogonal if the result is 0

# Context & Application

Orthogonality with respect to general forms is the central tool for decomposing vector spaces. The orthogonal complement W^perp of a subspace W plays the same structural role as in Euclidean geometry but with subtleties: W and W^perp may overlap when the form is degenerate on W.

# Examples

**Example 1** (p. 247): With dot product on R^3, (1,0,0) _|_ (0,1,0) since their dot product is 0.

**Example 2** (p. 247): With the Lorentz form, the vector (1,0,0,1) is self-orthogonal: 1^2 + 0 + 0 - 1^2 = 0.

# Relationships

## Builds Upon
- **Symmetric bilinear form** — Orthogonality requires a symmetric or Hermitian form

## Enables
- **Orthogonal complement** — The set of all vectors orthogonal to a subspace
- **Orthogonal basis** — A basis of mutually orthogonal vectors
- **Non-degenerate form** — Characterized by the nullspace (set of vectors orthogonal to everything)

# Common Errors

- **Error**: Assuming orthogonal vectors cannot be zero or self-orthogonal
  **Correction**: In indefinite forms, nonzero self-orthogonal vectors exist

# Common Confusions

- **Confusion**: Thinking orthogonality means "perpendicular" in a visual sense for indefinite forms
  **Clarification**: For indefinite forms, orthogonality is purely algebraic — (v, w) = 0 — and may not correspond to any visual notion of perpendicularity

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, pages 247-248.

# Verification Notes

- Definition source: Direct from p. 247
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
