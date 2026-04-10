---
concept: Weight Lattice
slug: weight-lattice
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
  - "P(R)"
  - "P"
prerequisites:
  - root-system
  - coroot
  - root-lattice
extends: []
related:
  - fundamental-weight
  - dominant-weight
  - simply-connected-algebraic-group
contrasts_with:
  - root-lattice
answers_questions:
  - "What is the weight lattice?"
---

# Quick Definition

The weight lattice P = P(R) is the lattice dual to the coroot lattice Q(R^∨): it consists of all x ∈ V with ⟨x, α^∨⟩ ∈ ℤ for every root α.

# Core Definition

The **weight lattice** P = P(R) is the lattice dual to Q(R^∨): P = {x ∈ V | ⟨x, α^∨⟩ ∈ ℤ for all α ∈ R}. Its elements are called **weights** of the root system. We have P(R) ⊃ Q(R), and P/Q is finite (Milne, 1.20, p. 303).

# Prerequisites

- **Root system** — P is defined from the root system
- **Coroot** — P is the dual lattice to ℤR^∨
- **Root lattice** — Q ⊂ P

# Key Properties

1. P ⊃ Q (since ⟨R, α^∨⟩ ⊂ ℤ)
2. For a base S, P has basis {ϖ_α | α ∈ S} (the fundamental weights), dual to S^∨ (1.21)
3. X*(Z(G(𝔤))) ≅ P/Q (Theorem 3.12d)
4. The simply connected group corresponds to X = P; the adjoint group to X = Q

# Examples

**Example 1** (p. 315): For A_n, P = Q + ℤϖ₁ and P/Q ≅ ℤ/(n+1)ℤ.

**Example 2** (p. 308): For sl₂, Q = ℤα and P = ℤ(α/2), so P/Q ≅ ℤ/2ℤ.

# Relationships

## Builds Upon
- **Root lattice** — Q ⊂ P

## Enables
- **Fundamental weight** — The basis elements of P
- **Dominant weight** — Non-negative integer combinations of fundamental weights
- **Simply connected algebraic group** — Has character lattice X = P

## Contrasts With
- **Root lattice** — Q ⊂ P; the index P/Q classifies possible centres

# Source Reference

Chapter III, Section 1i, 1.20–1.21, pages 303–304.

# Verification Notes

- Definition source: Direct from 1.20
- Confidence: HIGH
- Uncertainties: None
