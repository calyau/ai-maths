---
concept: Greedy Colouring Algorithm
slug: greedy-colouring-algorithm
category: vertex-coloring
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 154
section: "V.1 Vertex Colouring"
extraction_confidence: high
aliases:
  - "greedy algorithm for colouring"
  - "sequential colouring"
prerequisites:
  - vertex-colouring
  - chromatic-number
extends: []
related:
  - brooks-theorem
  - degeneracy-bound
contrasts_with: []
answers_questions:
  - "How does the greedy colouring algorithm work?"
  - "Why does vertex ordering matter for greedy colouring?"
---

# Quick Definition
The greedy colouring algorithm colours vertices one by one in a fixed order, assigning each vertex the smallest colour not used by any of its already-coloured neighbours.

# Core Definition
Given an ordering x₁, x₂, ..., xₙ of the vertices of G, the greedy algorithm assigns x₁ colour 1, then for each subsequent vertex xᵢ, assigns the smallest positive integer not used by any neighbour of xᵢ among {x₁, ..., xᵢ₋₁}. The algorithm always produces a valid colouring using at most Δ(G) + 1 colours, but may use more colours than necessary depending on the vertex ordering (Bollobás, p. 154).

# Prerequisites
- **Vertex colouring** — the algorithm produces a proper vertex colouring
- **Chromatic number** — the algorithm's output is compared against χ(G)

# Key Properties
1. Always produces a valid proper colouring
2. Uses at most Δ(G) + 1 colours regardless of ordering
3. For every graph, there exists an ordering where greedy uses exactly χ(G) colours
4. A bad ordering can cause greedy to use far more colours than χ(G)
5. When colouring vertex x of degree d(x), at least one of the first d(x) + 1 colours is available

# Construction / Recognition
## The Greedy Algorithm
1. Fix an ordering x₁, x₂, ..., xₙ of V(G)
2. Set c(x₁) = 1
3. For i = 2, 3, ..., n: set c(xᵢ) = min{j ∈ ℕ : j ≠ c(xₘ) for all neighbours xₘ of xᵢ with m < i}
4. Return the colouring c

# Context & Application
The greedy algorithm is the simplest colouring heuristic. While it does not guarantee optimal colourings, it provides useful upper bounds and is the basis for the proof of several important theorems including Brooks' theorem.

# Examples
**Example** (p. 154, Figure V.1): A bipartite graph (2-colourable) with 8 vertices where the greedy algorithm in the ordering x₁, ..., x₈ uses 4 colours — demonstrating that greedy can be wasteful.

# Relationships
## Builds Upon
- **Vertex colouring** — produces a valid colouring

## Enables
- **Degeneracy bound** (Theorem 1) — χ(G) ≤ max_H δ(H) + 1
- **Brooks' theorem** — proved by careful choice of vertex ordering for greedy

## Related
- Upper bound χ(G) ≤ Δ(G) + 1

# Common Errors
- **Error**: Assuming greedy always gives an optimal colouring
  **Correction**: Greedy is order-dependent and can use Δ(G) + 1 colours on a 2-chromatic graph

# Common Confusions
- **Confusion**: Thinking the greedy algorithm is useless because it's suboptimal
  **Clarification**: With the right vertex ordering, greedy achieves χ(G); it's the foundation of important theoretical results

# Source Reference
Chapter V: Colouring, Section V.1, pages 154–155.

# Verification Notes
- Definition source: Direct from p. 154
- Confidence rationale: Explicitly described algorithm with figure
- Uncertainties: None
- Cross-reference status: Verified
