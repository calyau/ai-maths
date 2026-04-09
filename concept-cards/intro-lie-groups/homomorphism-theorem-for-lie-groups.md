---
# === CORE IDENTIFICATION ===
concept: Homomorphism Theorem for Lie Groups
slug: homomorphism-theorem-for-lie-groups

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
  - "first isomorphism theorem for Lie groups"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group-morphism
  - lie-subgroup
  - coset-space
extends: []
related:
  - immersed-subgroup
  - quotient-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

For a morphism $f: G_1 \to G_2$ of Lie groups, the kernel is a normal Lie subgroup, and if the image is closed, then $G_1/\mathrm{Ker}\, f \cong \mathrm{Im}\, f$ as Lie groups.

# Core Definition

**Theorem 2.12** (Kirillov): Let $f: G_1 \to G_2$ be a morphism of Lie groups. Then $H = \mathrm{Ker}\, f$ is a normal Lie subgroup in $G_1$, and $f$ gives rise to an injective morphism $G_1/H \to G_2$, which is an immersion of manifolds. If $\mathrm{Im}\, f$ is closed, then it is a Lie subgroup in $G_2$ and $f$ gives an isomorphism of Lie groups $G_1/H \simeq \mathrm{Im}\, f$.

# Prerequisites

- **Lie group morphism** — the map being analyzed
- **Lie subgroup** — kernel is a Lie subgroup
- **Coset space** — $G_1/\mathrm{Ker}\, f$ is a coset space

# Key Properties

1. $\mathrm{Ker}\, f$ is always a normal Lie subgroup.
2. The induced map $G_1/\mathrm{Ker}\, f \to G_2$ is always an injective immersion.
3. If $\mathrm{Im}\, f$ is closed, we get a full isomorphism $G_1/\mathrm{Ker}\, f \cong \mathrm{Im}\, f$.
4. If $\mathrm{Im}\, f$ is not closed, the image is only an immersed subgroup.

# Construction / Recognition

## To Construct/Create:
1. Given a Lie group morphism $f: G_1 \to G_2$, compute $\mathrm{Ker}\, f$.
2. Form the quotient $G_1/\mathrm{Ker}\, f$.
3. This quotient maps injectively into $G_2$ via the induced map.

## To Identify/Recognize:
1. Any time you see a surjective Lie group morphism, the domain modulo kernel equals the codomain.

# Context & Application

This is the Lie group analog of the first isomorphism theorem for groups. It is used to establish relationships between classical groups (e.g., $\mathrm{SU}(2)/\mathbb{Z}_2 \cong \mathrm{SO}(3, \mathbb{R})$).

# Examples

**Example 2.13** (p. 11): The map $f: \mathbb{R} \to T^2$ given by $f(t) = (t \mod \mathbb{Z}, \alpha t \mod \mathbb{Z})$ for irrational $\alpha$ has image that is everywhere dense in $T^2$ but not closed. The image is an immersed subgroup but not a Lie subgroup.

**Example** (p. 18-19): The morphism $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$ has kernel $\mathbb{Z}_2$, giving $\mathrm{SU}(2)/\mathbb{Z}_2 \cong \mathrm{SO}(3, \mathbb{R})$.

# Relationships

## Builds Upon
- **Lie group morphism** — the map being analyzed
- **Lie subgroup** — kernel is a Lie subgroup

## Enables
- **Immersed subgroup** — the image may be an immersed subgroup when not closed

## Related
- **Quotient Lie group** — $G_1/\mathrm{Ker}\, f$ is a quotient Lie group

# Common Errors

- **Error**: Assuming the image of a Lie group morphism is always a Lie subgroup.
  **Correction**: The image is a Lie subgroup only if it is closed. Otherwise it is only an immersed subgroup (Example 2.13).

# Common Confusions

- **Confusion**: Whether the theorem requires $f$ to be surjective.
  **Clarification**: No. The theorem applies to any morphism; the isomorphism is between $G_1/\mathrm{Ker}\, f$ and $\mathrm{Im}\, f$ (not all of $G_2$).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Theorem 2.12, page 11.

# Verification Notes

- Definition source: Direct from Theorem 2.12
- Confidence rationale: Explicit theorem in source; proof deferred to Corollary 3.27
- Uncertainties: None
- Cross-reference status: Proof given at Corollary 3.27 in Chapter 3
