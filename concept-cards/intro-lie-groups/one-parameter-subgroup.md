---
# === CORE IDENTIFICATION ===
concept: One-Parameter Subgroup
slug: one-parameter-subgroup

# === CLASSIFICATION ===
category: lie-groups
subcategory: classical-groups
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 16
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "group morphism from $\\mathbb{R}$"
  - "$\\gamma_x(t)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - matrix-exponential
extends: []
related:
  - exponential-map
  - left-invariant-vector-field
  - immersed-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the exponential map?"
  - "How do I use the exponential map to go between Lie group and Lie algebra?"
---

# Quick Definition

A one-parameter subgroup of a Lie group $G$ is a Lie group morphism $\gamma: \mathbb{R} \to G$, i.e., a smooth curve satisfying $\gamma(t+s) = \gamma(t)\gamma(s)$. For matrix groups, $\gamma(t) = \exp(tx)$ for a unique $x \in \mathfrak{g}$.

# Core Definition

**Proposition 3.1** (Kirillov): Let $G$ be a Lie group, $\mathfrak{g} = T_1G$, and let $x \in \mathfrak{g}$. Then there exists a unique morphism of Lie groups $\gamma_x: \mathbb{R} \to G$ such that $\dot{\gamma}_x(0) = x$.

For matrix groups (Theorem 2.28 part 4): $t \mapsto \exp(tx)$ is a one-parameter subgroup with tangent vector $x$ at $t = 0$.

# Prerequisites

- **Lie group** — the group containing the subgroup
- **Matrix exponential** — constructs one-parameter subgroups for matrix groups

# Key Properties

1. $\gamma_x(t)$ is uniquely determined by $x = \dot{\gamma}(0) \in T_1G$.
2. $\gamma_x(\lambda t) = \gamma_{\lambda x}(t)$ (Kirillov, p. 20).
3. For matrix groups, $\gamma_x(t) = \exp(tx)$.
4. One-parameter subgroups are integral curves of left-invariant vector fields.
5. The image of a one-parameter subgroup is an immersed subgroup (Example 3.41).

# Construction / Recognition

## To Construct/Create:
1. Choose $x \in \mathfrak{g}$.
2. The one-parameter subgroup is $\gamma_x(t) = \exp(tx)$.

## To Identify/Recognize:
1. A smooth homomorphism $\mathbb{R} \to G$.

# Context & Application

One-parameter subgroups are the building blocks for the exponential map, which is defined as $\exp(x) = \gamma_x(1)$. They connect the Lie algebra to the Lie group.

# Examples

**Example 3.10** (p. 22): In $\mathrm{SO}(3, \mathbb{R})$, the one-parameter subgroups $\exp(tJ_x)$, $\exp(tJ_y)$, $\exp(tJ_z)$ are rotations around the coordinate axes.

**Example** (p. 16): The name "one-parameter subgroup" is not quite accurate since the image may not be a Lie subgroup (e.g., irrational winding on a torus).

# Relationships

## Builds Upon
- **Matrix exponential** — $\gamma_x(t) = \exp(tx)$ for matrix groups
- **Lie group** — the group containing the subgroup

## Enables
- **Exponential map** — defined via $\exp(x) = \gamma_x(1)$

## Related
- **Left-invariant vector field** — one-parameter subgroup is its integral curve through $1$
- **Immersed subgroup** — image of a one-parameter subgroup

# Common Errors

- **Error**: Assuming the image of a one-parameter subgroup is always a Lie subgroup.
  **Correction**: The image may be dense (e.g., irrational winding on torus); it is always an immersed subgroup.

# Common Confusions

- **Confusion**: Whether "one-parameter subgroup" refers to the map $\gamma$ or its image.
  **Clarification**: Strictly, it is the morphism $\gamma: \mathbb{R} \to G$, though the name suggests a subgroup.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, Theorem 2.28 part (4), page 16. Also Proposition 3.1, page 20.

# Verification Notes

- Definition source: Direct from Theorem 2.28(4) and Proposition 3.1
- Confidence rationale: Explicit in source
- Uncertainties: None
- Cross-reference status: Verified with Example 3.10, Definition 3.2
