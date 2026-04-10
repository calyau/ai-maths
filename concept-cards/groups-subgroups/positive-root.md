---
concept: Positive Root
slug: positive-root
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
  - "R⁺"
  - "R_+"
prerequisites:
  - base-of-root-system
extends: []
related:
  - simple-root
  - highest-root
  - borel-subalgebra-lie-algebra
contrasts_with: []
answers_questions:
  - "What is a positive root?"
---

# Quick Definition

A positive root (relative to a base S) is a root that can be written as a non-negative integer linear combination of simple roots.

# Core Definition

Let S be a base for a root system R. Then R = R₊ ⊔ R₋ where R₊ = {∑ m_α α | m_α ∈ ℕ} ∩ R and R₋ = {∑ m_α α | −m_α ∈ ℕ} ∩ R. The elements of R₊ are the **positive roots** and those of R₋ are the **negative roots** (Milne, 1.22, p. 303).

# Prerequisites

- **Base of root system** — Positive roots depend on choice of base

# Key Properties

1. Every root is either positive or negative (relative to a given base)
2. The simple roots are the indecomposable elements of R⁺
3. R⁺ is a maximal closed subset P of R with P ∩ (−P) = ∅
4. The set R⁺ determines the base S and the Borel subalgebra

# Examples

**Example 1** (p. 298): For A_n with base S = {e₁ − e₂, ..., e_n − e_{n+1}}, the positive roots are R⁺ = {e_i − e_j | i < j}.

# Relationships

## Builds Upon
- **Base of root system** — Positive roots are determined by the base

## Enables
- **Borel subalgebra** — 𝔟 = 𝔥 ⊕ ⊕_{α>0} 𝔤^α
- **Highest root** — The unique root with largest coefficients among positive roots

# Source Reference

Chapter III, Section 1i, pages 303–304.

# Verification Notes

- Definition source: Direct from 1.22
- Confidence: HIGH
- Uncertainties: None
