---
# === CORE IDENTIFICATION ===
concept: Conjugate Stabilizers Theorem
slug: conjugate-stabilizers-theorem

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
section: "Theorem 17.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - orbit
  - stabilizer
extends: []
related:
  - orbit-stabilizer-theorem
  - conjugacy-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the stabilizers of two points in the same orbit relate?"
---

# Quick Definition

Points in the same orbit have conjugate stabilizers: if $g(x) = y$, then $G_y = gG_xg^{-1}$.

# Core Definition

**(17.1) Theorem.** Points in the same orbit have conjugate stabilizers. Suppose $x$ and $y$ belong to the same orbit, say $g(x) = y$. Then $gG_xg^{-1} = G_y$ (Armstrong, p. 100).

# Prerequisites

- **Group action** -- the theorem concerns an action of $G$ on $X$
- **Orbit** -- the hypothesis requires $x$ and $y$ to be in the same orbit
- **Stabilizer** -- the conclusion relates stabilizer subgroups

# Key Properties

1. If $g(x) = y$ then $G_y = gG_xg^{-1}$
2. Stabilizers of points in the same orbit have the same order
3. Stabilizers of points in the same orbit are isomorphic (as conjugate subgroups)

# Construction / Recognition

## Proof Sketch (p. 100):
1. Let $h \in G_x$ (so $h(x) = x$). Then $ghg^{-1}(y) = ghg^{-1}(g(x)) = gh(x) = g(x) = y$, so $ghg^{-1} \in G_y$.
2. This shows $gG_xg^{-1} \subseteq G_y$.
3. Reversing roles of $x$ and $y$ gives $g^{-1}G_yg \subseteq G_x$, hence $G_y \subseteq gG_xg^{-1}$.
4. Therefore $G_y = gG_xg^{-1}$.

# Context & Application

This theorem is used in the proof of the Counting Theorem and in the classification of finite rotation groups (Chapter 19). It shows that the "type" of stabilizer is constant across an orbit.

# Examples

**Example (iv)** (p. 99): Under $SO_3$ acting on the unit sphere, the stabilizer of $\mathbf{e}_1$ is a copy of $SO_2$. Since the action is transitive (one orbit), the stabilizer of every unit vector is isomorphic to $SO_2$.

# Relationships

## Builds Upon
- **Stabilizer** -- the objects being compared
- **Orbit** -- the hypothesis that the points lie in the same orbit

## Enables
- **Counting theorem** -- uses the fact that $|G_x|$ is constant across orbits

## Related
- **Orbit-Stabilizer theorem** -- a companion result relating orbit size to stabilizer index

# Common Errors

- **Error**: Concluding that stabilizers of points in the same orbit are equal.
  **Correction**: They are conjugate, not necessarily equal. They are equal only if the stabilizer is a normal subgroup.

# Common Confusions

- **Confusion**: Thinking conjugate subgroups are always distinct.
  **Clarification**: If $G_x$ is normal in $G$, then $gG_xg^{-1} = G_x$ for all $g$, so all points in the orbit have the same stabilizer.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Theorem 17.1, page 100.

# Verification Notes

- Theorem statement and proof: Direct from p. 100
- Confidence: HIGH -- explicitly stated and proved theorem
