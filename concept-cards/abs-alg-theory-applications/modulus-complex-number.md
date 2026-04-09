---
# === CORE IDENTIFICATION ===
concept: Modulus of a Complex Number
slug: modulus-complex-number

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
pdf_page: 62
section: "Multiplicative Group of Complex Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - absolute value of complex number

# === TYPED RELATIONSHIPS ===
prerequisites:
  - complex-number
extends: []
related:
  - complex-conjugate
  - polar-form-complex-number
  - circle-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

The modulus (or absolute value) of a complex number $z = a + bi$ is $|z| = \sqrt{a^2 + b^2}$, representing its distance from the origin in the complex plane.

# Core Definition

"The absolute value or modulus of $z = a + bi$ is $|z| = \sqrt{a^2 + b^2}$" (Judson, p. 62).

# Prerequisites

- **Complex number** — Modulus is defined for complex numbers

# Key Properties

1. $|z| \geq 0$, with $|z| = 0$ iff $z = 0$
2. $|z|^2 = z\overline{z} = a^2 + b^2$
3. $|zw| = |z||w|$
4. In polar form, $|z| = r$

# Examples

**Example 1** (p. 63): If $z = 2 + 3i$, then $|z| = \sqrt{4 + 9} = \sqrt{13}$.

# Relationships

## Builds Upon
- **complex-number** — Modulus is a property of complex numbers

## Enables
- **circle-group** — $\mathbb{T} = \{z \in \mathbb{C} : |z| = 1\}$
- **polar-form-complex-number** — $r = |z|$ in polar form

# Source Reference

Chapter 4: Cyclic Groups, Section 4.2, page 62.

# Verification Notes

- Definition source: Direct quote from p. 62
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
