---
# === CORE IDENTIFICATION ===
concept: Complexification of a Lie Algebra
slug: complexification

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 33
section: "3.9"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathfrak{g}_\\mathbb{C}$"
  - "$\\mathfrak{g} \\otimes_\\mathbb{R} \\mathbb{C}$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - real-form
  - compact-real-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

The complexification of a real Lie algebra $\mathfrak{g}$ is $\mathfrak{g}_\mathbb{C} = \mathfrak{g} \otimes_\mathbb{R} \mathbb{C} = \mathfrak{g} \oplus i\mathfrak{g}$ with the obvious extension of the bracket. In this situation, $\mathfrak{g}$ is called a real form of $\mathfrak{g}_\mathbb{C}$.

# Core Definition

**Definition 3.51** (Kirillov): Let $\mathfrak{g}$ be a real Lie algebra. Its complexification is the complex Lie algebra $\mathfrak{g}_\mathbb{C} = \mathfrak{g} \otimes_\mathbb{R} \mathbb{C} = \mathfrak{g} \oplus i\mathfrak{g}$ with the obvious commutator. In this situation, we will also say that $\mathfrak{g}$ is a real form of $\mathfrak{g}_\mathbb{C}$.

# Prerequisites

- **Lie algebra** — the algebra being complexified

# Key Properties

1. $\dim_\mathbb{C} \mathfrak{g}_\mathbb{C} = \dim_\mathbb{R} \mathfrak{g}$.
2. Different real Lie algebras can have the same complexification (they are different real forms).
3. The bracket extends by $\mathbb{C}$-linearity: $[x + iy, x' + iy'] = [x,x'] - [y,y'] + i([x,y'] + [y,x'])$.
4. Algebraic properties (e.g., semisimplicity) are shared between a real form and its complexification.

# Construction / Recognition

## To Construct/Create:
1. Take $\mathfrak{g}_\mathbb{C} = \mathfrak{g} \oplus i\mathfrak{g}$ as a complex vector space.
2. Extend the bracket by $\mathbb{C}$-linearity.

## To Identify/Recognize:
1. A complex Lie algebra obtained by extending scalars from $\mathbb{R}$ to $\mathbb{C}$.

# Context & Application

Complexification allows one to use the simpler theory of complex Lie algebras to study real ones. Different real groups (e.g., $\mathrm{SU}(n)$ and $\mathrm{SL}(n, \mathbb{R})$) may share the same complexified Lie algebra.

# Examples

**Example** (p. 33): $\mathfrak{sl}(n, \mathbb{R})_\mathbb{C} = \mathfrak{sl}(n, \mathbb{C})$.

**Example 3.52** (p. 33): $\mathfrak{u}(n)_\mathbb{C} = \mathfrak{gl}(n, \mathbb{C})$ since any complex matrix decomposes uniquely as skew-Hermitian plus Hermitian ($= i \cdot$ skew-Hermitian).

**Example** (Section 3.10): $\mathfrak{su}(2)_\mathbb{C} \cong \mathfrak{sl}(2, \mathbb{C})$ and $\mathfrak{so}(3, \mathbb{R})_\mathbb{C} = \mathfrak{so}(3, \mathbb{C}) \cong \mathfrak{sl}(2, \mathbb{C})$.

# Relationships

## Builds Upon
- **Lie algebra** — the real algebra being complexified

## Enables
- **Transfer of algebraic properties** — semisimplicity, etc., transfer between real form and complexification

## Related
- **Real form** — a real algebra whose complexification gives a given complex algebra
- **Compact real form** — a real form that integrates to a compact group

# Common Errors

- **Error**: Assuming the complexification of a real form of $\mathfrak{g}_\mathbb{C}$ is always $\mathfrak{g}_\mathbb{C}$.
  **Correction**: This is true by definition.

# Common Confusions

- **Confusion**: Whether $\mathfrak{su}(n)_\mathbb{C} = \mathfrak{su}(n, \mathbb{C})$.
  **Clarification**: There is no "$\mathfrak{su}(n, \mathbb{C})$." The complexification of $\mathfrak{su}(n)$ is $\mathfrak{sl}(n, \mathbb{C})$, not a "complex version" of $\mathfrak{su}$.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.9, Definition 3.51, Example 3.52, pages 33-34.

# Verification Notes

- Definition source: Direct from Definition 3.51
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified with Examples 3.52, Section 3.10
