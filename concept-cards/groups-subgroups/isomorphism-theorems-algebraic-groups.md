---
concept: Isomorphism Theorems for Algebraic Groups
slug: isomorphism-theorems-algebraic-groups
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 121
section: "9 Group theory: the isomorphism theorems"
extraction_confidence: high
aliases:
  - Noether isomorphism theorems
prerequisites:
  - affine-algebraic-group
  - quotient-group
  - normal-subgroup
extends: []
related:
  - homomorphism-theorem
  - correspondence-theorem
  - schreier-refinement-theorem
contrasts_with: []
answers_questions:
  - "Do the standard isomorphism theorems hold for algebraic groups?"
---

# Quick Definition

The Noether isomorphism theorems from abstract group theory extend to algebraic groups: the homomorphism theorem (alpha factors as surjection-isomorphism-injection), the isomorphism theorem (H/(H cap N) -> HN/N), and the correspondence theorem (subgroups of G containing N correspond to subgroups of G/N).

# Core Definition

The isomorphism theorems for algebraic groups are (Milne, pp. 121-125):
- *(Existence of quotients, 9.1)*: Every normal subgroup arises as the kernel of a quotient map.
- *(Homomorphism theorem, 9.6)*: For any homomorphism alpha: G -> G', the kernel N is normal, the image alpha(G) is a subgroup of G', and alpha factors as G ->> G/N -> alpha(G) >-> G'.
- *(Isomorphism theorem, 9.12)*: If H normalizes N, then H/(H cap N) -> HN/N is an isomorphism.
- *(Correspondence theorem, 9.14)*: For normal N, H -> H/N is a bijection between subgroups of G containing N and subgroups of G/N. Normal subgroups correspond, and G/H -> (G/N)/(H/N).

# Prerequisites

- **Affine algebraic group** -- The groups under consideration
- **Quotient group** -- Quotients are essential throughout
- **Normal subgroup** -- Normal subgroups define the quotients

# Key Properties

1. All four classical isomorphism theorems hold for algebraic groups (not just smooth ones)
2. The category of commutative algebraic groups over a field is abelian (Theorem 9.21)
3. The Schreier refinement theorem holds: any two subnormal series have equivalent refinements (Theorem 9.18)
4. A key advantage of allowing nilpotents: these theorems fail for "smooth algebraic groups" in positive characteristic

# Context & Application

These theorems justify treating algebraic groups with the same group-theoretic intuition as abstract groups. The extension to non-smooth groups (allowing nilpotent elements in O(G)) was emphasized by Cartier and is essential for the theory to work cleanly in positive characteristic.

# Examples

**Example 1** (p. 122): PGL_n = GL_n/G_m and PSL_n = SL_n/mu_n. The natural map PSL_n -> PGL_n is an isomorphism of algebraic groups, even though SL_n(k)/mu_n(k) -> GL_n(k)/G_m(k) is not surjective in general.

**Example 2** (p. 124): For GL_n, H = SL_n, N = G_m, the isomorphism theorem gives SL_n/mu_n -> GL_n/G_m.

# Relationships

## Builds Upon
- **Quotient group** -- All theorems involve quotients

## Enables
- **Solvable algebraic group** -- Uses subnormal series and quotients
- **Composition series** -- Jordan-Holder type results

# Common Confusions

- **Confusion**: Thinking these theorems require smooth groups
  **Clarification**: The full generality requires allowing non-reduced group schemes. Over non-perfect fields, the isomorphism theorem fails for smooth groups (the map H/(H cap N) -> HN/N may only be a purely inseparable isogeny).

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 9, pages 121-128. Theorems 9.6, 9.12, 9.14, 9.18, 9.21.

# Verification Notes

- Definition source: Direct from Section 9
- Confidence rationale: Four explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
