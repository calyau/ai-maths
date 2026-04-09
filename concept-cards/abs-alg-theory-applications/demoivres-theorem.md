---
# === CORE IDENTIFICATION ===
concept: DeMoivre's Theorem
slug: demoivres-theorem

# === CLASSIFICATION ===
category: cyclic-groups
subcategory: complex-numbers
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cyclic Groups"
chapter_number: 4
pdf_page: 65
section: "Multiplicative Group of Complex Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "De Moivre's Theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polar-form-complex-number
  - mathematical-induction
extends: []
related:
  - roots-of-unity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

DeMoivre's Theorem states that $[r\operatorname{cis}\theta]^n = r^n\operatorname{cis}(n\theta)$ for any positive integer $n$. It provides a simple formula for computing powers of complex numbers in polar form.

# Core Definition

**Theorem 4.22 (DeMoivre)**: "Let $z = r\operatorname{cis}\theta$ be a nonzero complex number. Then $[r\operatorname{cis}\theta]^n = r^n\operatorname{cis}(n\theta)$ for $n = 1, 2, \ldots$" (Judson, p. 65). Proved by induction using the angle addition formula for $\cos$ and $\sin$.

# Prerequisites

- **Polar form of a complex number** — Theorem uses polar representation
- **Mathematical induction** — Proof technique

# Key Properties

1. Raises modulus to the $n$th power
2. Multiplies argument by $n$
3. Simplifies computation of high powers of complex numbers
4. Foundation for finding $n$th roots of unity

# Construction / Recognition

## To Compute $z^n$ Using DeMoivre's Theorem:
1. Convert $z$ to polar form: $z = r\operatorname{cis}\theta$
2. Apply the formula: $z^n = r^n\operatorname{cis}(n\theta)$
3. Convert back to rectangular form if needed

# Context & Application

DeMoivre's Theorem is essential for finding the $n$th roots of unity, which form cyclic subgroups of $\mathbb{C}^*$. It dramatically simplifies computations that would be intractable in rectangular form.

# Examples

**Example 1** (p. 65): Compute $(1 + i)^{10}$. Convert: $1 + i = \sqrt{2}\operatorname{cis}(\pi/4)$. Apply: $(1+i)^{10} = (\sqrt{2})^{10}\operatorname{cis}(10\pi/4) = 32\operatorname{cis}(5\pi/2) = 32\operatorname{cis}(\pi/2) = 32i$.

# Relationships

## Builds Upon
- **polar-form-complex-number** — Uses polar representation

## Enables
- **roots-of-unity** — Finding all $n$th roots of unity

# Common Errors

- **Error**: Forgetting to reduce the angle modulo $2\pi$
  **Correction**: $\operatorname{cis}(n\theta)$ should be reduced to $[0, 2\pi)$

# Source Reference

Chapter 4: Cyclic Groups, Section 4.2, Theorem 4.22, pages 65-66.

# Verification Notes

- Definition source: Direct quote from Theorem 4.22, p. 65
- Confidence: HIGH — explicit theorem with proof by induction
- Cross-reference status: Verified
- Uncertainties: None
