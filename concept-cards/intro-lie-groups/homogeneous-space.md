---
# === CORE IDENTIFICATION ===
concept: Homogeneous Space
slug: homogeneous-space

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
pdf_page: 12
section: "2.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "G-homogeneous space"
  - "transitive G-space"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action-on-manifold
  - orbit
  - stabilizer-subgroup
  - coset-space
extends:
  - orbit
related:
  - flag-manifold
  - grassmannian
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

A $G$-homogeneous space is a manifold $M$ with a transitive action of a Lie group $G$, meaning there is only one orbit. Every homogeneous space is diffeomorphic to a coset space $G/H$.

# Core Definition

**Definition 2.20** (Kirillov): A $G$-homogeneous space is a manifold with a transitive action of $G$.

By Corollary 2.19, each homogeneous space is diffeomorphic to a coset space $G/H$ where $H = \mathrm{Stab}_G(m)$ for any point $m \in M$.

# Prerequisites

- **Group action on a manifold** — the action must be transitive
- **Orbit** — a homogeneous space is a single orbit
- **Stabilizer subgroup** — the stabilizer determines the coset space
- **Coset space** — homogeneous spaces are diffeomorphic to coset spaces

# Key Properties

1. Every homogeneous space is diffeomorphic to $G/\mathrm{Stab}(m)$ for any $m \in M$.
2. The map $G \to M: g \mapsto gm$ is a fiber bundle over $M$ with fiber $\mathrm{Stab}(m)$ (Corollary 2.21).
3. A $G$-homogeneous space can be used to define smooth structure on a set with a transitive $G$-action.

# Construction / Recognition

## To Construct/Create:
1. Take a Lie group $G$ and a Lie subgroup $H$.
2. The coset space $G/H$ is a homogeneous space for $G$.
3. Alternatively, find a set with a transitive $G$-action.

## To Identify/Recognize:
1. A manifold where $G$ acts transitively (any point can be mapped to any other).

# Context & Application

Many important geometric spaces are homogeneous: spheres, projective spaces, Grassmannians, flag manifolds. The homogeneous space structure provides a powerful way to study their geometry.

# Examples

**Example 2.22** (p. 12):
- $S^{n-1} \cong \mathrm{SO}(n, \mathbb{R})/\mathrm{SO}(n-1, \mathbb{R})$
- $S^{2n-1} \cong \mathrm{SU}(n)/\mathrm{SU}(n-1)$

**Example 2.23** (p. 13): The flag manifold $\mathcal{B}_n(\mathbb{R}) \cong \mathrm{GL}(n, \mathbb{R})/B(n, \mathbb{R})$ has dimension $n(n-1)/2$.

**Example** (Exercise 2.5): The Grassmannian $G_{n,k} \cong \mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$.

# Relationships

## Builds Upon
- **Orbit** — a homogeneous space is a single orbit
- **Coset space** — the underlying manifold structure

## Enables
- **Flag manifold** — an important example
- **Grassmannian** — another important example
- **Topological computations** — fiber bundle structure enables computing $\pi_0$, $\pi_1$

## Related
- **Fiber bundle** — $G \to G/H$ is a fiber bundle

# Common Errors

- **Error**: Assuming the stabilizer is the same for all points.
  **Correction**: Stabilizers at different points are conjugate: $\mathrm{Stab}(g.m) = g \cdot \mathrm{Stab}(m) \cdot g^{-1}$.

# Common Confusions

- **Confusion**: Confusing homogeneous spaces with symmetric spaces.
  **Clarification**: Every symmetric space is homogeneous, but not every homogeneous space is symmetric (symmetry requires additional involution structure).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.3, Definition 2.20, Corollary 2.21, pages 12-13.

# Verification Notes

- Definition source: Direct from Definition 2.20
- Confidence rationale: Explicit definition with multiple examples
- Uncertainties: None
- Cross-reference status: Verified with Examples 2.22, 2.23, Corollary 2.21
