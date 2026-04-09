---
# === CORE IDENTIFICATION ===
concept: Derived Series
slug: derived-series

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
pdf_page: 67
section: "6.2. Solvable and nilpotent Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "derived filtration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutant
  - lie-algebra-ideal
extends:
  - commutant
related:
  - lower-central-series
  - solvable-lie-algebra
contrasts_with:
  - lower-central-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the derived series of a Lie algebra?"
  - "How is the derived series used to define solvability?"
---

# Quick Definition

The derived series of a Lie algebra $\mathfrak{g}$ is the descending chain of ideals $D^0\mathfrak{g} = \mathfrak{g}$, $D^{i+1}\mathfrak{g} = [D^i\mathfrak{g}, D^i\mathfrak{g}]$ obtained by iterating the commutant operation. A Lie algebra is solvable when this series reaches zero.

# Core Definition

**Definition 6.6** (Kirillov, p. 67): For a Lie algebra $\mathfrak{g}$, define the series of ideals $D^i\mathfrak{g}$ (called the derived series) by $D^0\mathfrak{g} = \mathfrak{g}$ and

$$D^{i+1}\mathfrak{g} = [D^i\mathfrak{g}, D^i\mathfrak{g}].$$

Each $D^i\mathfrak{g}$ is an ideal in $\mathfrak{g}$ and $D^i\mathfrak{g}/D^{i+1}\mathfrak{g}$ is abelian.

# Prerequisites

- **Commutant** — Each step of the derived series is a commutant of the previous term
- **Lie algebra ideal** — Each term $D^i\mathfrak{g}$ is an ideal in $\mathfrak{g}$

# Key Properties

1. Each $D^i\mathfrak{g}$ is an ideal in $\mathfrak{g}$ (not just in $D^{i-1}\mathfrak{g}$)
2. The quotient $D^i\mathfrak{g}/D^{i+1}\mathfrak{g}$ is abelian for each $i$
3. The series is descending: $D^0\mathfrak{g} \supset D^1\mathfrak{g} \supset D^2\mathfrak{g} \supset \cdots$
4. $D^1\mathfrak{g} = [\mathfrak{g}, \mathfrak{g}]$ is the commutant
5. The derived series terminates (stabilizes) because $\mathfrak{g}$ is finite-dimensional

# Construction / Recognition

## To Construct:
1. Set $D^0\mathfrak{g} = \mathfrak{g}$
2. Compute $D^1\mathfrak{g} = [\mathfrak{g}, \mathfrak{g}]$
3. Compute $D^2\mathfrak{g} = [D^1\mathfrak{g}, D^1\mathfrak{g}]$
4. Continue until the series stabilizes

## To Use:
1. If $D^n\mathfrak{g} = 0$ for some $n$, then $\mathfrak{g}$ is solvable
2. If the series stabilizes at a nonzero ideal, $\mathfrak{g}$ is not solvable

# Context & Application

The derived series is one of two fundamental descending chains used to classify Lie algebras by "how close to abelian" they are. Its vanishing defines solvability — the condition that the algebra can be built from successive abelian extensions.

# Examples

**Example 6.12** (p. 68): For the Lie algebra $\mathfrak{b}$ of upper-triangular matrices in $\mathfrak{gl}(n, \mathbb{K})$: $D^1\mathfrak{b} \subset \mathfrak{n}$ (strictly upper-triangular), and $D^{i+1}\mathfrak{b} \subset \mathfrak{a}_{2^i}$ where $\mathfrak{a}_k$ are matrices shifting entries $k$ positions above the diagonal. Thus $D^n\mathfrak{b} = 0$ for large $n$, so $\mathfrak{b}$ is solvable.

# Relationships

## Builds Upon
- **Commutant** — The derived series iterates the commutant operation

## Enables
- **Solvable Lie algebra** — Defined by the vanishing of the derived series

## Related
- **Lower central series** — Another descending chain measuring non-commutativity

## Contrasts With
- **Lower central series** — Uses $[D^i\mathfrak{g}, D^i\mathfrak{g}]$ vs. $[\mathfrak{g}, D_i\mathfrak{g}]$; the derived series descends faster

# Common Errors

- **Error**: Confusing $D^{i+1}\mathfrak{g} = [D^i\mathfrak{g}, D^i\mathfrak{g}]$ with $D_{i+1}\mathfrak{g} = [\mathfrak{g}, D_i\mathfrak{g}]$
  **Correction**: The derived series brackets each term with itself; the lower central series brackets each term with $\mathfrak{g}$

# Common Confusions

- **Confusion**: Thinking the derived series and lower central series always agree
  **Clarification**: $D^i\mathfrak{g} \subset D_i\mathfrak{g}$ always holds, but they can differ. A nilpotent algebra is always solvable, but not conversely.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.2, pages 67-69. Definition 6.6, Proposition 6.7.

# Verification Notes

- Definition source: Direct from Definition 6.6
- Confidence rationale: Explicitly defined with characterization theorem
- Uncertainties: None
- Cross-reference status: Verified against source
