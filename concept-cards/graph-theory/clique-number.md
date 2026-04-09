---
concept: Clique Number
slug: clique-number
category: graph-colouring
subcategory: perfect-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.5 Perfect graphs"
extraction_confidence: high
aliases:
  - "omega(G)"
prerequisites:
  - graph
extends: []
related:
  - chromatic-number
  - independence-number
  - perfect-graph
contrasts_with:
  - independence-number
answers_questions:
  - "What is the clique number of a graph?"
  - "How does the chromatic number relate to the clique number?"
---

# Quick Definition
The clique number omega(G) of a graph G is the largest integer r such that K^r is a subgraph of G. It provides a lower bound on the chromatic number: omega(G) <= chi(G).

# Core Definition
"The greatest integer r such that K^r is a subgraph of G is the clique number omega(G) of G" (Diestel, p. 126).

# Prerequisites
- **Graph** -- Defined for graphs

# Key Properties
1. omega(G) <= chi(G) (a clique needs distinct colours)
2. omega(G) = chi(G) for all induced subgraphs iff G is perfect
3. omega(G) = alpha(complement(G))
4. The gap chi(G) - omega(G) can be arbitrarily large (Erdos's theorem)

# Context & Application
The clique number is the fundamental lower bound for the chromatic number. For perfect graphs, it determines the chromatic number exactly. The relationship between omega and chi is central to the theory of perfect graphs.

# Relationships
## Enables
- **Perfect graph** -- Defined by chi = omega for all induced subgraphs

## Related
- **Chromatic number** -- omega(G) <= chi(G)
- **Independence number** -- alpha(G) = omega(complement(G))

## Contrasts With
- **Independence number** -- Maximum independent set vs maximum clique

# Source Reference
Chapter 5, Section 5.5, page 126.

# Verification Notes
- Definition from p. 126
- Confidence: HIGH -- explicit definition
