---
# === CORE IDENTIFICATION ===
concept: Simple Lie Algebra
slug: simple-lie-algebra

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 71
section: "6.4. The radical. Semisimple and reductive algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - lie-algebra-ideal
extends: []
related:
  - semisimple-lie-algebra
  - decomposition-into-simples
contrasts_with:
  - semisimple-lie-algebra
  - abelian-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple Lie algebra?"
  - "How does a simple Lie algebra relate to a semisimple one?"
---

# Quick Definition

A simple Lie algebra is a non-abelian Lie algebra whose only ideals are $0$ and itself. Simple algebras are the indecomposable building blocks of semisimple algebras.

# Core Definition

**Definition 6.20** (Kirillov, p. 71): A Lie algebra $\mathfrak{g}$ is called simple if it is not abelian and contains no ideals other than $0$ and $\mathfrak{g}$.

The condition of being non-abelian excludes the one-dimensional Lie algebra.

# Prerequisites

- **Lie algebra** — Simple is a property of Lie algebras
- **Lie algebra ideal** — Simplicity is defined via ideals

# Key Properties

1. Every simple Lie algebra is semisimple (Lemma 6.21)
2. A simple algebra has zero center
3. The invariant bilinear form on a simple algebra is unique up to a scalar (Exercise 4.4)
4. Every semisimple algebra decomposes as a direct sum of simple algebras (Corollary 6.43)

# Construction / Recognition

## To Identify/Recognize:
1. Check that $\mathfrak{g}$ is not abelian ($[\mathfrak{g}, \mathfrak{g}] \neq 0$)
2. Check that $\mathfrak{g}$ has no proper nonzero ideals

# Context & Application

Simple Lie algebras are the atoms of the classification theory. Every semisimple algebra decomposes uniquely into a direct sum of simple ones. The classification of simple complex Lie algebras (types $A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2$) is one of the great achievements of 19th-20th century mathematics.

# Examples

**Example 6.22** (p. 71): $\mathfrak{sl}(2, \mathbb{C})$ is simple. In the basis $e, f, h$, $\operatorname{ad} h$ has distinct eigenvalues $2, -2, 0$, so any invariant subspace is spanned by a subset of $\{e, f, h\}$. Checking each possibility shows that any nonzero ideal generates all of $\mathfrak{sl}(2, \mathbb{C})$.

**Remark 6.41** (p. 76): A simple real Lie algebra may have a complexification that is not simple (it can be a direct sum of two simple complex algebras).

# Relationships

## Enables
- **Semisimple Lie algebra** — Every semisimple algebra is a direct sum of simple algebras
- **Decomposition into simples** — Unique decomposition theorem (Corollary 6.43)

## Contrasts With
- **Semisimple Lie algebra** — Semisimple allows direct sums; simple is indecomposable
- **Abelian Lie algebra** — Excluded by definition; the one-dimensional algebra is not simple

# Common Errors

- **Error**: Including the one-dimensional algebra as simple
  **Correction**: The definition requires non-abelian, so $\dim \mathfrak{g} = 1$ is excluded

# Common Confusions

- **Confusion**: Thinking "simple" and "semisimple" are synonymous
  **Clarification**: Simple means no proper ideals; semisimple means no solvable ideals. $\mathfrak{sl}(2, \mathbb{C}) \oplus \mathfrak{sl}(2, \mathbb{C})$ is semisimple but not simple.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, pages 71. Definition 6.20, Lemma 6.21, Example 6.22.

# Verification Notes

- Definition source: Direct from Definition 6.20
- Confidence rationale: Explicitly defined with proof and example
- Uncertainties: None
- Cross-reference status: Verified
