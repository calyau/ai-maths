---
concept: Fixed Point Set
slug: fixed-point-set
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 182
section: "Groups Acting on Sets"
extraction_confidence: high
aliases:
  - "X_g"
  - "fixed set"
prerequisites:
  - group-action
extends: []
related:
  - stabilizer-subgroup
  - burnside-counting-theorem
contrasts_with:
  - stabilizer-subgroup
answers_questions:
  - "What is the fixed point set of a group element?"
---

# Quick Definition

The fixed point set of a group element $g \in G$ acting on $X$ is $X_g = \{x \in X : gx = x\}$, the set of all elements of $X$ left unchanged by $g$. Note $X_g \subset X$, while $G_x \subset G$.

# Core Definition

"The **fixed point set** of $g$ in $X$, denoted by $X_g$, is the set of all $x \in X$ such that $gx = x$" (Judson, p. 182). "It is important to remember that $X_g \subset X$ and $G_x \subset G$" (Remark 14.8).

# Prerequisites

- **Group action** — Fixed point sets are defined for actions

# Key Properties

1. $X_e = X$ (identity fixes everything)
2. $X_g \subset X$
3. $|X_g|$ counts how many points $g$ fixes
4. Burnside's theorem: $k = \frac{1}{|G|}\sum_{g \in G} |X_g|$ where $k$ is the number of orbits

# Examples

**Example 1** (p. 183): For $G = \{(1),(12)(3456),(35)(46),(12)(3654)\}$:
- $X_{(1)} = \{1,2,3,4,5,6\}$
- $X_{(35)(46)} = \{1,2\}$
- $X_{(12)(3456)} = X_{(12)(3654)} = \emptyset$

# Relationships

## Enables
- **Burnside's counting theorem** — Sums $|X_g|$ over all $g$

## Contrasts With
- **Stabilizer subgroup** — $G_x \subset G$ fixes a point; $X_g \subset X$ is fixed by a group element

# Source Reference

Chapter 14: Group Actions, Section 14.1, p. 182-183. Remark 14.8.

# Verification Notes

- Definition source: Direct from p. 182
- Confidence: HIGH
