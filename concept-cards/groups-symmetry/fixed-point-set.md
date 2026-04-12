---
# === CORE IDENTIFICATION ===
concept: Fixed-Point Set
slug: fixed-point-set

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Counting Orbits"
chapter_number: 18
pdf_page: 105
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "X^g"
  - "set of fixed points"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - stabilizer
  - counting-theorem
  - conjugate-fixed-point-sets
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the fixed-point set of a group element?"
  - "How does the fixed-point set relate to the Counting Theorem?"
---

# Quick Definition

Given an action of a finite group $G$ on a set $X$, the fixed-point set $X^g$ of an element $g \in G$ is the set of all points in $X$ that are left fixed by $g$: $X^g = \{x \in X \mid g(x) = x\}$.

# Core Definition

Suppose we have an action of a finite group $G$ on a set $X$. Write $X^g$ for the subset of $X$ consisting of those points which are **left fixed** by the element $g$ of $G$ (Armstrong, p. 105).

# Prerequisites

- **Group action** -- the fixed-point set is defined in terms of a group action

# Key Properties

1. $X^e = X$ (the identity fixes every point)
2. $X^g$ is a subset (possibly empty) of $X$
3. Conjugate elements fix the same number of points: if $ugu^{-1} = h$, then $|X^g| = |X^h|$ (Theorem 18.2)
4. The fixed-point set is dual to the stabilizer: $x \in X^g$ iff $g \in G_x$

# Construction / Recognition

## To Find $X^g$:
1. Fix an element $g \in G$
2. Apply $g$ to each point $x \in X$
3. Collect all $x$ for which $g(x) = x$

# Context & Application

The fixed-point set is the key ingredient in the Counting Theorem (18.1). The average number of fixed points over all group elements equals the number of orbits.

# Examples

**Emily's Problem** (p. 106): For the rotational symmetry group of a cube acting on coloured cubes, $|X^r| = 2^3$ for a face rotation $r$, $|X^{r^2}| = 2^4$ for a half-turn, $|X^s| = 2^2$ for a vertex rotation, $|X^t| = 2^3$ for an edge rotation, and $|X^e| = 2^6$.

# Relationships

## Builds Upon
- **Group action** -- the context in which fixed-point sets are defined

## Enables
- **Counting theorem** -- sums $|X^g|$ over all $g \in G$

## Related
- **Stabilizer** -- $G_x = \{g \mid x \in X^g\}$ is the dual perspective
- **Conjugate fixed-point sets** -- conjugate elements have equal-sized fixed-point sets

# Common Errors

- **Error**: Confusing $X^g$ (points fixed by $g$) with $G_x$ (group elements fixing $x$).
  **Correction**: $X^g \subseteq X$ is a subset of the set; $G_x \le G$ is a subgroup of the group.

# Common Confusions

- **Confusion**: Thinking $|X^g|$ depends on the specific conjugate chosen.
  **Clarification**: Theorem 18.2 shows that conjugate elements fix the same number of points, so $|X^g|$ is constant on conjugacy classes.

# Source Reference

Chapter 18: Counting Orbits, page 105. Notation introduced before Theorem 18.1.

# Verification Notes

- Definition: Direct from p. 105
- Confidence: HIGH -- explicit notation and definition
