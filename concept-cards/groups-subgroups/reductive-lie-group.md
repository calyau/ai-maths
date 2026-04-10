---
concept: Reductive Lie Group
slug: reductive-lie-group
category: lie-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Groups"
chapter_number: 4
pdf_page: 327
section: "Lie groups"
extraction_confidence: high
aliases: []
prerequisites:
  - real-lie-group
  - reductive-algebraic-group
extends:
  - real-lie-group
related:
  - algebraic-lie-group-functor
  - real-algebraic-envelope
contrasts_with: []
answers_questions:
  - "How do algebraic groups relate to Lie groups?"
---

# Quick Definition

A linear Lie group is reductive if every representation is semisimple. Complex reductive Lie groups are equivalent to complex reductive algebraic groups.

# Core Definition

A real (resp. complex) linear Lie group is **reductive** if every real (resp. complex) representation is semisimple (Milne, p. 327).

For complex Lie groups: G is reductive iff it contains a compact subgroup K with ℂ·Lie(K) = Lie(G) and G = K·G⁺ (Proposition 2.8). Every complex reductive Lie group is algebraic (Remark 2.11).

For real Lie groups: For every real reductive Lie group G, there exists an algebraic group T(G) with an equivalence Rep_ℝ(G) ≅ Rep_ℝ(T(G)) (Theorem 2.13).

# Prerequisites

- **Real Lie group** — Reductive Lie groups are a special class
- **Reductive algebraic group** — The algebraic analogue

# Key Properties

1. The functors T and L give quasi-inverse equivalences between complex reductive Lie groups and complex reductive algebraic groups (Remark 2.11)
2. Every compact connected real Lie group K defines a semisimple algebraic group T(K) with K ≅ T(K)(ℝ) (Theorem 2.14)

# Source Reference

Chapter IV, Sections 1–2, pages 327–331.

# Verification Notes

- Definition source: Direct from p. 327 and Remark 2.11
- Confidence: HIGH
- Uncertainties: None
