---
concept: Character Group
slug: character-group
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 334
section: "Split tori"
extraction_confidence: high
aliases:
  - "X*(T)"
  - "group of characters"
prerequisites:
  - split-torus
extends: []
related:
  - cocharacter-group
  - root-datum
contrasts_with:
  - cocharacter-group
answers_questions:
  - "What is the character group of a torus?"
---

# Quick Definition

The character group X*(T) = Hom(T, 𝔾_m) of a split torus T is the free abelian group of algebraic group homomorphisms from T to 𝔾_m. It is paired with the cocharacter group X_*(T) via ⟨χ, λ⟩ = χ ∘ λ.

# Core Definition

For a split torus T, the **character group** is X*(T) = Hom(T, 𝔾_m), the group of characters of T. It is a free abelian group of rank equal to dim T (Milne, §1b, p. 334).

There is a pairing ⟨ , ⟩: X*(T) × X_*(T) → End(𝔾_m) ≅ ℤ, defined by ⟨χ, λ⟩ = χ ∘ λ. This pairing realizes each group as the dual of the other.

# Prerequisites

- **Split torus** — Characters are defined for split tori

# Key Properties

1. Free abelian of rank dim T
2. Written additively: (aχ₁ + bχ₂)(t) = χ₁(t)^a χ₂(t)^b
3. For 𝔻_n, X*(T) has basis χ₁,...,χₙ where χᵢ(diag(a₁,...,aₙ)) = aᵢ

# Examples

**Example 1** (p. 335): For 𝔻_n, X*(T) = ⊕ ℤχᵢ and (5χ₂ + 7χ₃)(diag(a₁,a₂,a₃)) = a₂⁵a₃⁷.

# Relationships

## Contrasts With
- **Cocharacter group** — X_*(T) = Hom(𝔾_m, T), dual to X*(T)

# Source Reference

Chapter V, Section 1b, pages 334–335.

# Verification Notes

- Definition source: Direct from §1b
- Confidence: HIGH
- Uncertainties: None
