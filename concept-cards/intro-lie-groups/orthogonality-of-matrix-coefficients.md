---
# === CORE IDENTIFICATION ===
concept: Orthogonality of Matrix Coefficients
slug: orthogonality-of-matrix-coefficients

# === CLASSIFICATION ===
category: representations
subcategory: characters
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 47
section: "4.7 Orthogonality of characters and Peter-Weyl theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Schur orthogonality relations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - matrix-coefficient
  - schur-lemma
  - haar-measure
extends:
  - schur-lemma
related:
  - character-of-representation
  - orthogonality-of-characters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are matrix coefficients of different representations related?"
---

# Quick Definition

Matrix coefficients of non-isomorphic irreducible representations are orthogonal in $L^2(G)$, and those of the same irreducible representation satisfy precise norm relations.

# Core Definition

**Theorem 4.39** (Kirillov, pp. 47-48):

1. Let $V, W$ be non-isomorphic irreducible representations. Then for any choice of bases, the matrix coefficients are orthogonal: $(\rho_{ij}^V, \rho_{ab}^W) = 0$ where $(f_1, f_2) = \int_G f_1(g)\overline{f_2(g)}\, dg$.

2. Let $V$ be irreducible with an orthonormal basis (w.r.t. a $G$-invariant inner product). Then:
$$(\rho_{ij}^V, \rho_{kl}^V) = \frac{\delta_{ik}\delta_{jl}}{\dim V}$$

# Prerequisites

- **Matrix coefficient** — The objects whose orthogonality is being established
- **Schur's lemma** — Key tool in the proof (via Lemma 4.40)
- **Haar measure** — Defines the inner product on $L^2(G)$

# Key Properties

1. Matrix coefficients from different irreducible representations are orthogonal
2. Normalized matrix coefficients $\sqrt{\dim V}\, \rho_{ij}^V$ form an orthonormal system
3. The proof uses the averaging lemma: $\int_G gfg^{-1}\, dg = 0$ for non-isomorphic irreducibles, and $= \frac{\mathrm{tr}(f)}{\dim V}\,\mathrm{id}$ for endomorphisms of an irreducible (Lemma 4.40)

# Examples

**Example 4.49** (p. 50): For $G = S^1$, this gives $\int_0^1 e^{2\pi ikx}\overline{e^{2\pi ilx}}\, dx = \delta_{kl}$, the standard orthogonality of Fourier exponentials.

# Relationships

## Builds Upon
- **Schur's lemma** — Core of the proof

## Enables
- **Orthogonality of characters** — Follows as a special case
- **Peter-Weyl theorem** — Extends orthogonality to a completeness result

# Source Reference

Chapter 4, Section 4.7, Theorem 4.39, Lemma 4.40, pp. 47-48.

# Verification Notes

- Definition source: Direct from Theorem 4.39
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
