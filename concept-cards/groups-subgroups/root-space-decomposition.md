---
concept: Root Space Decomposition
slug: root-space-decomposition
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 308
section: "The roots of a split semisimple Lie algebra"
extraction_confidence: high
aliases:
  - "Cartan decomposition"
  - "eigenspace decomposition"
prerequisites:
  - split-semisimple-lie-algebra
  - cartan-subalgebra
extends: []
related:
  - root-system
  - sl2-triple
contrasts_with: []
answers_questions:
  - "What is the root space decomposition?"
---

# Quick Definition

The root space decomposition is the direct sum decomposition 𝔤 = 𝔥 ⊕ ⊕_{α∈R} 𝔤^α of a split semisimple Lie algebra into eigenspaces for the adjoint action of a Cartan subalgebra.

# Core Definition

Let (𝔤, 𝔥) be a split semisimple Lie algebra. For each α ∈ 𝔥^∨, define 𝔤^α = {x ∈ 𝔤 | [h,x] = α(h)x for all h ∈ 𝔥}. The **root space decomposition** is 𝔤 = 𝔥 ⊕ ⊕_{α∈R} 𝔤^α, where R is the set of nonzero α with 𝔤^α ≠ 0 (Milne, §2d, p. 308).

# Prerequisites

- **Split semisimple Lie algebra** — The decomposition requires a splitting Cartan subalgebra
- **Cartan subalgebra** — 𝔥 acts semisimply on 𝔤

# Key Properties

1. Each root space 𝔤^α is one-dimensional (Theorem 2.22a)
2. [𝔤^α, 𝔤^β] ⊂ 𝔤^{α+β} (Lemma 2.21)
3. 𝔥_α = [𝔤^α, 𝔤^{−α}] is one-dimensional (Theorem 2.22a)
4. For each α ∈ R, 𝔰_α = 𝔤^{−α} ⊕ 𝔥_α ⊕ 𝔤^α ≅ sl₂ (Theorem 2.22c)

# Examples

**Example 1** (p. 311): For sl_{n+1}, 𝔤 = 𝔥 ⊕ ⊕_{i≠j} kE_{ij} with 𝔤^{ε_i−ε_j} = kE_{ij}.

**Example 2** (p. 308): For sl₂, 𝔤 = 𝔤^α ⊕ 𝔥 ⊕ 𝔤^{−α} = ⟨x⟩ ⊕ ⟨h⟩ ⊕ ⟨y⟩.

# Relationships

## Builds Upon
- **Split semisimple Lie algebra** — The pair (𝔤, 𝔥)

## Enables
- **Root system** — R is extracted from this decomposition
- **sl₂-triple** — Each root gives an sl₂ subalgebra

# Source Reference

Chapter III, Sections 2d–2f, pages 308–310.

# Verification Notes

- Definition source: Direct from §2d
- Confidence: HIGH
- Uncertainties: None
