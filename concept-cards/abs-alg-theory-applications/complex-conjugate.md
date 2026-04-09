---
# === CORE IDENTIFICATION ===
concept: Complex Conjugate
slug: complex-conjugate

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
  - conjugate

# === TYPED RELATIONSHIPS ===
prerequisites:
  - complex-number
extends: []
related:
  - modulus-complex-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

The complex conjugate of $z = a + bi$ is $\overline{z} = a - bi$, obtained by negating the imaginary part.

# Core Definition

"The complex conjugate of a complex number $z = a + bi$ is defined to be $\overline{z} = a - bi$" (Judson, p. 62).

# Prerequisites

- **Complex number** — Conjugation operates on complex numbers

# Key Properties

1. $\overline{z} = a - bi$ when $z = a + bi$
2. $z \overline{z} = a^2 + b^2 = |z|^2$
3. $z^{-1} = \overline{z}/|z|^2$
4. $\overline{\overline{z}} = z$

# Examples

**Example 1** (p. 63): If $z = 2 + 3i$, then $\overline{z} = 2 - 3i$.

# Relationships

## Builds Upon
- **complex-number** — Defined for complex numbers

## Related
- **modulus-complex-number** — $|z|^2 = z\overline{z}$

# Source Reference

Chapter 4: Cyclic Groups, Section 4.2, page 62.

# Verification Notes

- Definition source: Direct quote from p. 62
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
