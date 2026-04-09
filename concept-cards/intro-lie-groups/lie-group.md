---
# === CORE IDENTIFICATION ===
concept: Lie Group
slug: lie-group

# === CLASSIFICATION ===
category: lie-groups
subcategory: definitions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 8
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "smooth group"
  - "differentiable group"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - lie-group-morphism
  - lie-subgroup
  - connected-component-of-identity
  - lie-algebra
contrasts_with:
  - discrete-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
  - "How does a Lie group combine algebraic and geometric structure?"
---

# Quick Definition

A Lie group is a set $G$ that is simultaneously a group and a smooth (real) manifold, where the group operations of multiplication and inversion are smooth maps.

# Core Definition

**Definition 2.1** (Kirillov): A Lie group is a set $G$ with two structures: $G$ is a group and $G$ is a (smooth, real) manifold. These structures agree in the following sense: multiplication and inversion are smooth maps.

In a similar way, one defines complex Lie groups. Unless specified otherwise, "Lie group" means a real Lie group.

# Prerequisites

Foundational concept with no prerequisites beyond basic differential geometry (smooth manifolds) and group theory.

# Key Properties

1. The word "smooth" can be understood as $C^1$, $C^\infty$, or analytic — all are equivalent (Remark 2.2). Every $C^0$ Lie group has a unique analytic structure.
2. A Lie group need not be connected; any finite group is a 0-dimensional Lie group.
3. Every Lie group has an associated Lie algebra $\mathfrak{g} = T_1G$, the tangent space at the identity.

# Construction / Recognition

## To Construct/Create:
1. Start with a group $G$ that also carries a smooth manifold structure.
2. Verify that the multiplication map $G \times G \to G$ is smooth.
3. Verify that the inversion map $G \to G$ is smooth.

## To Identify/Recognize:
1. Check for simultaneous group and manifold structure.
2. Verify smoothness of group operations.

# Context & Application

Lie groups are the central objects of study in this text. They arise naturally as symmetry groups of geometric objects and are ubiquitous in physics and mathematics. Most commonly encountered as matrix groups (subgroups of $\mathrm{GL}(n, \mathbb{K})$).

# Examples

**Example 2.3** (p. 8):
- $\mathbb{R}^n$ with addition
- $\mathbb{R}^*$, $\mathbb{R}_+$ with multiplication
- $S^1 = \{z \in \mathbb{C} : |z| = 1\}$ with multiplication
- $\mathrm{GL}(n, \mathbb{R}) \subset \mathbb{R}^{n^2}$
- $\mathrm{SU}(2) \cong S^3$
- All classical groups: $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n,\mathbb{R})$, $\mathrm{U}(n)$, $\mathrm{SO}(n,\mathbb{R})$, $\mathrm{SU}(n)$, $\mathrm{Sp}(2n,\mathbb{R})$

# Relationships

## Builds Upon
- **Smooth manifold** — provides the geometric structure
- **Group** — provides the algebraic structure

## Enables
- **Lie algebra** — every Lie group determines a Lie algebra via $\mathfrak{g} = T_1G$
- **Exponential map** — connects the Lie algebra back to the group
- **Representation of Lie group** — Lie groups act on vector spaces

## Related
- **Lie group morphism** — structure-preserving maps between Lie groups
- **Lie subgroup** — subgroups that are also submanifolds

## Contrasts With
- **Discrete group** — a 0-dimensional Lie group with no interesting smooth structure

# Common Errors

- **Error**: Assuming a Lie group must be connected.
  **Correction**: Any finite group is a 0-dimensional Lie group. The connected component of identity $G^0$ is always a normal Lie subgroup.

# Common Confusions

- **Confusion**: Conflating different smoothness requirements ($C^1$ vs $C^\infty$ vs analytic).
  **Clarification**: All are equivalent for Lie groups (Hilbert's 5th problem), so in practice one uses $C^\infty$.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Definition 2.1, page 8.

# Verification Notes

- Definition source: Direct from Definition 2.1
- Confidence rationale: Explicit definition in source text
- Uncertainties: None
- Cross-reference status: Verified against Examples 2.3, Remark 2.2
