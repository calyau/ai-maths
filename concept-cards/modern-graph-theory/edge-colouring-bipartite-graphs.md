---
concept: Edge Colouring of Bipartite Graphs
slug: edge-colouring-bipartite-graphs
category: edge-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 158
section: "V.2 Edge Colouring"
extraction_confidence: high
aliases:
  - "König's edge colouring theorem"
prerequisites:
  - chromatic-index
  - edge-colouring
extends: []
related:
  - vizings-theorem
  - galvins-theorem
contrasts_with: []
answers_questions:
  - "What is the chromatic index of a bipartite graph?"
---

# Quick Definition
The chromatic index of every bipartite graph equals its maximum degree: χ'(G) = Δ(G). This means every bipartite graph is Class 1.

# Core Definition
For a bipartite graph G, the edge set E(G) can be partitioned into Δ(G) classes of independent edges (perfect or near-perfect matchings), giving χ'(G) = Δ(G). This follows from Hall's theorem on matching in bipartite graphs (Bollobás, p. 158, citing Exercise III.22).

# Prerequisites
- **Chromatic index** — the quantity being determined
- **Edge colouring** — context

# Key Properties
1. χ'(G) = Δ(G) for every bipartite graph G
2. The proof uses Hall's marriage theorem
3. Every bipartite graph is Class 1
4. This result extends to bipartite multigraphs

# Context & Application
This result is one of the cleanest applications of Hall's theorem. It shows that bipartite graphs have optimal edge colourings, in contrast to general graphs where χ' may exceed Δ.

# Examples
**Example**: The complete bipartite graph K_{n,n} has Δ = n and χ' = n.

# Relationships
## Enables
- **Galvin's theorem** — extends this to list edge colouring: χ'_ℓ(G) = χ'(G) = Δ(G) for bipartite G
- **Perfect graph** results for line graphs of bipartite graphs

## Related
- **Vizing's theorem** — general bound χ' ∈ {Δ, Δ + 1}

# Common Errors
- **Error**: Trying to prove this by greedy algorithm alone
  **Correction**: The proof requires Hall's theorem / matching decomposition, not just greedy

# Source Reference
Chapter V: Colouring, Section V.2, page 158.

# Verification Notes
- Definition source: Direct statement from p. 158
- Confidence rationale: Explicit statement with reference to Hall's theorem proof
- Uncertainties: None
- Cross-reference status: Verified
