---
# === CORE IDENTIFICATION ===
concept: Semisimplicity of Classical Lie Algebras
slug: semisimplicity-of-classical-algebras

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
pdf_page: 74
section: "6.5. Invariant bilinear forms and semisimplicity of classical Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - trace-form
  - reductive-lie-algebra
  - semisimple-lie-algebra
extends:
  - trace-form
related:
  - killing-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which classical Lie algebras are semisimple?"
  - "How do I prove a classical Lie algebra is semisimple?"
---

# Quick Definition

The classical Lie algebras $\mathfrak{sl}(n)$, $\mathfrak{so}(n)$ ($n > 2$), $\mathfrak{su}(n)$, and $\mathfrak{sp}(2n)$ are all semisimple, while $\mathfrak{gl}(n)$ and $\mathfrak{u}(n)$ are reductive with one-dimensional center. This is proved via non-degeneracy of the trace form in the defining representation.

# Core Definition

**Theorem 6.33** (Kirillov, p. 74): All classical Lie algebras of Section 2.5 are reductive. Algebras $\mathfrak{sl}(n, \mathbb{K})$, $\mathfrak{so}(n, \mathbb{K})$ ($n > 2$), $\mathfrak{su}(n)$, $\mathfrak{sp}(2n, \mathbb{K})$ are semisimple; algebras $\mathfrak{gl}(n, \mathbb{K})$ and $\mathfrak{u}(n)$ have one-dimensional center: $\mathfrak{gl}(n, \mathbb{K}) = \mathbb{K} \cdot \operatorname{id} \oplus \mathfrak{sl}(n, \mathbb{K})$, $\mathfrak{u}(n) = i\mathbb{R} \cdot \operatorname{id} \oplus \mathfrak{su}(n)$.

# Prerequisites

- **Trace form** — The proof uses non-degeneracy of $B_V(x,y) = \operatorname{tr}(xy)$
- **Reductive Lie algebra** — Non-degenerate trace form implies reductivity
- **Semisimple Lie algebra** — Reductive with zero center implies semisimple

# Key Properties

1. For $\mathfrak{gl}(n)$: $B(x,y) = \sum x_{ij}y_{ji}$ is non-degenerate
2. For $\mathfrak{so}(n)$: $B(x,y) = -2\sum_{i>j} x_{ij}y_{ij}$ is non-degenerate
3. For $\mathfrak{u}(n)$: $B(x,y) = -\sum |x_{ij}|^2$ is negative definite
4. For $\mathfrak{su}(n)$: restriction of the $\mathfrak{u}(n)$ form is still non-degenerate

# Context & Application

This theorem provides the crucial link between abstract structure theory and the concrete classical matrix groups. It shows that the Lie algebras most commonly encountered in physics and mathematics have the rich structure guaranteed by semisimplicity.

# Examples

**Example** (p. 74): For $\mathfrak{gl}(n)$, the trace form is $B(x,y) = \operatorname{tr}(xy) = \sum x_{ij}y_{ji}$. The decomposition $\mathfrak{gl}(n) = \mathbb{K} \cdot \operatorname{id} \oplus \mathfrak{sl}(n)$ is orthogonal with respect to $B$, and the restriction to $\mathfrak{sl}(n)$ is non-degenerate.

# Relationships

## Builds Upon
- **Trace form** — Non-degeneracy is the proof tool

## Enables
- **Root decomposition** — Applies to these now-known-semisimple algebras

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.5, pages 74. Theorem 6.33.

# Verification Notes

- Definition source: Direct from Theorem 6.33
- Confidence rationale: Major theorem with detailed proof
- Uncertainties: $\mathfrak{sp}(2n)$ case left as exercise
- Cross-reference status: Verified
