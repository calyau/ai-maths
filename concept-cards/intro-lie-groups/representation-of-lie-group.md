---
# === CORE IDENTIFICATION ===
concept: Representation of a Lie Group
slug: representation-of-lie-group

# === CLASSIFICATION ===
category: representations
subcategory: basic-definitions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 38
section: "4.1 Basic definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "group representation"
  - "finite-dimensional representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - general-linear-group
extends: []
related:
  - representation-of-lie-algebra
  - intertwining-operator
  - trivial-representation
  - adjoint-representation-of-lie-group
contrasts_with:
  - representation-of-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a representation of a Lie group?"
  - "How does a Lie group act on a vector space?"
---

# Quick Definition

A representation of a Lie group $G$ is a vector space $V$ together with a smooth group homomorphism $\rho: G \to GL(V)$, giving a linear action of $G$ on $V$.

# Core Definition

**Definition 4.1** (Kirillov, p. 38): A representation of a Lie group $G$ is a vector space $V$ together with a morphism $\rho: G \to GL(V)$.

Unless specified otherwise, all representations are complex and finite-dimensional. For a real Lie group $G$, a complex representation requires that $\rho: G \to GL(V)$ be smooth, considering $GL(V)$ as a real manifold.

# Prerequisites

This is a foundational concept. Background assumed:
- **Lie group** — the group being represented
- **General linear group** $GL(V)$ — the target of the representation morphism

# Key Properties

1. A representation is a homomorphism: $\rho(gh) = \rho(g)\rho(h)$ and $\rho(e) = \mathrm{id}_V$
2. Complex representations are preferred even for real Lie groups, as they simplify the theory
3. Every representation of $G$ induces a representation of its Lie algebra $\mathfrak{g}$ via $\rho_* : \mathfrak{g} \to \mathfrak{gl}(V)$
4. If $G$ is connected and simply connected, representations of $G$ and $\mathfrak{g}$ are in bijection (Theorem 4.3)

# Construction / Recognition

## To Construct:
1. Choose a vector space $V$ (usually $\mathbb{C}^n$)
2. Define a smooth map $\rho: G \to GL(V)$
3. Verify it is a group homomorphism: $\rho(gh) = \rho(g)\rho(h)$

## To Identify/Recognize:
1. Check that $V$ is a vector space with a $G$-action
2. Verify the action is linear: each $\rho(g)$ is an invertible linear map
3. Verify the action respects group multiplication

# Context & Application

Representation theory translates abstract group structure into concrete linear algebra. This is the central object of study in Chapters 4-5, enabling the classification of how Lie groups can act linearly on vector spaces. Applications include quantum mechanics (where symmetry groups act on Hilbert spaces) and the study of differential equations with symmetry.

# Examples

**Example** (p. 38): The standard representation of $SL(n, \mathbb{C})$ on $\mathbb{C}^n$ by matrix multiplication is an irreducible representation.

**Example** (p. 39): For $G = SU(2)$, a representation is equivalent to a representation of $\mathfrak{su}(2)$, i.e., a vector space with three endomorphisms $X, Y, Z$ satisfying the commutation relations $XY - YX = Z$, $YZ - ZY = X$, $ZX - XZ = Y$.

# Relationships

## Builds Upon
- **Lie group** — The algebraic structure being represented

## Enables
- **Irreducible representation** — Simplest representations, building blocks
- **Subrepresentation** — Invariant subspaces of a representation
- **Character** — Trace function encoding a representation

## Related
- **Representation of a Lie algebra** — Infinitesimal version via differentiation
- **Adjoint representation** — Canonical representation on the Lie algebra

## Contrasts With
- **Representation of a Lie algebra** — Uses a Lie algebra homomorphism to $\mathfrak{gl}(V)$ rather than a group homomorphism to $GL(V)$

# Common Errors

- **Error**: Forgetting to verify smoothness of $\rho$ when working with real Lie groups and complex representations.
  **Correction**: The morphism $\rho: G \to GL(V)$ must be smooth as a map of real manifolds.

# Common Confusions

- **Confusion**: Believing that representations of a non-simply-connected group are the same as representations of its Lie algebra.
  **Clarification**: Only for connected, simply-connected groups is there a full equivalence (Theorem 4.3). For $G = SO(3, \mathbb{R})$, some representations of $\mathfrak{so}(3)$ do not lift to representations of $SO(3)$.

- **Confusion**: Thinking complex representations of real groups are somehow unnatural.
  **Clarification**: Complex representations simplify the theory significantly even for real groups (Remark after Definition 4.1).

# Source Reference

Chapter 4: Representations of Lie Groups and Lie Algebras, Section 4.1 "Basic definitions," pages 38-40. Definition 4.1 and Theorem 4.3.

# Verification Notes

- Definition source: Direct from Definition 4.1, p. 38
- Confidence rationale: Explicit definition with clear terminology
- Uncertainties: None
- Cross-reference status: Slugs verified against planned extractions
