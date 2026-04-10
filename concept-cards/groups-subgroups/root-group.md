---
concept: Root Group
slug: root-group
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
  - "U_α"
prerequisites:
  - split-reductive-group
  - root-datum
extends: []
related:
  - borel-subgroup
  - parabolic-subgroup
contrasts_with: []
answers_questions:
  - "What is a root group?"
---

# Quick Definition

The root group U_α of a root α in a split reductive group (G,T) is the unique subgroup isomorphic to 𝔾_a such that T acts on it through the character α: t · u_α(a) · t⁻¹ = u_α(α(t)a).

# Core Definition

For a split reductive group (G,T) and a root α ∈ R, the **root group** U_α is the unique subgroup of G isomorphic to 𝔾_a such that, for any isomorphism u_α: 𝔾_a → U_α, t · u_α(a) · t⁻¹ = u_α(α(t)a) for all t ∈ T(k^{al}), a ∈ G(k^{al}) (Milne, Proposition 2.9a, p. 344).

# Prerequisites

- **Split reductive group** — Root groups exist in split reductive groups
- **Root datum** — The roots index the root groups

# Key Properties

1. U_α ≅ 𝔾_a (additive group)
2. Lie(U_α) = 𝔤_α (the root space)
3. G_α = ⟨T, U_α, U_{−α}⟩ is a rank-1 subgroup centralizing T_α = Ker(α)°

# Examples

**Example 1** (p. 365): For GL_n with α = α_{ij}, exp_α(x) = I + xE_{ij}.

# Source Reference

Chapter V, Section 2j, Proposition 2.9, page 344; Section 4b, page 365.

# Verification Notes

- Definition source: Direct from Proposition 2.9a
- Confidence: HIGH
- Uncertainties: None
