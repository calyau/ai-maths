---
# === CORE IDENTIFICATION ===
concept: Transitive Action
slug: transitive-action

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "transitive group action"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - orbit
extends:
  - group-action
related:
  - orbit-stabilizer-theorem
  - stabilizer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean for a group action to be transitive?"
---

# Quick Definition

An action of $G$ on $X$ is transitive if there is only one orbit, meaning any point of $X$ can be sent to any other by some element of $G$.

# Core Definition

An action is **transitive** if there is only one orbit (Armstrong, p. 99). Equivalently, for any $x, y \in X$, there exists $g \in G$ with $g(x) = y$.

# Prerequisites

- **Group action** -- transitivity is a property of a group action
- **Orbit** -- defined as having exactly one orbit

# Key Properties

1. An action is transitive iff $G(x) = X$ for any (hence every) $x \in X$
2. In a transitive action on a finite set, $|X| = [G : G_x]$ for any $x$
3. In a transitive action, all stabilizers are conjugate to each other

# Construction / Recognition

## To Check Transitivity:
1. Pick any $x \in X$
2. Compute $G(x) = \{g(x) \mid g \in G\}$
3. The action is transitive iff $G(x) = X$

# Context & Application

Transitive actions arise naturally in geometry when a group of symmetries can move any point to any other. The action of $SO_3$ on the unit sphere is the prototypical example.

# Examples

**Example (iv)** (p. 99): The action of $SO_3$ on the unit sphere in $\mathbb{R}^3$ is transitive: any unit vector can be rotated to any other unit vector.

# Relationships

## Builds Upon
- **Group action** -- transitivity is a property of an action
- **Orbit** -- a transitive action has exactly one orbit

## Enables
- **Classification of finite rotation groups** -- transitive actions on poles play a role in Chapter 19

## Related
- **Orbit-Stabilizer theorem** -- in a transitive action, $|X| = [G : G_x]$

# Common Errors

- **Error**: Assuming transitivity on $X$ and $Y$ implies transitivity of the diagonal action on $X \times Y$.
  **Correction**: Exercise 17.7 (p. 102) asks for an example showing the diagonal action need not be transitive even when $G$ acts transitively on both $X$ and $Y$.

# Common Confusions

- **Confusion**: Confusing transitive actions with free actions.
  **Clarification**: Transitive means one orbit; free means trivial stabilizers. These are independent properties.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, page 99. Definition appears in Example (iv).

# Verification Notes

- Definition: From p. 99, stated in the context of Example (iv)
- Confidence: HIGH -- explicit definition
