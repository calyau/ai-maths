---
concept: Clique Number
slug: clique-number
category: vertex-coloring
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 152
section: "V.1 Vertex Colouring"
extraction_confidence: high
aliases:
  - "ω(G)"
  - "maximum clique size"
prerequisites: []
extends: []
related:
  - chromatic-number
  - independence-number
  - perfect-graph
contrasts_with:
  - independence-number
answers_questions:
  - "What is the clique number of a graph?"
  - "How does the clique number relate to the chromatic number?"
---

# Quick Definition
The clique number ω(G) of a graph G is the maximum order (number of vertices) of a complete subgraph of G.

# Core Definition
The clique number ω(G) is the maximal order of a complete subgraph of G. It provides a fundamental lower bound on the chromatic number: χ(G) ≥ ω(G), since the vertices of any complete subgraph Kₖ ⊂ G must all receive distinct colours (Bollobás, p. 152).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. ω(G) ≤ χ(G) for every graph G
2. ω(G) = 1 iff G has no edges
3. ω(G) = |G| iff G is a complete graph
4. ω(G̅) = α(G) (clique number of complement equals independence number)
5. The gap between ω(G) and χ(G) can be arbitrarily large

# Construction / Recognition
## To Find ω(G)
1. Search for complete subgraphs of increasing size
2. The largest complete subgraph found gives ω(G)
3. This is NP-hard in general

# Context & Application
The clique number is one of the most basic graph invariants. It serves as a trivial lower bound for chromatic number and defines perfect graphs (where χ = ω for all induced subgraphs).

# Examples
**Example** (p. 152): ω(Kₖ) = k, ω(K̄ₖ) = 1.

**Example** (p. 153): There exist graphs with ω(G) = 2 (triangle-free) yet χ(G) arbitrarily large.

# Relationships
## Enables
- **Perfect graph** — defined by equality χ(H) = ω(H) for all induced subgraphs H
- Lower bounds on chromatic number

## Related
- **Chromatic number** — ω(G) ≤ χ(G) always
- **Independence number** — ω(G̅) = α(G)

## Contrasts With
- **Independence number** — maximum independent set vs. maximum clique

# Common Errors
- **Error**: Assuming ω(G) = χ(G) for all graphs
  **Correction**: This holds only for perfect graphs

# Common Confusions
- **Confusion**: Confusing clique number with clique cover number
  **Clarification**: ω(G) is the size of the largest clique; the clique cover number is the minimum number of cliques covering all vertices

# Source Reference
Chapter V: Colouring, Section V.1, page 152.

# Verification Notes
- Definition source: Direct from p. 152
- Confidence rationale: Explicitly defined with notation ω(G)
- Uncertainties: None
- Cross-reference status: Verified
