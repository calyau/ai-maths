---
# === CORE IDENTIFICATION ===
concept: Multiplicity Formula
slug: multiplicity-formula

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
pdf_page: 49
section: "4.7 Orthogonality of characters and Peter-Weyl theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonality-of-characters
  - completely-reducible-representation
extends:
  - orthogonality-of-characters
related:
  - character-of-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I decompose a representation into irreducibles?"
  - "How do I compute the multiplicity of an irreducible in a given representation?"
---

# Quick Definition

For a completely reducible representation $V \simeq \bigoplus N_i V_i$ of a compact group, the multiplicity of each irreducible $V_i$ is given by the inner product $N_i = (\chi_V, \chi_{V_i})$.

# Core Definition

**Corollary 4.44** (Kirillov, p. 49): Let $V$ be a complex representation of a compact real Lie group $G$. Then:

1. $V$ is irreducible iff $(\chi_V, \chi_V) = 1$.
2. $V$ can be uniquely written as $V \simeq \bigoplus N_i V_i$ ($V_i$ pairwise non-isomorphic irreducible), and the multiplicities are $N_i = (\chi_V, \chi_{V_i})$.

# Prerequisites

- **Orthogonality of characters** — The multiplicities follow from orthogonality
- **Completely reducible representation** — $V$ must decompose as a direct sum

# Key Properties

1. $N_i = (\chi_V, \chi_{V_i}) = \int_G \chi_V(g)\overline{\chi_{V_i}(g)}\, dg$
2. $(\chi_V, \chi_V) = \sum N_i^2$ (self-inner product gives sum of squared multiplicities)
3. The decomposition is unique

# Context & Application

This gives a concrete computational method for decomposing representations, at least in principle. For compact groups, one computes the inner product of characters using the Haar measure. In practice, for Lie groups this is often done via weight theory rather than direct integration.

# Examples

**Example** (p. 49): For $G = S^1$ with $V$ a representation, $N_k = \int_0^1 \chi_V(x) e^{-2\pi ikx}\, dx$ gives the $k$-th Fourier coefficient — so the multiplicity formula is precisely Fourier analysis.

# Relationships

## Builds Upon
- **Orthogonality of characters** — The theoretical foundation

## Enables
- **Practical decomposition** — Given characters of irreducibles, compute multiplicities

# Source Reference

Chapter 4, Section 4.7, Corollary 4.44, p. 49.

# Verification Notes

- Definition source: Direct from Corollary 4.44
- Confidence rationale: Explicit corollary
- Uncertainties: None
- Cross-reference status: Verified
