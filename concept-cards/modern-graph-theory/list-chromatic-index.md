---
concept: List-Chromatic Index
slug: list-chromatic-index
category: list-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 171
section: "V.4 List Colouring"
extraction_confidence: high
aliases:
  - "χ'_ℓ(G)"
  - "list edge-chromatic number"
  - "edge choosability number"
  - "ch'(G)"
prerequisites:
  - list-colouring
  - chromatic-index
extends:
  - chromatic-index
related:
  - galvins-theorem
  - list-chromatic-number
contrasts_with:
  - chromatic-index
answers_questions:
  - "What is the list-chromatic index?"
---

# Quick Definition
The list-chromatic index χ'_ℓ(G) is the minimum k such that G has an L-edge-colouring whenever |L(e)| ≥ k for every edge e. For bipartite graphs, χ'_ℓ(G) = χ'(G) = Δ(G).

# Core Definition
For a graph G, the **list-chromatic index** (or list edge-chromatic number) χ'_ℓ(G) is the minimal k such that G is k-edge-choosable: G has an L-edge-colouring whenever |L(e)| ≥ k for every e ∈ E(G). An L-edge-colouring is a proper edge colouring λ with λ(e) ∈ L(e) for every edge (Bollobás, p. 171).

# Prerequisites
- **List colouring** — the concept applied to edges
- **Chromatic index** — χ'_ℓ ≥ χ' always

# Key Properties
1. χ'_ℓ(G) ≥ χ'(G) for every graph G
2. χ'_ℓ(G) = Δ(G) for bipartite graphs (Galvin's theorem)
3. χ'_ℓ(G) ≤ 2Δ(G) − 1 trivially
4. Kahn (1996): χ'_ℓ(G) ≤ (1+ε)Δ(G) for large Δ
5. Conjecture: χ'_ℓ(G) = χ'(G) for all graphs

# Context & Application
The list-edge-chromatic number and the conjecture χ'_ℓ = χ' is one of the major open problems in graph colouring. Galvin's theorem for bipartite graphs was a breakthrough.

# Relationships
## Builds Upon
- **Chromatic index** — χ'_ℓ ≥ χ' always

## Related
- **Galvin's theorem** — proves equality for bipartite graphs
- **List-chromatic number** — the vertex version

## Contrasts With
- **Chromatic index** — conjectured equal for all graphs, proved only for bipartite

# Source Reference
Chapter V: Colouring, Section V.4, pages 171–175.

# Verification Notes
- Definition source: Direct from p. 171
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
