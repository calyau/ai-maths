---
concept: Edge Colouring
slug: edge-colouring
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
  - "edge coloring"
  - "proper edge colouring"
prerequisites: []
extends: []
related:
  - chromatic-index
  - vertex-colouring
contrasts_with:
  - vertex-colouring
answers_questions:
  - "What distinguishes vertex coloring from edge coloring?"
---

# Quick Definition
An edge colouring of a graph G is an assignment of colours to the edges such that no two adjacent edges (sharing an endpoint) receive the same colour.

# Core Definition
A colouring of the edges of H is an assignment of colours to the edges such that no two adjacent edges have the same colour. The minimum number of colours needed is the edge-chromatic number or chromatic index χ'(H). Note that χ'(H) = χ(L(H)), where L(H) is the line graph of H (Bollobás, p. 152).

The motivating problem: each of n businessmen wishes to hold confidential pairwise meetings lasting a day each. The minimum number of days is χ'(H) where H is the graph of desired meetings.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. χ'(G) = χ(L(G)) where L(G) is the line graph
2. χ'(G) ≥ Δ(G) always (trivial lower bound)
3. χ'(G) = Δ(G) for bipartite graphs
4. χ'(G) ∈ {Δ(G), Δ(G) + 1} for all graphs (Vizing's theorem)

# Construction / Recognition
## To Edge-Colour a Graph
1. Compute Δ(G), the maximum degree
2. Try to find a Δ(G)-edge-colouring
3. If that fails, find a (Δ(G) + 1)-edge-colouring (always possible by Vizing's theorem)

# Context & Application
Edge colouring has applications in scheduling (scheduling meetings, assigning communication channels) and is closely related to matchings in bipartite graphs.

# Examples
**Example** (p. 152): The businessman scheduling problem — vertices are businessmen, edges are desired meetings. χ'(H) gives the minimum number of days.

**Example** (p. 159): χ'(Kⁿ) = n − 1 if n is even, and χ'(Kⁿ) = n if n ≥ 3 is odd.

# Relationships
## Enables
- **Chromatic index** — the minimum edge-colouring number
- **Vizing's theorem** — χ'(G) ∈ {Δ, Δ + 1}

## Related
- **Vertex colouring** — edge colouring of G equals vertex colouring of L(G)

## Contrasts With
- **Vertex colouring** — colours vertices (adjacent differ) vs. edges (incident differ)

# Common Errors
- **Error**: Confusing "adjacent edges" with "adjacent vertices"
  **Correction**: Two edges are adjacent if they share an endpoint; an edge colouring requires adjacent edges to have distinct colours

# Common Confusions
- **Confusion**: Thinking edge colouring and vertex colouring are unrelated
  **Clarification**: χ'(G) = χ(L(G)), so edge colouring is a special case of vertex colouring on the line graph

# Source Reference
Chapter V: Colouring, introduction and Section V.2, pages 152, 158–160.

# Verification Notes
- Definition source: Direct from p. 152
- Confidence rationale: Explicit definition with notation
- Uncertainties: None
- Cross-reference status: Verified
