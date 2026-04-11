---
concept: Long Exact Sequence in Cohomology
slug: long-exact-sequence-in-cohomology
category: homological-algebra
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 779
section: "17.1 Introduction to Homological Algebra"
extraction_confidence: high
aliases:
  - "connecting homomorphism"
prerequisites:
  - chain-complex
  - homology-group
  - exact-sequence
extends: []
related:
  - ext-functor
  - tor-functor
contrasts_with: []
answers_questions:
  - "What is the long exact sequence in cohomology?"
---

# Quick Definition
A short exact sequence of cochain complexes 0 → A → B → C → 0 induces a long exact sequence 0 → H^0(A) → H^0(B) → H^0(C) → H^1(A) → ··· with connecting homomorphisms.

# Core Definition
**Theorem 2 (Long Exact Sequence in Cohomology)**: Given a short exact sequence 0 → A → B → C → 0 of cochain complexes, there is a long exact sequence: 0 → H^0(A) → H^0(B) → H^0(C) →^{δ_0} H^1(A) → H^1(B) → H^1(C) →^{δ_1} H^2(A) → ··· (p. 779). The maps δ_n are called connecting homomorphisms.

# Prerequisites
- **chain-complex** — Involves complexes
- **homology-group** — The long sequence consists of cohomology groups
- **exact-sequence** — Must understand exactness

# Key Properties
1. If two of the three complexes are exact, so is the third
2. The connecting homomorphisms δ_n are functorial

# Relationships
## Enables
- **ext-functor** — Ext arises from long exact sequences applied to Hom
- **tor-functor** — Tor arises similarly from tensor products

# Source Reference
Chapter 17, Section 17.1, Theorem 2, page 779.

# Verification Notes
- Confidence: HIGH — major theorem stated explicitly
