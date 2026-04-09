---
# === CORE IDENTIFICATION ===
concept: Transitive Action
slug: transitive-action

# === CLASSIFICATION ===
category: group-actions
subcategory: action-properties
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 58
section: "Orbits"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - orbit
extends:
  - group-action
related:
  - homogeneous-g-set
  - doubly-transitive-action
contrasts_with:
  - faithful-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a transitive group action?"
  - "What is the difference between a faithful and a transitive group action?"
---

# Quick Definition

An action is transitive if there is only one orbit, i.e., for any $x, y \in X$, there exists $g \in G$ with $gx = y$.

# Core Definition

"The action of $G$ on $X$ is said to be transitive, and $G$ is said to act transitively on $X$, if there is only one orbit, i.e., for any two elements $x$ and $y$ of $X$, there exists a $g \in G$ such that $gx = y$. The set $X$ is then called a homogeneous $G$-set" (Milne, p. 58).

# Prerequisites

- **Group action** — Transitivity is a property of an action
- **Orbit** — Transitive means exactly one orbit

# Key Properties

1. Transitive iff $Gx_0 = X$ for any $x_0 \in X$
2. Every transitive $G$-set is isomorphic to $G/\operatorname{Stab}(x_0)$ (Proposition 4.7)
3. Transitivity depends on the choice of $X$; conjugation on $G$ is never transitive for $G \neq 1$ (since $\{1\}$ is always a conjugacy class)
4. $G$ always acts transitively on $G/H$

# Context & Application

Transitive actions correspond to coset spaces. Every transitive $G$-set with a chosen basepoint is equivalent to data of a subgroup of $G$.

# Examples

**Example 1** (p. 58): $S_n$ acts transitively on $\{1, 2, \ldots, n\}$.

**Example 2** (p. 58): $G$ acts transitively on $G/H$ for any $H \leq G$.

**Non-Example** (p. 58): Conjugation of $G$ on itself is never transitive if $G \neq 1$.

# Relationships

## Builds Upon
- **group-action**, **orbit**

## Enables
- **homogeneous-g-set** — Synonym for transitive $G$-set
- **doubly-transitive-action** — Stronger condition
- **primitive-action** — Primitive implies transitive (or trivial)

## Contrasts With
- **faithful-action** — Independent properties

# Source Reference

Chapter 4: Groups Acting on Sets, "Orbits", page 58.

# Verification Notes

- Definition source: Direct from p. 58
- Confidence: HIGH — explicit definition
- Uncertainties: None
