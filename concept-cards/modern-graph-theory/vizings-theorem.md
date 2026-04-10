---
concept: Vizing's Theorem
slug: vizings-theorem
category: edge-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 159
section: "V.2 Edge Colouring"
extraction_confidence: high
aliases:
  - "Theorem V.7"
  - "Vizing theorem"
prerequisites:
  - chromatic-index
  - edge-colouring
extends: []
related:
  - brooks-theorem
  - class-one-class-two
contrasts_with:
  - brooks-theorem
answers_questions:
  - "What distinguishes Brooks' theorem from Vizing's theorem?"
  - "How tightly can we bound the chromatic index?"
---

# Quick Definition
Vizing's theorem states that every graph G with maximum degree Δ has edge-chromatic number either Δ or Δ + 1.

# Core Definition
**Theorem 7** (Bollobás, p. 159): A graph G of maximal degree Δ has edge-chromatic number Δ or Δ + 1.

The proof is constructive: given all but one edge coloured with Δ + 1 colours, it shows how to recolour edges to accommodate the last edge. The key technique involves constructing sequences of edges and using Kempe-chain-like colour swaps.

# Prerequisites
- **Chromatic index** — the quantity being bounded
- **Edge colouring** — the context

# Key Properties
1. χ'(G) ∈ {Δ(G), Δ(G) + 1} for every graph G
2. The upper bound χ'(G) ≤ 2Δ − 1 from Brooks' theorem applied to L(G) is much weaker
3. Graphs with χ' = Δ are called Class 1; those with χ' = Δ + 1 are Class 2
4. The proof gives an algorithm for (Δ + 1)-edge-colouring

# Construction / Recognition
## Proof Technique (Sketch)
1. Assume all but one edge xy₁ is coloured with colours 1, ..., Δ + 1
2. Let s be a colour missing at x, tᵢ a colour missing at yᵢ
3. Construct sequences xy₁, xy₂, ... and t₁, t₂, ... where xyᵢ₊₁ has colour tᵢ
4. Two cases arise: (a) no edge xy has colour t_h — recolour and assign t_h to xy_h; (b) cycle back — use Kempe chain (two-colour subgraph) swaps to resolve

# Context & Application
Vizing's theorem is the edge-colouring analogue of Brooks' theorem for vertex colouring. While Brooks shows χ(G) ≤ Δ with two exceptions, Vizing shows the much tighter result that χ'(G) is within 1 of the trivial lower bound Δ. Classifying graphs as Class 1 or Class 2 is NP-complete.

# Examples
**Example** (p. 158): Bipartite graphs are Class 1 (χ' = Δ).

**Example** (p. 159): Complete graphs Kₙ with n odd are Class 2 (χ' = Δ + 1 = n).

**Example**: The Petersen graph is Class 2 (Δ = 3, χ' = 4).

# Relationships
## Builds Upon
- **Chromatic index** — establishes its range

## Enables
- **Class 1/Class 2 classification** of graphs
- Edge-colouring algorithms

## Related
- **Brooks' theorem** — analogous result for vertex colouring: χ(G) ≤ Δ with exceptions

## Contrasts With
- **Brooks' theorem** — Brooks bounds χ by Δ (with exceptions); Vizing bounds χ' by Δ + 1 (no exceptions for the upper bound)

# Common Errors
- **Error**: Thinking Vizing's theorem says χ'(G) = Δ always
  **Correction**: It says χ' ∈ {Δ, Δ + 1}; both values occur

# Common Confusions
- **Confusion**: Confusing Vizing's theorem with Brooks' theorem
  **Clarification**: Vizing is for edges (χ' ≤ Δ + 1), Brooks is for vertices (χ ≤ Δ with exceptions)

# Source Reference
Chapter V: Colouring, Section V.2, Theorem 7, pages 159–160.

# Verification Notes
- Definition source: Direct theorem statement from p. 159
- Confidence rationale: Explicit theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
