---
concept: Dominant Weight
slug: dominant-weight
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
  - "P₊₊"
  - "P_{++}"
prerequisites:
  - weight-lattice
  - fundamental-weight
  - base-of-root-system
extends: []
related:
  - highest-weight-representation
  - representations-of-split-reductive-groups
contrasts_with: []
answers_questions:
  - "What is a dominant weight?"
---

# Quick Definition

A weight λ is dominant if ⟨λ, α^∨⟩ ∈ ℕ for all simple roots α. Dominant weights parametrize the simple representations of semisimple Lie algebras and reductive groups.

# Core Definition

A weight λ is **dominant** if ⟨λ, α^∨⟩ ∈ ℕ for all α ∈ S (a chosen base). The set of dominant weights is P₊₊ = {x ∈ V | ⟨x, α^∨⟩ ∈ ℕ for all α ∈ S} ⊂ P₊(R) (Milne, 1.22, p. 303).

In terms of fundamental weights: P₊₊ = {∑ m_i ϖ_i | m_i ∈ ℕ}.

# Prerequisites

- **Weight lattice** — Dominant weights are elements of P
- **Fundamental weight** — Dominant weights are ℕ-linear combinations of fundamental weights

# Key Properties

1. V ↦ ϖ_V defines a bijection from isomorphism classes of simple 𝔤-modules to P₊₊ (Theorems 2.38–2.39)
2. Every dominant weight occurs as the highest weight of some simple module (Theorem 2.38)

# Examples

**Example 1** (p. 315): For sl_{n+1}, the dominant weights are ∑ m_i ϖ_i with m_i ∈ ℕ. The simple module with highest weight ϖ_r is ∧^r(k^{n+1}).

# Relationships

## Enables
- **Highest weight representation** — Simple modules are indexed by dominant weights

# Source Reference

Chapter III, Section 1i, 1.22, page 303.

# Verification Notes

- Definition source: Direct from 1.22
- Confidence: HIGH
- Uncertainties: None
