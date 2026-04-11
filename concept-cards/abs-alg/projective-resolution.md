---
concept: Projective Resolution
slug: projective-resolution
category: homological-algebra
subcategory: resolutions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 780
section: "17.1 Introduction to Homological Algebra"
extraction_confidence: high
aliases:
  - "free resolution"
prerequisites:
  - module
  - projective-module
extends: []
related:
  - ext-functor
  - injective-resolution
contrasts_with:
  - injective-resolution
answers_questions:
  - "What is a projective resolution?"
---

# Quick Definition
A projective resolution of a module A is an exact sequence ··· → P_n → ··· → P_1 → P_0 → A → 0 where each P_i is projective. Every module has one.

# Core Definition
A **projective resolution** of an R-module A is an exact sequence ··· → P_n →^{d_n} P_{n-1} → ··· →^{d_1} P_0 →^{ε} A → 0 where each P_i is a projective R-module (Definition, p. 780). Every module has a projective (in fact, free) resolution, constructed by iteratively taking free modules mapping onto kernels.

# Prerequisites
- **module** — A is an R-module
- **projective-module** — The P_i must be projective

# Key Properties
1. Always exists (constructed from free modules)
2. Lifts of homomorphisms exist (Proposition 4)
3. Different projective resolutions give the same Ext groups (Theorem 6)

# Relationships
## Enables
- **ext-functor** — Ext is computed via projective resolutions

## Contrasts With
- **injective-resolution** — Uses injective modules instead

# Source Reference
Chapter 17, Section 17.1, Definition and Propositions 4-5, Theorem 6, pages 780-785.

# Verification Notes
- Confidence: HIGH — explicit construction and uniqueness up to homotopy
