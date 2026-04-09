---
# === CORE IDENTIFICATION ===
concept: Semisimple Algebras are Perfect
slug: semisimple-equals-self-commutant

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 76
section: "6.7. Properties of semisimple Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "[g,g] = g"
  - "perfect Lie algebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
  - simple-lie-algebra
extends: []
related:
  - commutant
  - decomposition-into-simples
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is the commutant of a semisimple Lie algebra equal to itself?"
---

# Quick Definition

If $\mathfrak{g}$ is semisimple, then $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$. This means $\mathfrak{g}$ is a "perfect" Lie algebra: it equals its own commutant. The proof reduces to the simple case where $[\mathfrak{g}, \mathfrak{g}]$ is a nonzero ideal, hence all of $\mathfrak{g}$.

# Core Definition

**Corollary 6.44** (Kirillov, p. 76): If $\mathfrak{g}$ is a semisimple Lie algebra, then $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$.

# Prerequisites

- **Semisimple Lie algebra** — The hypothesis
- **Simple Lie algebra** — Used in the proof (reduce to simple summands)

# Key Properties

1. For simple $\mathfrak{g}$: $[\mathfrak{g}, \mathfrak{g}]$ is a nonzero ideal (since $\mathfrak{g}$ is not abelian), hence $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$
2. For semisimple: apply to each simple summand
3. This means the quotient $\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}] = 0$: semisimple algebras have no abelian quotients

# Relationships

## Builds Upon
- **Decomposition into simples** — Reduces to the simple case

## Related
- **Commutant** — $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$ is maximal

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.7, page 76. Corollary 6.44.

# Verification Notes

- Definition source: Direct from Corollary 6.44
- Confidence rationale: Short corollary with clear proof
- Uncertainties: None
- Cross-reference status: Verified
