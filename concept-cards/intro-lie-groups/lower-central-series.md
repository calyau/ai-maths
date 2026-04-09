---
# === CORE IDENTIFICATION ===
concept: Lower Central Series
slug: lower-central-series

# === CLASSIFICATION ===
category: structure-theory
subcategory: solvable-nilpotent
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 68
section: "6.2. Solvable and nilpotent Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "descending central series"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - lie-algebra-ideal
extends: []
related:
  - derived-series
  - nilpotent-lie-algebra
contrasts_with:
  - derived-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the lower central series of a Lie algebra?"
  - "How does the lower central series differ from the derived series?"
---

# Quick Definition

The lower central series of a Lie algebra $\mathfrak{g}$ is the descending chain $D_0\mathfrak{g} = \mathfrak{g}$, $D_{i+1}\mathfrak{g} = [\mathfrak{g}, D_i\mathfrak{g}]$, obtained by repeatedly bracketing with $\mathfrak{g}$ itself. Its vanishing defines nilpotency.

# Core Definition

**Definition 6.9** (Kirillov, p. 68): For a Lie algebra $\mathfrak{g}$, define a series of ideals $D_i\mathfrak{g} \subset \mathfrak{g}$ (called the lower central series) by $D_0\mathfrak{g} = \mathfrak{g}$ and

$$D_{i+1}\mathfrak{g} = [\mathfrak{g}, D_i\mathfrak{g}].$$

# Prerequisites

- **Lie algebra** — The lower central series is defined for any Lie algebra
- **Lie algebra ideal** — Each $D_i\mathfrak{g}$ is an ideal in $\mathfrak{g}$

# Key Properties

1. Each $D_i\mathfrak{g}$ is an ideal in $\mathfrak{g}$ (not just in $D_{i-1}\mathfrak{g}$)
2. $[\mathfrak{g}, D_i\mathfrak{g}] \subset D_{i+1}\mathfrak{g}$, which is stronger than the derived series condition
3. $D^i\mathfrak{g} \subset D_i\mathfrak{g}$ always (the derived series descends at least as fast)
4. $D_1\mathfrak{g} = [\mathfrak{g}, \mathfrak{g}] = D^1\mathfrak{g}$ (the first terms agree)

# Construction / Recognition

## To Construct:
1. Set $D_0\mathfrak{g} = \mathfrak{g}$
2. Compute $D_1\mathfrak{g} = [\mathfrak{g}, \mathfrak{g}]$
3. Compute $D_2\mathfrak{g} = [\mathfrak{g}, D_1\mathfrak{g}]$
4. Continue until stabilization

# Context & Application

The lower central series provides a finer measure of non-commutativity than the derived series. While the derived series detects solvability, the lower central series detects nilpotency, a strictly stronger condition.

# Examples

**Example 6.12** (p. 68): For the strictly upper-triangular matrices $\mathfrak{n} \subset \mathfrak{gl}(n, \mathbb{K})$: $D_i\mathfrak{n} \subset \mathfrak{a}_{i+1}$ where $\mathfrak{a}_k$ consists of matrices with nonzero entries only $k$ positions above the diagonal. Thus $D_n\mathfrak{n} = 0$, confirming nilpotency.

# Relationships

## Builds Upon
- **Lie algebra** — Defined for any Lie algebra

## Enables
- **Nilpotent Lie algebra** — Defined by vanishing of this series

## Contrasts With
- **Derived series** — Uses $[D^i\mathfrak{g}, D^i\mathfrak{g}]$ instead of $[\mathfrak{g}, D_i\mathfrak{g}]$; the lower central series descends more slowly

# Common Errors

- **Error**: Mixing up the subscript notation $D_i\mathfrak{g}$ (lower central) with $D^i\mathfrak{g}$ (derived)
  **Correction**: The subscript version brackets with $\mathfrak{g}$; the superscript version brackets with itself

# Common Confusions

- **Confusion**: Assuming the lower central series and derived series always terminate simultaneously
  **Clarification**: The derived series can reach zero while the lower central series does not (solvable but not nilpotent), but if the lower central series reaches zero, so does the derived series.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.2, pages 68-69. Definition 6.9, Proposition 6.10.

# Verification Notes

- Definition source: Direct from Definition 6.9
- Confidence rationale: Explicitly defined with clear notation
- Uncertainties: None
- Cross-reference status: Verified
