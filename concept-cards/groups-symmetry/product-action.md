---
# === CORE IDENTIFICATION ===
concept: Product Action
slug: product-action

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Actions, Orbits, and Stabilizers"
chapter_number: 17
pdf_page: 98
section: "Exercise 17.5"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "direct product action"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - direct-product
extends:
  - group-action
related:
  - diagonal-action
contrasts_with:
  - diagonal-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a product group act on a product set?"
---

# Quick Definition

If $G$ acts on $X$ and $H$ acts on $Y$, the product action of $G \times H$ on $X \times Y$ is defined by $(g, h)(x, y) = (g(x), h(y))$.

# Core Definition

If $G$ acts on $X$ and $H$ acts on $Y$, one proves that $G \times H$ acts on $X \times Y$ via $(g, h)(x, y) = (g(x), h(y))$. The orbit of $(x, y)$ is $G(x) \times H(y)$ and the stabilizer is $G_x \times H_y$ (Armstrong, Exercise 17.5, p. 102).

# Prerequisites

- **Group action** -- requires two existing group actions
- **Direct product** -- uses the product group $G \times H$ and product set $X \times Y$

# Key Properties

1. The orbit of $(x, y)$ is $G(x) \times H(y)$
2. The stabilizer of $(x, y)$ is $G_x \times H_y$
3. The two group components act independently on their respective sets

# Construction / Recognition

## To Construct:
1. Start with an action of $G$ on $X$ and an action of $H$ on $Y$
2. Define $(g, h) \cdot (x, y) = (g(x), h(y))$
3. Verify the action axioms using the axioms for each factor

# Context & Application

The product action arises naturally when combining independent symmetries. Armstrong uses it in Exercise 17.6 to study actions on $\mathbb{R}^4$ viewed as $\mathbb{R}^2 \times \mathbb{R}^2$ or $\mathbb{R}^3 \times \mathbb{R}$.

# Examples

**Exercise 17.6(b)** (p. 101): $\mathbb{R}^4 = \mathbb{R}^2 \times \mathbb{R}^2$ with the product action of $SO_2 \times SO_2$.

**Exercise 17.6(d)** (p. 101): $\mathbb{R}^4 = \mathbb{R}^3 \times \mathbb{R}$ with the product action of $SO_3 \times \mathbb{Z}$, where $\mathbb{Z}$ acts on $\mathbb{R}$ by addition.

# Relationships

## Builds Upon
- **Group action** -- requires two group actions as input
- **Direct product** -- uses product structure on both group and set

## Related
- **Diagonal action** -- a different way to make $G$ act on $X \times Y$

## Contrasts With
- **Diagonal action** -- in the diagonal action a single group acts on both factors simultaneously

# Common Errors

- **Error**: Confusing product action with diagonal action.
  **Correction**: Product action uses $(g, h)(x, y) = (g(x), h(y))$ with two different groups; diagonal action uses $g(x, y) = (g(x), g(y))$ with a single group.

# Common Confusions

- **Confusion**: Assuming the stabilizer of $(x, y)$ involves interaction between the two factors.
  **Clarification**: In the product action, the stabilizer is simply $G_x \times H_y$ -- the factors are independent.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Exercise 17.5, page 102.

# Verification Notes

- Definition: From Exercise 17.5, p. 102
- Confidence: MEDIUM -- defined in an exercise rather than the main text, but clearly stated
