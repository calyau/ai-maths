---
concept: Galvin's Theorem
slug: galvins-theorem
category: list-coloring
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 174
section: "V.4 List Colouring"
extraction_confidence: high
aliases:
  - "Theorem V.14"
prerequisites:
  - list-chromatic-index
  - edge-colouring-bipartite-graphs
  - stable-matching
extends:
  - edge-colouring-bipartite-graphs
related:
  - list-chromatic-number
contrasts_with: []
answers_questions:
  - "What is the list-chromatic index of a bipartite graph?"
---

# Quick Definition
The list-chromatic index of every bipartite graph equals its chromatic index: χ'_ℓ(G) = χ'(G) = Δ(G).

# Core Definition
**Theorem 14** (Bollobás, p. 174): The list-chromatic index of a bipartite graph equals its chromatic index. Since χ'(G) = Δ(G) for bipartite G, this means χ'_ℓ(G) = Δ(G).

The proof uses stable matchings from Section III.5 and Theorem 13 about choosability with respect to total functions. It proceeds by induction on the size of G, using a stable matching to remove edges of one colour.

# Prerequisites
- **List-chromatic index** — the quantity being determined
- **Edge colouring of bipartite graphs** — χ'(G) = Δ(G)
- **Stable matching** — key tool in the proof

# Key Properties
1. χ'_ℓ(G) = χ'(G) = Δ(G) for bipartite G
2. The result extends to bipartite multigraphs
3. The proof uses a preference assignment and stable matchings
4. Supports the conjecture that χ'_ℓ = χ' for all graphs

# Context & Application
Galvin's theorem was a breakthrough in list colouring theory. The proof is short and elegant, though much effort had been expended before Galvin found his ingenious approach using stable matchings.

# Examples
**Example**: For K_{n,n}, the list-chromatic index equals n = Δ.

# Relationships
## Builds Upon
- **Edge colouring of bipartite graphs** — extends from ordinary to list colouring

## Related
- Evidence for the conjecture χ'_ℓ(G) = χ'(G) for all G

# Source Reference
Chapter V: Colouring, Section V.4, Theorems 13–14, pages 173–175.

# Verification Notes
- Definition source: Direct theorem statement from p. 174
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
