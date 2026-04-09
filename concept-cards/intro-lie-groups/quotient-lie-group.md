---
# === CORE IDENTIFICATION ===
concept: Quotient Lie Group
slug: quotient-lie-group

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
pdf_page: 10
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "factor group of Lie groups"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - lie-subgroup
  - coset-space
extends:
  - coset-space
related:
  - homomorphism-theorem-for-lie-groups
  - quotient-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

When $H$ is a normal Lie subgroup of $G$, the coset space $G/H$ inherits a canonical Lie group structure, called the quotient Lie group.

# Core Definition

**Theorem 2.10, part (2)** (Kirillov): If $H$ is a normal Lie subgroup then $G/H$ has a canonical structure of a Lie group.

Its Lie algebra is the quotient $\mathfrak{g}/\mathfrak{h}$ (Theorem 3.19).

# Prerequisites

- **Lie group** — the ambient group
- **Lie subgroup** — must be normal for the quotient to be a group
- **Coset space** — the quotient inherits its manifold structure from the coset space

# Key Properties

1. The Lie algebra of $G/H$ is $\mathfrak{g}/\mathfrak{h}$ (Theorem 3.19 part 2).
2. $\dim(G/H) = \dim G - \dim H$.
3. If $H$ is connected and $\mathfrak{h}$ is an ideal, then $H$ is normal (Theorem 3.19 part 2, converse).

# Construction / Recognition

## To Construct/Create:
1. Verify $H$ is a normal Lie subgroup of $G$.
2. The coset space $G/H$ automatically has Lie group structure.

## To Identify/Recognize:
1. A Lie group that arises as the quotient of another Lie group by a normal subgroup.

# Context & Application

Quotient Lie groups appear in the homomorphism theorem (Theorem 2.12) and in the classification of Lie groups with a given Lie algebra via discrete central subgroups (Corollary 3.49).

# Examples

**Example** (p. 18-19): $\mathrm{SO}(3, \mathbb{R}) \cong \mathrm{SU}(2)/\mathbb{Z}_2$ where $\mathbb{Z}_2 = \{I, -I\}$ is a discrete normal subgroup.

**Example** (p. 9): $G/G^0$ is a discrete quotient Lie group.

# Relationships

## Builds Upon
- **Coset space** — provides manifold structure

## Enables
- **Quotient Lie algebra** — the Lie algebra of $G/H$ is $\mathfrak{g}/\mathfrak{h}$

## Related
- **Homomorphism theorem for Lie groups** — $G_1/\mathrm{Ker}\, f \cong \mathrm{Im}\, f$

# Common Errors

- **Error**: Attempting to form $G/H$ as a Lie group when $H$ is not normal.
  **Correction**: $G/H$ is a manifold for any Lie subgroup, but is a Lie group only when $H$ is normal.

# Common Confusions

- **Confusion**: Confusing quotient Lie groups with coset spaces.
  **Clarification**: Every quotient Lie group is a coset space, but not every coset space is a group.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Theorem 2.10(2), page 10.

# Verification Notes

- Definition source: Direct from Theorem 2.10 part (2)
- Confidence rationale: Explicit theorem in source
- Uncertainties: None
- Cross-reference status: Verified with Theorem 2.12, Theorem 3.19, Corollary 3.49
