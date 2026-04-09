---
concept: Stabilizer Subgroup
slug: stabilizer-subgroup
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
  - "isotropy subgroup"
  - "G_x"
  - "stabilizer of x"
prerequisites:
  - group-action
  - subgroup
extends:
  - subgroup
related:
  - orbit
  - orbit-stabilizer-theorem
  - fixed-point-set
contrasts_with:
  - fixed-point-set
answers_questions:
  - "What is the stabilizer subgroup?"
  - "How does the stabilizer relate to orbits?"
---

# Quick Definition

The stabilizer (or isotropy) subgroup of an element $x$ in a $G$-set is $G_x = \{g \in G : gx = x\}$, the set of all group elements that fix $x$. It is always a subgroup of $G$.

# Core Definition

"The group elements $g$ that fix a given $x \in X$... This subgroup is called the **stabilizer subgroup** or **isotropy subgroup** of $x$. We will denote the stabilizer subgroup of $x$ by $G_x$" (Judson, p. 182). By Proposition 14.10, $G_x$ is indeed a subgroup of $G$.

# Prerequisites

- **Group action** — The stabilizer is defined for a group action
- **Subgroup** — $G_x$ is a subgroup

# Key Properties

1. $G_x = \{g \in G : gx = x\}$
2. $G_x$ is a subgroup of $G$ (Proposition 14.10)
3. $G_x \subset G$ (important: it's a subset of the group, not the set)
4. $|\mathcal{O}_x| = [G:G_x]$ (Orbit-Stabilizer Theorem)
5. If $x \sim y$ then $G_x \cong G_y$ (Lemma 14.18)

# Examples

**Example 1** (p. 183): For $G = \{(1),(12)(3456),(35)(46),(12)(3654)\}$ acting on $\{1,\ldots,6\}$:
- $G_1 = G_2 = \{(1),(35)(46)\}$
- $G_3 = G_4 = G_5 = G_6 = \{(1)\}$

# Relationships

## Builds Upon
- **Group action** — Stabilizers are defined for actions
- **Subgroup** — $G_x$ is a subgroup of $G$

## Enables
- **Orbit-stabilizer theorem** — $|\mathcal{O}_x| = [G:G_x]$
- **Burnside's counting theorem** — Uses stabilizer sizes

## Contrasts With
- **Fixed point set** — $X_g \subset X$ (points fixed by $g$) vs. $G_x \subset G$ (group elements fixing $x$)

# Source Reference

Chapter 14: Group Actions, Section 14.1, pages 182-183. Proposition 14.10.

# Verification Notes

- Definition source: Direct from p. 182
- Confidence: HIGH
