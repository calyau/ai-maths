---
concept: Ramsey's Theorem (Infinite Version)
slug: ramsey-theorem-infinite
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 190
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "Theorem VI.4"
  - "infinite Ramsey theorem"
prerequisites:
  - ramsey-number
extends:
  - ramsey-theorem-finite
related:
  - compactness-argument
contrasts_with: []
answers_questions:
  - "Does Ramsey's theorem hold for infinite sets?"
---

# Quick Definition
If the r-tuples of an infinite set A are coloured with finitely many colours, then A contains an infinite monochromatic subset — all r-tuples from this subset have the same colour.

# Core Definition
**Theorem 4** (Bollobás, p. 190): Let 1 ≤ r < ∞ and let c: A⁽ʳ⁾ → [k] be a k-colouring of the r-tuples of an infinite set A. Then A contains a monochromatic infinite set.

The proof uses induction on r. For r = 1 it's the pigeonhole principle. For r > 1, pick x₁ ∈ A, define a (r−1)-colouring on B₁ = A − {x₁} by c₁(τ) = c(τ ∪ {x₁}), find monochromatic A₁ by induction, iterate, then use pigeonhole on the colour sequence d₁, d₂, ...

# Prerequisites
- **Ramsey number** — the infinite version extends the finite one

# Key Properties
1. Implies the finite version via compactness (Theorem 6)
2. The infinite version is the original form proved by Ramsey (1930)
3. The proof constructs a nested sequence A₀ ⊃ A₁ ⊃ ... of infinite sets
4. A stronger form (Theorem 5): exists M ⊂ ℕ such that for every r, all r-tuples with min ≥ rth element of M are monochromatic

# Context & Application
The infinite Ramsey theorem is the original result of Ramsey (1930). It implies the finite version via a compactness argument and is the starting point for partition calculus in set theory.

# Examples
**Example** (p. 187): If edges of K_ℕ are coloured red/blue, some infinite set has all its edges one colour.

# Relationships
## Builds Upon
- **Ramsey theorem (finite)** — the infinite version is stronger

## Enables
- **Compactness argument** — derives finite version from infinite
- **Canonical Ramsey theorems** — extend to infinitely many colours

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, Theorem 4, pages 190–191.

# Verification Notes
- Definition source: Direct theorem statement from p. 190
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
