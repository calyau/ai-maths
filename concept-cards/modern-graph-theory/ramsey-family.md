---
concept: Ramsey Family
slug: ramsey-family
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 216
section: "VI.5 Subsequences"
extraction_confidence: high
aliases:
  - "Ramsey set"
prerequisites:
  - ramsey-theorem-infinite
extends: []
related:
  - galvin-prikry-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for a family to be Ramsey?"
---

# Quick Definition
A family F ⊂ 2^ℕ is Ramsey if there exists an infinite M ⊂ ℕ with either M^(ω) ⊂ F or M^(ω) ⊂ 2^ℕ \ F. Not every family is Ramsey, but all open sets are (Galvin-Prikry).

# Core Definition
A family F ⊂ 2^ℕ is **Ramsey** if there exists an M ∈ ℕ^(ω) such that either M^(ω) ⊂ F or M^(ω) ⊂ 2^ℕ − F. This asks whether a red-blue colouring of ℕ^(ω) (the infinite subsets of ℕ) always has an infinite monochromatic set. Not every F is Ramsey (Exercise 45), but open sets are (Theorem 29) (Bollobás, p. 216).

# Prerequisites
- **Ramsey theorem (infinite)** — context

# Key Properties
1. Not every family is Ramsey (contrast with finite Ramsey)
2. Open families are Ramsey (Galvin-Prikry)
3. Sets "insensitive to small changes" are Ramsey
4. Sets "sensitive to small changes" need not be Ramsey

# Relationships
## Related
- **Galvin-Prikry theorem** — open sets are Ramsey

# Source Reference
Chapter VI: Ramsey Theory, Section VI.5, page 216.

# Verification Notes
- Definition source: Direct from p. 216
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
