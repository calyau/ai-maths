---
concept: Complex Lie Group
slug: complex-lie-group
category: lie-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Groups"
chapter_number: 4
pdf_page: 327
section: "Lie groups"
extraction_confidence: high
aliases: []
prerequisites:
  - real-lie-group
extends:
  - real-lie-group
related:
  - algebraic-lie-group-functor
contrasts_with:
  - real-lie-group
answers_questions:
  - "How do algebraic groups relate to Lie groups?"
---

# Quick Definition

A complex Lie group is a complex manifold G with a group structure such that multiplication and inverse are holomorphic.

# Core Definition

A **complex Lie group** is a complex manifold G together with a group structure such that both the multiplication map G × G → G and the inverse map G → G are holomorphic (Milne, Definition 1.1b, p. 327).

A complex Lie group is **algebraic** if it is the Lie group defined by an algebraic group over ℂ (§2c, p. 329).

# Prerequisites

- **Real Lie group** — A complex Lie group is in particular a real Lie group

# Key Properties

1. A complex Lie group G may have many more representations than the algebraic group defining it (Example 2.7)
2. All representations of G are semisimple iff G contains a compact subgroup K with ℂ·Lie(K) = Lie(G) and G = K·G⁺ (Proposition 2.8)
3. Every complex reductive Lie group is algebraic (Remark 2.11, p. 330)

# Examples

**Example 1** (p. 329): z ↦ e^z: ℂ → ℂ× is a homomorphism of Lie groups not arising from an algebraic group homomorphism 𝔾_a → 𝔾_m.

# Source Reference

Chapter IV, Section 1, Definition 1.1b, page 327; Sections 2c–2d, pages 329–331.

# Verification Notes

- Definition source: Direct from Definition 1.1b
- Confidence: HIGH
- Uncertainties: None
