---
# === CORE IDENTIFICATION ===
concept: Cartan Conjugacy Theorem
slug: cartan-conjugacy

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 85
section: "7.2. Cartan subalgebra"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "conjugacy of Cartan subalgebras"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartan-subalgebra
extends: []
related:
  - rank-of-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are Cartan subalgebras unique?"
  - "In what sense are all Cartan subalgebras equivalent?"
---

# Quick Definition

Any two Cartan subalgebras in a semisimple Lie algebra are conjugate under the adjoint action of the corresponding Lie group. This ensures the root system is an invariant of the algebra, independent of the choice of Cartan subalgebra.

# Core Definition

**Theorem 7.13** (Kirillov, p. 85): Any two Cartan subalgebras in a semisimple Lie algebra are conjugate: if $\mathfrak{h}_1, \mathfrak{h}_2 \subset \mathfrak{g}$ are Cartan subalgebras, then there exists $g$ in the Lie group $G$ corresponding to $\mathfrak{g}$ such that $\mathfrak{h}_2 = \operatorname{Ad} g(\mathfrak{h}_1)$.

# Prerequisites

- **Cartan subalgebra** — The objects being compared

# Key Properties

1. Conjugacy means the root system does not depend on the choice of $\mathfrak{h}$
2. In particular, all Cartan subalgebras have the same dimension (Corollary 7.14)
3. The proof is not given in the source; referenced to other texts

# Context & Application

This is one of the most important structural results. Without conjugacy, the root system would depend on the choice of Cartan subalgebra, and the classification theory would not work. Conjugacy ensures the root system is a true invariant of the isomorphism class of $\mathfrak{g}$.

# Examples

**Example**: In $\mathfrak{sl}(n, \mathbb{C})$, any Cartan subalgebra is conjugate to the standard diagonal one. Different choices of "maximal commuting diagonalizable matrices" are related by a change of basis in $\mathbb{C}^n$.

# Relationships

## Builds Upon
- **Cartan subalgebra** — The objects being proved conjugate

## Enables
- **Rank of Lie algebra** — Well-defined by conjugacy
- **Root system as invariant** — The root system classifies the algebra

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.2, page 85. Theorem 7.13.

# Verification Notes

- Definition source: Direct from Theorem 7.13
- Confidence rationale: Stated without proof; referenced to standard texts
- Uncertainties: Proof not given
- Cross-reference status: Verified
