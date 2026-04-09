---
# === CORE IDENTIFICATION ===
concept: Complementary Ideal Theorem
slug: complementary-ideal

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
  - killing-form
  - orthogonal-complement
  - cartan-criterion-semisimplicity
extends: []
related:
  - decomposition-into-simples
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does every ideal in a semisimple Lie algebra have a complement?"
---

# Quick Definition

In a semisimple Lie algebra, every ideal has a complementary ideal: if $I$ is an ideal of $\mathfrak{g}$, then $\mathfrak{g} = I \oplus I^\perp$ where $I^\perp$ is the Killing form orthogonal complement. This is a key structural property unique to semisimple algebras.

# Core Definition

**Theorem 6.42** (Kirillov, p. 76): Let $\mathfrak{g}$ be a semisimple Lie algebra and $I \subset \mathfrak{g}$ an ideal. Then there is an ideal $I'$ such that $\mathfrak{g} = I \oplus I'$.

Proof: Take $I' = I^\perp$. Then $I \cap I^\perp$ has zero Killing form, hence is solvable by Cartan's criterion, hence zero by semisimplicity.

# Prerequisites

- **Semisimple Lie algebra** — The theorem requires semisimplicity
- **Killing form** — The complement is the Killing form orthogonal complement
- **Orthogonal complement** — $I^\perp$ is an ideal (Lemma 6.29)
- **Cartan criterion (semisimplicity)** — Used to show $I \cap I^\perp$ is solvable

# Key Properties

1. The complement is unique: $I' = I^\perp$ with respect to the Killing form
2. Both $I$ and $I'$ are ideals, so $[I, I'] = 0$
3. The decomposition is as Lie algebras (not just vector spaces)

# Context & Application

This theorem is the engine behind the decomposition of semisimple algebras into simple summands. Applied iteratively, it produces the direct sum decomposition $\mathfrak{g} = \mathfrak{g}_1 \oplus \cdots \oplus \mathfrak{g}_k$.

# Examples

**Example**: For $\mathfrak{g} = \mathfrak{sl}(2, \mathbb{C}) \oplus \mathfrak{sl}(3, \mathbb{C})$, the ideal $I = \mathfrak{sl}(2, \mathbb{C})$ has complement $I^\perp = \mathfrak{sl}(3, \mathbb{C})$.

# Relationships

## Builds Upon
- **Killing form** — Provides the orthogonal complement

## Enables
- **Decomposition into simples** — Iterative application

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.7, page 76. Theorem 6.42.

# Verification Notes

- Definition source: Direct from Theorem 6.42
- Confidence rationale: Explicit theorem with short proof
- Uncertainties: None
- Cross-reference status: Verified
