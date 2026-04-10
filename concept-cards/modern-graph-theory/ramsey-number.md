---
concept: Ramsey Number
slug: ramsey-number
category: ramsey-theory
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 187
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "R(s,t)"
  - "R(s)"
  - "diagonal Ramsey number"
  - "off-diagonal Ramsey number"
prerequisites: []
extends: []
related:
  - ramsey-theorem-finite
  - ramsey-number-bounds
  - hypergraph-ramsey-number
contrasts_with: []
answers_questions:
  - "What is a Ramsey number?"
  - "What must I know before understanding Ramsey theory?"
---

# Quick Definition
The Ramsey number R(s, t) is the smallest n such that every red-blue colouring of the edges of Kₙ contains either a red Kₛ or a blue Kₜ. The diagonal Ramsey number R(s) = R(s, s).

# Core Definition
The **Ramsey number** R(s, t) is defined as the smallest value of n for which every red-blue colouring of Kₙ yields a red Kₛ or a blue Kₜ. If no such n exists, R(s, t) = ∞ (but Theorem 1 proves it is always finite). R(s, t) = R(t, s) and R(s, 2) = s. The **diagonal Ramsey number** R(s) = R(s, s) is the minimal n such that every graph of order n has a trivial subgraph of order s — either a complete or empty subgraph of order s (Bollobás, pp. 187–188).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. R(s, t) = R(t, s) (symmetry)
2. R(s, 2) = s
3. R(s, t) ≤ R(s−1, t) + R(s, t−1) (Theorem 1)
4. R(s, t) ≤ C(s+t−2, s−1) (binomial coefficient bound)
5. R(s) ≤ C(2s−2, s−1) ≤ 2²ˢ⁻²/√s
6. R(3,3) = 6: "at a party of 6, three mutual acquaintances or three mutual strangers exist"
7. Very few Ramsey numbers are known exactly

# Construction / Recognition
## To Show R(s,t) ≤ n
1. Consider an arbitrary red-blue colouring of Kₙ
2. Show it must contain a red Kₛ or blue Kₜ

## To Show R(s,t) > n
1. Exhibit a specific red-blue colouring of Kₙ with no red Kₛ and no blue Kₜ

# Context & Application
Ramsey numbers express the principle that "complete disorder is impossible" — any large enough structure must contain regular substructures. They are notoriously difficult to compute; only a handful of exact values are known despite decades of effort.

# Examples
**Example** (p. 188): R(3,3) = 6, R(3,4) = 9, R(3,5) = 14, R(4,4) = 18, R(4,5) = 25.

**Example** (p. 188): R(3,8) = 28 and R(3,9) = 36 require considerable effort to prove.

**Example** (Table VI.1, p. 189): Bounds for many two-colour Ramsey numbers are tabulated.

# Relationships
## Enables
- **Ramsey theorem** — proves R(s,t) is always finite
- **Hypergraph Ramsey numbers** — generalization to r-tuples
- **Graphical Ramsey numbers** — generalization to arbitrary graphs

## Related
- **Probabilistic method** — gives lower bounds R(s) ≥ 2^{s/2}
- **Cups and caps** — Erdős-Szekeres theorem gives exact values for related functions

# Common Errors
- **Error**: Expecting to determine R(s,t) exactly for moderate s,t
  **Correction**: Even R(5,5) is unknown; exact computation is extraordinarily difficult

# Common Confusions
- **Confusion**: Thinking R(s,t) grows polynomially
  **Clarification**: R(s) grows exponentially: 2^{s/2} ≤ R(s) ≤ 4^s/√s

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, pages 187–189.

# Verification Notes
- Definition source: Direct from p. 187
- Confidence rationale: Explicitly defined with extensive discussion
- Uncertainties: None
- Cross-reference status: Verified
