---
# === CORE IDENTIFICATION ===
concept: Flag Manifold
slug: flag-manifold

# === CLASSIFICATION ===
category: lie-groups
subcategory: homogeneous-spaces
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 13
section: "2.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathcal{B}_n(\\mathbb{K})$"
  - "flag variety"
  - "complete flag variety"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homogeneous-space
  - general-linear-group
extends:
  - homogeneous-space
related:
  - coset-space
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

The flag manifold $\mathcal{B}_n(\mathbb{K})$ is the set of all complete flags $\{0\} \subset V_1 \subset \cdots \subset V_n = \mathbb{K}^n$ (with $\dim V_i = i$). It is a homogeneous space $\mathrm{GL}(n, \mathbb{K})/B(n, \mathbb{K})$ of dimension $n(n-1)/2$.

# Core Definition

**Example 2.23** (Kirillov): A flag in $\mathbb{R}^n$ is a sequence $\{0\} \subset V_1 \subset V_2 \subset \cdots \subset V_n = \mathbb{R}^n$ with $\dim V_i = i$. The set $\mathcal{B}_n(\mathbb{R})$ of all flags is a homogeneous space for $\mathrm{GL}(n, \mathbb{R})$ with stabilizer $B(n, \mathbb{R})$ (invertible upper-triangular matrices) for the standard flag.

Thus $\mathcal{B}_n(\mathbb{R}) = \mathrm{GL}(n, \mathbb{R})/B(n, \mathbb{R})$, a manifold of dimension $n^2 - n(n+1)/2 = n(n-1)/2$.

# Prerequisites

- **Homogeneous space** — flag manifold is a homogeneous space
- **General linear group** — acts transitively on flags

# Key Properties

1. $\dim \mathcal{B}_n = n(n-1)/2$.
2. $\mathcal{B}_n(\mathbb{C}) = \mathrm{GL}(n, \mathbb{C})/B(n, \mathbb{C}) = \mathrm{U}(n)/T(n)$ where $T(n)$ is the $n$-torus (Exercise 2.4).
3. $\mathcal{B}_n(\mathbb{C})$ is a compact complex manifold.

# Construction / Recognition

## To Construct/Create:
1. Take the orbit of the standard flag under $\mathrm{GL}(n)$.
2. The stabilizer is the Borel subgroup $B(n)$ of upper-triangular matrices.

## To Identify/Recognize:
1. The space of all complete flags in $\mathbb{K}^n$.

# Context & Application

Flag manifolds are central objects in representation theory and algebraic geometry. They appear as $G/B$ where $B$ is a Borel subgroup.

# Examples

**Example 2.23** (p. 13): The standard flag is $V^{st} = (\{0\} \subset \langle e_1 \rangle \subset \langle e_1, e_2 \rangle \subset \cdots \subset \mathbb{R}^n)$.

**Exercise 2.4** (p. 18): $\mathcal{B}_n(\mathbb{C}) = \mathrm{U}(n)/T(n)$ where $T(n) \cong (\mathbb{R}/\mathbb{Z})^n$.

# Relationships

## Builds Upon
- **Homogeneous space** — $\mathcal{B}_n = G/B$

## Enables
- **Borel subgroup** — $B(n)$ is the stabilizer of the standard flag

## Related
- **Coset space** — $G/B$ structure

# Common Errors

- **Error**: Confusing the flag manifold with the Grassmannian.
  **Correction**: The Grassmannian $G_{n,k}$ parametrizes $k$-planes; the flag manifold parametrizes complete chains of subspaces.

# Common Confusions

- **Confusion**: Whether the flag manifold depends on the choice of standard flag.
  **Clarification**: No, any flag can serve as basepoint; different choices give conjugate stabilizers.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.3, Example 2.23, page 13. Exercise 2.4, page 18.

# Verification Notes

- Definition source: Direct from Example 2.23
- Confidence rationale: Explicit example with dimension computation
- Uncertainties: None
- Cross-reference status: Verified with Exercise 2.4
