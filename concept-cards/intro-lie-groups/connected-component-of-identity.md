---
# === CORE IDENTIFICATION ===
concept: Connected Component of Identity
slug: connected-component-of-identity

# === CLASSIFICATION ===
category: lie-groups
subcategory: subgroups
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 9
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "identity component"
  - "$G^0$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - lie-subgroup
  - universal-cover-of-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can the study of Lie groups be reduced to connected Lie groups?"
---

# Quick Definition

The connected component of the identity $G^0$ in a Lie group $G$ is the connected component containing the identity element $1$. It is always a normal Lie subgroup with discrete quotient $G/G^0$.

# Core Definition

**Theorem 2.4** (Kirillov): Let $G$ be a Lie group. Denote by $G^0$ the connected component of unity. Then $G^0$ is a normal subgroup of $G$ and is a Lie group itself. The quotient group $G/G^0$ is discrete.

# Prerequisites

- **Lie group** — the ambient group whose component we take

# Key Properties

1. $G^0$ is closed under multiplication and inversion (since continuous images of connected sets are connected).
2. $G^0$ is a normal subgroup: for any $g \in G$, conjugation by $g$ maps $G^0$ to itself (since conjugation is continuous and fixes $1$).
3. The quotient $G/G^0$ is discrete, reducing the study to discrete groups and connected Lie groups.
4. If $G$ is connected and $U$ is any neighborhood of $1$, then $U$ generates $G$ (Corollary 2.9).

# Construction / Recognition

## To Construct/Create:
1. Take the connected component of $G$ containing the identity element.

## To Identify/Recognize:
1. It is the largest connected subset of $G$ containing $1$.

# Context & Application

This theorem reduces the study of arbitrary Lie groups to the study of finite (discrete) groups and connected Lie groups. One can go further and reduce to simply-connected Lie groups via the universal cover.

# Examples

**Example** (p. 16): $\mathrm{O}(n, \mathbb{R})$ has two connected components; $\mathrm{SO}(n, \mathbb{R})$ is the connected component of the identity. Both have the same Lie algebra $\{x \mid x + x^t = 0\}$.

**Example** (p. 8): $\mathrm{GL}(n, \mathbb{R})$ has two connected components (positive and negative determinant); $\pi_0(\mathrm{GL}(n, \mathbb{R})) = \mathbb{Z}_2$.

# Relationships

## Builds Upon
- **Lie group** — the group whose identity component we consider

## Enables
- **Universal cover of Lie group** — further reduces to simply-connected case
- **Corollary 2.9** — neighborhoods of identity generate connected Lie groups

## Related
- **Lie subgroup** — $G^0$ is a particular Lie subgroup

# Common Errors

- **Error**: Assuming $G^0$ and $G$ have different Lie algebras.
  **Correction**: Since $G^0$ is open in $G$, they share the same tangent space at identity, hence the same Lie algebra.

# Common Confusions

- **Confusion**: Confusing $G^0$ with the trivial subgroup.
  **Clarification**: $G^0$ is typically a large subgroup; it equals $G$ when $G$ is connected.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Theorem 2.4, page 9.

# Verification Notes

- Definition source: Direct from Theorem 2.4
- Confidence rationale: Explicit theorem with proof sketch in source
- Uncertainties: None
- Cross-reference status: Verified with classical group tables on pp. 16-17
