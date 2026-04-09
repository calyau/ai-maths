---
# === CORE IDENTIFICATION ===
concept: Existence of Cartan Subalgebras
slug: existence-of-cartan-subalgebra

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - maximal-toroidal-subalgebra
  - existence-of-semisimple-elements
extends: []
related:
  - cartan-subalgebra
  - cartan-conjugacy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does every semisimple complex Lie algebra have a Cartan subalgebra?"
---

# Quick Definition

Every complex semisimple Lie algebra contains a Cartan subalgebra. This follows from the existence of semisimple elements (Corollary 7.4), which can be extended to maximal toroidal subalgebras, which are automatically Cartan (Theorem 7.11).

# Core Definition

**Corollary 7.12** (Kirillov, p. 85): In every complex semisimple Lie algebra $\mathfrak{g}$, there exists a Cartan subalgebra.

# Prerequisites

- **Maximal toroidal subalgebra** — Every maximal toroidal is Cartan
- **Existence of semisimple elements** — Semisimple elements exist, giving toroidal subalgebras

# Key Properties

1. Start with a nonzero semisimple element (exists by Corollary 7.4)
2. Extend to a maximal toroidal subalgebra (by Zorn's lemma or finite-dimensionality)
3. Apply Theorem 7.11: maximal toroidal = Cartan

# Context & Application

This existence result, combined with conjugacy (Theorem 7.13), ensures the root decomposition can always be formed and is essentially unique.

# Relationships

## Builds Upon
- **Maximal toroidal subalgebra** — Proves it is Cartan

## Enables
- **Root decomposition** — Requires a Cartan subalgebra

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.2, page 85. Corollary 7.12.

# Verification Notes

- Definition source: Direct from Corollary 7.12
- Confidence rationale: Immediate corollary of Theorem 7.11
- Uncertainties: None
- Cross-reference status: Verified
