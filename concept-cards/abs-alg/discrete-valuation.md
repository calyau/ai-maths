---
concept: Discrete Valuation
slug: discrete-valuation
category: commutative-algebra
subcategory: valuation-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Artinian Rings, Discrete Valuation Rings, and Dedekind Domains"
chapter_number: 16
pdf_page: 757
section: "16.2 Discrete Valuation Rings"
extraction_confidence: high
aliases:
  - "p-adic valuation"
prerequisites:
  - field
extends: []
related:
  - discrete-valuation-ring
contrasts_with: []
answers_questions:
  - "What is a discrete valuation?"
---

# Quick Definition
A discrete valuation on a field K is a surjective function ν: K× → Z satisfying ν(xy) = ν(x) + ν(y) and ν(x+y) ≥ min{ν(x), ν(y)}.

# Core Definition
A **discrete valuation** on a field K is a function ν: K× → Z satisfying: (i) ν is surjective, (ii) ν(xy) = ν(x) + ν(y) for all x,y, (iii) ν(x+y) ≥ min{ν(x), ν(y)} when x+y ≠ 0 (Definition, p. 757). The valuation ring {x ∈ K | ν(x) ≥ 0} ∪ {0} is a DVR.

# Prerequisites
- **field** — Valuations are defined on fields

# Key Properties
1. ν(1) = 0
2. ν(x^{-1}) = -ν(x)
3. The valuation ring is a DVR

# Examples
**Example** (p. 757): The p-adic valuation v_p on Q: for a/b = p^n(a_1/b_1) with gcd(a_1,p) = gcd(b_1,p) = 1, define v_p(a/b) = n. The valuation ring is Z_(p).

# Relationships
## Enables
- **discrete-valuation-ring** — Valuation rings are DVRs

# Source Reference
Chapter 16, Section 16.2, Definition, pages 757-758.

# Verification Notes
- Confidence: HIGH — explicit definition with examples
