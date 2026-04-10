---
concept: Paris-Harrington Theorem
slug: paris-harrington-theorem
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 192
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "Theorem VI.7"
  - "R*(s)"
prerequisites:
  - ramsey-theorem-infinite
  - ramsey-number
extends:
  - ramsey-theorem-finite
related:
  - compactness-argument
contrasts_with: []
answers_questions:
  - "What is the Paris-Harrington theorem?"
  - "How does Ramsey theory connect to logic?"
---

# Quick Definition
The Paris-Harrington theorem strengthens Ramsey's theorem by requiring |S| ≥ min S for the monochromatic set. Though a statement about finite sets, it cannot be proved within Peano arithmetic.

# Core Definition
**Theorem 7** (Bollobás, p. 192): Let r, k and s ≥ 2. If n is sufficiently large, then for every k-colouring of [n]⁽ʳ⁾ there is a monochromatic set S ⊂ [n] such that |S| ≥ max{s, min S}. The function R*(s) (for r = 2, k = 2) satisfies 2^{2^{cs}} < R*(s) < 2^{2^{ds}} for constants c, d.

The remarkable result of Paris and Harrington (1977): although this is a statement about finite sets, it cannot be proved from the Peano axioms.

# Prerequisites
- **Ramsey theorem (infinite)** — used in the proof
- **Ramsey number** — R*(s) ≥ R(s)

# Key Properties
1. R*(s) exists but grows much faster than R(s)
2. R*(s) is doubly exponential: 2^{2^{Θ(s)}}
3. The statement is true but unprovable in Peano arithmetic
4. The proof uses infinite Ramsey theory and compactness

# Context & Application
The Paris-Harrington theorem was the first "natural" mathematical statement shown to be independent of Peano arithmetic, connecting combinatorics to mathematical logic. It started an active area connecting combinatorics and logic.

# Relationships
## Builds Upon
- **Ramsey theorem** — strengthened version

## Related
- Connections between combinatorics and mathematical logic

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, Theorem 7, page 192.

# Verification Notes
- Definition source: Direct from p. 192
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
