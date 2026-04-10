---
concept: Five Colour Theorem
slug: five-colour-theorem
category: planar-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 161
section: "V.3 Graphs on Surfaces"
extraction_confidence: high
aliases:
  - "Theorem V.8"
  - "5-colour theorem"
prerequisites:
  - chromatic-number
  - euler-formula-for-planar-graphs
extends: []
related:
  - four-colour-theorem
  - kempe-chain
contrasts_with:
  - four-colour-theorem
answers_questions:
  - "How many colours suffice to colour any planar graph?"
---

# Quick Definition
Every planar graph is 5-colourable. This was the strongest result known for over a century before the four-colour theorem was proved.

# Core Definition
**Theorem 8** (Bollobás, p. 161): Every plane graph is 5-colourable.

The proof uses the fact that every planar graph has a vertex of degree ≤ 5 (from Euler's formula) and Kempe chains (two-colour exchange paths). A hypothetical minimal counterexample with 6-chromatic planar graph leads to a contradiction by analysing paths P₁₃ and P₂₄ around a degree-5 vertex.

# Prerequisites
- **Chromatic number** — the quantity being bounded
- **Euler's formula for planar graphs** — implies every planar graph has a vertex of degree ≤ 5

# Key Properties
1. Every planar graph has chromatic number at most 5
2. The proof uses Kempe chains: paths alternating two colours
3. The key argument shows that P₁₃ and P₂₄ paths cannot coexist around a degree-5 vertex in a planar graph
4. First proved by Heawood (1890) by modifying Kempe's false proof of the four-colour theorem

# Construction / Recognition
## Proof Strategy
1. Take a minimal 6-chromatic planar graph G
2. Find a vertex x of degree ≤ 5 (by Euler's formula)
3. G − x is 5-colourable; all 5 colours must appear among neighbours of x
4. Consider H(i,j) subgraph of colours i,j
5. If x₁, x₃ are in different components of H(1,3), swap colours to free a colour
6. Otherwise P₁₃ path exists; but then P₂₄ path cannot cross it (planarity), so swap on H(2,4) works

# Context & Application
The five-colour theorem was proved by Heawood in 1890, after he refuted Kempe's 1879 proof of the four-colour theorem. It remained the best result for 86 years until Appel and Haken proved the four-colour theorem in 1976.

# Examples
**Example** (p. 162): The cycle x₁P₁₃x₃ separates x₂ from x₄, so P₂₄ cannot exist (Figure V.4).

# Relationships
## Builds Upon
- **Euler's formula** — provides the degree-5 vertex

## Enables
- Understanding the proof structure of the four-colour theorem
- Thomassen's list colouring result (Theorem 12)

## Related
- **Kempe chain** — the proof technique

## Contrasts With
- **Four colour theorem** — the stronger (and harder) result: every planar graph is 4-colourable

# Common Errors
- **Error**: Attempting to extend the proof to 4 colours using the same approach
  **Correction**: Kempe's attempt at this fails because with 4 colours the chain arguments become circular; the four-colour theorem requires fundamentally different techniques

# Source Reference
Chapter V: Colouring, Section V.3, Theorem 8, pages 161–162.

# Verification Notes
- Definition source: Direct theorem and proof from pp. 161–162
- Confidence rationale: Explicit theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
