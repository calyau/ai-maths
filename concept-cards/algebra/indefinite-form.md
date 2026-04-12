---
# === CORE IDENTIFICATION ===
concept: Indefinite Form
slug: indefinite-form

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
section: "8.2 Symmetric Forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetric-bilinear-form
extends:
  - symmetric-bilinear-form
related:
  - lorentz-form
  - signature
contrasts_with:
  - positive-definite-form
  - negative-definite-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an indefinite form?"
---

# Quick Definition

A symmetric form that is not positive definite is called indefinite. In an indefinite form, (v, v) can be positive for some vectors and negative for others.

# Core Definition

A symmetric form that is not positive definite is called indefinite (Artin, p. 242). More precisely, an indefinite form has signature (p, m) with both p > 0 and m > 0, meaning there exist vectors v with (v, v) > 0 and vectors w with (w, w) < 0.

# Prerequisites

- **Symmetric bilinear form** — Indefiniteness is a classification of symmetric forms

# Key Properties

1. There exist nonzero vectors v with (v, v) > 0 and nonzero vectors w with (w, w) < 0
2. The matrix has both positive and negative eigenvalues
3. A nonzero vector v may be self-orthogonal: (v, v) = 0
4. The signature (p, m) has both p and m positive

# Construction / Recognition

## To Construct:
1. Use a diagonal matrix with both positive and negative entries, e.g., diag(1, 1, 1, -1)

## To Recognize:
1. Find eigenvalues of the matrix — check for both positive and negative eigenvalues
2. Check determinant and trace: if the signs of eigenvalues differ, the form is indefinite

# Context & Application

The Lorentz form in special relativity is the most important example of an indefinite form. Indefinite forms appear in number theory (representation of integers by quadratic forms), relativity, and the classification of conics and quadrics.

# Examples

**Example 1** (p. 242): The Lorentz form x_1 y_1 + x_2 y_2 + x_3 y_3 - x_4 y_4 on R^4 is an indefinite symmetric form with signature (3, 1).

# Relationships

## Builds Upon
- **Symmetric bilinear form** — Indefiniteness is a property of symmetric forms

## Related
- **Lorentz form** — The canonical example of an indefinite form
- **Signature** — Classifies indefinite forms by their type (p, m)

## Contrasts With
- **Positive definite form** — All (v, v) > 0 for nonzero v
- **Negative definite form** — All (v, v) < 0 for nonzero v

# Common Errors

- **Error**: Assuming orthogonality in an indefinite form behaves like in a positive definite form
  **Correction**: In indefinite forms, a nonzero vector can be orthogonal to itself, which cannot happen in a positive definite form

# Common Confusions

- **Confusion**: Thinking "indefinite" means the form is degenerate
  **Clarification**: Indefinite forms can be nondegenerate (e.g., the Lorentz form has an invertible matrix)

# Source Reference

Chapter 8: Bilinear Forms, Section 8.2, page 242.

# Verification Notes

- Definition source: Direct from p. 242
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
