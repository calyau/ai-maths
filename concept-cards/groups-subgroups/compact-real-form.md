---
concept: Compact Real Form
slug: compact-real-form
category: lie-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Groups"
chapter_number: 4
pdf_page: 332
section: "Compact topological groups"
extraction_confidence: high
aliases:
  - "anisotropic real form"
prerequisites:
  - reductive-algebraic-group
  - anisotropic-algebraic-group
extends: []
related:
  - real-algebraic-envelope
contrasts_with: []
answers_questions:
  - "What is a compact real form?"
---

# Quick Definition

A compact real form of a complex reductive group G is an anisotropic real form whose real points form a maximal compact subgroup of G(ℂ). There is a bijection between maximal compact subgroups and anisotropic real forms.

# Core Definition

Let G be a reductive algebraic group over ℂ and K a maximal compact subgroup of G(ℂ). Then the complex algebraic envelope of K is G, and the real algebraic envelope of K is a **compact real form** (anisotropic real form) of G (Milne, Theorem 3.5, p. 332).

**Corollary 3.6**: There is a one-to-one correspondence between maximal compact subgroups of G(ℂ) and anisotropic real forms of G.

# Prerequisites

- **Reductive algebraic group** — The complex group G
- **Anisotropic algebraic group** — The real form is anisotropic

# Key Properties

1. Maximal compact subgroups of G(ℂ) are conjugate (Aside 3.8)
2. K determines G via the algebraic envelope
3. H¹(Gal(ℂ/ℝ), K) → H¹(Gal(ℂ/ℝ), G(ℂ)) is an isomorphism (Theorem 3.7)

# Examples

**Example**: SU(n) is a compact real form of SL_n(ℂ). SO(n) is a compact real form of SO_n(ℂ).

# Source Reference

Chapter IV, Section 3, Theorem 3.5 and Corollary 3.6, page 332.

# Verification Notes

- Definition source: Synthesized from Theorem 3.5 and Corollary 3.6
- Confidence: HIGH
- Uncertainties: None
