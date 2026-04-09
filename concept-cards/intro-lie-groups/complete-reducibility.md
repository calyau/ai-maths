---
# === CORE IDENTIFICATION ===
concept: Complete Reducibility of Semisimple Representations
slug: complete-reducibility

# === CLASSIFICATION ===
category: structure-theory
subcategory: complete-reducibility
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 78
section: "6.9. Complete reducibility of representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Weyl's theorem"
  - "semisimplicity of representations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
  - casimir-element
extends: []
related:
  - cohomology-vanishing
  - compact-real-form
  - reductive-lie-algebra-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are all representations of semisimple Lie algebras completely reducible?"
  - "How is complete reducibility proved?"
---

# Quick Definition

Every finite-dimensional representation of a semisimple Lie algebra is completely reducible (i.e., decomposes as a direct sum of irreducible representations). This is one of the most fundamental results in the theory.

# Core Definition

**Theorem 6.57** (Kirillov, p. 79): Any representation of a semisimple Lie algebra $\mathfrak{g}$ is completely reducible.

# Prerequisites

- **Semisimple Lie algebra** — The result holds specifically for semisimple algebras
- **Casimir element** — Key tool in the algebraic proof

# Key Properties

1. Equivalent to: every short exact sequence $0 \to V_1 \to W \to V_2 \to 0$ of $\mathfrak{g}$-modules splits
2. Equivalent to: $\operatorname{Ext}^1(V_1, V_2) = 0$ for all representations $V_1, V_2$
3. Equivalent to: $H^1(\mathfrak{g}, V) = 0$ for all representations $V$
4. Two proofs: Weyl's unitary trick (via compact groups) and algebraic (via Casimir element)

# Construction / Recognition

## Algebraic Proof Outline:
1. Show $H^1(\mathfrak{g}, V) = 0$ for irreducible $V$ (Lemma 6.58) using the Casimir element
2. For non-trivial irreducible $V$: Casimir separates eigenvalues in extensions $0 \to \mathbb{C} \to W \to V \to 0$
3. For $V = \mathbb{C}$: the extension has nilpotent image, contradicting semisimplicity
4. Extend to all $V$ by induction on dimension (Lemma 6.59)
5. Use $\operatorname{Hom}$ functor and long exact sequence to prove general splitting

# Context & Application

Complete reducibility is the cornerstone of representation theory for semisimple algebras. It means every representation is fully determined by its composition factors (with multiplicities), which dramatically simplifies the theory. It is also the basis for the decomposition of tensor products.

# Examples

**Example**: The adjoint representation of a semisimple algebra $\mathfrak{g} = \mathfrak{g}_1 \oplus \cdots \oplus \mathfrak{g}_k$ decomposes as a direct sum of the adjoint representations of the simple summands.

**Theorem 6.61** (p. 81): As a corollary, every reductive Lie algebra splits as $\mathfrak{g} = \mathfrak{z} \oplus \mathfrak{g}_{ss}$.

# Relationships

## Builds Upon
- **Casimir element** — Used to separate eigenvalues
- **Semisimple Lie algebra** — The hypothesis

## Enables
- **Reductive Lie algebra decomposition** — $\mathfrak{g} = \mathfrak{z} \oplus \mathfrak{g}_{ss}$ (Theorem 6.61)

## Related
- **Cohomology vanishing** — $H^1(\mathfrak{g}, V) = 0$ is equivalent to complete reducibility
- **Compact real form** — Weyl's unitary trick gives an alternative proof

# Common Confusions

- **Confusion**: Thinking complete reducibility holds for all Lie algebras
  **Clarification**: It fails for solvable algebras (e.g., the 2-dimensional non-abelian algebra has indecomposable representations)

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.9, pages 78-81. Theorem 6.57, Lemma 6.58, Lemma 6.59, Theorem 6.61.

# Verification Notes

- Definition source: Direct from Theorem 6.57
- Confidence rationale: Major theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
