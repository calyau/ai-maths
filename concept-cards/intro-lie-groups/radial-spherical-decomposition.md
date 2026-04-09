---
# === CORE IDENTIFICATION ===
concept: Radial-Spherical Decomposition
slug: radial-spherical-decomposition

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
  - "polar decomposition of Laplacian"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spherical-laplace-operator
extends: []
related:
  - hydrogen-atom-connection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is the Laplacian decomposed into radial and spherical parts?"
---

# Quick Definition

The Laplacian on $\mathbb{R}^3 \setminus \{0\}$ splits as $\Delta = \frac{1}{r^2}\Delta_{\mathrm{sph}} + \Delta_{\mathrm{radial}}$, using the identification $\mathbb{R}^3 \setminus \{0\} \simeq S^2 \times \mathbb{R}_+$ via $\vec{x} \mapsto (\mathbf{u}, r)$ where $\mathbf{u} = \vec{x}/|\vec{x}|$ and $r = |\vec{x}|$.

# Core Definition

**Lemma 5.8** (Kirillov, p. 61): Under the identification $\mathbb{R}^3 \setminus \{0\} \simeq S^2 \times \mathbb{R}_+$:

$$\Delta = \frac{1}{r^2}\Delta_{\mathrm{sph}} + \Delta_{\mathrm{radial}}$$

where $\Delta_{\mathrm{radial}} = \partial_r^2 + \frac{2}{r}\partial_r$ and $\Delta_{\mathrm{sph}} = J_x^2 + J_y^2 + J_z^2$.

# Prerequisites

- **Spherical Laplace operator** — One component of the decomposition

# Key Properties

1. $\Delta_{\mathrm{sph}}$ acts on functions on $S^2$ (angular variables only)
2. $\Delta_{\mathrm{radial}}$ acts on functions of $r$ only
3. This separation enables the method of separation of variables
4. The $1/r^2$ factor couples the radial and spherical parts

# Context & Application

This decomposition is the starting point for the hydrogen atom problem and all central force problems in quantum mechanics. It allows separation of variables: write $\psi(\vec{x}) = \sum f_i(r) g_i(\mathbf{u})$ where $g_i$ are eigenfunctions of $\Delta_{\mathrm{sph}}$.

# Relationships

## Enables
- **Spherical Laplace operator** — Defines $\Delta_{\mathrm{sph}}$ as the angular part
- **Separation of variables** — The physical motivation

# Source Reference

Chapter 5, Section 5.2, Lemma 5.8, equation (5.5)-(5.6), pp. 61-62.

# Verification Notes

- Definition source: Direct from Lemma 5.8
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified
