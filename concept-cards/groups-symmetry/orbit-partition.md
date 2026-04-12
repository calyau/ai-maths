---
# === CORE IDENTIFICATION ===
concept: Orbit Partition
slug: orbit-partition

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
  - "partition into orbits"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - orbit
  - equivalence-relation
extends: []
related:
  - counting-theorem
  - conjugacy-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the orbits of a group action partition the set?"
---

# Quick Definition

The distinct orbits of a group action on a set $X$ form a partition of $X$. This follows because the relation "there exists $g \in G$ with $g(x) = y$" is an equivalence relation on $X$.

# Core Definition

Let $\mathscr{R}$ be the subset of $X \times X$ consisting of those ordered pairs $(x, y)$ such that $g(x) = y$ for some $g \in G$. Then $\mathscr{R}$ is an equivalence relation on $X$. The equivalence classes of $\mathscr{R}$ are just the orbits. Therefore, the distinct orbits partition $X$ (Armstrong, p. 98).

# Prerequisites

- **Group action** -- the action defines the equivalence relation
- **Orbit** -- the equivalence classes are orbits
- **Equivalence relation** -- reflexivity, symmetry, transitivity must be verified

# Key Properties

1. Reflexive: $e(x) = x$, so $x \sim x$
2. Symmetric: if $g(x) = y$ then $g^{-1}(y) = x$
3. Transitive: if $g(x) = y$ and $g'(y) = z$ then $g'g(x) = z$
4. The partition is into disjoint, non-empty subsets whose union is $X$
5. For finite $X$: $|X| = \sum_i |G(x_i)|$ summed over orbit representatives

# Context & Application

The orbit partition is the foundation for the Counting Theorem: the number of orbits equals $\frac{1}{|G|}\sum_{g \in G} |X^g|$. In the conjugation action, the orbit partition is the partition into conjugacy classes.

# Relationships

## Builds Upon
- **Orbit** -- the partition elements
- **Equivalence relation** -- the mathematical framework

## Enables
- **Counting theorem** -- counts the number of parts in the partition

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, page 98. Proof of equivalence relation on p. 98.

# Verification Notes

- Proof: Direct from p. 98
- Confidence: HIGH -- explicit proof of equivalence relation
