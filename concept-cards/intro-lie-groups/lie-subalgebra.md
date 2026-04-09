---
# === CORE IDENTIFICATION ===
concept: Lie Subalgebra
slug: lie-subalgebra

# === CLASSIFICATION ===
category: lie-algebras
subcategory: subalgebras-ideals
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 25
section: "3.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "subalgebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - lie-subgroup
  - ideal-of-lie-algebra
  - immersed-subgroup
contrasts_with:
  - ideal-of-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

A Lie subalgebra $\mathfrak{h} \subset \mathfrak{g}$ is a subspace closed under the commutator: $[x, y] \in \mathfrak{h}$ for all $x, y \in \mathfrak{h}$.

# Core Definition

**Definition 3.18** (Kirillov): Let $\mathfrak{g}$ be a Lie algebra. A subspace $\mathfrak{h} \subset \mathfrak{g}$ is called a Lie subalgebra if it is closed under commutator, i.e., for any $x, y \in \mathfrak{h}$, we have $[x, y] \in \mathfrak{h}$.

**Theorem 3.19 part (1)**: If $H$ is a Lie subgroup in $G$, then $\mathfrak{h} = T_1H$ is a Lie subalgebra in $\mathfrak{g}$.

# Prerequisites

- **Lie algebra** — the ambient algebra

# Key Properties

1. Every Lie subgroup gives a subalgebra (Theorem 3.19).
2. Every subalgebra corresponds to a connected immersed subgroup (Theorem 3.43).
3. A subalgebra is itself a Lie algebra with the inherited bracket.

# Construction / Recognition

## To Construct/Create:
1. Take a subspace of $\mathfrak{g}$.
2. Verify it is closed under the bracket.

## To Identify/Recognize:
1. A subspace $\mathfrak{h}$ with $[\mathfrak{h}, \mathfrak{h}] \subset \mathfrak{h}$.

# Context & Application

Subalgebras are the Lie algebra analog of subgroups. Every subalgebra corresponds to a (possibly immersed) subgroup.

# Examples

**Example** (p. 30): $\mathfrak{h} = \{(t, \alpha t) \mid t \in \mathbb{R}\} \subset \mathbb{R}^2$ is a subalgebra (trivially, since the bracket is zero), but corresponds only to an immersed subgroup (irrational winding) when $\alpha$ is irrational.

**Example** (p. 25): $\mathfrak{h} = T_1H$ for any Lie subgroup $H$.

# Relationships

## Builds Upon
- **Lie algebra** — subalgebras are subspaces with inherited structure

## Enables
- **Immersed subgroup** — every subalgebra corresponds to one (Theorem 3.43)

## Related
- **Lie subgroup** — gives rise to a subalgebra

## Contrasts With
- **Ideal of Lie algebra** — an ideal has the stronger condition $[\mathfrak{g}, \mathfrak{h}] \subset \mathfrak{h}$

# Common Errors

- **Error**: Assuming every subalgebra corresponds to a closed (Lie) subgroup.
  **Correction**: It corresponds to an immersed subgroup, which may not be closed (Example 3.37).

# Common Confusions

- **Confusion**: Confusing subalgebras with ideals.
  **Clarification**: A subalgebra requires $[\mathfrak{h}, \mathfrak{h}] \subset \mathfrak{h}$; an ideal requires $[\mathfrak{g}, \mathfrak{h}] \subset \mathfrak{h}$.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.4, Definition 3.18, page 25.

# Verification Notes

- Definition source: Direct from Definition 3.18
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.19, 3.43
