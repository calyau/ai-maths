---
# === CORE IDENTIFICATION ===
concept: First Fundamental Theorem of Lie Theory
slug: first-fundamental-theorem

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
pdf_page: 30
section: "3.8"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 3.38"
  - "Lie's first theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-functor
  - simply-connected-lie-group
  - second-fundamental-theorem-of-lie-theory
extends:
  - lie-functor
related:
  - lie-third-theorem
  - equivalence-of-categories
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

If $G_1$ is connected and simply connected, then every Lie algebra morphism $\mathfrak{g}_1 \to \mathfrak{g}_2$ lifts to a unique Lie group morphism $G_1 \to G_2$: $\mathrm{Hom}(G_1, G_2) = \mathrm{Hom}(\mathfrak{g}_1, \mathfrak{g}_2)$.

# Core Definition

**Theorem 3.38** (Kirillov): If $G_1$ is a connected, simply connected Lie group then $\mathrm{Hom}(G_1, G_2) = \mathrm{Hom}(\mathfrak{g}_1, \mathfrak{g}_2)$.

# Prerequisites

- **Lie functor** — the Lie group to Lie algebra correspondence
- **Simply-connected Lie group** — the hypothesis on $G_1$
- **Second fundamental theorem** — the proof of Theorem 3.38 uses Theorem 3.43

# Key Properties

1. Without simple connectedness, we only get injectivity (Theorem 3.17).
2. Simply connected is essential: Example 3.36 shows $\mathrm{id}: \mathfrak{g}_1 \to \mathfrak{g}_2$ (with $\mathbb{R}$ and $S^1$) does not lift.
3. The theorem follows from Theorem 3.43 (Proposition 3.44).

# Construction / Recognition

## To Construct/Create:
1. Given $f: \mathfrak{g}_1 \to \mathfrak{g}_2$, construct the graph subalgebra $\mathfrak{h} = \{(x, f(x))\} \subset \mathfrak{g}_1 \times \mathfrak{g}_2$.
2. By Theorem 3.43, $\mathfrak{h}$ corresponds to a subgroup $H \subset G_1 \times G_2$.
3. Project: $H \to G_1$ is a covering (isomorphism since $G_1$ simply connected).
4. Compose: $G_1 \to H \to G_2$ gives the desired morphism.

## To Identify/Recognize:
1. Any claim that algebra morphisms lift to group morphisms.

# Context & Application

This is one of the three fundamental theorems of Lie theory. It says that for simply-connected groups, the Lie algebra completely determines the morphisms.

# Examples

**Example 3.36** (p. 30): Counterexample without simply-connectedness: the identity map $\mathbb{R} \to \mathbb{R}$ between Lie algebras of $S^1$ and $\mathbb{R}$ does not lift, since any group morphism $S^1 \to \mathbb{R}$ must satisfy $f(\mathbb{Z}) = \{0\}$.

# Relationships

## Builds Upon
- **Lie functor** — extends it to a bijection on Hom sets
- **Second fundamental theorem** — used in the proof

## Enables
- **Equivalence of categories** — combined with the other theorems

## Related
- **Lie's third theorem** — every algebra arises from a group

# Common Errors

- **Error**: Applying the theorem when $G_1$ is not simply connected.
  **Correction**: For non-simply-connected $G_1$, one must check that the morphism respects the fundamental group.

# Common Confusions

- **Confusion**: Whether the theorem works for non-connected $G_1$.
  **Clarification**: It requires both connected and simply connected; connectedness is needed for injectivity, simple connectedness for surjectivity.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.8, Theorem 3.38, Proposition 3.44, pages 30-31.

# Verification Notes

- Definition source: Direct from Theorem 3.38
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified with Proposition 3.44, Example 3.36
