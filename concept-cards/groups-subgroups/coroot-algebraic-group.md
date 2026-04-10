---
concept: Coroot of an Algebraic Group
slug: coroot-algebraic-group
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 344
section: "Definition of the coroots"
extraction_confidence: high
aliases:
  - "α^∨ (algebraic group)"
prerequisites:
  - split-reductive-group
  - cocharacter-group
  - root-group
extends: []
related:
  - coroot
  - root-datum
contrasts_with: []
answers_questions:
  - "How are coroots defined for algebraic groups?"
---

# Quick Definition

For a split reductive group (G,T) and root α, the coroot α^∨ ∈ X_*(T) is the unique cocharacter such that the reflection s_α acts on X*(T) by s_α(x) = x − ⟨x, α^∨⟩α, with ⟨α, α^∨⟩ = 2.

# Core Definition

For a root α of a split reductive group (G,T), let T_α = Ker(α)° and G_α = C_G(T_α). The Weyl group W(G_α, T) contains a unique nontrivial element s_α, and there is a unique **coroot** α^∨ ∈ X_*(T) such that s_α(x) = x − ⟨x, α^∨⟩α for all x ∈ X*(T), with ⟨α, α^∨⟩ = 2 (Milne, Proposition 2.9b, p. 344).

# Prerequisites

- **Split reductive group** — Coroots are defined in this context
- **Cocharacter group** — α^∨ is a cocharacter
- **Root group** — G_α involves root groups U_α, U_{−α}

# Key Properties

1. ⟨α, α^∨⟩ = 2
2. α^∨ is determined by the rank-1 subgroup G_α
3. For GL_n: α_{ij}^∨ = λ_i − λ_j (Example 2.12)
4. For SL₂: α^∨ = λ (the unique cocharacter with ⟨2χ, λ⟩ = 2)

# Examples

**Example 1** (p. 345): For GL_n with α = χ₁−χ₂, the nontrivial Weyl group element swaps entries 1 and 2, giving α^∨ = λ₁ − λ₂.

# Source Reference

Chapter V, Section 2j, Proposition 2.9, pages 344–346.

# Verification Notes

- Definition source: Direct from Proposition 2.9b
- Confidence: HIGH
- Uncertainties: None
