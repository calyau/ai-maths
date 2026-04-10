---
concept: Fundamental Weight
slug: fundamental-weight
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 303
section: "The root and weight lattices"
extraction_confidence: high
aliases:
  - "ϖ_α"
  - "fundamental dominant weight"
prerequisites:
  - weight-lattice
  - base-of-root-system
  - coroot
extends: []
related:
  - dominant-weight
  - highest-weight-representation
contrasts_with: []
answers_questions:
  - "What is a fundamental weight?"
---

# Quick Definition

The fundamental weights {ϖ_α | α ∈ S} are the basis of the weight lattice P dual to the coroot basis S^∨, satisfying ⟨ϖ_α, β^∨⟩ = δ_{α,β} for all α, β ∈ S.

# Core Definition

Let S be a base for a root system R. For each simple root α, the **fundamental weight** ϖ_α ∈ P(R) is defined by ⟨ϖ_α, β^∨⟩ = δ_{α,β} for all β ∈ S. Then {ϖ_α | α ∈ S} is a basis for P(R), dual to S^∨ (Milne, 1.21, p. 303).

# Prerequisites

- **Weight lattice** — Fundamental weights form a basis for P
- **Base of root system** — Indexed by simple roots
- **Coroot** — Defined via pairing with coroots

# Key Properties

1. The fundamental weights are dominant: ⟨ϖ_α, β^∨⟩ ≥ 0 for all β ∈ S
2. P = ℤϖ₁ ⊕ ... ⊕ ℤϖₙ
3. P₊₊ = {∑ m_i ϖ_i | m_i ∈ ℕ}

# Examples

**Example 1** (p. 315): For sl_{n+1}, ϖ_i = ε₁ + ... + ε_i (restricted to 𝔥). The simple representation with highest weight ϖ_r is ∧^r W (exterior power).

# Relationships

## Enables
- **Dominant weight** — Non-negative integer linear combinations of fundamental weights
- **Highest weight representation** — Simple representations are indexed by dominant weights

# Source Reference

Chapter III, Section 1i, 1.21, page 303.

# Verification Notes

- Definition source: Direct from 1.21
- Confidence: HIGH
- Uncertainties: None
