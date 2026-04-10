---
concept: Algebraic-to-Lie Group Functor
slug: algebraic-lie-group-functor
category: lie-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Groups"
chapter_number: 4
pdf_page: 328
section: "Lie groups and algebraic groups"
extraction_confidence: high
aliases:
  - "functor L"
  - "G(ℝ) as Lie group"
  - "G(ℂ) as Lie group"
prerequisites:
  - real-lie-group
  - affine-algebraic-group
extends: []
related:
  - reductive-lie-group
  - real-algebraic-envelope
contrasts_with: []
answers_questions:
  - "How do algebraic groups relate to Lie groups?"
---

# Quick Definition

There is a canonical functor L from the category of real (resp. complex) algebraic groups to real (resp. complex) Lie groups, faithful on connected algebraic groups, that respects Lie algebras.

# Core Definition

There is a canonical functor L from the category of real (resp. complex) algebraic groups to real (resp. complex) Lie groups, which respects Lie algebras and takes GL_n to GL_n(ℝ) (resp. GL_n(ℂ)) with its natural Lie group structure. It is faithful on connected algebraic groups (Milne, Theorem 2.1, p. 328).

We often write G(ℝ) or G(ℂ) for L(G).

# Prerequisites

- **Real Lie group** — The target category
- **Affine algebraic group** — The source category

# Key Properties

1. Faithful on connected algebraic groups (all algebraic groups in the complex case)
2. Not faithful on nonconnected real algebraic groups (Example 2.2)
3. Not full: z ↦ e^z: ℂ → ℂ× is not algebraic (Example 2.3)
4. Complex reductive Lie groups and algebraic groups are equivalent categories (Remark 2.11)

# Context & Application

This functor is the bridge between algebraic group theory and Lie group theory. For reductive groups, it gives an equivalence in the complex case, but subtleties arise in the real case and for non-reductive groups.

# Examples

**Example 1** (p. 328): μ₃ maps to μ₃(ℝ) = {1}, which is not faithful.

**Example 2** (p. 328): SL₃(ℝ) → PSL₃(ℝ) is an isomorphism of Lie groups, but SL₃ → PSL₃ is not an isomorphism of algebraic groups.

# Source Reference

Chapter IV, Section 2a–2b, Theorem 2.1 and Examples 2.2–2.7, pages 328–329.

# Verification Notes

- Definition source: Direct from Theorem 2.1
- Confidence: HIGH
- Uncertainties: None
