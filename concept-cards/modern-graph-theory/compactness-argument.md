---
concept: Compactness Argument for Ramsey Theory
slug: compactness-argument
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 191
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "Theorem VI.6"
  - "König's infinity lemma argument"
prerequisites:
  - ramsey-theorem-infinite
extends: []
related:
  - ramsey-theorem-finite
contrasts_with: []
answers_questions:
  - "How does the infinite Ramsey theorem imply the finite version?"
---

# Quick Definition
The infinite Ramsey theorem implies the finite version via compactness: if the finite version failed, there would exist colourings of [n] for each n without large monochromatic sets, and a limit colouring of ℕ would contradict the infinite theorem.

# Core Definition
**Theorem 6** (Bollobás, p. 191): Let r and k be natural numbers, and for every n ≥ 1, let Cₙ be a non-empty set of k-colourings of [n]⁽ʳ⁾ such that if n < m and c_m ∈ C_m then its restriction to [n]⁽ʳ⁾ belongs to Cₙ. Then there exists a colouring c: ℕ⁽ʳ⁾ → [k] whose restriction to [n]⁽ʳ⁾ belongs to Cₙ for every n.

This is a special case of Tychonov's theorem (product of compact spaces is compact).

# Prerequisites
- **Ramsey theorem (infinite)** — the infinite version being used

# Key Properties
1. A consistency condition on finite colourings implies existence of a global colouring
2. Derives finite Ramsey from infinite (but without explicit bounds)
3. Used repeatedly throughout the chapter (Schur, van der Waerden, Rado)
4. This is why the infinite version is often more useful for proving finite results

# Relationships
## Enables
- Deriving finite Ramsey numbers from the infinite theorem
- Deriving finite versions of Schur's, van der Waerden's, and Rado's theorems

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, Theorem 6, page 191.

# Verification Notes
- Definition source: Direct theorem statement from p. 191
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
