---
# === CORE IDENTIFICATION ===
concept: Diagonal Action
slug: diagonal-action

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
section: "Exercise 17.7"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends:
  - group-action
related:
  - product-action
contrasts_with:
  - product-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a single group act diagonally on a product of sets?"
---

# Quick Definition

If $G$ acts on $X$ and on $Y$, the diagonal action of $G$ on $X \times Y$ is defined by $g((x, y)) = (g(x), g(y))$. The stabilizer of $(x, y)$ is $G_x \cap G_y$.

# Core Definition

If $G$ acts on $X$ and on $Y$, the formula $g((x, y)) = (g(x), g(y))$ defines an action of $G$ on $X \times Y$. The stabilizer of $(x, y)$ is the intersection $G_x \cap G_y$ (Armstrong, Exercise 17.7, p. 102).

# Prerequisites

- **Group action** -- requires $G$ to act on both $X$ and $Y$

# Key Properties

1. The stabilizer of $(x, y)$ is $G_x \cap G_y$
2. The diagonal action need not be transitive even if $G$ acts transitively on both $X$ and $Y$ individually
3. A single group acts simultaneously on both coordinates

# Construction / Recognition

## To Construct:
1. Start with actions of $G$ on $X$ and on $Y$
2. Define $g \cdot (x, y) = (g(x), g(y))$
3. Verify: $gh \cdot (x, y) = (gh(x), gh(y)) = (g(h(x)), g(h(y))) = g \cdot (h(x), h(y)) = g \cdot (h \cdot (x, y))$

# Context & Application

The diagonal action uses a single group to act on a product, applying the same group element to both factors. This is distinct from the product action where different group elements act on different factors.

# Examples

**Exercise 17.8** (p. 102): Let $X = \{1, 2, 3, 4\}$ and $G = \langle (1234), (24) \rangle \le S_4$. The orbits and stabilizers for the diagonal action of $G$ on $X \times X$ are to be computed.

# Relationships

## Builds Upon
- **Group action** -- requires two actions of the same group

## Related
- **Product action** -- a different construction for actions on products

## Contrasts With
- **Product action** -- product action uses two different groups; diagonal uses one group acting on both factors

# Common Errors

- **Error**: Assuming transitivity on factors implies transitivity of the diagonal action.
  **Correction**: Armstrong explicitly notes (Exercise 17.7) that the diagonal action may fail to be transitive even when $G$ acts transitively on both $X$ and $Y$.

# Common Confusions

- **Confusion**: Confusing diagonal and product actions.
  **Clarification**: Diagonal: same group element on both factors, $g(x, y) = (g(x), g(y))$. Product: different groups/elements, $(g, h)(x, y) = (g(x), h(y))$.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Exercise 17.7, page 102.

# Verification Notes

- Definition: From Exercise 17.7, p. 102
- Confidence: MEDIUM -- defined in an exercise, but clearly stated with explicit properties
