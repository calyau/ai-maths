---
# === CORE IDENTIFICATION ===
concept: Invariant Bilinear Forms on Low-Dimensional Algebras
slug: invariant-bilinear-form-examples

# === CLASSIFICATION ===
category: lie-algebras
subcategory: examples
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 35
section: "3.10"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - so-3-r-lie-algebra
  - su-2-lie-algebra
  - sl-2-c-lie-algebra
  - adjoint-action-on-lie-algebra
extends: []
related:
  - invariant-bilinear-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

Each of $\mathfrak{so}(3, \mathbb{R})$, $\mathfrak{su}(2)$, $\mathfrak{sl}(2, \mathbb{C})$ has a canonical $\mathrm{Ad}$-invariant symmetric bilinear form defined by $(x, y) = -\mathrm{tr}(xy)$. For compact algebras ($\mathfrak{so}(3)$, $\mathfrak{su}(2)$), this form is positive definite.

# Core Definition

**Section 3.10, "Invariant bilinear form"** (Kirillov):

- $\mathfrak{so}(3, \mathbb{R})$: $(x, y) = \mathrm{tr}(xy^t)$. Elements $J_x, J_y, J_z$ are orthogonal, $(J_k, J_k) = 2$.
- $\mathfrak{su}(2)$: $(x, y) = \mathrm{tr}(x\bar{y}^t)$. Elements $i\sigma_k$ are orthogonal, $(i\sigma_k, i\sigma_k) = 2$.
- $\mathfrak{sl}(2, \mathbb{C})$: $(h, h) = -2$, $(e, f) = (f, e) = -1$, all other pairings zero.

# Prerequisites

- **$\mathfrak{so}(3, \mathbb{R})$**, **$\mathfrak{su}(2)$**, **$\mathfrak{sl}(2, \mathbb{C})$** — the algebras
- **Adjoint representation (Ad)** — the invariance condition

# Key Properties

1. For compact algebras, the form is positive definite (negative of the Killing form).
2. The form for $\mathfrak{sl}(2, \mathbb{C})$ is non-degenerate but indefinite.
3. All are proportional to the Killing form $B(x, y) = \mathrm{tr}(\mathrm{ad}\, x \circ \mathrm{ad}\, y)$.
4. Exercise 2.11 proves invariance for $\mathfrak{su}(2)$.

# Construction / Recognition

## To Construct/Create:
1. Define $(x, y) = -\mathrm{tr}(xy)$ (or a scalar multiple).
2. Verify Ad-invariance.

## To Identify/Recognize:
1. A bilinear form preserved by the adjoint action.

# Context & Application

These are concrete instances of the Killing form, which is the primary tool for classifying semisimple Lie algebras. The positive definiteness for compact forms is the basis of Weyl's unitary trick.

# Examples

**Example** (p. 35): For $\mathfrak{so}(3, \mathbb{R})$: $(J_x, J_x) = -\mathrm{tr}(J_x^2) = -\mathrm{tr}\begin{pmatrix}0&0&0\\0&-1&0\\0&0&-1\end{pmatrix} = 2$.

# Relationships

## Builds Upon
- **The three example algebras** — the algebras on which forms are defined

## Enables
- **Killing form** — these are proportional to the Killing form
- **Casimir element** — constructed from the dual of the invariant form

## Related
- **Invariant bilinear form** — the general concept

# Common Errors

- **Error**: Using $(x, y) = \mathrm{tr}(xy)$ instead of $-\mathrm{tr}(xy)$.
  **Correction**: The minus sign ensures positive definiteness for compact algebras.

# Common Confusions

- **Confusion**: Whether the form on $\mathfrak{sl}(2, \mathbb{C})$ is positive definite.
  **Clarification**: No, $(h, h) = -2 < 0$. Only the compact real form $\mathfrak{su}(2)$ has a positive definite invariant form.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.10, "Invariant bilinear form," page 35.

# Verification Notes

- Definition source: Direct from Section 3.10
- Confidence rationale: Explicit formulas for all three algebras
- Uncertainties: None
- Cross-reference status: Verified with Exercise 2.11
