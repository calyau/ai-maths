---
# === CORE IDENTIFICATION ===
concept: Universal Cover of a Lie Group
slug: universal-cover-of-lie-group

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
  - "$\\tilde{G}$"
  - "simply-connected cover"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - connected-component-of-identity
extends: []
related:
  - simply-connected-lie-group
  - spin-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

The universal cover $\tilde{G}$ of a connected Lie group $G$ carries a canonical Lie group structure such that the covering map $p: \tilde{G} \to G$ is a morphism of Lie groups with $\mathrm{Ker}\, p = \pi_1(G)$.

# Core Definition

**Theorem 2.5** (Kirillov): If $G$ is a connected Lie group then its universal cover $\tilde{G}$ has a canonical structure of a Lie group such that the covering map $p: \tilde{G} \to G$ is a morphism of Lie groups, and $\mathrm{Ker}\, p = \pi_1(G)$ as a group. Moreover, $\mathrm{Ker}\, p$ is a discrete central subgroup in $\tilde{G}$.

# Prerequisites

- **Lie group** — the group being covered
- **Connected component of identity** — must restrict to connected groups

# Key Properties

1. The kernel of $p$ is isomorphic to the fundamental group $\pi_1(G)$.
2. The kernel is a discrete central subgroup of $\tilde{G}$.
3. $\tilde{G}$ and $G$ have the same Lie algebra.
4. Any connected Lie group with a given Lie algebra is a quotient of the simply-connected cover by a discrete central subgroup (Corollary 3.49).

# Construction / Recognition

## To Construct/Create:
1. Take a connected Lie group $G$.
2. Form its topological universal cover $\tilde{G}$.
3. Lift the multiplication and inversion maps from $G$ to $\tilde{G}$ using the lifting property.

## To Identify/Recognize:
1. A connected, simply-connected Lie group covering $G$.

# Context & Application

This reduces the study of connected Lie groups to simply-connected ones plus discrete central subgroups. Combined with the fundamental theorems of Lie theory, it establishes the equivalence between simply-connected Lie groups and Lie algebras.

# Examples

**Example** (p. 17): The universal cover of $\mathrm{SO}(n, \mathbb{R})$ for $n \geq 3$ is the spin group $\mathrm{Spin}(n)$, a twofold cover since $\pi_1(\mathrm{SO}(n, \mathbb{R})) = \mathbb{Z}_2$.

**Example** (p. 18): $\mathrm{SU}(2) \cong S^3$ is the universal cover of $\mathrm{SO}(3, \mathbb{R})$, with $\mathrm{SO}(3,\mathbb{R}) \cong \mathrm{SU}(2)/\mathbb{Z}_2$.

# Relationships

## Builds Upon
- **Lie group** — the group being covered
- **Connected component of identity** — prerequisite for taking the cover

## Enables
- **Simply-connected Lie group** — the universal cover is always simply-connected
- **Fundamental theorems of Lie theory** — the equivalence of categories uses simply-connected groups

## Related
- **Spin group** — universal cover of $\mathrm{SO}(n, \mathbb{R})$

# Common Errors

- **Error**: Assuming the universal cover always differs from the original group.
  **Correction**: If $G$ is already simply-connected (e.g., $\mathrm{SU}(n)$ for $n \geq 2$), then $\tilde{G} = G$.

# Common Confusions

- **Confusion**: Whether the universal cover has the same Lie algebra.
  **Clarification**: Yes, $\mathrm{Lie}(\tilde{G}) = \mathrm{Lie}(G)$ since $p$ is a local diffeomorphism.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Theorem 2.5, page 9.

# Verification Notes

- Definition source: Direct from Theorem 2.5
- Confidence rationale: Explicit theorem in source
- Uncertainties: None
- Cross-reference status: Verified with Corollary 3.49, spin group discussion p. 17
