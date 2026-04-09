---
# === CORE IDENTIFICATION ===
concept: Morphism of Representations
slug: morphism-of-representations

# === CLASSIFICATION ===
category: lie-groups
subcategory: group-actions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 11
section: "2.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "intertwining operator"
  - "equivariant map"
  - "G-map"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
extends: []
related:
  - lie-group-morphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
---

# Quick Definition

A morphism between two representations $V$ and $W$ of a Lie group $G$ is a linear map $f: V \to W$ that commutes with the group action: $f \circ \rho^V(g) = \rho^W(g) \circ f$ for all $g \in G$.

# Core Definition

**Definition 2.16** (Kirillov): A morphism between two representations $V, W$ is a linear map $f: V \to W$ which commutes with the action of $G$: $f \rho^V(g) = \rho^W(g) f$.

# Prerequisites

- **Representation of Lie group** — the objects between which morphisms are defined

# Key Properties

1. Morphisms preserve the $G$-action structure.
2. The kernel and image of a morphism are subrepresentations.
3. Morphisms are the arrows in the category of $G$-representations.

# Construction / Recognition

## To Construct/Create:
1. Given representations $(V, \rho^V)$ and $(W, \rho^W)$, define a linear map $f: V \to W$.
2. Verify $f \rho^V(g) = \rho^W(g) f$ for all $g \in G$.

## To Identify/Recognize:
1. A linear map between representation spaces that intertwines the group actions.

# Context & Application

Morphisms of representations allow comparison of different representations and are essential for decomposing representations into irreducible components.

# Examples

**Example** (p. 11): The map induced on tangent spaces by a $G$-equivariant map between manifolds is a morphism of the induced tangent representations.

# Relationships

## Builds Upon
- **Representation of Lie group** — the objects being mapped

## Enables
- **Schur's lemma** — characterizes morphisms between irreducible representations (later chapters)

## Related
- **Lie group morphism** — morphisms of representations are the representation-theoretic analog

# Common Errors

- **Error**: Checking the intertwining condition only for generators of $G$.
  **Correction**: While it suffices to check on a generating set, one must be careful that the generating set is sufficiently large.

# Common Confusions

- **Confusion**: Whether a morphism of representations must be invertible.
  **Clarification**: No, a morphism is any linear map commuting with the action; it need not be an isomorphism.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.2, Definition 2.16, page 11.

# Verification Notes

- Definition source: Direct from Definition 2.16
- Confidence rationale: Explicit definition in source
- Uncertainties: None
- Cross-reference status: Verified
