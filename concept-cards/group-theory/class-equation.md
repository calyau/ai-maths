---
# === CORE IDENTIFICATION ===
concept: Class Equation
slug: class-equation

# === CLASSIFICATION ===
category: group-actions
subcategory: orbits-stabilizers
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 61
section: "The class equation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugacy-class
  - centralizer
  - orbit-stabilizer-theorem
extends:
  - orbit-stabilizer-theorem
related:
  - cauchy-theorem
  - p-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the class equation?"
---

# Quick Definition

The class equation expresses $|G|$ as the sum of conjugacy class sizes: $|G| = |Z(G)| + \sum (G : C_G(y))$, where $y$ ranges over non-central conjugacy class representatives.

# Core Definition

"$|G| = \sum (G : C_G(x))$ (x runs over a set of representatives for the conjugacy classes), or $|G| = |Z(G)| + \sum (G : C_G(y))$ (y runs over set of representatives for the conjugacy classes containing more than one element)" (Milne, Proposition 4.12, p. 61).

# Prerequisites

- **Conjugacy class** — The terms in the equation
- **Centralizer** — Appears as $C_G(x)$
- **Orbit-stabilizer theorem** — Each term is an orbit size

# Key Properties

1. First form: $|G| = \sum (G : C_G(x_i))$ over all conjugacy class representatives
2. Second form: separates the centre (classes of size 1) from the rest
3. Each non-central term $(G : C_G(y))$ divides $|G|$ and is $> 1$
4. Fundamental tool for proving results about $p$-groups

# Context & Application

The class equation is the key tool for proving Cauchy's theorem, the non-triviality of centres of $p$-groups, and classifying groups of order $p^2$.

# Examples

**Example 1** (p. 68): For $S_4$: $24 = 1 + 6 + 8 + 3 + 6$ (five conjugacy classes).

# Relationships

## Builds Upon
- **conjugacy-class**, **centralizer**, **orbit-stabilizer-theorem**

## Enables
- **cauchy-theorem** — Proved using the class equation
- **p-group** — Centre of a $p$-group is nontrivial (Theorem 4.16)

# Source Reference

Chapter 4: Groups Acting on Sets, "The class equation", Proposition 4.12, page 61.

# Verification Notes

- Definition source: Proposition 4.12, equations (21)-(22), p. 61
- Confidence: HIGH — explicit statement
- Uncertainties: None
