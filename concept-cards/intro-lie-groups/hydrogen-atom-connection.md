---
# === CORE IDENTIFICATION ===
concept: Hydrogen Atom Connection
slug: hydrogen-atom-connection

# === CLASSIFICATION ===
category: applications
subcategory: hydrogen-atom
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 62
section: "5.2 Spherical Laplace operator and hydrogen atom"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "central force problem"
  - "Schrodinger equation and angular momentum"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spherical-laplace-operator
  - eigenvalues-of-spherical-laplacian
  - radial-spherical-decomposition
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does representation theory connect to the hydrogen atom?"
---

# Quick Definition

The hydrogen atom Hamiltonian $H = -\Delta - c/r$ can be analyzed via separation of variables using the eigenvalues of $\Delta_{\mathrm{sph}}$. The $SO(3)$ symmetry of the central force potential enables this decomposition, reducing the 3D problem to a family of 1D radial equations.

# Core Definition

(Kirillov, pp. 62-63): The quantum-mechanical Hamiltonian for a particle in a central force field is $H = -\Delta + V(r)$. Using the decomposition $\Delta = \frac{1}{r^2}\Delta_{\mathrm{sph}} + \Delta_{\mathrm{radial}}$ and writing $\psi(\vec{x}) = \sum f_i(r) g_i(\mathbf{u})$ where $g_i$ are eigenfunctions of $\Delta_{\mathrm{sph}}$, the equation $H\psi = \lambda\psi$ reduces to a second-order ODE for each $f_i(r)$.

For the hydrogen atom: $V(r) = -c/r$ with $c > 0$ (Exercise 5.4).

# Prerequisites

- **Spherical Laplace operator** — The angular part of the Hamiltonian
- **Eigenvalues of spherical Laplacian** — $\lambda_k = -k(k+1)$ substituted into the radial equation
- **Radial-spherical decomposition** — The separation of variables

# Key Properties

1. The Schrodinger equation is $\dot{\psi} = iH\psi$ where $H = -\Delta + V(r)$
2. Separation of variables: $\psi = \sum f_i(r) g_i(\mathbf{u})$ with $\Delta_{\mathrm{sph}} g_i = \lambda_i g_i$
3. Substituting eigenvalues of $\Delta_{\mathrm{sph}}$ gives an ODE for each $f_i$
4. For the Coulomb potential $V = -c/r$, the radial equation can be solved explicitly
5. The energy levels and their degeneracies are determined by representation theory

# Context & Application

This is the physical motivation for the entire Chapter 5. The representation-theoretic approach to the spherical Laplacian demonstrates how symmetry (the $SO(3)$ invariance of the Coulomb potential) can be exploited to solve differential equations. This is a paradigmatic example of the utility of Lie group theory in physics.

# Examples

**Exercise 5.4** (p. 65): Find eigenvalues and multiplicities of $H = -\Delta - c/r$ in $L^2(\mathbb{R}^3, \mathbb{C})$ (the hydrogen atom).

# Relationships

## Builds Upon
- **Eigenvalues of spherical Laplacian** — Provides the angular eigenvalues
- **Radial-spherical decomposition** — Enables separation of variables

# Common Confusions

- **Confusion**: Thinking representation theory alone solves the hydrogen atom.
  **Clarification**: Representation theory determines the angular part. The radial equation still requires solving an ODE, which uses classical analysis techniques (not covered in this text).

# Source Reference

Chapter 5, Section 5.2, pp. 62-63, Exercise 5.4, p. 65.

# Verification Notes

- Definition source: Synthesized from discussion on pp. 62-63
- Confidence rationale: Medium — the text sketches the connection without fully developing it; Exercise 5.4 asks the reader to complete the computation
- Uncertainties: Full eigenvalue computation deferred to Exercise 5.4 and reference [16]
- Cross-reference status: Verified
