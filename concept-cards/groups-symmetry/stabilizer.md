---
# === CORE IDENTIFICATION ===
concept: Stabilizer
slug: stabilizer

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
  - "isotropy subgroup"
  - "stabilizer subgroup"
  - "point stabilizer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - orbit
  - orbit-stabilizer-theorem
  - conjugate-stabilizers-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the stabilizer of a point under a group action?"
  - "How do stabilizers of points in the same orbit relate to each other?"
---

# Quick Definition

Given an action of $G$ on $X$, the stabilizer of a point $x \in X$ is the subgroup $G_x = \{g \in G \mid g(x) = x\}$ consisting of all group elements that leave $x$ fixed.

# Core Definition

If $x$ is a point of $X$, the elements of $G$ which leave $x$ fixed form a subgroup of $G$ called the **stabilizer** $G_x$ of $x$ (Armstrong, p. 98).

# Prerequisites

- **Group action** -- stabilizers are defined in terms of a group acting on a set

# Key Properties

1. $G_x$ is a subgroup of $G$ (closure, identity, inverses all hold)
2. Points in the same orbit have conjugate stabilizers: if $g(x) = y$ then $G_y = gG_xg^{-1}$ (Theorem 17.1, p. 100)
3. The index of $G_x$ in $G$ equals the size of the orbit $G(x)$ (Orbit-Stabilizer theorem)
4. If $G$ is finite, $|G_x|$ divides $|G|$

# Construction / Recognition

## To Find the Stabilizer of a Point:
1. Fix $x \in X$
2. For each $g \in G$, check whether $g(x) = x$
3. Collect all such $g$; this set is $G_x$

## To Verify $G_x$ Is a Subgroup:
1. The identity $e$ fixes every point, so $e \in G_x$
2. If $g(x) = x$ and $h(x) = x$, then $gh(x) = g(h(x)) = g(x) = x$
3. If $g(x) = x$, then $g^{-1}(x) = x$

# Context & Application

Stabilizers measure how much of the group "fixes" a particular point. Together with orbits, they completely describe the local behaviour of a group action. The conjugation action gives stabilizers that are centralisers (Exercise 17.10, p. 102).

# Examples

**Example (i)** (p. 98): Under $\mathbb{Z}$ acting on $\mathbb{R}$ by translation, the stabilizer of each real number is $\{0\}$.

**Example (ii)** (p. 98): Under the action $n \cdot x = (-1)^n x$, the stabilizer of nonzero $x$ is $2\mathbb{Z}$; the stabilizer of $0$ is all of $\mathbb{Z}$.

**Example (iii)** (p. 99): Under $\mathbb{Z}_4$ acting on cube edges by rotation, the stabilizer of every edge is $\{0\}$.

**Example (iv)** (p. 99): Under $SO_3$ acting on the unit sphere, the stabilizer of $\mathbf{e}_1$ is a copy of $SO_2$ inside $SO_3$.

**Example (v)** (p. 100): Under conjugation, $G_x = \{g \in G \mid gxg^{-1} = x\} = \{g \in G \mid gx = xg\}$, i.e., the set of elements commuting with $x$.

# Relationships

## Builds Upon
- **Group action** -- stabilizers are defined from actions

## Enables
- **Orbit-Stabilizer theorem** -- $|G(x)| = [G : G_x]$

## Related
- **Orbit** -- orbit size and stabilizer order multiply to give $|G|$
- **Centralizer** -- the stabilizer under conjugation (Exercise 17.10)
- **Conjugate stabilizers theorem** -- points in the same orbit have conjugate stabilizers

# Common Errors

- **Error**: Assuming stabilizers of all points are the same.
  **Correction**: Stabilizers of points in the same orbit are conjugate (not necessarily equal). Points in different orbits may have non-conjugate stabilizers.

# Common Confusions

- **Confusion**: Confusing the stabilizer $G_x$ (a subgroup of $G$) with the fixed-point set $X^g$ (a subset of $X$).
  **Clarification**: $G_x = \{g \in G \mid g(x) = x\}$ is a subgroup of the group; $X^g = \{x \in X \mid g(x) = x\}$ is a subset of the set.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, page 98. Definition on p. 98, conjugate stabilizers theorem on p. 100, examples throughout pp. 98--100.

# Verification Notes

- Definition: Direct from p. 98
- Conjugacy of stabilizers: Theorem 17.1, p. 100
- Confidence: HIGH -- explicit definition with clear notation
