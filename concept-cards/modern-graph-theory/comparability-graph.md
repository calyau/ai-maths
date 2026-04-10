---
concept: Comparability Graph
slug: comparability-graph
category: perfect-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 177
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - perfect-graph
extends: []
related:
  - dilworths-theorem
contrasts_with: []
answers_questions:
  - "What is a comparability graph?"
---

# Quick Definition
The comparability graph C(P) of a partially ordered set P = (X, <) has vertex set X with edges between comparable pairs. Comparability graphs and their complements are perfect.

# Core Definition
Given a partially ordered set P = (X, <), its **comparability graph** is C(P) = (X, E) where E = {xy ∈ X⁽²⁾ : x < y or y < x}. **Theorem 17** (Bollobás, p. 177): Comparability graphs and their complements are perfect. The proof uses rank functions for χ(H) = ω(H) and Dilworth's theorem for χ(H̅) = ω(H̅).

# Prerequisites
- **Perfect graph** — comparability graphs are examples of perfect graphs

# Key Properties
1. Comparability graphs are perfect
2. Complements of comparability graphs are perfect
3. χ(C(P)) equals the length of the longest chain in P
4. χ(C̅(P)) equals the minimum number of chains partitioning P (by Dilworth's theorem)

# Relationships
## Related
- **Dilworth's theorem** — the equality χ(C̅(P)) = ω(C̅(P)) is exactly Dilworth's theorem

# Source Reference
Chapter V: Colouring, Section V.5, Theorem 17, page 177.

# Verification Notes
- Definition source: Direct from p. 177
- Confidence rationale: Explicitly defined with proof
- Uncertainties: None
- Cross-reference status: Verified
