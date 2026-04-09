---
# === CORE IDENTIFICATION ===
concept: Reductive Lie Algebra
slug: reductive-lie-algebra

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
pdf_page: 72
section: "6.4. The radical. Semisimple and reductive algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - radical
  - semisimple-lie-algebra
extends:
  - semisimple-lie-algebra
related:
  - trace-form
  - killing-form
contrasts_with:
  - semisimple-lie-algebra
  - solvable-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reductive Lie algebra?"
  - "What distinguishes a semisimple Lie algebra from a reductive one?"
---

# Quick Definition

A reductive Lie algebra is one whose radical equals its center: $\operatorname{rad}(\mathfrak{g}) = \mathfrak{z}(\mathfrak{g})$. Equivalently, it is a direct sum of a semisimple algebra and an abelian algebra. Reductive algebras have well-behaved representation theory.

# Core Definition

**Definition 6.28** (Kirillov, p. 72): A Lie algebra is called reductive if $\operatorname{rad}(\mathfrak{g}) = \mathfrak{z}(\mathfrak{g})$, i.e., if $\mathfrak{g}/\mathfrak{z}(\mathfrak{g})$ is semisimple.

**Theorem 6.61** (p. 81): Any reductive Lie algebra can be written as $\mathfrak{g} = \mathfrak{z} \oplus \mathfrak{g}_{ss}$ with $\mathfrak{z}$ commutative and $\mathfrak{g}_{ss}$ semisimple.

# Prerequisites

- **Radical** — Reductivity is characterized by the radical equaling the center
- **Semisimple Lie algebra** — The quotient by the center must be semisimple

# Key Properties

1. Every semisimple algebra is reductive (with $\mathfrak{z} = 0$)
2. $\mathfrak{g} = \mathfrak{z} \oplus \mathfrak{g}_{ss}$ as Lie algebras (Theorem 6.61)
3. The condition $[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})] = 0$ characterizes reductivity
4. If $V$ is a representation with non-degenerate trace form $B_V$, then $\mathfrak{g}$ is reductive (Theorem 6.32)

# Construction / Recognition

## To Identify/Recognize:
1. Compute $\operatorname{rad}(\mathfrak{g})$ and $\mathfrak{z}(\mathfrak{g})$
2. Check if they coincide
3. Alternatively, find a faithful representation with non-degenerate trace form

# Context & Application

Reductive algebras occupy the middle ground between semisimple and general algebras. They have clean representation theory because their radical acts by scalars (Theorem 6.27). The classical algebras $\mathfrak{gl}(n)$ and $\mathfrak{u}(n)$ are reductive but not semisimple.

# Examples

**Theorem 6.33** (p. 74): $\mathfrak{gl}(n, \mathbb{K}) = \mathbb{K} \cdot \operatorname{id} \oplus \mathfrak{sl}(n, \mathbb{K})$ is reductive with one-dimensional center. Similarly, $\mathfrak{u}(n) = i\mathbb{R} \cdot \operatorname{id} \oplus \mathfrak{su}(n)$.

# Relationships

## Builds Upon
- **Semisimple Lie algebra** — Quotient $\mathfrak{g}/\mathfrak{z}(\mathfrak{g})$ is semisimple

## Related
- **Trace form** — Non-degeneracy of the trace form implies reductivity

## Contrasts With
- **Semisimple Lie algebra** — Semisimple requires $\mathfrak{z} = 0$; reductive allows a center
- **Solvable Lie algebra** — A solvable algebra is reductive only if it is abelian

# Common Confusions

- **Confusion**: Thinking reductive and semisimple are the same
  **Clarification**: Reductive allows an abelian center; $\mathfrak{gl}(n)$ is reductive but not semisimple

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, pages 72-73. Definition 6.28, Theorem 6.32, Theorem 6.61.

# Verification Notes

- Definition source: Direct from Definition 6.28
- Confidence rationale: Explicitly defined with characterization theorems
- Uncertainties: None
- Cross-reference status: Verified
