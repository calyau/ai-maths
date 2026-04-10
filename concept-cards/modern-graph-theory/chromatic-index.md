---
concept: Chromatic Index
slug: chromatic-index
category: edge-coloring
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 152
section: "V.2 Edge Colouring"
extraction_confidence: high
aliases:
  - "χ'(G)"
  - "edge-chromatic number"
  - "edge chromatic number"
prerequisites:
  - edge-colouring
extends: []
related:
  - chromatic-number
  - vizings-theorem
contrasts_with:
  - chromatic-number
  - list-chromatic-index
answers_questions:
  - "What is the chromatic index of a graph?"
  - "How does the chromatic index relate to maximum degree?"
---

# Quick Definition
The chromatic index χ'(G) is the minimum number of colours needed in a proper edge colouring of G. It always satisfies Δ(G) ≤ χ'(G) ≤ Δ(G) + 1.

# Core Definition
The chromatic index χ'(H), also called the edge-chromatic number, is the minimal number of colours in an edge-colouring of H. It satisfies χ'(H) = χ(L(H)), where L(H) is the line graph (Bollobás, p. 152). The trivial lower bound is χ'(G) ≥ Δ(G), since the edges incident with any vertex must all get distinct colours (p. 158).

# Prerequisites
- **Edge colouring** — χ'(G) minimizes the number of colours used

# Key Properties
1. χ'(G) ≥ Δ(G) (trivial lower bound)
2. χ'(G) ≤ Δ(G) + 1 (Vizing's theorem)
3. χ'(G) = Δ(G) for bipartite graphs (König's theorem)
4. χ'(G) = χ(L(G)) where L(G) is the line graph
5. χ'(Kⁿ) = n − 1 if n is even; χ'(Kⁿ) = n if n ≥ 3 is odd

# Construction / Recognition
## To Determine χ'(G)
1. Compute Δ(G) — this is a lower bound
2. Check if G is bipartite — if so, χ'(G) = Δ(G)
3. Otherwise, determine if G is Class 1 (χ' = Δ) or Class 2 (χ' = Δ + 1)

# Context & Application
The chromatic index is fundamental to scheduling theory. Determining whether χ'(G) = Δ(G) or Δ(G) + 1 is NP-complete in general, making the classification into Class 1 and Class 2 graphs an important open area.

# Examples
**Example** (p. 159): χ'(Kⁿ) = n − 1 for even n; χ'(Kⁿ) = n for odd n ≥ 3.

**Example** (p. 158): For bipartite graphs, χ'(G) = Δ(G) (by Hall's theorem).

# Relationships
## Builds Upon
- **Edge colouring** — χ'(G) is the minimum number of edge colours

## Enables
- Classification into Class 1 and Class 2 graphs

## Related
- **Vizing's theorem** — proves χ'(G) ∈ {Δ, Δ + 1}

## Contrasts With
- **Chromatic number** — vertex vs. edge colouring minimum
- **List-chromatic index** — minimum list size for edge list colouring

# Common Errors
- **Error**: Assuming χ'(G) = Δ(G) for all graphs
  **Correction**: χ'(G) can be Δ + 1 (e.g., odd complete graphs, Petersen graph)

# Common Confusions
- **Confusion**: Confusing χ(G) and χ'(G)
  **Clarification**: χ(G) is for vertex colouring; χ'(G) is for edge colouring. They are related by χ'(G) = χ(L(G))

# Source Reference
Chapter V: Colouring, Sections V.1–V.2, pages 152, 158–160.

# Verification Notes
- Definition source: Direct from pp. 152, 158
- Confidence rationale: Explicit definition with standard notation
- Uncertainties: None
- Cross-reference status: Verified
