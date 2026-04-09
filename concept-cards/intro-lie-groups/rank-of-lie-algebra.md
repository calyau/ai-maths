---
# === CORE IDENTIFICATION ===
concept: Rank of a Lie Algebra
slug: rank-of-lie-algebra

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 85
section: "7.2. Cartan subalgebra"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rank(g)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartan-subalgebra
  - cartan-conjugacy
extends: []
related:
  - root-decomposition
  - rank-of-root-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rank of a semisimple Lie algebra?"
---

# Quick Definition

The rank of a semisimple Lie algebra $\mathfrak{g}$ is the dimension of any Cartan subalgebra: $\operatorname{rank}(\mathfrak{g}) = \dim \mathfrak{h}$. This is well-defined because all Cartan subalgebras are conjugate and hence have the same dimension.

# Core Definition

**Corollary 7.14** (Kirillov, p. 85): Any two Cartan subalgebras in $\mathfrak{g}$ have the same dimension. This dimension is called the rank of $\mathfrak{g}$:

$$\operatorname{rank}(\mathfrak{g}) = \dim \mathfrak{h}.$$

# Prerequisites

- **Cartan subalgebra** — The rank is defined as its dimension
- **Cartan conjugacy** — Ensures the definition is independent of the choice of $\mathfrak{h}$

# Key Properties

1. Well-defined by Cartan conjugacy (Theorem 7.13)
2. Equals the rank of the associated root system
3. Equals the dimension of any maximal toroidal subalgebra

# Examples

**Example 7.15** (p. 85): $\operatorname{rank}(\mathfrak{sl}(n, \mathbb{C})) = n - 1$.

# Relationships

## Builds Upon
- **Cartan subalgebra** — Rank = dim of Cartan subalgebra

## Related
- **Rank of root system** — Coincides with the Lie algebra rank

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.2, page 85. Corollary 7.14, Example 7.15.

# Verification Notes

- Definition source: Direct from Corollary 7.14
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
