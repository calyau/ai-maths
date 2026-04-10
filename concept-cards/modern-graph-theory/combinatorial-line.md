---
concept: Combinatorial Line
slug: combinatorial-line
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 208
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "line in a cube"
prerequisites: []
extends: []
related:
  - hales-jewett-theorem
  - combinatorial-cube
contrasts_with: []
answers_questions:
  - "What is a combinatorial line?"
---

# Quick Definition
A combinatorial line in the cube Aⁿ is a set of |A| points obtained by fixing some coordinates and letting the remaining coordinates all take the same value, varying over A.

# Core Definition
A **combinatorial line** in Aⁿ is a set L of the form L = {(a₁,...,aₙ) ∈ Aⁿ : aᵢ = aⱼ for i,j ∈ I and aᵢ = aᵢ⁰ for i ∉ I}, where I ⊂ [n] is non-empty and aᵢ⁰ are fixed elements. Every line has exactly |A| elements. There are (p+1)ⁿ − pⁿ lines in [p]ⁿ (Bollobás, p. 208).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Every line has exactly |A| = p elements
2. Determined by a non-empty set I of "variable" coordinates and fixed values for the rest
3. In [p]², there are 2p + 1 lines: p vertical, p horizontal, 1 diagonal
4. Total number in [p]ⁿ: (p+1)ⁿ − pⁿ

# Relationships
## Enables
- **Hales-Jewett theorem** — seeks monochromatic lines

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, page 208.

# Verification Notes
- Definition source: Direct from p. 208
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
