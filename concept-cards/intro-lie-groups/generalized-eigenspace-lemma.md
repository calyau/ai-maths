---
# === CORE IDENTIFICATION ===
concept: Generalized Eigenspace Bracket Lemma
slug: generalized-eigenspace-lemma

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 82
section: "7.1. Semisimple elements and toroidal subalgebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lemma 7.3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - root-space-decomposition-toroidal
  - jordan-decomposition-lie-algebras
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do generalized eigenspaces of ad(x) interact under the bracket?"
---

# Quick Definition

For any $x \in \mathfrak{g}$, the generalized eigenspaces $\mathfrak{g}_\lambda = \{y \mid (\operatorname{ad} x - \lambda)^n y = 0\}$ satisfy $[\mathfrak{g}_\lambda, \mathfrak{g}_\mu] \subset \mathfrak{g}_{\lambda+\mu}$. This is the generalized version of the root space property.

# Core Definition

**Lemma 7.3** (Kirillov, p. 83): $[\mathfrak{g}_\lambda, \mathfrak{g}_\mu] \subset \mathfrak{g}_{\lambda+\mu}$, where $\mathfrak{g}_\lambda$ is the generalized eigenspace of $\operatorname{ad} x$ with eigenvalue $\lambda$.

Proof: By Jacobi identity, $(\operatorname{ad} x - \lambda - \mu)^n[y, z] = \sum \binom{n}{k}[(\operatorname{ad} x - \lambda)^k y, (\operatorname{ad} x - \mu)^{n-k} z] = 0$ for large $n$.

# Prerequisites

- **Lie algebra** — Uses only the Jacobi identity

# Key Properties

1. The proof uses only the Jacobi identity — no semisimplicity needed
2. This is the key step in proving the Jordan decomposition in Lie algebras
3. It implies the semisimple part $(\operatorname{ad} x)_s$ is a derivation

# Context & Application

This lemma is used to show that the semisimple part of $\operatorname{ad} x$ is a derivation of $\mathfrak{g}$, which by Proposition 6.47 must be inner. This is the key step in proving the abstract Jordan decomposition (Theorem 7.2).

# Relationships

## Enables
- **Jordan decomposition in Lie algebras** — Shows $(\operatorname{ad} x)_s$ is a derivation

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.1, pages 82-83. Lemma 7.3.

# Verification Notes

- Definition source: Direct from Lemma 7.3
- Confidence rationale: Explicit lemma with proof
- Uncertainties: None
- Cross-reference status: Verified
