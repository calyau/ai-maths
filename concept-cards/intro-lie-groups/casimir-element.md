---
# === CORE IDENTIFICATION ===
concept: Casimir Element
slug: casimir-element

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
  - "Casimir operator"
  - "C_B"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - invariant-bilinear-form
  - universal-enveloping-algebra
extends: []
related:
  - complete-reducibility
  - killing-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Casimir element?"
  - "How is the Casimir element used to prove complete reducibility?"
---

# Quick Definition

The Casimir element $C_B = \sum x_i x^i \in U\mathfrak{g}$ is a central element in the universal enveloping algebra constructed from a non-degenerate invariant bilinear form. It acts by a nonzero scalar on non-trivial irreducible representations and by zero on the trivial representation.

# Core Definition

**Proposition 6.54** (Kirillov, p. 78): Let $\mathfrak{g}$ be a Lie algebra, $B$ a non-degenerate invariant symmetric bilinear form, $x_i$ a basis of $\mathfrak{g}$, and $x^i$ the dual basis with respect to $B$. Then

$$C_B = \sum x_i x^i \in U\mathfrak{g}$$

does not depend on the choice of basis and is central.

# Prerequisites

- **Invariant bilinear form** — Must be non-degenerate to define dual basis
- **Universal enveloping algebra** — The Casimir element lives in $U\mathfrak{g}$

# Key Properties

1. $C_B$ is independent of the choice of basis $x_i$
2. $C_B$ is central: $[y, C_B] = 0$ for all $y \in \mathfrak{g}$
3. For simple $\mathfrak{g}$, $C_B$ is unique up to a scalar (since $B$ is)
4. $C_B$ acts by $\frac{\dim \mathfrak{g}'}{\dim V}$ on a non-trivial irreducible $V$ (Proposition 6.55)
5. $C_B$ acts by zero on the trivial representation

# Construction / Recognition

## To Construct:
1. Choose any non-degenerate invariant form $B$ on $\mathfrak{g}$
2. Choose a basis $x_1, \ldots, x_n$
3. Find the dual basis $x^1, \ldots, x^n$ with $B(x_i, x^j) = \delta_{ij}$
4. Form $C_B = \sum x_i x^i$ in $U\mathfrak{g}$

# Context & Application

The Casimir element is the key tool for the algebraic proof of complete reducibility. Its eigenvalue separates the trivial representation from non-trivial irreducibles, allowing one to split extensions.

# Examples

**Proposition 6.55** (p. 79): For the trace form $B_V(x,y) = \operatorname{tr}_V(\rho(x)\rho(y))$ and irreducible $V$, the Casimir element acts on $V$ by $\lambda = \frac{\dim \mathfrak{g}'}{\dim V}$ where $\mathfrak{g}'$ is the semisimple part complementary to $\operatorname{Ker} B_V$.

# Relationships

## Builds Upon
- **Invariant bilinear form** — Needed to define dual basis

## Enables
- **Complete reducibility** — The key tool in the algebraic proof

# Common Confusions

- **Confusion**: Thinking the Casimir element is unique
  **Clarification**: It depends on the choice of form $B$. For simple algebras, $B$ is unique up to scalar, so $C_B$ is unique up to scalar.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.9, pages 78-79. Proposition 6.54, Proposition 6.55.

# Verification Notes

- Definition source: Direct from Proposition 6.54
- Confidence rationale: Explicit definition with properties
- Uncertainties: None
- Cross-reference status: Verified
