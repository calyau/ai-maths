---
concept: List Colouring
slug: list-colouring
category: list-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 168
section: "V.4 List Colouring"
extraction_confidence: high
aliases:
  - "list coloring"
  - "L-colouring"
  - "choosability colouring"
prerequisites:
  - vertex-colouring
  - chromatic-number
extends:
  - vertex-colouring
related:
  - list-chromatic-number
  - list-chromatic-index
contrasts_with:
  - vertex-colouring
answers_questions:
  - "What is list colouring and how does it differ from ordinary colouring?"
---

# Quick Definition
In list colouring, each vertex x has a prescribed list L(x) of available colours. An L-colouring assigns to each vertex a colour from its own list such that adjacent vertices get distinct colours.

# Core Definition
Given a graph G and a map L assigning to each vertex a set L(x) of colours, an **L-colouring** of G is a proper colouring c such that c(x) ∈ L(x) for every x ∈ V(G). List colouring is strictly harder than ordinary colouring: even bipartite graphs (χ = 2) can have arbitrarily large list-chromatic number (Bollobás, pp. 168–169).

# Prerequisites
- **Vertex colouring** — list colouring generalizes ordinary vertex colouring
- **Chromatic number** — list-chromatic number is always ≥ χ(G)

# Key Properties
1. χ_ℓ(G) ≥ χ(G) always (ordinary colouring is list colouring with identical lists)
2. χ_ℓ(G) can be strictly greater than χ(G)
3. K_{3,3} with lists of size 2 has no L-colouring (example on p. 168)
4. For every k ≥ 2, there exists a bipartite graph with χ_ℓ > k
5. χ_ℓ(G) ≤ Δ(G) + 1 by the greedy algorithm

# Context & Application
List colouring models situations where each vertex has a restricted set of available colours (e.g., each speaker is available only on certain days). It leads to surprising results: having different lists can be harder than having the same list.

# Examples
**Example** (p. 168, Figure V.9): K_{3,3} with lists L(xᵢ) = L(yᵢ) = {1,2,3} \ {i} for i = 1,2,3 has no proper L-colouring, even though |L(x)| = 2 = χ(K_{3,3}).

# Relationships
## Builds Upon
- **Vertex colouring** — list colouring with identical lists reduces to ordinary colouring

## Enables
- **List-chromatic number** — minimum list size guaranteeing L-colourability
- Thomassen's theorem (planar graphs have χ_ℓ ≤ 5)

## Contrasts With
- **Vertex colouring** — in ordinary colouring all vertices share the same colour set

# Common Errors
- **Error**: Assuming that if |L(x)| ≥ χ(G) for all x, then an L-colouring exists
  **Correction**: This fails even for bipartite graphs; the K_{3,3} example shows lists of size 2 don't suffice

# Common Confusions
- **Confusion**: Thinking "the worst case is when all lists are identical"
  **Clarification**: This intuition is wrong — different lists can create more conflicts than identical lists

# Source Reference
Chapter V: Colouring, Section V.4, pages 168–169.

# Verification Notes
- Definition source: Direct from p. 168
- Confidence rationale: Explicitly defined with motivating examples
- Uncertainties: None
- Cross-reference status: Verified
