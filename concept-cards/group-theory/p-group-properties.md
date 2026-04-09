---
# === CORE IDENTIFICATION ===
concept: Properties of p-Groups
slug: p-group-properties

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
pdf_page: 62
section: "p-groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - p-group
  - class-equation
  - cauchy-theorem
extends:
  - p-group
related:
  - centre-of-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the key structural properties of p-groups?"
---

# Quick Definition

Finite $p$-groups have nontrivial centres, possess normal subgroups of every prime-power order dividing $|G|$, and groups of order $p^2$ are always abelian.

# Core Definition

Key theorems about $p$-groups (Milne, pp. 62-63):
- "Every nontrivial finite $p$-group has nontrivial centre" (Theorem 4.16)
- "A group of order $p^n$ has normal subgroups of order $p^m$ for all $m \leq n$" (Corollary 4.17)
- "Every group of order $p^2$ is commutative, and hence is isomorphic to $C_p \times C_p$ or $C_{p^2}$" (Proposition 4.18)

# Prerequisites

- **p-group** — The groups whose properties are studied
- **Class equation** — Used in the proof of Theorem 4.16
- **Cauchy's theorem** — Provides elements of order $p$

# Key Properties

1. Nontrivial centre: the class equation forces $p | |Z(G)|$ (Theorem 4.16)
2. Full chain of normal subgroups by induction through $G/Z$ (Corollary 4.17)
3. If $|G| = p^2$ then $Z(G) \neq 1$, so $G/Z$ is cyclic, hence $G$ is abelian (Proposition 4.18)
4. If $H \subset Z(G)$ and $G/H$ is cyclic, then $G$ is abelian (Lemma 4.19)
5. For $p$ odd: exactly two noncommutative groups of order $p^3$ (up to isomorphism)

# Examples

**Example 1** (p. 62): Groups of order $p^2$: only $C_{p^2}$ and $C_p \times C_p$.

**Example 2** (p. 62): A noncommutative group of order 8 is either $D_4$ or $Q_8$ (Example 4.21).

# Relationships

## Builds Upon
- **p-group**, **class-equation**, **cauchy-theorem**

# Source Reference

Chapter 4: Groups Acting on Sets, "p-groups", pages 62-63.

# Verification Notes

- Definition source: Theorems 4.16, Corollaries 4.17-4.18, pp. 62-63
- Confidence: HIGH — explicit theorems with proofs
- Uncertainties: None
