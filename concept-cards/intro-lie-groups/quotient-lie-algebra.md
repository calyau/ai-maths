---
# === CORE IDENTIFICATION ===
concept: Quotient Lie Algebra
slug: quotient-lie-algebra

# === CLASSIFICATION ===
category: lie-algebras
subcategory: subalgebras-ideals
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 25
section: "3.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "factor algebra"
  - "$\\mathfrak{g}/\\mathfrak{h}$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - ideal-of-lie-algebra
extends: []
related:
  - quotient-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

If $\mathfrak{h}$ is an ideal in $\mathfrak{g}$, the quotient vector space $\mathfrak{g}/\mathfrak{h}$ inherits a Lie algebra structure via $[\bar{x}, \bar{y}] = \overline{[x, y]}$.

# Core Definition

(Kirillov, p. 25): If $\mathfrak{h}$ is an ideal, then $\mathfrak{g}/\mathfrak{h}$ has a canonical structure of a Lie algebra.

**Theorem 3.19**: $\mathrm{Lie}(G/H) = \mathfrak{g}/\mathfrak{h}$ when $H$ is a normal Lie subgroup.

# Prerequisites

- **Lie algebra** — the algebra being quotiented
- **Ideal of Lie algebra** — required for the quotient to be well-defined

# Key Properties

1. The bracket is well-defined because $\mathfrak{h}$ is an ideal.
2. $\dim(\mathfrak{g}/\mathfrak{h}) = \dim \mathfrak{g} - \dim \mathfrak{h}$.
3. The natural projection $\pi: \mathfrak{g} \to \mathfrak{g}/\mathfrak{h}$ is a Lie algebra morphism.

# Construction / Recognition

## To Construct/Create:
1. Verify $\mathfrak{h}$ is an ideal.
2. Form the vector space quotient $\mathfrak{g}/\mathfrak{h}$.
3. Define $[\bar{x}, \bar{y}] = \overline{[x, y]}$ (well-defined since $\mathfrak{h}$ is an ideal).

## To Identify/Recognize:
1. A Lie algebra arising as the tangent space of $G/H$ for a normal subgroup $H$.

# Context & Application

Quotient algebras appear in the structure theory of Lie algebras (e.g., $\mathfrak{g}/\mathrm{rad}(\mathfrak{g})$ is semisimple).

# Examples

**Example**: $\mathfrak{gl}(n)/\mathfrak{sl}(n) \cong \mathbb{R}$ (or $\mathbb{C}$), the one-dimensional abelian algebra.

# Relationships

## Builds Upon
- **Ideal of Lie algebra** — required for the quotient

## Enables
- **Structure theory** — semisimple quotients, solvable radicals

## Related
- **Quotient Lie group** — $\mathrm{Lie}(G/H) = \mathfrak{g}/\mathfrak{h}$

# Common Errors

- **Error**: Attempting to form $\mathfrak{g}/\mathfrak{h}$ when $\mathfrak{h}$ is only a subalgebra, not an ideal.
  **Correction**: The bracket on the quotient is well-defined only when $\mathfrak{h}$ is an ideal.

# Common Confusions

- **Confusion**: Whether $\mathfrak{g}/\mathfrak{h}$ as a vector space always has a Lie algebra structure.
  **Clarification**: Only when $\mathfrak{h}$ is an ideal. If $\mathfrak{h}$ is just a subalgebra, the quotient is only a vector space.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.4, page 25. Theorem 3.19.

# Verification Notes

- Definition source: Synthesized from p. 25 statement and Theorem 3.19
- Confidence rationale: Explicit statement in source
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.19
