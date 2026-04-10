---
concept: Brooks' Theorem
slug: brooks-theorem
category: vertex-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 155
section: "V.1 Vertex Colouring"
extraction_confidence: high
aliases:
  - "Theorem V.3"
  - "Brooks's theorem"
prerequisites:
  - chromatic-number
  - greedy-colouring-algorithm
  - degeneracy-bound
extends:
  - degeneracy-bound
related:
  - vizings-theorem
contrasts_with:
  - vizings-theorem
answers_questions:
  - "What distinguishes Brooks' theorem from Vizing's theorem?"
  - "What is the best upper bound on chromatic number in terms of maximum degree?"
---

# Quick Definition
Brooks' theorem states that every connected graph G with maximum degree Δ ≥ 3 that is neither a complete graph nor an odd cycle satisfies χ(G) ≤ Δ.

# Core Definition
**Theorem 3** (Bollobás, p. 155): Let G be a connected graph with maximal degree Δ. Suppose G is neither a complete graph nor an odd cycle. Then χ(G) ≤ Δ.

The proof reduces to the case where G is 2-connected and Δ-regular (since non-regular connected graphs already satisfy χ ≤ Δ by the degeneracy bound). It then constructs a clever vertex ordering for the greedy algorithm.

# Prerequisites
- **Chromatic number** — the quantity being bounded
- **Greedy colouring algorithm** — the proof technique
- **Degeneracy bound** — handles the non-regular case

# Key Properties
1. χ(G) ≤ Δ(G) for connected G that is neither complete nor an odd cycle
2. The bound is tight: Kₙ requires n = Δ + 1 colours, and odd cycles require 3 = Δ + 1 colours
3. The proof works by finding two non-adjacent neighbours of a vertex xₙ, giving them the same colour, then greedily colouring the rest
4. The assumption Δ ≥ 3 is needed; connected 2-regular 3-chromatic graphs are exactly odd cycles

# Construction / Recognition
## Proof Strategy (for Δ-regular, 2-connected G ≠ Kₙ)
1. Choose any vertex xₙ
2. Find two non-adjacent neighbours x₁, x₂ of xₙ (exist since G is regular but not complete)
3. Order remaining vertices by BFS from xₙ backward: x₃, ..., xₙ₋₁
4. Greedy-colour in order x₁, x₂, ..., xₙ
5. x₁ and x₂ get the same colour (not adjacent)
6. When colouring xₙ (last), it has Δ neighbours but x₁, x₂ share a colour, so only Δ − 1 colours used among neighbours

# Context & Application
Brooks' theorem is one of the fundamental results of graph colouring. It shows that the trivial upper bound Δ + 1 can almost always be improved to Δ, with only two natural exceptions. It has analogues for edge colouring (Vizing's theorem) and list colouring.

# Examples
**Example** (p. 155): The complete graph Kₙ has Δ = n − 1 and χ = n = Δ + 1 (exception).
**Example**: The odd cycle C₂ₖ₊₁ has Δ = 2 and χ = 3 = Δ + 1 (exception).
**Example**: The Petersen graph has Δ = 3 and χ = 3 = Δ (satisfies Brooks' bound).

# Relationships
## Builds Upon
- **Degeneracy bound** — handles the non-regular case
- **Greedy colouring algorithm** — proof technique

## Enables
- Upper bounds in edge colouring (applied to line graphs)
- **Perfect graph** characterizations

## Related
- **Vizing's theorem** — the edge-colouring analogue: χ'(G) ∈ {Δ, Δ + 1}

## Contrasts With
- **Vizing's theorem** — Brooks bounds vertex chromatic number; Vizing bounds edge chromatic number

# Common Errors
- **Error**: Applying Brooks' theorem to odd cycles or complete graphs
  **Correction**: These are the two exceptions where χ = Δ + 1

# Common Confusions
- **Confusion**: Confusing Brooks' theorem (vertex colouring) with Vizing's theorem (edge colouring)
  **Clarification**: Brooks: χ(G) ≤ Δ for most graphs. Vizing: χ'(G) ≤ Δ + 1 for all graphs, and χ'(G) ≥ Δ always.

# Source Reference
Chapter V: Colouring, Section V.1, Theorem 3, pages 155–156.

# Verification Notes
- Definition source: Direct theorem statement from p. 155
- Confidence rationale: Explicit theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
