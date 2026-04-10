---
concept: sl₂-Triple
slug: sl2-triple
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 310
section: "The root system attached to a split semisimple Lie algebra"
extraction_confidence: high
aliases:
  - "sl_2-triple"
  - "TDS"
prerequisites:
  - root-space-decomposition
extends: []
related:
  - cartan-subalgebra
  - root-system
contrasts_with: []
answers_questions:
  - "What is an sl₂-triple?"
---

# Quick Definition

An sl₂-triple in a Lie algebra 𝔤 is a triple (x, h, y) ≠ (0,0,0) satisfying [x,y] = h, [h,x] = 2x, [h,y] = −2y, giving an injective homomorphism sl₂ → 𝔤.

# Core Definition

An **sl₂-triple** in a Lie algebra 𝔤 is a triple (x, h, y) ≠ (0,0,0) of elements such that [x,y] = h, [h,x] = 2x, [h,y] = −2y (Milne, p. 310).

For each root α of a split semisimple Lie algebra (𝔤,𝔥), choosing nonzero x_α ∈ 𝔤^α determines a unique sl₂-triple (x_α, h_α, y_α) with α(h_α) = 2 (Theorem 2.22).

# Prerequisites

- **Root space decomposition** — sl₂-triples arise from root spaces

# Key Properties

1. Canonical one-to-one correspondence between sl₂-triples and injective homomorphisms sl₂ → 𝔤
2. 𝔰_α = 𝔤^{−α} ⊕ 𝔥_α ⊕ 𝔤^α ≅ sl₂ (Theorem 2.22c)
3. Jacobson-Morozov theorem: every nonzero nilpotent element extends to an sl₂-triple (Aside 2.24)

# Examples

**Example 1** (p. 308): In sl₂ itself, (x,h,y) = ([[0,1],[0,0]], [[1,0],[0,−1]], [[0,0],[1,0]]).

# Source Reference

Chapter III, Sections 2e–2f, pages 308–310.

# Verification Notes

- Definition source: Direct from p. 310
- Confidence: HIGH
- Uncertainties: None
