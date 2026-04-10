---
concept: Coroot
slug: coroot
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 296
section: "Root systems and their classification"
extraction_confidence: high
aliases:
  - "inverse root"
  - "dual root"
  - "α^∨"
  - "α-check"
prerequisites:
  - root-system
  - reflection
extends: []
related:
  - inverse-root-system
  - root-datum
  - cocharacter-group
contrasts_with:
  - root
answers_questions:
  - "What is a coroot?"
---

# Quick Definition

The coroot α^∨ of a root α is the unique element of V^∨ such that ⟨α, α^∨⟩ = 2 and the reflection s_α: x ↦ x − ⟨x, α^∨⟩α preserves the root system.

# Core Definition

For a root system (V, R), given a root α ∈ R, the **coroot** α^∨ is the unique element of V^∨ such that ⟨α, α^∨⟩ = 2, ⟨R, α^∨⟩ ⊂ ℤ, and the reflection s_α: x ↦ x − ⟨x, α^∨⟩α maps R into R (Milne, Definition 1.3, p. 296).

When V is equipped with an invariant inner product, α^∨ corresponds to 2α/(α,α) under the identification V ≅ V^∨.

The set R^∨ = {α^∨ | α ∈ R} is itself a root system in V^∨, called the **inverse** (or dual) root system (Milne, 1.19, p. 303).

# Prerequisites

- **Root system** — Coroots are defined relative to a root system
- **Reflection** — The coroot determines the reflection s_α

# Key Properties

1. ⟨α, α^∨⟩ = 2 for every root α
2. ⟨β, α^∨⟩ ∈ ℤ for all β ∈ R (the integrality condition)
3. With an inner product, 2(β,α)/(α,α) = ⟨β, α^∨⟩ (Milne, p. 298)
4. The coroots R^∨ form a root system in V^∨

# Context & Application

Coroots are essential for defining root lattices, weight lattices, Cartan matrices, and root data. In the theory of algebraic groups, the coroot α^∨ of a root α corresponds to a specific cocharacter of a maximal torus.

# Examples

**Example 1** (p. 308): For sl₂, R = {α, −α} where α(h) = 2. The coroot α^∨ = h, the diagonal matrix diag(1,−1).

**Example 2** (p. 301): For the rank 2 root systems, n(β,α) = ⟨β, α^∨⟩ takes values 0, ±1, ±2, or ±3 depending on the type (A₁×A₁, A₂, B₂, G₂).

# Relationships

## Builds Upon
- **Root system** — Each root determines a coroot

## Enables
- **Inverse root system** — The set of coroots forms a root system
- **Root datum** — Uses coroots as part of its structure
- **Cartan matrix** — Entries are ⟨α, β^∨⟩

## Contrasts With
- **Root** — A root lives in V; its coroot lives in V^∨

# Source Reference

Chapter III, Section 1a–1b, pages 296–303. Also Chapter V, Section 2j for the algebraic group perspective.

# Verification Notes

- Definition source: Direct from Definition 1.3 and 1.19
- Confidence: HIGH — explicitly defined
- Uncertainties: None
