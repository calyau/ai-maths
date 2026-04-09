---
# === CORE IDENTIFICATION ===
concept: "SO(3) Commutation with Spherical Laplacian"
slug: so3-commutation-with-laplacian

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
pdf_page: 62
section: "5.2 Spherical Laplace operator and hydrogen atom"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spherical-laplace-operator
  - casimir-operator
extends: []
related:
  - eigenvalues-of-spherical-laplacian
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does the spherical Laplacian commute with rotations?"
---

# Quick Definition

The spherical Laplacian $\Delta_{\mathrm{sph}}$ commutes with the action of $SO(3,\mathbb{R})$ on $C^\infty(S^2)$ because it is (up to a factor) the Casimir element of $\mathfrak{so}(3,\mathbb{R})$, hence central in $U\mathfrak{so}(3,\mathbb{R})$.

# Core Definition

**Lemma 5.9** (Kirillov, p. 62): $\Delta_{\mathrm{sph}}: C^\infty(S^2) \to C^\infty(S^2)$ commutes with the action of $SO(3,\mathbb{R})$.

**Proof**: $\Delta_{\mathrm{sph}} = J_x^2 + J_y^2 + J_z^2$ is the element $C \in U\mathfrak{so}(3,\mathbb{R})$ corresponding to the Casimir. Centrality is verified by $[J_x, C] = [J_x, J_y^2] + [J_x, J_z^2] = J_z J_y + J_y J_z - J_y J_z - J_z J_y = 0$.

# Prerequisites

- **Spherical Laplace operator** — The operator in question
- **Casimir operator** — $\Delta_{\mathrm{sph}}$ is a Casimir element

# Key Properties

1. Commutation means eigenspaces of $\Delta_{\mathrm{sph}}$ are $SO(3)$-representations
2. This allows decomposing eigenspaces into irreducibles
3. By Schur's lemma, $\Delta_{\mathrm{sph}}$ acts as a scalar on each irreducible

# Context & Application

This is the representation-theoretic reason why the eigenvalue problem for $\Delta_{\mathrm{sph}}$ reduces to computing Casimir eigenvalues on irreducible representations. The symmetry does all the work.

# Relationships

## Builds Upon
- **Casimir operator** — $\Delta_{\mathrm{sph}}$ is a Casimir element

## Enables
- **Eigenvalues of spherical Laplacian** — Computed via representation theory

# Source Reference

Chapter 5, Section 5.2, Lemma 5.9, p. 62.

# Verification Notes

- Definition source: Direct from Lemma 5.9
- Confidence rationale: Explicit lemma with proof
- Uncertainties: None
- Cross-reference status: Verified
