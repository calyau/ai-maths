---
# === CORE IDENTIFICATION ===
concept: Orthogonality of Characters
slug: orthogonality-of-characters

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
pdf_page: 48
section: "4.7 Orthogonality of characters and Peter-Weyl theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-representation
  - orthogonality-of-matrix-coefficients
extends:
  - orthogonality-of-matrix-coefficients
related:
  - multiplicity-formula
  - peter-weyl-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are characters of different irreducible representations related?"
  - "How do I determine multiplicities using characters?"
---

# Quick Definition

Characters of non-isomorphic irreducible representations of a compact group are orthogonal in $L^2(G)$, and each irreducible character has norm 1. This yields the multiplicity formula $N_i = (\chi_V, \chi_{V_i})$.

# Core Definition

**Theorem 4.43** (Kirillov, pp. 48-49):

1. Let $V, W$ be non-isomorphic complex irreducible representations of a compact real Lie group $G$. Then $(\chi_V, \chi_W) = 0$.
2. For any irreducible representation $V$, $(\chi_V, \chi_V) = 1$.

The set $\{\chi_V \mid V \in \widehat{G}\}$ is an orthonormal family of functions on $G$, where $\widehat{G}$ denotes the set of isomorphism classes of irreducible representations.

# Prerequisites

- **Character of representation** — The objects satisfying orthogonality
- **Orthogonality of matrix coefficients** — The more general result from which this follows

# Key Properties

1. $(\chi_V, \chi_V) = 1$ iff $V$ is irreducible (Corollary 4.44)
2. Multiplicities: $N_i = (\chi_V, \chi_{V_i})$ (Corollary 4.44)
3. The decomposition $V \simeq \bigoplus N_i V_i$ is unique
4. Characters form an orthonormal basis of class functions in $L^2(G)$ (Corollary 4.48)

# Examples

**Example 4.49** (p. 50): For $G = S^1$, orthogonality of characters gives $\int_0^1 e^{2\pi ikx}\overline{e^{2\pi ilx}}\, dx = \delta_{kl}$, the orthogonality of Fourier exponentials.

# Relationships

## Builds Upon
- **Orthogonality of matrix coefficients** — Characters are traces of matrix coefficients

## Enables
- **Multiplicity formula** — $N_i = (\chi_V, \chi_{V_i})$
- **Irreducibility criterion** — $(\chi_V, \chi_V) = 1$

# Source Reference

Chapter 4, Section 4.7, Theorem 4.43, Corollary 4.44, pp. 48-49.

# Verification Notes

- Definition source: Direct from Theorem 4.43
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
