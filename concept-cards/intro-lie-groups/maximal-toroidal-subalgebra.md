---
# === CORE IDENTIFICATION ===
concept: Maximal Toroidal Subalgebra
slug: maximal-toroidal-subalgebra

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
pdf_page: 84
section: "7.2. Cartan subalgebra"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "maximal toral subalgebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - toroidal-subalgebra
extends:
  - toroidal-subalgebra
related:
  - cartan-subalgebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does a maximal toroidal subalgebra equal a Cartan subalgebra?"
---

# Quick Definition

A maximal toroidal subalgebra is a toroidal subalgebra not properly contained in any larger toroidal subalgebra. Theorem 7.11 proves that every maximal toroidal subalgebra is automatically a Cartan subalgebra (equals its centralizer).

# Core Definition

**Theorem 7.11** (Kirillov, p. 84): Let $\mathfrak{h} \subset \mathfrak{g}$ be a maximal toroidal subalgebra. Then $\mathfrak{h}$ is a Cartan subalgebra.

# Prerequisites

- **Toroidal subalgebra** — A maximal one is sought

# Key Properties

1. The proof proceeds in four steps:
   - Step 1: Jordan decomposition preserves the centralizer $C(\mathfrak{h})$
   - Step 2: $C(\mathfrak{h})$ is reductive (trace form = Killing form is non-degenerate on $C(\mathfrak{h})$)
   - Step 3: $C(\mathfrak{h})$ is commutative (otherwise could extend $\mathfrak{h}$)
   - Step 4: $C(\mathfrak{h})$ contains no nonzero nilpotent elements (Killing form argument)
2. Therefore $C(\mathfrak{h})$ consists entirely of semisimple elements, so $C(\mathfrak{h})$ is toroidal, and by maximality $C(\mathfrak{h}) = \mathfrak{h}$

# Context & Application

This theorem provides the practical method for constructing Cartan subalgebras: simply find a maximal commutative set of semisimple elements.

# Relationships

## Builds Upon
- **Toroidal subalgebra** — Maximality condition

## Enables
- **Cartan subalgebra** — Proves existence

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.2, pages 84-85. Theorem 7.11.

# Verification Notes

- Definition source: Direct from Theorem 7.11
- Confidence rationale: Major theorem with detailed four-step proof
- Uncertainties: None
- Cross-reference status: Verified
