---
# === CORE IDENTIFICATION ===
concept: Lorentz Form
slug: lorentz-form

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
aliases:
  - "Minkowski form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - indefinite-form
extends:
  - symmetric-bilinear-form
related:
  - lorentz-group
  - signature
contrasts_with:
  - positive-definite-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Lorentz form?"
---

# Quick Definition

The Lorentz form on R^4 is the indefinite symmetric form (X, Y) = x_1 y_1 + x_2 y_2 + x_3 y_3 - x_4 y_4, where x_4 is the time coordinate. It has signature (3, 1) and its matrix is diag(1, 1, 1, -1).

# Core Definition

The Lorentz form is the symmetric bilinear form on "space-time" R^4 defined by (X, Y) = x_1 y_1 + x_2 y_2 + x_3 y_3 - x_4 y_4, where x_4 is the "time" coordinate and the speed of light is normalized to 1. Its matrix with respect to the standard basis is I_{3,1} = diag(1, 1, 1, -1) (Artin, (8.2.2), p. 242).

# Prerequisites

- **Indefinite form** — The Lorentz form is the prototypical indefinite form

# Key Properties

1. Symmetric and nondegenerate
2. Indefinite — has signature (3, 1)
3. Matrix is I_{3,1} = diag(1, 1, 1, -1)
4. Vectors with (X, X) = 0 form the "light cone"
5. The Lorentz group O_{3,1} is the group of matrices preserving this form

# Construction / Recognition

## To Construct:
1. Use the matrix diag(1, 1, 1, -1) on R^4

# Context & Application

The Lorentz form defines the geometry of special relativity. Light-like vectors satisfy (X, X) = 0, time-like vectors have (X, X) < 0, and space-like vectors have (X, X) > 0. The Lorentz group preserves this form.

# Examples

**Example 1** (p. 242): The matrix diag(1, 1, 1, -1) with respect to the standard basis of R^4.

# Relationships

## Builds Upon
- **Indefinite form** — The Lorentz form is indefinite

## Enables
- **Lorentz group** — The group preserving this form

## Contrasts With
- **Positive definite form** — Dot product is positive definite; Lorentz form is not

# Source Reference

Chapter 8: Bilinear Forms, Section 8.2, page 242. Also Section 9.1 for the Lorentz group.

# Verification Notes

- Definition source: Direct from (8.2.2), p. 242
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
