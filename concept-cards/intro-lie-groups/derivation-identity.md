---
# === CORE IDENTIFICATION ===
concept: Inner Derivation Identity for Semisimple Algebras
slug: derivation-identity

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
section: "6.7. Properties of semisimple Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Der g = g"
  - "all derivations are inner"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
  - killing-form
extends: []
related:
  - complementary-ideal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are all derivations of a semisimple Lie algebra inner?"
---

# Quick Definition

For a semisimple Lie algebra $\mathfrak{g}$, every derivation is inner: $\operatorname{Der} \mathfrak{g} = \mathfrak{g}$ (via the identification $x \mapsto \operatorname{ad} x$). Consequently, the automorphism group $\operatorname{Aut} \mathfrak{g} / \operatorname{Ad} G$ is discrete.

# Core Definition

**Proposition 6.47** (Kirillov, p. 77): If $\mathfrak{g}$ is a semisimple Lie algebra, then $\operatorname{Der} \mathfrak{g} = \mathfrak{g}$ (identifying $\mathfrak{g}$ with $\operatorname{ad} \mathfrak{g}$), and $\operatorname{Aut} \mathfrak{g} / \operatorname{Ad} G$ is discrete.

# Prerequisites

- **Semisimple Lie algebra** — The result requires semisimplicity
- **Killing form** — Used to find the orthogonal complement of $\mathfrak{g}$ in $\operatorname{Der} \mathfrak{g}$

# Key Properties

1. $\mathfrak{g} \hookrightarrow \operatorname{Der} \mathfrak{g}$ is injective since $\mathfrak{z}(\mathfrak{g}) = 0$
2. $\mathfrak{g}$ is an ideal in $\operatorname{Der} \mathfrak{g}$ (since $[\delta, \operatorname{ad} x] = \operatorname{ad} \delta(x)$)
3. The complement $I = \mathfrak{g}^\perp$ commutes with $\mathfrak{g}$, so $\delta(x) = 0$ for $\delta \in I$, hence $I = 0$

# Context & Application

This result is used in Chapter 7 to show that the semisimple part of the Jordan decomposition lies in $\mathfrak{g}$ (not just in $\operatorname{Der} \mathfrak{g}$). It also shows that outer automorphisms of semisimple algebras form a finite group (the symmetries of the Dynkin diagram).

# Examples

**Example**: For $\mathfrak{sl}(n, \mathbb{C})$, every derivation is of the form $x \mapsto [a, x]$ for some $a \in \mathfrak{sl}(n, \mathbb{C})$.

# Relationships

## Builds Upon
- **Semisimple Lie algebra** — Requires semisimplicity
- **Killing form** — Used in the proof

## Enables
- **Jordan decomposition in Lie algebras** — Used to show $x_s \in \mathfrak{g}$ (not just $\operatorname{Der} \mathfrak{g}$)

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.7, pages 76-77. Proposition 6.47.

# Verification Notes

- Definition source: Direct from Proposition 6.47
- Confidence rationale: Explicit proposition with proof
- Uncertainties: None
- Cross-reference status: Verified
