---
concept: Classification of Split Semisimple Algebraic Groups
slug: split-semisimple-algebraic-group-classification
category: semisimple-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 324
section: "Classification"
extraction_confidence: high
aliases: []
prerequisites:
  - classification-of-semisimple-lie-algebras
  - simply-connected-algebraic-group
  - adjoint-algebraic-group
  - weight-lattice
  - root-lattice
extends:
  - classification-of-semisimple-lie-algebras
related:
  - existence-theorem-reductive-groups
  - isomorphism-theorem-reductive-groups
contrasts_with: []
answers_questions:
  - "How are semisimple algebraic groups classified?"
---

# Quick Definition

Split semisimple algebraic groups (in characteristic zero) are classified by "diagrams" (V, R, X): a root system (V, R) plus a lattice X with Q(R) ⊂ X ⊂ P(R). The root system classifies the Lie algebra; the lattice choice classifies the group.

# Core Definition

A **diagram** (V, R, X) consists of a reduced root system (V, R) over ℚ and a lattice X contained between Q(R) and P(R) (Milne, p. 324).

- **Existence** (Theorem 3.19): Every diagram arises from a split semisimple algebraic group.
- **Isogeny** (Theorem 3.21): Every isomorphism V → V' sending R → R' and X → X' arises from an isogeny G → G'.

The simply connected group has X = P; the adjoint group has X = Q. For each indecomposable root system, the possible lattices X correspond to subgroups of P/Q.

# Prerequisites

- **Classification of semisimple Lie algebras** — Provides the root system
- **Simply connected algebraic group** — X = P
- **Adjoint algebraic group** — X = Q
- **Weight lattice** and **Root lattice** — Bound the lattice X

# Key Properties

1. For A_n: P/Q ≅ ℤ/(n+1)ℤ, so there are divisors of n+1 many groups
2. For E_8, F_4, G_2: P = Q, so only one group (simply connected = adjoint)
3. The construction uses Tannaka duality: Rep(𝔤)^X is a tannakian subcategory

# Examples

**Example 1**: For A₁, P/Q ≅ ℤ/2ℤ. Two groups: SL₂ (simply connected, X = P) and PGL₂ (adjoint, X = Q).

**Example 2** (p. 376, table): For each Dynkin diagram type, P/Q is: A_n → C_{n+1}, B_n → C_2, C_n → C_2, D_n (odd) → C_4, D_n (even) → C_2 × C_2, E_6 → C_3, E_7 → C_2, E_8 → 1, F_4 → 1, G_2 → 1.

# Source Reference

Chapter III, Section 3e, Theorems 3.19–3.21, pages 324–325; Chapter V, §6a, p. 376.

# Verification Notes

- Definition source: Direct from Theorems 3.19–3.21
- Confidence: HIGH
- Uncertainties: None
