---
# === CORE IDENTIFICATION ===
concept: Lie Algebra Morphism
slug: lie-algebra-morphism

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 24
section: "3.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "morphism of Lie algebras"
  - "Lie algebra homomorphism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - lie-group-morphism
  - lie-functor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

A morphism of Lie algebras is a linear map $f: \mathfrak{g}_1 \to \mathfrak{g}_2$ that preserves the commutator: $f([x, y]) = [f(x), f(y)]$.

# Core Definition

**Definition 3.16** (Kirillov): A morphism of Lie algebras is a linear map $f: \mathfrak{g}_1 \to \mathfrak{g}_2$ which preserves the commutator.

# Prerequisites

- **Lie algebra** — the objects between which morphisms are defined

# Key Properties

1. Every Lie group morphism $\varphi: G_1 \to G_2$ induces a Lie algebra morphism $\varphi_*: \mathfrak{g}_1 \to \mathfrak{g}_2$.
2. For connected, simply-connected $G_1$, every Lie algebra morphism lifts to a Lie group morphism (Theorem 3.38).
3. The kernel of a Lie algebra morphism is an ideal.

# Construction / Recognition

## To Construct/Create:
1. Define a linear map $f: \mathfrak{g}_1 \to \mathfrak{g}_2$.
2. Verify $f([x, y]) = [f(x), f(y)]$ for all $x, y \in \mathfrak{g}_1$.

## To Identify/Recognize:
1. A bracket-preserving linear map between Lie algebras.

# Context & Application

Lie algebra morphisms are the structure-preserving maps in the category of Lie algebras. The functor $G \mapsto \mathrm{Lie}(G)$ sends Lie group morphisms to Lie algebra morphisms, and this is an equivalence on the simply-connected level.

# Examples

**Example** (p. 24): $\mathrm{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ is a morphism of Lie algebras (Theorem 3.15).

**Example** (pp. 34-35): $\mathfrak{su}(2) \xrightarrow{\sim} \mathfrak{so}(3, \mathbb{R})$ is an isomorphism of Lie algebras.

# Relationships

## Builds Upon
- **Lie algebra** — the objects being mapped

## Enables
- **Lie functor** — the assignment $G \mapsto \mathrm{Lie}(G)$, $\varphi \mapsto \varphi_*$
- **First fundamental theorem** — lifts algebra morphisms to group morphisms

## Related
- **Lie group morphism** — induces a Lie algebra morphism

# Common Errors

- **Error**: Assuming every Lie algebra morphism lifts to a Lie group morphism.
  **Correction**: This requires $G_1$ to be simply connected (Example 3.36).

# Common Confusions

- **Confusion**: Whether a Lie algebra morphism must be injective.
  **Clarification**: No, it can have a nontrivial kernel (which is then an ideal).

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.3, Definition 3.16, page 24.

# Verification Notes

- Definition source: Direct from Definition 3.16
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.17, 3.38
