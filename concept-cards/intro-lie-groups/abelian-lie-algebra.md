---
# === CORE IDENTIFICATION ===
concept: Abelian Lie Algebra
slug: abelian-lie-algebra

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
section: "6.1. Ideals and commutant"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "commutative Lie algebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - commutant
  - solvable-lie-algebra
  - nilpotent-lie-algebra
contrasts_with:
  - simple-lie-algebra
  - semisimple-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an abelian Lie algebra?"
---

# Quick Definition

An abelian (commutative) Lie algebra has $[x, y] = 0$ for all $x, y$. Equivalently, $[\mathfrak{g}, \mathfrak{g}] = 0$. Abelian algebras are both solvable and nilpotent but are never simple (by definition).

# Core Definition

A Lie algebra $\mathfrak{g}$ is abelian if $[x, y] = 0$ for all $x, y \in \mathfrak{g}$. Equivalently, $\mathfrak{g} = \mathfrak{z}(\mathfrak{g})$, or $[\mathfrak{g}, \mathfrak{g}] = 0$ (Kirillov, p. 67).

# Prerequisites

- **Lie algebra** — An abelian algebra is a special case

# Key Properties

1. Every abelian algebra is both solvable (trivially) and nilpotent
2. The one-dimensional Lie algebra is abelian — and explicitly excluded from being simple
3. $\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}]$ is always abelian (Lemma 6.4)
4. Abelian algebras can appear as the center of reductive algebras

# Context & Application

Abelian Lie algebras are the "trivial" case of the structure theory. The entire Chapter 6 can be viewed as measuring "how far" a Lie algebra is from being abelian, with solvable and nilpotent being progressively weaker notions of "almost abelian."

# Relationships

## Enables
- **Solvable Lie algebra** — Built from abelian extensions
- **Commutant** — $[\mathfrak{g}, \mathfrak{g}] = 0$ characterizes abelianness

## Contrasts With
- **Simple Lie algebra** — Non-abelian by definition
- **Semisimple Lie algebra** — Zero center; abelian algebras have maximal center

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.1, page 67.

# Verification Notes

- Definition source: Standard; referenced implicitly throughout
- Confidence rationale: Standard concept used as baseline
- Uncertainties: None
- Cross-reference status: Verified
