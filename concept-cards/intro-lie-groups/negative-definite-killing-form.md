---
# === CORE IDENTIFICATION ===
concept: Negative Definite Killing Form and Compact Groups
slug: negative-definite-killing-form

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 77
section: "6.8. Relation with compact groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - killing-form
  - semisimple-lie-algebra
extends:
  - killing-form
related:
  - compact-real-form
  - reductive-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the sign of the Killing form relate to compactness?"
---

# Quick Definition

For a compact real Lie group $G$, the Killing form on $\mathfrak{g} = \operatorname{Lie}(G)$ is negative semidefinite with kernel equal to the center. Conversely, a semisimple real Lie algebra with negative definite Killing form is the Lie algebra of a compact group.

# Core Definition

**Theorem 6.49** (Kirillov, p. 77): Let $G$ be a compact real Lie group. Then $\mathfrak{g} = \operatorname{Lie}(G)$ is reductive, and the Killing form is negative semidefinite with $\operatorname{Ker} K = \mathfrak{z}(\mathfrak{g})$.

Conversely, a semisimple real Lie algebra with negative definite Killing form is the Lie algebra of a compact Lie group.

# Prerequisites

- **Killing form** — The theorem characterizes the sign of the Killing form
- **Semisimple Lie algebra** — The converse requires semisimplicity

# Key Properties

1. Compactness of $G$ implies every representation is unitary, so trace forms are negative semidefinite
2. Negative definite Killing form implies $\operatorname{Ad}(G) \subset SO(\mathfrak{g})$, hence compact
3. Positive definite Killing form forces $\mathfrak{g} = 0$ (Lemma 6.51)

# Examples

**Example 6.48** (p. 77): For $\mathfrak{u}(n)$: $\operatorname{tr}(xy) = -\operatorname{tr}(x\bar{y}^t)$ and $\operatorname{tr}(x^2) = -\sum |x_{ij}|^2 \leq 0$.

# Relationships

## Builds Upon
- **Killing form** — Characterizes its sign

## Enables
- **Compact real form** — Existence and characterization

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.8, pages 77-78. Example 6.48, Theorem 6.49, Lemma 6.51.

# Verification Notes

- Definition source: Direct from Theorem 6.49
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
