---
concept: Ramsey Number for Independent Edges vs. Complete Graph
slug: ramsey-independent-edges
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 198
section: "VI.3 Ramsey Theory For Graphs"
extraction_confidence: high
aliases:
  - "Theorem VI.10"
  - "r(ℓK₂, K_p)"
prerequisites:
  - graphical-ramsey-number
extends: []
related:
  - ramsey-for-multiple-copies
contrasts_with: []
answers_questions:
  - "What is r(ℓK₂, Kₚ)?"
---

# Quick Definition
r(ℓK₂, Kₚ) = 2ℓ + p − 2 for ℓ ≥ 1, p ≥ 2: the Ramsey number for ℓ independent edges versus a complete graph of order p.

# Core Definition
**Theorem 10** (Bollobás, p. 198): For ℓ ≥ 1 and p ≥ 2, r(ℓK₂, Kₚ) = 2ℓ + p − 2. The lower bound: K_{2ℓ−1} ∪ E_{p−2} has no ℓ independent edges and its complement has no Kₚ. The upper bound: in a graph of order 2ℓ + p − 2, a maximal set of s ≤ ℓ − 1 independent edges leaves ≥ p uncovered vertices spanning a complete subgraph in the complement.

# Prerequisites
- **Graphical Ramsey number** — the quantity being determined

# Key Properties
1. r(ℓK₂, Kₚ) = 2ℓ + p − 2 (exact)
2. For any graph H of order h: r(ℓK₂, H) ≤ 2ℓ + h − 2

# Relationships
## Related
- **Ramsey for multiple copies** — related exact formulas

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, Theorem 10, page 198.

# Verification Notes
- Definition source: Direct theorem statement from p. 198
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
