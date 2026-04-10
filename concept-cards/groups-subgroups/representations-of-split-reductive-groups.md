---
concept: Representations of Split Reductive Groups
slug: representations-of-split-reductive-groups
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 378
section: "Representations of split reductive groups"
extraction_confidence: high
aliases: []
prerequisites:
  - split-reductive-group
  - root-datum
  - dominant-weight
  - borel-subgroup
extends:
  - highest-weight-representation
related:
  - fundamental-weight
contrasts_with: []
answers_questions:
  - "What must I know before understanding representations of split reductive groups?"
---

# Quick Definition

Simple representations of a split reductive group G are classified by dominant weights in X*(T): each simple representation has a unique highest weight (a dominant weight stabilized by B), and every dominant weight occurs.

# Core Definition

Let G be a reductive group with maximal torus T and Borel subgroup B (Milne, §8, p. 378). For a simple representation r: G → GL_W (Theorem 8.1):

(a) There is a unique one-dimensional subspace L of W stabilized by B
(b) L = W_{λ_r} is a weight space for T (the highest weight)
(c) λ_r is dominant
(d) Every other weight satisfies λ = λ_r − ∑ m_i α_i with m_i ∈ ℕ

**Theorem 8.2**: V ↦ λ_r is a bijection from isomorphism classes of simple representations to dominant weights in X*(T).

# Prerequisites

- **Split reductive group** — The representation theory of G
- **Root datum** — Weights and roots live in the root datum
- **Dominant weight** — Parametrize simple representations
- **Borel subgroup** — Stabilizes the highest weight line

# Key Properties

1. Every representation of a reductive group (char 0) is semisimple
2. Simple representations are indexed by dominant weights λ = ∑ m_i λ_i + λ_0 with m_i ∈ ℕ, λ_0 ∈ X_0
3. Generalizes the highest weight theory for Lie algebras to reductive (not just semisimple) groups

# Examples

**Example 1** (p. 379): For SL₂, root datum (ℤ, {±2}, ℤ, {±1}), P⁺ = ℕ. The simple representation of degree m+1 is SL₂ acting on homogeneous polynomials of degree m.

**Example 2** (p. 380): For GL_n, simple representations with highest weight e₁+...+e_i are the exterior powers ∧ⁱ(kⁿ).

# Source Reference

Chapter V, Section 8, Theorems 8.1–8.2, pages 378–380.

# Verification Notes

- Definition source: Direct from Theorems 8.1–8.2
- Confidence: HIGH
- Uncertainties: None
