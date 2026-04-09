---
# === CORE IDENTIFICATION ===
concept: Coset Space
slug: coset-space

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
pdf_page: 10
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "quotient space $G/H$"
  - "homogeneous space"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - lie-subgroup
extends: []
related:
  - fiber-bundle
  - homogeneous-space
  - quotient-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

The coset space $G/H$ of a Lie group $G$ by a Lie subgroup $H$ is a smooth manifold of dimension $\dim G - \dim H$, with the canonical map $p: G \to G/H$ forming a fiber bundle with fiber $H$.

# Core Definition

**Theorem 2.10** (Kirillov): Let $G$ be a Lie group of dimension $n$ and $H \subset G$ a Lie subgroup of dimension $k$. Then the coset space $G/H$ has a natural structure of a manifold of dimension $n - k$ such that the canonical map $p: G \to G/H$ is a fiber bundle, with fiber diffeomorphic to $H$. The tangent space at $\bar{1} = p(1)$ is given by $T_{\bar{1}}(G/H) = T_1G/T_1H$. If $H$ is a normal Lie subgroup then $G/H$ has a canonical structure of a Lie group.

# Prerequisites

- **Lie group** — the group $G$
- **Lie subgroup** — the subgroup $H$ being quotiented out

# Key Properties

1. $\dim(G/H) = \dim G - \dim H$.
2. The projection $p: G \to G/H$ is a fiber bundle with fiber $H$.
3. $T_{\bar{1}}(G/H) = T_1G / T_1H$.
4. If $H$ is normal, $G/H$ is itself a Lie group.
5. If $H$ is connected, then $\pi_0(G) = \pi_0(G/H)$ (Corollary 2.11).

# Construction / Recognition

## To Construct/Create:
1. Take a Lie group $G$ and a Lie subgroup $H$.
2. Form the set of left cosets $\{gH \mid g \in G\}$.
3. The smooth structure is obtained by choosing local transversal sections to $H$.

## To Identify/Recognize:
1. A manifold that arises as the set of orbits of the right action of $H$ on $G$.

# Context & Application

Coset spaces provide the manifold structure for orbits of group actions and are the geometric foundation for homogeneous spaces. They appear throughout geometry as spheres, Grassmannians, flag manifolds, etc.

# Examples

**Example 2.22** (p. 12): $S^{n-1} \cong \mathrm{SO}(n, \mathbb{R}) / \mathrm{SO}(n-1, \mathbb{R})$ and $S^{2n-1} \cong \mathrm{SU}(n) / \mathrm{SU}(n-1)$.

**Example 2.23** (p. 13): The flag manifold $\mathcal{B}_n(\mathbb{R}) = \mathrm{GL}(n, \mathbb{R}) / B(n, \mathbb{R})$ where $B(n, \mathbb{R})$ is the group of invertible upper-triangular matrices.

# Relationships

## Builds Upon
- **Lie group** — the group being quotiented
- **Lie subgroup** — the subgroup defining the cosets

## Enables
- **Homogeneous space** — every homogeneous space is a coset space
- **Fiber bundle** — $G \to G/H$ is a fiber bundle

## Related
- **Quotient Lie group** — when $H$ is normal

# Common Errors

- **Error**: Assuming $G/H$ is always a Lie group.
  **Correction**: $G/H$ is a Lie group only when $H$ is a normal subgroup. In general, it is only a manifold.

# Common Confusions

- **Confusion**: Confusing the coset space $G/H$ (set of left cosets) with the orbit space $M/G$ (set of orbits of an action on $M$).
  **Clarification**: The coset space $G/H$ is always a well-behaved manifold; the orbit space $M/G$ can be very singular.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Theorem 2.10, pages 10-11.

# Verification Notes

- Definition source: Direct from Theorem 2.10
- Confidence rationale: Explicit theorem with proof in source
- Uncertainties: None
- Cross-reference status: Verified with Examples 2.22, 2.23, Corollary 2.11
