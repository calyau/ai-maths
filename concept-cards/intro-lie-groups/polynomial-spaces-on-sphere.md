---
# === CORE IDENTIFICATION ===
concept: Polynomial Spaces on the Sphere
slug: polynomial-spaces-on-sphere

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
pdf_page: 63
section: "5.2 Spherical Laplace operator and hydrogen atom"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "P_n"
  - "polynomial functions on S^2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spherical-laplace-operator
  - classification-of-sl2-representations
extends: []
related:
  - decomposition-of-polynomial-spaces
  - eigenvalues-of-spherical-laplacian
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the polynomial spaces P_n on the sphere?"
  - "How do polynomial spaces decompose into irreducible SO(3) representations?"
---

# Quick Definition

$P_n$ is the space of complex-valued functions on $S^2$ that can be written as polynomials in $x, y, z$ of total degree $\leq n$. Each $P_n$ is a finite-dimensional representation of $SO(3,\mathbb{R})$ that decomposes as $P_n \simeq V_0 \oplus V_2 \oplus \cdots \oplus V_{2n}$.

# Core Definition

(Kirillov, p. 63, equation 5.9):

$$P_n = \left\{\text{Complex-valued functions on } S^2 \text{ which can be written as polynomials in } x, y, z \text{ of total degree } \leq n\right\}$$

Each $P_n$ is a finite-dimensional $SO(3,\mathbb{R})$-representation and is $\Delta_{\mathrm{sph}}$-invariant.

# Prerequisites

- **Spherical Laplace operator** — $P_n$ is $\Delta_{\mathrm{sph}}$-invariant
- **Classification of sl(2,C) representations** — Used for the decomposition

# Key Properties

1. $P_n$ is finite-dimensional and $SO(3)$-invariant
2. $\bigcup P_n$ is dense in $C^\infty(S^2)$
3. A basis of $P_n$ is given by $f_{p,k} = z^p(\sqrt{1-z^2})^{|k|} e^{ik\varphi}$ with $p + |k| \leq n$ (Lemma 5.10)
4. $J_z f_{p,k} = ik\, f_{p,k}$
5. $\dim P_n[2k] = n + 1 - |k|$ (dimension of weight $2k$ subspace)

# Construction / Recognition

## Basis Construction (Lemma 5.10):
1. Use cylindrical coordinates: $u = x + iy$, $v = x - iy$, $z$
2. Monomials $z^p u^k$ and $z^p v^k$ with $p + k \leq n$ form a basis
3. Rewrite as $f_{p,k} = z^p \rho^{|k|} e^{ik\varphi}$ where $\rho = \sqrt{x^2 + y^2}$
4. On $S^2$: $\rho = \sqrt{1 - z^2}$

# Context & Application

The spaces $P_n$ provide a concrete, finite-dimensional setting for decomposing functions on $S^2$ into irreducible $SO(3)$-representations. This avoids the analytical difficulties of working with all of $C^\infty(S^2)$.

# Examples

**Equation (5.10)** (p. 64): $P_n \simeq V_0 \oplus V_2 \oplus \cdots \oplus V_{2n}$.

**Example**: $P_0 = V_0$ (constants), $P_1 = V_0 \oplus V_2$ (constants + linear functions give 1 + 3 = 4 dimensions).

# Relationships

## Enables
- **Decomposition of polynomial spaces** — $P_n \simeq \bigoplus_{k=0}^n V_{2k}$
- **Eigenvalues of spherical Laplacian** — From the decomposition

# Source Reference

Chapter 5, Section 5.2, equation (5.9), Lemma 5.10, pp. 63-64.

# Verification Notes

- Definition source: Direct from equation (5.9)
- Confidence rationale: Explicit definition with basis construction
- Uncertainties: None
- Cross-reference status: Verified
