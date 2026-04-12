---
# === CORE IDENTIFICATION ===
concept: Negative Definite Form
slug: negative-definite-form

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
  - positive-definite-form
  - signature
contrasts_with:
  - positive-definite-form
  - indefinite-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a negative definite form?"
---

# Quick Definition

A symmetric form is negative definite if (v, v) < 0 for every nonzero vector v. Negative definite forms are simply the negatives of positive definite forms.

# Core Definition

A symmetric form on a real vector space is negative definite if (v, v) < 0 for all nonzero vectors v. A symmetric form is negative semi-definite if (v, v) <= 0 for all nonzero vectors (Artin, p. 242).

# Prerequisites

- **Symmetric bilinear form** — Negative definiteness is a property of symmetric forms

# Key Properties

1. (v, v) < 0 for all nonzero v
2. A form is negative definite if and only if its negative is positive definite
3. All eigenvalues of the matrix are negative
4. The signature is (0, n) for an n-dimensional space

# Construction / Recognition

## To Construct:
1. Take any positive definite form and negate it
2. Or use a diagonal matrix with all negative entries

## To Recognize:
1. Check that all eigenvalues of the matrix are negative
2. Or check that -A is positive definite

# Context & Application

Negative definite forms are less commonly encountered than positive definite ones, but arise naturally when studying maxima in optimization and in the classification of forms by signature.

# Examples

**Example 1** (p. 242): The form -(x_1^2 + ... + x_n^2) on R^n is negative definite.

# Relationships

## Builds Upon
- **Symmetric bilinear form** — Negative definiteness is a special case

## Enables
- **Signature** — A negative definite form has signature (0, n)

## Contrasts With
- **Positive definite form** — Has (v, v) > 0 instead
- **Indefinite form** — Has both positive and negative values

# Common Errors

- **Error**: Confusing negative definite with indefinite
  **Correction**: Negative definite means ALL values (v,v) are negative; indefinite means some are positive and some negative

# Common Confusions

- **Confusion**: Thinking a form with some negative diagonal entries is negative definite
  **Clarification**: All eigenvalues must be negative, not just diagonal entries

# Source Reference

Chapter 8: Bilinear Forms, Section 8.2, page 242.

# Verification Notes

- Definition source: Direct from p. 242
- Confidence rationale: Briefly but explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
