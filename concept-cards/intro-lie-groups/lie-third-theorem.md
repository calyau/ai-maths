---
# === CORE IDENTIFICATION ===
concept: "Lie's Third Theorem"
slug: lie-third-theorem

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
  - "Theorem 3.48"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - second-fundamental-theorem-of-lie-theory
extends: []
related:
  - first-fundamental-theorem
  - equivalence-of-categories
  - simply-connected-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

Every finite-dimensional Lie algebra is isomorphic to the Lie algebra of some Lie group. This is the surjectivity of the Lie functor on objects.

# Core Definition

**Theorem 3.48** (Kirillov, Lie's third theorem): Any finite-dimensional Lie algebra is isomorphic to a Lie algebra of a Lie group.

The proof relies on Ado's theorem (every Lie algebra embeds in $\mathfrak{gl}(n)$) combined with Theorem 3.43.

# Prerequisites

- **Lie algebra** — the given algebra
- **Second fundamental theorem** — used to construct the group from a subalgebra of $\mathfrak{gl}(n)$

# Key Properties

1. The simplest case is when $\mathfrak{z}(\mathfrak{g}) = 0$: then $\mathrm{ad}: \mathfrak{g} \hookrightarrow \mathfrak{gl}(\mathfrak{g})$ is injective.
2. The general case requires Ado's theorem (proof is long and requires structure theory).
3. Combined with the other theorems, gives: for every Lie algebra, there is a unique connected simply-connected group (Corollary 3.49).

# Construction / Recognition

## To Construct/Create:
1. Embed $\mathfrak{g}$ into $\mathfrak{gl}(n)$ (Ado's theorem).
2. Apply Theorem 3.43 to get a connected immersed subgroup $H \subset \mathrm{GL}(n)$.
3. Take the universal cover of $H$.

## To Identify/Recognize:
1. Any claim that abstract Lie algebras have concrete Lie group realizations.

# Context & Application

This completes the fundamental theorem trifecta. Together with Theorems 3.38 and 3.43, it establishes the equivalence of categories between finite-dimensional Lie algebras and connected simply-connected Lie groups.

# Examples

**Example** (p. 33): If $\mathfrak{z}(\mathfrak{g}) = 0$, then $\mathrm{ad}: \mathfrak{g} \hookrightarrow \mathfrak{gl}(\mathfrak{g})$ provides the embedding directly.

# Relationships

## Builds Upon
- **Second fundamental theorem** — subalgebras give subgroups
- **Lie algebra** — the abstract object to be realized

## Enables
- **Equivalence of categories** — Corollary 3.50
- **Simply-connected Lie group** — unique one for each algebra (Corollary 3.49)

## Related
- **Ado's theorem** — every Lie algebra embeds in $\mathfrak{gl}(n)$ (needed for proof)

# Common Errors

- **Error**: Thinking the proof is elementary.
  **Correction**: The proof requires Ado's theorem, which itself needs significant structure theory.

# Common Confusions

- **Confusion**: Whether the Lie group is unique.
  **Clarification**: The connected simply-connected one is unique. Other connected groups are quotients by discrete central subgroups (Corollary 3.49).

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.8, Theorem 3.48, Corollary 3.49, pages 33.

# Verification Notes

- Definition source: Direct from Theorem 3.48
- Confidence rationale: Explicit theorem statement; proof referenced
- Uncertainties: Full proof not in source
- Cross-reference status: Verified with Corollary 3.49, 3.50
