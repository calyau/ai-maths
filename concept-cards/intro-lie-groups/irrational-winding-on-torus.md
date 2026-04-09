---
# === CORE IDENTIFICATION ===
concept: Irrational Winding on the Torus
slug: irrational-winding-on-torus

# === CLASSIFICATION ===
category: lie-groups
subcategory: subgroups
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 11
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "dense winding"
  - "dense one-parameter subgroup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - one-parameter-subgroup
  - immersed-subgroup
extends: []
related:
  - lie-subgroup
  - second-fundamental-theorem-of-lie-theory
contrasts_with:
  - lie-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

The irrational winding is the image of $f: \mathbb{R} \to T^2$ given by $f(t) = (t \bmod \mathbb{Z}, \alpha t \bmod \mathbb{Z})$ for irrational $\alpha$. It is everywhere dense in $T^2$, providing the canonical example of an immersed subgroup that is not a Lie subgroup.

# Core Definition

**Example 2.13** (Kirillov): Let $G_1 = \mathbb{R}$, $G_2 = T^2 = \mathbb{R}^2/\mathbb{Z}^2$. Define $f(t) = (t \bmod \mathbb{Z}, \alpha t \bmod \mathbb{Z})$ for irrational $\alpha$. The image is everywhere dense in $T^2$.

# Prerequisites

- **One-parameter subgroup** — the irrational winding is one
- **Immersed subgroup** — the image is an immersed subgroup

# Key Properties

1. The image is a subgroup of $T^2$.
2. The image is everywhere dense (not closed) in $T^2$.
3. The image is an immersed submanifold but not an embedded one.
4. The kernel of $f$ is trivial, so $f$ is injective.
5. The corresponding Lie subalgebra is $\{(t, \alpha t)\} \subset \mathbb{R}^2 = \mathrm{Lie}(T^2)$.

# Construction / Recognition

## To Construct/Create:
1. Choose an irrational $\alpha$.
2. Map $t \mapsto (t \bmod \mathbb{Z}, \alpha t \bmod \mathbb{Z})$.

## To Identify/Recognize:
1. A line of irrational slope on the torus $\mathbb{R}^2/\mathbb{Z}^2$.

# Context & Application

This is the key counterexample showing that:
1. The image of a Lie group morphism need not be a Lie subgroup (Theorem 2.12).
2. Not every Lie subalgebra corresponds to a Lie subgroup (Example 3.37).
3. The weaker notion of immersed subgroup is needed (Definition 3.39).

# Examples

**Example 2.13** (p. 11) and **Example 3.37** (p. 30): Both reference this construction.

# Relationships

## Builds Upon
- **One-parameter subgroup** — the winding is a one-parameter subgroup
- **Immersed subgroup** — the image has this structure

## Enables
- **Motivation for immersed subgroups** — shows why this notion is needed

## Contrasts With
- **Lie subgroup** — the image is not closed, hence not a Lie subgroup

# Common Errors

- **Error**: Assuming one-parameter subgroups always have closed image.
  **Correction**: The image can be dense, as this example shows.

# Common Confusions

- **Confusion**: Whether the irrational winding is a manifold.
  **Clarification**: With the subspace topology from $T^2$, it is not a manifold. But with the topology inherited from $\mathbb{R}$ (via the injective immersion), it is diffeomorphic to $\mathbb{R}$.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Example 2.13, page 11.

# Verification Notes

- Definition source: Direct from Example 2.13
- Confidence rationale: Explicit example, well-known
- Uncertainties: None
- Cross-reference status: Verified with Example 3.37
