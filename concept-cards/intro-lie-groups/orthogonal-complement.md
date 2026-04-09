---
# === CORE IDENTIFICATION ===
concept: Orthogonal Complement of an Ideal
slug: orthogonal-complement

# === CLASSIFICATION ===
category: structure-theory
subcategory: bilinear-forms
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 73
section: "6.5. Invariant bilinear forms and semisimplicity of classical Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "I^perp"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - invariant-bilinear-form
  - lie-algebra-ideal
extends: []
related:
  - killing-form
  - complementary-ideal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is the orthogonal complement of an ideal also an ideal?"
---

# Quick Definition

If $B$ is an invariant bilinear form on $\mathfrak{g}$ and $I$ is an ideal, then the orthogonal complement $I^\perp = \{x \in \mathfrak{g} \mid B(x,y) = 0 \text{ for all } y \in I\}$ is also an ideal. This is the basic mechanism connecting bilinear forms to the ideal structure.

# Core Definition

**Lemma 6.29** (Kirillov, p. 73): Let $B$ be an invariant bilinear form on $\mathfrak{g}$, and $I \subset \mathfrak{g}$ an ideal. Then $I^\perp = \{x \in \mathfrak{g} \mid B(x,y) = 0 \text{ for all } y \in I\}$ is also an ideal in $\mathfrak{g}$. In particular, $\operatorname{Ker} B = \mathfrak{g}^\perp$ is an ideal.

# Prerequisites

- **Invariant bilinear form** — The form must be invariant for the result to hold
- **Lie algebra ideal** — The input and output are ideals

# Key Properties

1. $I^\perp$ is an ideal whenever $B$ is invariant and $I$ is an ideal
2. $\operatorname{Ker} B = \mathfrak{g}^\perp$ is always an ideal
3. In general, $I \cap I^\perp$ can be nonzero, even for non-degenerate $B$
4. If $B$ is non-degenerate and $I \cap I^\perp = 0$, then $\mathfrak{g} = I \oplus I^\perp$

# Context & Application

This lemma is the key technical tool connecting bilinear forms to the ideal structure. It is used in: (1) proving the Cartan criterion, (2) showing semisimple algebras decompose into simple summands, and (3) proving $\operatorname{Der} \mathfrak{g} = \mathfrak{g}$ for semisimple $\mathfrak{g}$.

# Examples

**Application** (Theorem 6.42, p. 76): For semisimple $\mathfrak{g}$ with Killing form $K$, if $I$ is an ideal, then $I \cap I^\perp$ has zero Killing form, hence is solvable by Cartan's criterion, hence zero. Thus $\mathfrak{g} = I \oplus I^\perp$.

# Relationships

## Builds Upon
- **Invariant bilinear form** — Requires invariance of $B$

## Enables
- **Complementary ideal** — When $I \cap I^\perp = 0$, gives direct sum decomposition
- **Decomposition into simples** — Used iteratively to split semisimple algebras

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.5, page 73. Lemma 6.29.

# Verification Notes

- Definition source: Direct from Lemma 6.29
- Confidence rationale: Explicit lemma statement
- Uncertainties: None
- Cross-reference status: Verified
