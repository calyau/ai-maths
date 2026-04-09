---
# === CORE IDENTIFICATION ===
concept: Equivalence of Categories (Lie Groups and Lie Algebras)
slug: equivalence-of-categories

# === CLASSIFICATION ===
category: lie-algebras
subcategory: fundamental-theorems
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 33
section: "3.8"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Corollary 3.50"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-fundamental-theorem
  - lie-third-theorem
  - simply-connected-lie-group
extends: []
related:
  - lie-functor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

The categories of finite-dimensional Lie algebras and connected, simply-connected Lie groups are equivalent. The equivalence is given by the Lie functor $G \mapsto \mathrm{Lie}(G)$.

# Core Definition

**Corollary 3.50** (Kirillov): The categories of finite-dimensional Lie algebras and connected, simply-connected Lie groups are equivalent.

# Prerequisites

- **First fundamental theorem** — bijection on Hom sets
- **Lie's third theorem** — surjectivity on objects
- **Simply-connected Lie group** — the group side of the equivalence

# Key Properties

1. Every Lie algebra has a unique simply-connected group (surjective on objects).
2. Every Lie algebra morphism lifts uniquely (bijection on morphisms).
3. This means any "algebraic" question about Lie groups reduces to Lie algebras.

# Construction / Recognition

## To Construct/Create:
Not applicable (a categorical statement).

## To Identify/Recognize:
1. The statement that studying Lie algebras is equivalent to studying simply-connected Lie groups.

# Context & Application

This is the culmination of Chapter 3. It justifies the entire algebraic approach to Lie group theory: rather than working with manifolds and smooth maps, one can work with vector spaces and linear maps.

# Examples

**Example**: $\mathfrak{su}(2) \cong \mathfrak{so}(3, \mathbb{R})$ as Lie algebras. Since $\mathrm{SU}(2)$ and $\mathrm{Spin}(3)$ are both simply-connected with these algebras, $\mathrm{SU}(2) \cong \mathrm{Spin}(3)$.

# Relationships

## Builds Upon
- **First fundamental theorem** — Hom bijection
- **Lie's third theorem** — object surjectivity

## Enables
- **All subsequent structure theory** — can work at algebra level

## Related
- **Lie functor** — the functor implementing the equivalence

# Common Errors

- **Error**: Applying the equivalence to non-simply-connected groups.
  **Correction**: The equivalence is only for simply-connected groups. Non-simply-connected groups with the same algebra are quotients $G/Z$.

# Common Confusions

- **Confusion**: Whether this means Lie groups and Lie algebras are "the same."
  **Clarification**: Only for simply-connected groups. The global topology (fundamental group) is additional data not captured by the algebra.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.8, Corollary 3.50, page 33.

# Verification Notes

- Definition source: Direct from Corollary 3.50
- Confidence rationale: Explicit corollary
- Uncertainties: None
- Cross-reference status: Verified with Theorems 3.38, 3.43, 3.48
