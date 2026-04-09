---
# === CORE IDENTIFICATION ===
concept: Complex Number
slug: complex-number

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - complex-conjugate
  - modulus-complex-number
  - polar-form-complex-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

A complex number is an expression of the form $z = a + bi$ where $a, b \in \mathbb{R}$ and $i^2 = -1$. The nonzero complex numbers $\mathbb{C}^*$ form a group under multiplication.

# Core Definition

"The complex numbers are defined as $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$, where $i^2 = -1$. If $z = a + bi$, then $a$ is the real part of $z$ and $b$ is the imaginary part of $z$" (Judson, p. 62).

Addition: $(a + bi) + (c + di) = (a + c) + (b + d)i$.
Multiplication: $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$.
Inverse: $z^{-1} = \frac{a - bi}{a^2 + b^2}$ for $z = a + bi \neq 0$.

# Prerequisites

- **Set** — $\mathbb{C}$ is a set

# Key Properties

1. Addition and multiplication are defined componentwise (with $i^2 = -1$)
2. Every nonzero complex number has a multiplicative inverse
3. $\mathbb{C}^*$ forms a group under multiplication (Example 3.16)
4. Can be represented in rectangular or polar form
5. $\mathbb{R} \subset \mathbb{C}$ (real numbers are complex numbers with $b = 0$)

# Construction / Recognition

## To Add Complex Numbers:
1. Add real parts: $a + c$
2. Add imaginary parts: $b + d$
3. Result: $(a + c) + (b + d)i$

## To Multiply Complex Numbers:
1. Expand using distributive law
2. Replace $i^2$ with $-1$
3. Result: $(ac - bd) + (ad + bc)i$

# Context & Application

Complex numbers provide important examples of cyclic subgroups (roots of unity) and the circle group. They are essential in the study of group theory through DeMoivre's Theorem and polar representations.

# Examples

**Example 1** (p. 62): If $z = 2 + 3i$ and $w = 1 - 2i$, then $z + w = 3 + i$ and $zw = 8 - i$.

**Example 2** (p. 63): $z^{-1} = \frac{2}{13} - \frac{3}{13}i$, $|z| = \sqrt{13}$, $\overline{z} = 2 - 3i$.

# Relationships

## Enables
- **circle-group** — $\mathbb{T} \subset \mathbb{C}^*$
- **roots-of-unity** — Solutions to $z^n = 1$ in $\mathbb{C}$

## Related
- **polar-form-complex-number** — Alternative representation
- **complex-conjugate** — $\overline{z} = a - bi$
- **modulus-complex-number** — $|z| = \sqrt{a^2 + b^2}$

# Source Reference

Chapter 4: Cyclic Groups, Section 4.2, pages 62-63.

# Verification Notes

- Definition source: Direct quote from p. 62
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
