---
concept: Burnside's Counting Theorem
slug: burnside-counting-theorem
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 185
section: "Burnside's Counting Theorem"
extraction_confidence: high
aliases:
  - "Burnside's lemma"
  - "Cauchy-Frobenius lemma"
  - "orbit-counting theorem"
prerequisites:
  - group-action
  - orbit
  - stabilizer-subgroup
  - fixed-point-set
extends: []
related:
  - orbit-stabilizer-theorem
contrasts_with: []
answers_questions:
  - "How do I count distinct objects up to symmetry?"
  - "What is Burnside's Counting Theorem?"
---

# Quick Definition

Burnside's Counting Theorem states that the number of orbits $k$ of a finite group $G$ acting on a set $X$ equals the average number of fixed points: $k = \frac{1}{|G|}\sum_{g \in G} |X_g|$.

# Core Definition

**Theorem 14.19 (Burnside)**: "Let $G$ be a finite group acting on a set $X$ and let $k$ denote the number of orbits of $X$. Then $k = \frac{1}{|G|} \sum_{g \in G} |X_g|$" (Judson, p. 186).

# Prerequisites

- **Group action** — A group acting on a set
- **Orbit** — $k$ counts the number of orbits
- **Stabilizer subgroup** — Used in the proof
- **Fixed point set** — $|X_g|$ counts fixed points of each $g$

# Key Properties

1. $k = \frac{1}{|G|}\sum_{g \in G} |X_g|$
2. The sum counts total fixed points over all group elements
3. Equivalently: $\sum_{g \in G} |X_g| = \sum_{x \in X} |G_x| = k \cdot |G|$
4. For permutation groups with $n$ cycles in cycle decomposition: $|X_g| = |Y|^n$ (Proposition 14.21)

# Construction / Recognition

## To Apply Burnside's Theorem:
1. Identify the symmetry group $G$ and the set $X$ of configurations
2. For each $g \in G$, count the number of elements of $X$ fixed by $g$
3. Sum these counts and divide by $|G|$

# Context & Application

Burnside's theorem is widely applied in combinatorics, chemistry (counting molecular configurations), physics, and switching theory. It provides an efficient way to count distinct objects under symmetry.

# Examples

**Example 1** (p. 186): Coloring vertices of a square with 2 colors, $G = D_4$: $k = \frac{1}{8}(16 + 2 + 4 + 2 + 4 + 4 + 8 + 8) = 6$ distinct colorings.

**Example 2** (p. 186): $X = \{1,2,3,4,5\}$, $G = \{(1),(13),(13)(25),(25)\}$: $k = \frac{1}{4}(5+3+1+3) = 3$ orbits.

**Example 3** (p. 188): Coloring vertices of a square with 4 colors: $k = \frac{1}{8}(4^4 + 4 + 4^2 + 4 + 4^2 + 4^2 + 4^3 + 4^3) = 55$.

# Relationships

## Builds Upon
- **Orbit-stabilizer theorem** — Underlying relationship
- **Fixed point set** — The $|X_g|$ terms

## Related
- **Switching functions** — Application to circuit design

# Source Reference

Chapter 14: Group Actions, Section 14.3, pages 185-190. Theorem 14.19, Proposition 14.21.

# Verification Notes

- Definition source: Theorem 14.19
- Confidence: HIGH — major theorem with full proof and multiple examples
