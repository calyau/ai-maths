---
# === CORE IDENTIFICATION ===
concept: Orbit
slug: orbit

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
  - "G-orbit"
  - "orbit of a point"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - stabilizer
  - orbit-stabilizer-theorem
  - transitive-action
  - conjugacy-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the orbit of a point under a group action?"
  - "How do orbits partition the set being acted upon?"
---

# Quick Definition

Given an action of $G$ on $X$ and a point $x \in X$, the orbit of $x$ is the set $G(x) = \{g(x) \mid g \in G\}$ of all images of $x$ under elements of $G$. The distinct orbits partition $X$.

# Core Definition

Given an action of $G$ on $X$ and a point $x \in X$, the set of all images $g(x)$, as $g$ varies through $G$, is called the **orbit** of $x$ and written $G(x)$. The orbit $G(x)$ is a subset of $X$ (Armstrong, p. 98).

The relation $\mathscr{R}$ on $X \times X$ defined by $(x, y) \in \mathscr{R}$ if $g(x) = y$ for some $g \in G$ is an equivalence relation. The equivalence classes are the orbits, and therefore the distinct orbits partition $X$ (p. 98).

# Prerequisites

- **Group action** -- orbits are defined in terms of a group acting on a set

# Key Properties

1. $G(x)$ is a non-empty subset of $X$ (since $e(x) = x$, so $x \in G(x)$)
2. Two orbits are either identical or disjoint
3. The distinct orbits partition $X$ into equivalence classes
4. For finite $G$, the size of each orbit divides $|G|$ (Corollary 17.3)
5. Points in the same orbit have conjugate stabilizers (Theorem 17.1)

# Construction / Recognition

## To Find the Orbit of a Point:
1. Fix a point $x \in X$
2. Apply every element $g \in G$ to $x$
3. Collect all distinct images $g(x)$; this set is $G(x)$

## To Verify Two Points Are in the Same Orbit:
1. Check whether there exists $g \in G$ such that $g(x) = y$
2. If such $g$ exists, then $G(x) = G(y)$

# Context & Application

Orbits are fundamental to understanding how a group partitions the set it acts on. Counting the number of distinct orbits is the central problem addressed by the Counting Theorem (Burnside's lemma). In the conjugation action, orbits are conjugacy classes.

# Examples

**Example (i)** (p. 98): Under $\mathbb{Z}$ acting on $\mathbb{R}$ by translation, the orbit of $x$ is $\{n + x \mid n \in \mathbb{Z}\}$.

**Example (ii)** (p. 98): Under the action $n \cdot x = (-1)^n x$, the orbit of a nonzero $x$ is $\{x, -x\}$; the orbit of $0$ is $\{0\}$.

**Example (iii)** (p. 99): Under $\mathbb{Z}_4$ acting on cube edges by rotation, there are three orbits: the four top edges, the four bottom edges, and the four vertical edges.

**Example (iv)** (p. 99): Under the action of $SO_3$ on the unit sphere, the orbit of any unit vector is the whole sphere.

**Example (v)** (p. 100): Under conjugation, the orbits are the conjugacy classes of $G$.

# Relationships

## Builds Upon
- **Group action** -- orbits are defined from actions

## Enables
- **Orbit-Stabilizer theorem** -- relates orbit size to stabilizer index
- **Counting theorem** -- counts the number of distinct orbits

## Related
- **Stabilizer** -- the subgroup fixing a point; its index equals the orbit size
- **Transitive action** -- an action with exactly one orbit
- **Conjugacy class** -- the orbit under the conjugation action

# Common Errors

- **Error**: Assuming orbits of different points are always different.
  **Correction**: If $y \in G(x)$, then $G(y) = G(x)$. Orbits are equivalence classes.

# Common Confusions

- **Confusion**: Conflating orbits with cosets.
  **Clarification**: Orbits are subsets of the acted-upon set $X$; cosets are subsets of the group $G$. The Orbit-Stabilizer theorem establishes a bijection between the orbit $G(x)$ and the set of left cosets of $G_x$ in $G$.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, page 98. Definition on p. 98, equivalence relation argument on p. 98, examples on pp. 98--100.

# Verification Notes

- Definition: Direct from p. 98
- Partition property: Proved via equivalence relation on p. 98
- Confidence: HIGH -- explicit definition with proof of partition property
