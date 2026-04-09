---
# === CORE IDENTIFICATION ===
concept: Polynomial Eigenfunctions of Spherical Laplacian
slug: eigenfunctions-are-polynomial

# === CLASSIFICATION ===
category: applications
subcategory: spherical-harmonics
tier: advanced

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
  - eigenvalues-of-spherical-laplacian
  - decomposition-of-polynomial-spaces
extends:
  - eigenvalues-of-spherical-laplacian
related:
  - peter-weyl-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are all eigenfunctions of the spherical Laplacian polynomial?"
---

# Quick Definition

Every eigenfunction of $\Delta_{\mathrm{sph}}$ on $C^\infty(S^2)$ is a polynomial (restricted to $S^2$). There are no "exotic" eigenfunctions beyond spherical harmonics.

# Core Definition

**Theorem 5.12** (Kirillov, p. 64): Each eigenfunction of $\Delta_{\mathrm{sph}}$ is polynomial. The eigenvalues are $\lambda_k = -k(k+1)$, and the multiplicity of $\lambda_k$ is $2k+1$.

**Proof sketch**: $\Delta_{\mathrm{sph}}$ is self-adjoint on $L^2(S^2)$ (since $J_x, J_y, J_z$ are skew-Hermitian). The spaces $E_n = P_n \ominus P_{n-1}$ satisfy $E_n \simeq V_{2n}$. Since polynomials are dense in $L^2(S^2)$, we get $L^2(S^2) = \widehat{\bigoplus}_{n \geq 0} E_n$. Any eigenfunction must lie in some $E_n$.

# Prerequisites

- **Eigenvalues of spherical Laplacian** — The eigenvalue result
- **Decomposition of polynomial spaces** — Provides the $E_n$ spaces

# Key Properties

1. The space of eigenfunctions with eigenvalue $\lambda_k$ is exactly $E_k \simeq V_{2k}$
2. These are the spherical harmonics of degree $k$
3. The proof uses density of polynomials in $L^2(S^2)$ and self-adjointness

# Relationships

## Builds Upon
- **Eigenvalues of spherical Laplacian** — This strengthens the result to all of $C^\infty(S^2)$

## Related
- **Peter-Weyl theorem** — Similar completeness argument

# Source Reference

Chapter 5, Section 5.2, Theorem 5.12, p. 64.

# Verification Notes

- Definition source: Direct from Theorem 5.12
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
