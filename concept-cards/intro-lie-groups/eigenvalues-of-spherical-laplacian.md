---
# === CORE IDENTIFICATION ===
concept: Eigenvalues of the Spherical Laplacian
slug: eigenvalues-of-spherical-laplacian

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
aliases:
  - "spectrum of Delta_sph"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - decomposition-of-polynomial-spaces
  - casimir-operator
extends: []
related:
  - spherical-laplace-operator
  - hydrogen-atom-connection
  - eigenfunctions-are-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the eigenvalues of the spherical Laplace operator?"
  - "How does representation theory determine the spectrum of a differential operator?"
---

# Quick Definition

The eigenvalues of $\Delta_{\mathrm{sph}}$ on $S^2$ are $\lambda_k = -k(k+1)$ for $k = 0, 1, 2, \ldots$, with multiplicity $2k+1$.

# Core Definition

**Theorem 5.11** (Kirillov, p. 64): The eigenvalues of the spherical Laplace operator $\Delta_{\mathrm{sph}}$ in the space $P_n$ are

$$\lambda_k = -k(k+1), \qquad k = 0, \ldots, n$$

and the multiplicity of $\lambda_k$ is $\dim V_{2k} = 2k + 1$.

**Theorem 5.12** (p. 64): Each eigenfunction of $\Delta_{\mathrm{sph}}$ in $C^\infty(S^2)$ is polynomial. The eigenvalues are $\lambda_k = -k(k+1)$ with multiplicity $2k+1$.

# Prerequisites

- **Decomposition of polynomial spaces** — $P_n \simeq V_0 \oplus V_2 \oplus \cdots \oplus V_{2n}$
- **Casimir operator** — $J_x^2 + J_y^2 + J_z^2$ acts on $V_l$ by $-l(l+2)/4$

# Key Properties

1. Eigenvalues $\lambda_k = -k(k+1)$ are all non-positive
2. Multiplicity of $\lambda_k$ is $2k+1$ (dimension of the $k$-th spherical harmonic space)
3. Every eigenfunction is polynomial (Theorem 5.12)
4. The eigenfunctions for eigenvalue $\lambda_k$ span a space isomorphic to $V_{2k}$ as an $SO(3)$-representation
5. $\bigoplus_{k \geq 0} E_k$ (where $E_k \simeq V_{2k}$) gives the orthogonal decomposition of $L^2(S^2)$

# Construction / Recognition

## How eigenvalues are computed:
1. Decompose $P_n \simeq V_0 \oplus V_2 \oplus \cdots \oplus V_{2n}$ (using weight multiplicities and Exercise 5.1)
2. $\Delta_{\mathrm{sph}} = J_x^2 + J_y^2 + J_z^2$ is the Casimir, so it acts as a scalar on each $V_{2k}$
3. By Exercise 4.3, $J_x^2 + J_y^2 + J_z^2$ acts on $V_l$ by $-l(l+2)/4$
4. For $l = 2k$: eigenvalue $= -2k(2k+2)/4 = -k(k+1)$

# Context & Application

This is the culmination of Chapter 5: eigenvalues of a PDE on the sphere determined purely by representation theory. The eigenvalues $-k(k+1)$ are the well-known angular momentum eigenvalues in quantum mechanics. The eigenfunctions are the spherical harmonics $Y_k^m$ ($-k \leq m \leq k$, giving $2k+1$ functions).

# Examples

**Example**: $k = 0$: eigenvalue $0$, multiplicity $1$ (constant functions).
$k = 1$: eigenvalue $-2$, multiplicity $3$ (linear functions $x, y, z$ restricted to $S^2$).
$k = 2$: eigenvalue $-6$, multiplicity $5$.

# Relationships

## Builds Upon
- **Decomposition of polynomial spaces** — Provides the irreducible decomposition
- **Casimir operator** — Gives the eigenvalue on each irreducible

## Enables
- **Hydrogen atom** — Via separation of variables with these eigenvalues

# Common Confusions

- **Confusion**: Thinking there might be additional eigenvalues beyond $-k(k+1)$.
  **Clarification**: Theorem 5.12 proves these are all eigenvalues of $\Delta_{\mathrm{sph}}$ on $C^\infty(S^2)$, not just on polynomial subspaces.

# Source Reference

Chapter 5, Section 5.2, Theorems 5.11, 5.12, p. 64.

# Verification Notes

- Definition source: Direct from Theorems 5.11 and 5.12
- Confidence rationale: Explicit theorems with derivation
- Uncertainties: None
- Cross-reference status: Verified
