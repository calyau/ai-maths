---
# === CORE IDENTIFICATION ===
concept: Semisimplicity and Complexification
slug: semisimplicity-and-complexification

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
  - cartan-criterion-semisimplicity
extends: []
related:
  - compact-real-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is a real Lie algebra semisimple iff its complexification is?"
---

# Quick Definition

A real Lie algebra $\mathfrak{g}$ is semisimple if and only if its complexification $\mathfrak{g}^{\mathbb{C}}$ is semisimple. However, this equivalence fails for simplicity: a simple real algebra can have a non-simple complexification.

# Core Definition

**Proposition 6.40** (Kirillov, p. 76): Let $\mathfrak{g}$ be a real Lie algebra. Then $\mathfrak{g}$ is semisimple iff $\mathfrak{g}^{\mathbb{C}}$ is semisimple.

**Remark 6.41**: This fails for "simple": there exist simple real Lie algebras $\mathfrak{g}$ such that $\mathfrak{g}^{\mathbb{C}}$ is a direct sum of two simple algebras.

# Prerequisites

- **Semisimple Lie algebra** — The property being studied
- **Cartan criterion (semisimplicity)** — The proof is immediate from this criterion

# Key Properties

1. The Killing form of $\mathfrak{g}^{\mathbb{C}}$ is the complexification of $K^{\mathfrak{g}}$
2. Non-degeneracy is preserved by complexification
3. Simplicity does NOT transfer: real simple can complexify to non-simple

# Context & Application

This result allows one to study real semisimple algebras by first complexifying and using the richer structure of complex semisimple algebras. The classification of real semisimple algebras proceeds by classifying complex ones first, then finding real forms.

# Examples

**Remark 6.41** (p. 76): $\mathfrak{sl}(2, \mathbb{R})$ is simple, and $\mathfrak{sl}(2, \mathbb{R})^{\mathbb{C}} = \mathfrak{sl}(2, \mathbb{C})$ is also simple. But there exist real simple algebras whose complexification splits.

# Relationships

## Builds Upon
- **Cartan criterion (semisimplicity)** — Proof is immediate

## Related
- **Compact real form** — A key real form of any complex semisimple algebra

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.7, page 76. Proposition 6.40, Remark 6.41.

# Verification Notes

- Definition source: Direct from Proposition 6.40
- Confidence rationale: Explicit proposition with proof
- Uncertainties: None
- Cross-reference status: Verified
