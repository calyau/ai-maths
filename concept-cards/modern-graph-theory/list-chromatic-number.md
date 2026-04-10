---
concept: List-Chromatic Number
slug: list-chromatic-number
category: list-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 169
section: "V.4 List Colouring"
extraction_confidence: high
aliases:
  - "χ_ℓ(G)"
  - "choosability"
  - "choice number"
prerequisites:
  - list-colouring
  - chromatic-number
extends:
  - chromatic-number
related:
  - list-chromatic-index
contrasts_with:
  - chromatic-number
answers_questions:
  - "What is the list-chromatic number of a graph?"
---

# Quick Definition
The list-chromatic number χ_ℓ(G) is the minimum integer k such that G has an L-colouring whenever |L(x)| ≥ k for every vertex x.

# Core Definition
The list-chromatic number χ_ℓ(G) is the minimal integer k such that G has an L-colouring whenever |L(x)| ≥ k for every x ∈ V(G). It satisfies χ_ℓ(G) ≥ χ(G) always, but the gap can be arbitrarily large even for bipartite graphs (Bollobás, p. 169).

# Prerequisites
- **List colouring** — χ_ℓ(G) measures the minimum list size
- **Chromatic number** — χ_ℓ(G) ≥ χ(G) always

# Key Properties
1. χ_ℓ(G) ≥ χ(G) for every graph G
2. χ_ℓ(G) ≤ Δ(G) + 1 (greedy algorithm)
3. For bipartite graphs: χ_ℓ can be arbitrarily large (while χ = 2)
4. For planar graphs: χ_ℓ ≤ 5 (Thomassen's theorem)
5. For line graphs of bipartite graphs: χ_ℓ = χ (Galvin's theorem)

# Context & Application
The list-chromatic number captures the difficulty of colouring with prescribed lists. It is generally harder to compute than χ(G) and reveals that the colouring problem depends on the lists in subtle ways.

# Examples
**Example** (p. 169): For every k ≥ 2, there is a bipartite graph G with χ_ℓ(G) > k (constructed using complete bipartite graphs with carefully chosen lists from k-subsets of [2k−1]).

# Relationships
## Builds Upon
- **Chromatic number** — always a lower bound

## Related
- **List-chromatic index** — the edge version
- Thomassen's theorem — χ_ℓ ≤ 5 for planar graphs

## Contrasts With
- **Chromatic number** — can differ arbitrarily; χ_ℓ is at least χ

# Common Errors
- **Error**: Assuming χ_ℓ(G) = χ(G) for bipartite graphs
  **Correction**: Even K_{3,3} has χ_ℓ ≥ 3 while χ = 2

# Source Reference
Chapter V: Colouring, Section V.4, page 169.

# Verification Notes
- Definition source: Direct from p. 169
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
