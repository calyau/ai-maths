---
concept: Conjugacy of Borel Subgroups
slug: conjugacy-of-borel-subgroups
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 355
section: "Borel subgroups"
extraction_confidence: high
aliases: []
prerequisites:
  - borel-subgroup
  - borel-fixed-point-theorem
extends: []
related:
  - split-maximal-torus
contrasts_with: []
answers_questions:
  - "Are Borel subgroups conjugate?"
---

# Quick Definition

All Borel subgroups of a reductive group G are conjugate by elements of G(k^{al}). Similarly, all maximal tori are conjugate. These conjugacy results follow from the Borel fixed point theorem.

# Core Definition

**Theorem 3.21**: Let G be a reductive group. Any two Borel subgroups are conjugate by an element of G(k^{al}).

**Theorem 3.22**: All maximal tori in a smooth connected algebraic group G are conjugate by an element of G(k^{al}) (Milne, pp. 355–356).

Proof idea: Let B' act on G/B (which is projective). The Borel fixed point theorem gives a fixed point gB, meaning B' ⊂ gBg⁻¹, hence B' = gBg⁻¹ by maximality.

# Prerequisites

- **Borel subgroup** — The subgroups being conjugated
- **Borel fixed point theorem** — The key tool

# Key Properties

1. Over a separably closed field: conjugacy by G(k) (Grothendieck)
2. Maximal split tori are conjugate by G(k) (Borel-Tits, Remark 3.23b)
3. Implies the root datum depends (up to isomorphism) only on G, not on T

# Source Reference

Chapter V, Section 3d, Theorems 3.21–3.22, pages 355–356.

# Verification Notes

- Definition source: Direct from Theorems 3.21–3.22
- Confidence: HIGH
- Uncertainties: None
