---
concept: G-Equivalence
slug: g-equivalence
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
  - "G-equivalent"
prerequisites:
  - group-action
  - g-set
extends: []
related:
  - orbit
  - equivalence-relation
contrasts_with: []
answers_questions:
  - "What is G-equivalence?"
  - "How does a group action define an equivalence relation?"
---

# Quick Definition

Two elements $x, y$ of a $G$-set $X$ are $G$-equivalent ($x \sim_G y$) if there exists $g \in G$ such that $gx = y$. This is an equivalence relation on $X$ whose equivalence classes are the orbits.

# Core Definition

"If $G$ acts on a set $X$ and $x, y \in X$, then $x$ is said to be **$G$-equivalent** to $y$ if there exists a $g \in G$ such that $gx = y$" (Judson, p. 182). By Proposition 14.6, $G$-equivalence is an equivalence relation on $X$.

# Prerequisites

- **Group action** — $G$-equivalence arises from a group action
- **G-set** — The set on which equivalence is defined

# Key Properties

1. Reflexive: $ex = x$, so $x \sim x$
2. Symmetric: if $gx = y$ then $g^{-1}y = x$
3. Transitive: if $gx = y$ and $hy = z$ then $(hg)x = z$
4. Equivalence classes are orbits

# Relationships

## Builds Upon
- **Group action** — Defines the equivalence

## Enables
- **Orbit** — Orbits are the equivalence classes

# Source Reference

Chapter 14: Group Actions, Section 14.1, p. 182. Proposition 14.6.

# Verification Notes

- Definition source: Direct from p. 182
- Confidence: HIGH
