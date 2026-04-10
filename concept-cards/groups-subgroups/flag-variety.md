---
concept: Flag Variety
slug: flag-variety
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 351
section: "Brief review of algebraic geometry"
extraction_confidence: high
aliases:
  - "G/B"
  - "generalized flag variety"
prerequisites:
  - borel-subgroup
extends: []
related:
  - parabolic-subgroup
  - grassmann-variety
  - borel-fixed-point-theorem
contrasts_with: []
answers_questions:
  - "What is a flag variety?"
---

# Quick Definition

The flag variety G/B of a reductive group G with Borel subgroup B is a projective variety parametrizing the Borel subgroups of G. More generally, G/P for a parabolic P is a generalized flag variety.

# Core Definition

For a sequence of integers n > d_r > ... > d_1 > 0, the set of flags V_r ⊃ ... ⊃ V_1 with V_i of dimension d_i has a natural structure of a projective algebraic variety called a **flag variety** (Milne, 3.2c, p. 351).

For a reductive group G, the **flag variety** is G/B where B is a Borel subgroup. It is projective (Theorem 3.21). More generally, G/P for a parabolic subgroup P is a **generalized flag variety**, also projective.

# Prerequisites

- **Borel subgroup** — G/B is the flag variety

# Key Properties

1. G/B is projective (Theorem 3.21)
2. G/B parametrizes the Borel subgroups of G
3. The Borel fixed point theorem applies to actions on G/B
4. Has a cell decomposition by Schubert cells (via Bruhat decomposition)

# Examples

**Example 1** (p. 353): GL₂/𝕋₂ ≅ ℙ¹ (the projective line parametrizes lines in k²).

**Example 2** (p. 358): For GL_V, the flag variety parametrizes maximal flags V_{n-1} ⊃ ... ⊃ V_1.

# Source Reference

Chapter V, Sections 3a–3d, pages 351–356.

# Verification Notes

- Definition source: Synthesized from §3a–3d
- Confidence: HIGH
- Uncertainties: None
