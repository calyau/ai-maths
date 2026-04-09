---
# === CORE IDENTIFICATION ===
concept: Quotient by Commutant
slug: quotient-by-commutant

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
  - "abelianization"
  - "g/[g,g]"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutant
  - lie-algebra-ideal
extends:
  - commutant
related:
  - solvable-lie-algebra
  - abelian-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the abelianization of a Lie algebra?"
  - "Why is the quotient by the commutant abelian?"
---

# Quick Definition

The quotient $\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}]$ is the largest abelian quotient of $\mathfrak{g}$. It is abelian because all brackets vanish in the quotient, and $[\mathfrak{g}, \mathfrak{g}]$ is the smallest ideal for which this holds.

# Core Definition

**Lemma 6.4** (Kirillov, p. 67): The quotient $\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}]$ is an abelian Lie algebra. Moreover, $[\mathfrak{g}, \mathfrak{g}]$ is the smallest ideal with this property: if $\mathfrak{g}/I$ is abelian for some ideal $I \subset \mathfrak{g}$, then $I \supset [\mathfrak{g}, \mathfrak{g}]$.

# Prerequisites

- **Commutant** — The ideal being quotiented out
- **Lie algebra ideal** — Quotient construction requires an ideal

# Key Properties

1. $\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}]$ is always abelian
2. It is the universal abelian quotient (largest abelian quotient)
3. $\dim(\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}])$ measures "how abelian" $\mathfrak{g}$ is
4. For semisimple $\mathfrak{g}$: $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$, so the quotient is zero

# Context & Application

The abelianization is the starting point for measuring non-commutativity. In the context of solvable algebras, the chain of quotients $D^i\mathfrak{g}/D^{i+1}\mathfrak{g}$ (each abelian) provides the successive abelian extensions that build up the algebra.

# Examples

**Example 6.5** (p. 67): $\mathfrak{gl}(n)/[\mathfrak{gl}(n), \mathfrak{gl}(n)] = \mathfrak{gl}(n)/\mathfrak{sl}(n) \cong \mathbb{K}$, the one-dimensional abelian algebra (scalar matrices).

# Relationships

## Builds Upon
- **Commutant** — The ideal defining the quotient

## Enables
- **Derived series** — Each step produces an abelian quotient

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.1, page 67. Lemma 6.4.

# Verification Notes

- Definition source: Direct from Lemma 6.4
- Confidence rationale: Explicitly stated lemma
- Uncertainties: None
- Cross-reference status: Verified
