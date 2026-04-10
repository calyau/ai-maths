---
concept: Parabolic Subgroup
slug: parabolic-subgroup
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 357
section: "Parabolic subgroups"
extraction_confidence: high
aliases: []
prerequisites:
  - borel-subgroup
  - borel-fixed-point-theorem
extends: []
related:
  - borel-subgroup
  - flag-variety
  - base-of-root-system
contrasts_with:
  - borel-subgroup
answers_questions:
  - "What is a parabolic subgroup?"
  - "How do Borel subgroups relate to parabolic subgroups?"
  - "What distinguishes a Borel subgroup from a parabolic subgroup?"
---

# Quick Definition

A parabolic subgroup P of an algebraic group G is one for which G/P is projective. Equivalently, P contains a Borel subgroup. Parabolic subgroups containing a fixed Borel subgroup B are parametrized by subsets of the simple roots.

# Core Definition

An algebraic subgroup P of a connected algebraic group G is **parabolic** if G/P is projective (Milne, Definition 3.26, p. 357).

**Theorem 3.27**: P is parabolic if and only if it contains a Borel subgroup.

For a split reductive group (G,T) with a chosen base S and Borel subgroup B, the parabolic subgroups containing B are in bijection with subsets I ⊂ S: the parabolic P_I is characterized by U_{−α} ⊂ P_I iff α ∈ I (Theorem 4.10). There are 2^|S| such parabolic subgroups.

# Prerequisites

- **Borel subgroup** — A parabolic subgroup contains a Borel subgroup
- **Borel fixed point theorem** — Used in the proof of Theorem 3.27

# Key Properties

1. G/P is projective (definition)
2. P is parabolic iff P ⊃ B for some Borel B (Theorem 3.27)
3. A connected solvable parabolic subgroup is a Borel subgroup (Corollary 3.28)
4. Parabolic subgroups containing B correspond to subsets of simple roots (Theorem 4.10)
5. The number of parabolic subgroups containing B is 2^|S|

# Construction / Recognition

## To Construct:
1. Fix (G,T,B) with base S
2. Choose a subset I ⊂ S
3. P_I = ⟨B, U_{−α} | α ∈ I⟩

## To Recognize:
- P is parabolic iff G/P is projective
- Equivalently, iff P contains a Borel subgroup

# Examples

**Example 1** (p. 365): For GL₅ with simple roots χ₁−χ₂, ..., χ₄−χ₅, the subset {χ₁−χ₂, χ₂−χ₃, χ₄−χ₅} gives a block upper triangular parabolic subgroup with blocks of sizes 3, 2.

**Example 2** (p. 358): For GL_V, the parabolic subgroups are the stabilizers of (partial) flags.

# Relationships

## Builds Upon
- **Borel subgroup** — The minimal parabolic

## Related
- **Flag variety** — G/P is a generalized flag variety
- **Base of root system** — Subsets of S parametrize parabolic subgroups

## Contrasts With
- **Borel subgroup** — A Borel subgroup is the minimal parabolic (I = ∅)

# Source Reference

Chapter V, Section 3e, pages 357–358; Section 4, Theorem 4.10, page 365.

# Verification Notes

- Definition source: Direct from Definition 3.26
- Confidence: HIGH
- Uncertainties: None
