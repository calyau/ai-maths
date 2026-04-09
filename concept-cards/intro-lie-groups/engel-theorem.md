---
# === CORE IDENTIFICATION ===
concept: Engel Theorem
slug: engel-theorem

# === CLASSIFICATION ===
category: structure-theory
subcategory: solvable-nilpotent
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 70
section: "6.3. Lie and Engel theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Engel's theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nilpotent-lie-algebra
extends: []
related:
  - lie-theorem
  - nilpotent-operator-theorem
contrasts_with:
  - lie-theorem

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I determine if a Lie algebra is nilpotent?"
  - "What is the relationship between nilpotent elements and nilpotent algebras?"
---

# Quick Definition

Engel's theorem states that a Lie algebra $\mathfrak{g}$ is nilpotent if and only if $\operatorname{ad} x$ is a nilpotent operator for every $x \in \mathfrak{g}$. It provides an element-wise criterion for nilpotency of the whole algebra.

# Core Definition

**Theorem 6.18** (Kirillov, p. 70): A Lie algebra $\mathfrak{g}$ is nilpotent if and only if for every $x \in \mathfrak{g}$, the operator $\operatorname{ad} x \in \operatorname{End}(\mathfrak{g})$ is nilpotent.

This relies on **Theorem 6.17**: If $\mathfrak{g} \subset \mathfrak{gl}(V)$ consists of nilpotent operators, then there exists a basis in which all elements of $\mathfrak{g}$ are strictly upper-triangular.

# Prerequisites

- **Nilpotent Lie algebra** — Engel's theorem characterizes nilpotency

# Key Properties

1. One direction is immediate: if $\mathfrak{g}$ is nilpotent, then $(\operatorname{ad} x)^n = 0$ by definition
2. The converse uses Theorem 6.17 to find a chain of ideals $\mathfrak{g}^i$ with $[\mathfrak{g}, \mathfrak{g}^i] \subset \mathfrak{g}^{i-1}$
3. The theorem works over both $\mathbb{R}$ and $\mathbb{C}$

# Construction / Recognition

## To Apply Engel's Theorem:
1. For each $x \in \mathfrak{g}$, check if $\operatorname{ad} x$ is nilpotent
2. If yes for all $x$, conclude $\mathfrak{g}$ is nilpotent
3. If $\operatorname{ad} x$ is not nilpotent for some $x$, then $\mathfrak{g}$ is not nilpotent

# Context & Application

Engel's theorem provides a practical criterion for nilpotency that can be checked element by element. It is used in the proof of the Cartan criterion for solvability and plays a role throughout the structure theory. It is the nilpotent analog of Lie's theorem for solvable algebras.

# Examples

**Example** (p. 70, from proof of Theorem 6.18): If $\operatorname{ad} x$ is nilpotent for every $x$, then by Theorem 6.17 applied to the adjoint representation, there exist subspaces $0 \subset \mathfrak{g}^1 \subset \cdots \subset \mathfrak{g}^n = \mathfrak{g}$ with $\operatorname{ad} x.\mathfrak{g}^i \subset \mathfrak{g}^{i-1}$, showing $[\mathfrak{g}, \mathfrak{g}^i] \subset \mathfrak{g}^{i-1}$.

# Relationships

## Builds Upon
- **Nilpotent Lie algebra** — Provides the characterization

## Enables
- **Cartan criterion (solvability)** — Engel's theorem is used in its proof (via Lemma 6.39)

## Contrasts With
- **Lie theorem** — Lie's theorem is for solvable algebras and gives upper-triangular form; Engel gives strictly upper-triangular form for nilpotent algebras

# Common Errors

- **Error**: Checking nilpotency of $\operatorname{ad} x$ for only a basis, not all elements
  **Correction**: The condition must hold for ALL $x \in \mathfrak{g}$, not just a basis (though in practice, for a subalgebra of $\mathfrak{gl}(V)$ consisting of nilpotent matrices, Theorem 6.17 applies directly)

# Common Confusions

- **Confusion**: Thinking Engel's theorem says "all elements nilpotent implies algebra nilpotent" without the adjoint condition
  **Clarification**: The precise statement is about $\operatorname{ad} x$ being nilpotent, not about $x$ itself being nilpotent in some ambient algebra

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.3, pages 70. Theorem 6.17, Theorem 6.18.

# Verification Notes

- Definition source: Direct from Theorem 6.18
- Confidence rationale: Named theorem with explicit statement; proof of Theorem 6.17 is referenced but not given
- Uncertainties: None
- Cross-reference status: Verified
