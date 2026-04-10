---
concept: Borel Fixed Point Theorem
slug: borel-fixed-point-theorem
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 354
section: "The Borel fixed point theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - reductive-algebraic-group
  - complete-variety
extends: []
related:
  - borel-subgroup
  - parabolic-subgroup
  - flag-variety
contrasts_with: []
answers_questions:
  - "What is the Borel fixed point theorem?"
  - "What must I know before understanding the Borel fixed point theorem?"
---

# Quick Definition

The Borel fixed point theorem states that any smooth connected solvable algebraic group acting on a complete variety over an algebraically closed field has a fixed point.

# Core Definition

**Theorem 3.18 (Borel Fixed Point Theorem)**: Any smooth connected solvable algebraic group acting on a complete variety over an algebraically closed field has a fixed point (Milne, p. 355).

This is proved via Theorem 3.17: when a smooth connected solvable algebraic group acts on an algebraic variety, no orbit contains a complete subvariety of dimension > 0. Therefore any closed orbit (which exists by 3.8) must be a finite set of points, hence a single point by connectedness.

# Prerequisites

- **Reductive algebraic group** — The theorem is applied within the theory of reductive groups
- **Complete variety** — The target must be complete (e.g., projective)

# Key Properties

1. Immediate consequence: the Lie-Kolchin theorem can be recovered (Remark 3.19)
2. Applied to G/B: shows any two Borel subgroups are conjugate (Theorem 3.21)
3. Applied to G/P: shows parabolic subgroups contain Borel subgroups (Theorem 3.27)

# Construction / Recognition

## Key Applications:
1. Conjugacy of Borel subgroups: let B' act on G/B; the fixed point theorem gives gB fixed by B', so B' ⊂ gBg⁻¹
2. Conjugacy of maximal tori: reduce to the solvable case via Borel subgroups
3. Connectedness of torus centralizers (Theorem 3.25)

# Context & Application

The Borel fixed point theorem is a cornerstone of the structure theory of algebraic groups. It replaces analytic arguments from Lie group theory with purely algebraic ones, allowing the theory to work over arbitrary algebraically closed fields.

# Examples

**Example 1** (p. 355, Remark 3.19): Let G be a connected solvable subgroup of GL_V. G acts on the flag variety (projective). The fixed point theorem gives a fixed flag, recovering the Lie-Kolchin theorem (G is conjugate to upper triangular matrices).

# Relationships

## Enables
- **Borel subgroup** — Conjugacy theorem (3.21)
- **Parabolic subgroup** — Characterization via Borel subgroups (3.27)
- **Bruhat decomposition** — Via applications of the fixed point theorem

# Source Reference

Chapter V, Section 3c, Theorems 3.17–3.18, pages 354–355.

# Verification Notes

- Definition source: Direct from Theorem 3.18
- Confidence: HIGH — major named theorem
- Uncertainties: None
