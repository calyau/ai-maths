---
# === CORE IDENTIFICATION ===
concept: Orbit as Equivalence Class
slug: orbit-equivalence-relation

# === CLASSIFICATION ===
category: equivalence-partitions
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Partitions"
chapter_number: 12
pdf_page: 68
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "orbit"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - equivalence-relation
  - permutation-group
extends:
  - equivalence-class
related:
  - partition
  - conjugacy-equivalence-relation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an orbit of a group action?"
  - "Why do orbits partition the set being acted on?"
---

# Quick Definition

When a group $G$ acts on a set $X$ by permutations, the orbit of a point $x$ is the set of all points $g(x)$ for $g \in G$. Orbits are equivalence classes and partition $X$.

# Core Definition

Let $X$ be a set and let $G$ be a subgroup of $S_X$. Define $(x, y) \in \mathcal{R}$ if $g(x) = y$ for some $g \in G$. This is an equivalence relation on $X$ whose equivalence classes are called the **orbits** of $G$ (Armstrong, Ch. 12, Example (v), p. 70).

Verification: $\varepsilon(x) = x$ (reflexivity); if $g(x) = y$ then $g^{-1}(y) = x$ (symmetry); if $g(x) = y$ and $g'(y) = z$ then $g'g(x) = z$ (transitivity).

# Prerequisites

- **Equivalence relation** — The orbit relation is an equivalence relation
- **Permutation group** — $G$ acts as a group of permutations on $X$

# Key Properties

1. The distinct orbits form a partition of $X$ (by Theorem 12.2)
2. An orbit is fixed setwise by $G$: if $y$ is in the orbit of $x$, then the orbit of $y$ equals the orbit of $x$
3. A point $x$ is a fixed point of $G$ iff its orbit is $\{x\}$

# Construction / Recognition

## To Construct:
1. Start with $x \in X$
2. Compute $g(x)$ for every $g \in G$
3. The resulting set is the orbit of $x$

# Context & Application

Armstrong introduces orbits here as an application of the equivalence-relation partition theorem, foreshadowing the orbit-counting results of Chapters 17-18. The concrete example of $SO_3$ acting on $\mathbb{R}^3$ shows orbits as concentric spheres.

# Examples

**Example 1** (p. 70): Take $X = \mathbb{R}^3$ and $G = \{f_A \mid A \in SO_3\}$. The origin is fixed by every transformation, so its orbit is $\{0\}$. The orbit of a non-zero vector $\mathbf{x}$ is the sphere of radius $\|\mathbf{x}\|$ centred at the origin. These spheres, together with the origin, partition $\mathbb{R}^3$.

# Relationships

## Builds Upon
- **Equivalence class** — Orbits are equivalence classes of the action relation

## Enables
- **Orbit-counting theorem** — Chapters 17-18 develop orbit counting

## Related
- **Conjugacy equivalence relation** — Conjugacy classes are orbits of the conjugation action

# Common Errors

- **Error**: Forgetting that the identity permutation contributes $x$ itself to the orbit
  **Correction**: $x$ is always in its own orbit, since $\varepsilon(x) = x$

# Common Confusions

- **Confusion**: Thinking orbits depend on a choice of starting point
  **Clarification**: If $y$ is in the orbit of $x$, then the orbit of $y$ equals the orbit of $x$. The orbit is the equivalence class, independent of representative.

# Source Reference

Chapter 12: Partitions, Example (v), p. 70 (pdf).

# Verification Notes

- Definition source: Direct from Example (v), p. 70
- Confidence rationale: HIGH — explicitly defined with verification
- Uncertainties: None
