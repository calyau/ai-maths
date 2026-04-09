---
# === CORE IDENTIFICATION ===
concept: Spherical Laplace Operator
slug: spherical-laplace-operator

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
pdf_page: 61
section: "5.2 Spherical Laplace operator and hydrogen atom"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Laplace-Beltrami operator on the sphere"
  - "angular Laplacian"
  - "Delta_sph"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - casimir-operator
  - classification-of-sl2-representations
extends: []
related:
  - radial-spherical-decomposition
  - eigenvalues-of-spherical-laplacian
  - polynomial-spaces-on-sphere
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the spherical Laplace operator?"
  - "How does representation theory help find eigenvalues of the spherical Laplacian?"
---

# Quick Definition

The spherical Laplace operator $\Delta_{\mathrm{sph}}$ is the angular part of the Laplacian on $\mathbb{R}^3$, equal to $J_x^2 + J_y^2 + J_z^2$ where $J_x, J_y, J_z$ are generators of $\mathfrak{so}(3,\mathbb{R})$. It is essentially the Casimir element of $\mathfrak{so}(3,\mathbb{R})$ and commutes with the $SO(3)$ action.

# Core Definition

**Lemma 5.8** (Kirillov, pp. 61-62): The Laplacian $\Delta = \partial_x^2 + \partial_y^2 + \partial_z^2$ on $\mathbb{R}^3$ can be decomposed as:

$$\Delta = \frac{1}{r^2}\Delta_{\mathrm{sph}} + \Delta_{\mathrm{radial}}$$

where $\Delta_{\mathrm{radial}} = \partial_r^2 + \frac{2}{r}\partial_r$ and

$$\Delta_{\mathrm{sph}} = J_x^2 + J_y^2 + J_z^2$$

with $J_x = y\partial_z - z\partial_y$, $J_y = z\partial_x - x\partial_z$, $J_z = x\partial_y - y\partial_x$ being the vector fields generating rotations (generators of $\mathfrak{so}(3,\mathbb{R})$).

# Prerequisites

- **Casimir operator** — $\Delta_{\mathrm{sph}}$ is the Casimir element of $\mathfrak{so}(3,\mathbb{R})$
- **Classification of sl(2,C) representations** — Used to find eigenvalues

# Key Properties

1. $\Delta_{\mathrm{sph}}$ is a differential operator on $S^2$
2. It commutes with the action of $SO(3,\mathbb{R})$ on functions on $S^2$ (Lemma 5.9)
3. This commutation follows from $\Delta_{\mathrm{sph}}$ being a Casimir element (central in $U\mathfrak{so}(3,\mathbb{R})$)
4. Its eigenvalues are $\lambda_k = -k(k+1)$ with multiplicity $2k+1$ (Theorem 5.11)
5. Every eigenfunction is a polynomial (Theorem 5.12)

# Construction / Recognition

## Key Insight:
$\Delta_{\mathrm{sph}} = J_x^2 + J_y^2 + J_z^2$ is (up to a factor) the Casimir element of $\mathfrak{so}(3,\mathbb{R})$ corresponding to the invariant bilinear form $\mathrm{tr}(ab)$. Therefore:
1. It commutes with $SO(3)$ action
2. It acts as a scalar on each irreducible representation
3. Finding its eigenvalues reduces to computing Casimir eigenvalues

# Context & Application

This is the motivating application of the chapter: using representation theory to diagonalize a differential operator. Instead of solving a PDE, one decomposes the function space into irreducible $SO(3)$-representations and reads off eigenvalues from the Casimir. This is far more efficient than working in coordinates.

The eigenvalues of $\Delta_{\mathrm{sph}}$ are directly relevant to:
- Spherical harmonics ($Y_l^m$ are eigenfunctions)
- The hydrogen atom (via separation of variables)
- Any rotationally symmetric physical system

# Examples

**Theorem 5.11** (p. 64): Eigenvalues of $\Delta_{\mathrm{sph}}$ in the space of polynomial functions $P_n$ are $\lambda_k = -k(k+1)$ for $k = 0, \ldots, n$, with multiplicity $\dim V_{2k} = 2k+1$.

# Relationships

## Builds Upon
- **Casimir operator** — $\Delta_{\mathrm{sph}}$ is a Casimir element
- **Classification of sl(2,C) representations** — Determines eigenvalues

## Enables
- **Eigenvalues of spherical Laplacian** — The main result
- **Hydrogen atom** — Via separation of variables

## Related
- **Radial-spherical decomposition** — Splits $\Delta$ into radial and spherical parts

# Common Confusions

- **Confusion**: Thinking one needs to write $\Delta_{\mathrm{sph}}$ in spherical coordinates to find eigenvalues.
  **Clarification**: The representation-theoretic approach is far more elegant. As Kirillov notes, the coordinate expression "is very messy; more importantly, it will be useless for our purposes" (p. 62).

# Source Reference

Chapter 5, Section 5.2, Lemma 5.8, Lemma 5.9, Theorem 5.11, pp. 61-64.

# Verification Notes

- Definition source: Direct from Lemma 5.8
- Confidence rationale: Explicit formula and proof
- Uncertainties: None
- Cross-reference status: Verified
