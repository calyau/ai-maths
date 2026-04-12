---
# === CORE IDENTIFICATION ===
concept: Hermitian Space
slug: hermitian-space

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
section: "8.5 Euclidean Spaces and Hermitian Spaces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - positive-definite-form
  - hermitian-form
extends: []
related:
  - euclidean-space
  - unitary-group
contrasts_with:
  - euclidean-space

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Hermitian space?"
---

# Quick Definition

A Hermitian space is a complex vector space equipped with a positive definite Hermitian form. The standard example is C^n with the form X*Y.

# Core Definition

A complex vector space together with a positive definite Hermitian form is called a Hermitian space (Artin, p. 256). The standard Hermitian space is C^n with the form (X, Y) = X*Y. An orthonormal basis for any Hermitian space refers it back to the standard Hermitian space, and changes of orthonormal bases are given by unitary matrices.

# Prerequisites

- **Positive definite form** — Defines the geometry
- **Hermitian form** — The form must be Hermitian

# Key Properties

1. For any subspace W, V = W direct-sum W^perp (Corollary 8.5.1)
2. Orthonormal bases always exist
3. Changes of orthonormal bases are given by unitary matrices
4. The standard Hermitian space is C^n with X*Y
5. Provides the setting for the spectral theorem for normal, Hermitian, and unitary operators

# Construction / Recognition

## To Construct:
1. Take a complex vector space V
2. Choose a positive definite Hermitian form

## To Recognize:
1. A complex vector space with a positive definite Hermitian form

# Context & Application

Hermitian spaces are the complex analogue of Euclidean spaces. They are the natural setting for quantum mechanics, the spectral theorem for normal operators, and unitary representation theory.

# Examples

**Example 1** (p. 256): C^n with the form X*Y is the standard Hermitian space.

# Relationships

## Builds Upon
- **Hermitian form** — Provides the form
- **Positive definite form** — The form must be positive definite

## Enables
- **Spectral theorem for normal operators** — Proved on Hermitian spaces
- **Unitary operator** — Preserves the form on a Hermitian space

## Contrasts With
- **Euclidean space** — The real analogue

# Common Errors

- **Error**: Using transpose instead of conjugate transpose in a Hermitian space
  **Correction**: In a Hermitian space, the adjoint is A*, not A^t

# Common Confusions

- **Confusion**: Thinking a Hermitian space is the same as a space with a Hermitian form
  **Clarification**: A Hermitian space requires the form to be positive definite; a Hermitian form can be indefinite

# Source Reference

Chapter 8: Bilinear Forms, Section 8.5, pages 256-257.

# Verification Notes

- Definition source: Direct from p. 256
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
