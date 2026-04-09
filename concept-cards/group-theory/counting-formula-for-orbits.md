---
# === CORE IDENTIFICATION ===
concept: Counting Formula for Orbits
slug: counting-formula-for-orbits

# === CLASSIFICATION ===
category: group-actions
subcategory: counting
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
aliases:
  - orbit-counting formula

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orbit
  - orbit-stabilizer-theorem
extends:
  - orbit-stabilizer-theorem
related:
  - class-equation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I apply the orbit-counting lemma?"
  - "How do I count the total elements in a G-set using orbits?"
---

# Quick Definition

When $X$ is finite, $|X| = \sum_{i=1}^m |O_i| = \sum_{i=1}^m (G : \operatorname{Stab}(x_i))$, summing over one representative $x_i$ per orbit $O_i$.

# Core Definition

"The number of elements in $X$ is $|X| = \sum_{i=1}^m |O_i| = \sum_{i=1}^m (G : \operatorname{Stab}(x_i))$, $x_i$ in $O_i$" (Milne, Proposition 4.11, p. 61, equation (20)).

# Prerequisites

- **Orbit** — $X$ decomposes into orbits
- **Orbit-stabilizer theorem** — Each orbit size is an index

# Key Properties

1. Orbits partition $X$, so $|X|$ is the sum of orbit sizes
2. Each orbit size divides $|G|$
3. The class equation is the special case of conjugation on $G$

# Context & Application

This formula is the basis for all counting arguments in group actions. The class equation, Burnside's lemma, and Sylow theory all derive from it.

# Relationships

## Builds Upon
- **orbit**, **orbit-stabilizer-theorem**

## Enables
- **class-equation** — Special case for conjugation

# Source Reference

Chapter 4: Groups Acting on Sets, Proposition 4.11, page 61.

# Verification Notes

- Definition source: Proposition 4.11, equation (20), p. 61
- Confidence: HIGH
- Uncertainties: None
