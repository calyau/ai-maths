---
concept: Chain Complex
slug: chain-complex
category: homological-algebra
subcategory: complexes
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 776
section: "17.1 Introduction to Homological Algebra"
extraction_confidence: high
aliases:
  - "cochain complex"
prerequisites:
  - module
  - homomorphism
extends: []
related:
  - homology-group
  - exact-sequence
contrasts_with: []
answers_questions:
  - "What is a chain complex?"
  - "What must I know before studying homological algebra?"
---

# Quick Definition
A chain complex is a sequence of abelian groups (or modules) with homomorphisms where the composition of any two successive maps is zero. Cohomology groups measure the failure of exactness.

# Core Definition
A sequence C: 0 → C^0 → C^1 → ··· → C^n → ··· is a **cochain complex** if the composition d_{n+1} ∘ d_n = 0 for all n (Definition, p. 776). The n-th **cohomology group** is H^n(C) = ker d_{n+1}/image d_n. Similarly, a **chain complex** has decreasing indices with homology groups H_n(C) = ker d_n/image d_{n+1}. A complex is exact iff all cohomology/homology groups vanish.

# Prerequisites
- **module** — Chain complexes consist of modules
- **homomorphism** — Differentials are module homomorphisms

# Key Properties
1. d_{n+1} ∘ d_n = 0 (image ⊆ kernel at each stage)
2. Exactness ↔ all cohomology groups vanish
3. Homomorphisms of complexes induce maps on cohomology (Proposition 1)
4. Short exact sequences of complexes give long exact sequences in cohomology (Theorem 2)

# Relationships
## Enables
- **homology-group** — Cohomology/homology groups measure non-exactness
- **ext-functor** — Ext groups are cohomology groups of Hom-applied complexes

# Source Reference
Chapter 17, Section 17.1, Definition and Theorem 2, pages 776-779.

# Verification Notes
- Confidence: HIGH — explicit definitions
