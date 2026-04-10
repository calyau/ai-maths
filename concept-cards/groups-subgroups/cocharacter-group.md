---
concept: Cocharacter Group
slug: cocharacter-group
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
  - "X_*(T)"
  - "group of cocharacters"
  - "one-parameter subgroup"
prerequisites:
  - split-torus
extends: []
related:
  - character-group
  - root-datum
contrasts_with:
  - character-group
answers_questions:
  - "What is the cocharacter group of a torus?"
---

# Quick Definition

The cocharacter group X_*(T) = Hom(𝔾_m, T) of a split torus T is the free abelian group of algebraic group homomorphisms from 𝔾_m to T. It is dual to the character group X*(T).

# Core Definition

For a split torus T, the **cocharacter group** is X_*(T) = Hom(𝔾_m, T), the group of cocharacters (or one-parameter subgroups) of T. It is a free abelian group of rank dim T, and the pairing ⟨ , ⟩: X*(T) × X_*(T) → ℤ realizes each as the dual of the other (Milne, §1b, p. 334).

# Prerequisites

- **Split torus** — Cocharacters are defined for split tori

# Key Properties

1. Free abelian of rank dim T
2. For 𝔻_n, X_*(T) has basis λ₁,...,λₙ where λᵢ(t) = diag(1,...,t,...,1)
3. ⟨χⱼ, λᵢ⟩ = δᵢⱼ

# Examples

**Example 1** (p. 335): For 𝔻_n, ∑aᵢλᵢ maps t to diag(t^{a₁},...,t^{aₙ}).

# Relationships

## Contrasts With
- **Character group** — X*(T) = Hom(T, 𝔾_m), dual to X_*(T)

# Source Reference

Chapter V, Section 1b, pages 334–335.

# Verification Notes

- Definition source: Direct from §1b
- Confidence: HIGH
- Uncertainties: None
