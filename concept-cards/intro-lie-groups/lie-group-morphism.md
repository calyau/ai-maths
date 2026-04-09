---
# === CORE IDENTIFICATION ===
concept: Lie Group Morphism
slug: lie-group-morphism

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
  - "morphism of Lie groups"
  - "Lie group homomorphism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - lie-algebra-morphism
  - representation-of-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a morphism between Lie groups?"
  - "How do Lie groups relate to their Lie algebras?"
---

# Quick Definition

A morphism of Lie groups is a smooth map between Lie groups that also preserves the group operation.

# Core Definition

**Definition 2.1** (Kirillov): A morphism of Lie groups is a smooth map $f: G_1 \to G_2$ which also preserves the group operation: $f(gh) = f(g)f(h)$, $f(1) = 1$.

# Prerequisites

- **Lie group** — must know what Lie groups are to define maps between them

# Key Properties

1. A Lie group morphism is simultaneously a group homomorphism and a smooth map.
2. Every morphism of Lie groups $\varphi: G_1 \to G_2$ induces a morphism of Lie algebras $\varphi_*: \mathfrak{g}_1 \to \mathfrak{g}_2$ (Theorem 3.17).
3. For connected $G_1$, the map $\mathrm{Hom}(G_1, G_2) \to \mathrm{Hom}(\mathfrak{g}_1, \mathfrak{g}_2)$ is injective (Proposition 3.9).

# Construction / Recognition

## To Construct/Create:
1. Define a map $f: G_1 \to G_2$ between Lie groups.
2. Verify it is a group homomorphism: $f(gh) = f(g)f(h)$.
3. Verify it is a smooth map of manifolds.

## To Identify/Recognize:
1. Check that the map respects both group and smooth structures simultaneously.

# Context & Application

Morphisms are the structure-preserving maps in the category of Lie groups. They are essential for relating different Lie groups and for the fundamental correspondence between Lie groups and Lie algebras.

# Examples

**Example** (p. 10): The homomorphism theorem (Theorem 2.12) states that for a morphism $f: G_1 \to G_2$, the kernel $H = \mathrm{Ker}\, f$ is a normal Lie subgroup and $f$ gives an injective morphism $G_1/H \to G_2$.

**Example** (p. 18): The map $\varphi: \mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$ defined by the adjoint action is a morphism of Lie groups.

# Relationships

## Builds Upon
- **Lie group** — morphisms are maps between Lie groups

## Enables
- **Lie algebra morphism** — every Lie group morphism induces a Lie algebra morphism
- **Homomorphism theorem for Lie groups** — kernel and image structure

## Related
- **Representation of Lie group** — a representation is a morphism $G \to \mathrm{GL}(V)$

# Common Errors

- **Error**: Forgetting the smoothness requirement and only checking the group homomorphism property.
  **Correction**: A Lie group morphism must be both a group homomorphism and a smooth map.

# Common Confusions

- **Confusion**: Whether the condition $f(1) = 1$ is redundant.
  **Clarification**: For group homomorphisms, $f(1) = 1$ follows from $f(gh) = f(g)f(h)$, but it is often stated explicitly for clarity.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Definition 2.1, page 8.

# Verification Notes

- Definition source: Direct from Definition 2.1
- Confidence rationale: Explicit definition in source
- Uncertainties: None
- Cross-reference status: Verified against Theorem 2.12, Theorem 3.17
