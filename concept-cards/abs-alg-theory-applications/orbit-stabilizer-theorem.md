---
concept: Orbit-Stabilizer Theorem
slug: orbit-stabilizer-theorem
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 183
section: "Groups Acting on Sets"
extraction_confidence: high
aliases:
  - "orbit-counting lemma"
prerequisites:
  - orbit
  - stabilizer-subgroup
  - lagranges-theorem
extends: []
related:
  - class-equation
  - burnside-counting-theorem
contrasts_with: []
answers_questions:
  - "How are orbit size and stabilizer size related?"
---

# Quick Definition

The Orbit-Stabilizer Theorem states that for a finite group $G$ acting on a finite set $X$, the size of the orbit of $x$ equals the index of the stabilizer: $|\mathcal{O}_x| = [G : G_x] = |G|/|G_x|$.

# Core Definition

**Theorem 14.11**: "Let $G$ be a finite group and $X$ a finite $G$-set. If $x \in X$, then $|\mathcal{O}_x| = [G : G_x]$" (Judson, p. 183). The proof constructs a bijection between $\mathcal{O}_x$ and the left cosets of $G_x$ in $G$.

# Prerequisites

- **Orbit** — One side of the equation
- **Stabilizer subgroup** — The other side
- **Lagrange's theorem** — $[G:G_x] = |G|/|G_x|$

# Key Properties

1. $|\mathcal{O}_x| \cdot |G_x| = |G|$
2. The orbit size divides $|G|$
3. The bijection: $y = gx \mapsto gG_x$

# Context & Application

This theorem is the key link between orbits and stabilizers. It underlies the class equation and is used in the proof of Burnside's Counting Theorem.

# Relationships

## Builds Upon
- **Orbit** and **Stabilizer subgroup** — Related by this theorem

## Enables
- **Class equation** — $|G| = |Z(G)| + \sum [G:C(x_i)]$
- **Burnside's counting theorem** — Uses orbit-stabilizer relationship

# Source Reference

Chapter 14: Group Actions, Section 14.1, p. 183. Theorem 14.11.

# Verification Notes

- Definition source: Theorem 14.11
- Confidence: HIGH — theorem with full proof
