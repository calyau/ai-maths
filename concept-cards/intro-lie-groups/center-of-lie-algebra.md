---
# === CORE IDENTIFICATION ===
concept: Center of a Lie Algebra
slug: center-of-lie-algebra

# === CLASSIFICATION ===
category: lie-algebras
subcategory: subalgebras-ideals
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 28
section: "3.6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathfrak{z}(\\mathfrak{g})$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - ideal-of-lie-algebra
extends: []
related:
  - center-of-lie-group
  - ad-map
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

The center of a Lie algebra $\mathfrak{g}$ is $\mathfrak{z}(\mathfrak{g}) = \{x \in \mathfrak{g} \mid [x, y] = 0 \;\forall y \in \mathfrak{g}\}$. It is always an ideal.

# Core Definition

**Definition 3.31** (Kirillov): The center of $\mathfrak{g}$ is $\mathfrak{z}(\mathfrak{g}) = \{x \in \mathfrak{g} \mid [x, y] = 0 \;\forall y \in \mathfrak{g}\}$. Obviously, $\mathfrak{z}(\mathfrak{g})$ is an ideal in $\mathfrak{g}$.

# Prerequisites

- **Lie algebra** — the algebra whose center is taken
- **Ideal of Lie algebra** — the center is an ideal

# Key Properties

1. $\mathfrak{z}(\mathfrak{g}) = \mathrm{Ker}(\mathrm{ad})$ (since $\mathrm{ad}\, x = 0 \iff [x, y] = 0$ for all $y$).
2. $\mathfrak{z}(\mathfrak{g})$ is an abelian ideal.
3. For connected $G$: $\mathrm{Lie}(Z(G)) = \mathfrak{z}(\mathfrak{g})$ (Theorem 3.32).
4. If $\mathfrak{z}(\mathfrak{g}) = 0$, then ad embeds $\mathfrak{g}$ into $\mathfrak{gl}(\mathfrak{g})$.

# Construction / Recognition

## To Construct/Create:
1. Find all $x \in \mathfrak{g}$ such that $[x, y] = 0$ for every $y \in \mathfrak{g}$.

## To Identify/Recognize:
1. The kernel of the ad map.

# Context & Application

The center is important for the structure theory: a Lie algebra with trivial center can be embedded in $\mathfrak{gl}(\mathfrak{g})$ via ad. Semisimple Lie algebras have trivial center.

# Examples

**Example**: $\mathfrak{z}(\mathfrak{gl}(n)) = \{aI \mid a \in \mathbb{K}\}$ (scalar matrices).

**Example**: $\mathfrak{z}(\mathfrak{sl}(n)) = 0$ for $n \geq 2$.

**Example**: $\mathfrak{z}(\mathfrak{su}(2)) = 0$ (from the commutation relations).

# Relationships

## Builds Upon
- **Lie algebra** — the algebra
- **Ideal of Lie algebra** — the center is an ideal

## Enables
- **Ado theorem approach** — if center is trivial, $\mathrm{ad}$ gives faithful representation

## Related
- **Center of Lie group** — $\mathrm{Lie}(Z(G)) = \mathfrak{z}(\mathfrak{g})$
- **ad map** — $\mathfrak{z}(\mathfrak{g}) = \mathrm{Ker}(\mathrm{ad})$

# Common Errors

- **Error**: Confusing $\mathfrak{z}(\mathfrak{g})$ with the centralizer of a subalgebra.
  **Correction**: The center is the centralizer of all of $\mathfrak{g}$. A centralizer of a subalgebra $\mathfrak{h}$ is $\{x \in \mathfrak{g} \mid [x, y] = 0\; \forall y \in \mathfrak{h}\}$.

# Common Confusions

- **Confusion**: Whether the center of $\mathfrak{u}(n)$ is trivial.
  **Clarification**: No, $\mathfrak{z}(\mathfrak{u}(n)) = i\mathbb{R} \cdot I$ (purely imaginary scalar matrices), which is one-dimensional.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.6, Definition 3.31, page 28.

# Verification Notes

- Definition source: Direct from Definition 3.31
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.32
