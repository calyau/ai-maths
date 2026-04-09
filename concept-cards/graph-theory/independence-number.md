---
concept: Independence Number
slug: independence-number
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
  - "alpha(G)"
prerequisites:
  - graph
extends: []
related:
  - clique-number
  - chromatic-number
  - perfect-graph
contrasts_with:
  - clique-number
answers_questions:
  - "What is the independence number of a graph?"
---

# Quick Definition
The independence number alpha(G) is the largest integer r such that G contains an independent set of r vertices (an edgeless induced subgraph K^r-bar).

# Core Definition
"The greatest integer r such that K^r-bar is an induced subgraph of G is the independence number alpha(G) of G. Clearly, alpha(G) = omega(complement(G)) and omega(G) = alpha(complement(G))" (Diestel, p. 126).

# Prerequisites
- **Graph**

# Key Properties
1. alpha(G) = omega(complement(G))
2. chi(G) >= |V|/alpha(G)
3. Each colour class has at most alpha(G) vertices
4. For perfect graphs, alpha and omega determine chi completely

# Relationships
## Related
- **Clique number** -- alpha(G) = omega(complement(G))
- **Chromatic number** -- chi(G) >= n/alpha(G)

## Contrasts With
- **Clique number** -- Independence vs clique

# Source Reference
Chapter 5, Section 5.5, page 126.

# Verification Notes
- Definition from p. 126
- Confidence: HIGH
