---
# === CORE IDENTIFICATION ===
concept: Decomposition of Polynomial Spaces on the Sphere
slug: decomposition-of-polynomial-spaces

# === CLASSIFICATION ===
category: applications
subcategory: spherical-harmonics
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 64
section: "5.2 Spherical Laplace operator and hydrogen atom"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-spaces-on-sphere
  - classification-of-sl2-representations
extends: []
related:
  - eigenvalues-of-spherical-laplacian
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do polynomial spaces on the sphere decompose into irreducible SO(3) representations?"
---

# Quick Definition

The space $P_n$ of polynomial functions of degree $\leq n$ on $S^2$ decomposes as $P_n \simeq V_0 \oplus V_2 \oplus \cdots \oplus V_{2n}$ under $SO(3,\mathbb{R})$.

# Core Definition

**Equation (5.10)** (Kirillov, p. 64): Using the multiplicity formula from Exercise 5.1 and the weight space dimensions $\dim P_n[2k] = n + 1 - |k|$:

$$P_n \simeq V_0 \oplus V_2 \oplus \cdots \oplus V_{2n}$$

where $V_{2k}$ are the irreducible representations of $SO(3,\mathbb{R})$ (which correspond to even-highest-weight representations of $\mathfrak{sl}(2,\mathbb{C})$).

# Prerequisites

- **Polynomial spaces on sphere** — The spaces being decomposed
- **Classification of sl(2,C) representations** — Provides the irreducible summands

# Key Properties

1. Each irreducible $V_{2k}$ appears with multiplicity 1
2. $\dim V_{2k} = 2k + 1$
3. $\dim P_n = \sum_{k=0}^n (2k+1) = (n+1)^2$
4. The orthogonal complement $E_n = P_n \ominus P_{n-1}$ satisfies $E_n \simeq V_{2n}$

# Context & Application

This decomposition is the key step in computing eigenvalues of $\Delta_{\mathrm{sph}}$. The subspaces $E_n \simeq V_{2n}$ are eigenspaces of $\Delta_{\mathrm{sph}}$ (since the Casimir acts as a scalar on each irreducible).

# Examples

**Example**: $P_0 = V_0$ (constants, dim 1). $P_1 = V_0 \oplus V_2$ (dim 1 + 3 = 4). $P_2 = V_0 \oplus V_2 \oplus V_4$ (dim 1 + 3 + 5 = 9).

# Relationships

## Builds Upon
- **Polynomial spaces on sphere** and **classification of sl(2,C) reps**

## Enables
- **Eigenvalues of spherical Laplacian** — Each $V_{2k}$ is an eigenspace

# Source Reference

Chapter 5, Section 5.2, equation (5.10), p. 64.

# Verification Notes

- Definition source: Direct from equation (5.10)
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified
