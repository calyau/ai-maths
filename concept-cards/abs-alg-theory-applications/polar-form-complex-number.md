---
# === CORE IDENTIFICATION ===
concept: Polar Form of a Complex Number
slug: polar-form-complex-number

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
pdf_page: 63
section: "Multiplicative Group of Complex Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - polar representation
  - cis notation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - complex-number
  - modulus-complex-number
extends: []
related:
  - demoivres-theorem
  - roots-of-unity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

The polar form of a nonzero complex number $z = a + bi$ is $z = r(\cos\theta + i\sin\theta) = r\operatorname{cis}\theta$, where $r = |z|$ and $\theta$ is the angle from the positive real axis.

# Core Definition

"Nonzero complex numbers can also be represented using polar coordinates... $z = a + bi = r(\cos\theta + i\sin\theta)$" where $r = |z| = \sqrt{a^2 + b^2}$, $a = r\cos\theta$, and $b = r\sin\theta$ (Judson, p. 64). The abbreviation $r\operatorname{cis}\theta$ is used for $r(\cos\theta + i\sin\theta)$.

**Proposition 4.20**: If $z = r\operatorname{cis}\theta$ and $w = s\operatorname{cis}\phi$, then $zw = rs\operatorname{cis}(\theta + \phi)$.

# Prerequisites

- **Complex number** — Polar form is a representation of complex numbers
- **Modulus of a complex number** — $r = |z|$

# Key Properties

1. $r = |z|$ (modulus), $\theta$ = argument (angle)
2. $a = r\cos\theta$, $b = r\sin\theta$
3. Multiplication: $zw = rs\operatorname{cis}(\theta + \phi)$ — multiply moduli, add angles
4. Representation is unique for $0 \leq \theta < 2\pi$

# Construction / Recognition

## To Convert Rectangular to Polar:
1. Compute $r = \sqrt{a^2 + b^2}$
2. Compute $\theta = \arctan(b/a)$ (adjusting for quadrant)

## To Convert Polar to Rectangular:
1. Compute $a = r\cos\theta$
2. Compute $b = r\sin\theta$

# Context & Application

Polar form simplifies multiplication and exponentiation of complex numbers, making it essential for DeMoivre's Theorem and finding roots of unity.

# Examples

**Example 1** (p. 64): $z = 2\operatorname{cis}60° = 2\cos 60° + 2i\sin 60° = 1 + \sqrt{3}i$.

**Example 2** (p. 64): $3\sqrt{2} - 3\sqrt{2}i = 6\operatorname{cis}315°$.

**Example 3** (p. 65): If $z = 3\operatorname{cis}(\pi/3)$ and $w = 2\operatorname{cis}(\pi/6)$, then $zw = 6\operatorname{cis}(\pi/2) = 6i$.

# Relationships

## Builds Upon
- **complex-number** — Represents complex numbers
- **modulus-complex-number** — $r = |z|$

## Enables
- **demoivres-theorem** — Uses polar form for powers
- **roots-of-unity** — Expressed naturally in polar form

# Common Errors

- **Error**: Forgetting to adjust the angle for the correct quadrant when computing $\theta$
  **Correction**: $\arctan(b/a)$ gives the reference angle; adjust based on the signs of $a$ and $b$

# Source Reference

Chapter 4: Cyclic Groups, Section 4.2, pages 63-65. Proposition 4.20.

# Verification Notes

- Definition source: Direct from p. 64
- Confidence: HIGH — explicit definition with examples
- Cross-reference status: Verified
- Uncertainties: None
