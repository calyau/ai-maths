---
concept: Colouring Number
slug: colouring-number
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.2 Colouring vertices"
extraction_confidence: high
aliases:
  - "col(G)"
  - "degeneracy plus one"
prerequisites:
  - greedy-colouring
extends:
  - greedy-colouring
related:
  - chromatic-number
  - degeneracy
  - brooks-theorem
contrasts_with: []
answers_questions:
  - "What is the colouring number of a graph?"
  - "How does the colouring number relate to the chromatic number?"
---

# Quick Definition
The colouring number col(G) is the least k such that G has a vertex enumeration where each vertex is preceded by fewer than k of its neighbours. It equals max{delta(H) : H subgraph of G} + 1.

# Core Definition
**Proposition 5.2.2**: "Every graph G satisfies chi(G) <= col(G) = max{delta(H) | H subgraph of G} + 1" (Diestel, p. 115).

# Prerequisites
- **Greedy colouring** -- col(G) is the number of colours the greedy algorithm uses with an optimal ordering

# Key Properties
1. chi(G) <= col(G) <= Delta(G) + 1
2. col(G) = max_H delta(H) + 1, where H ranges over all subgraphs of G
3. Every graph G has a subgraph of minimum degree at least chi(G) - 1 (Corollary 5.2.3)
4. Related to arboricity (Theorem 2.4.4)

# Context & Application
The colouring number captures how well the greedy algorithm performs with an optimal vertex ordering. It provides a tighter upper bound on chi(G) than Delta(G) + 1 for many graphs. The colouring number minus 1 is also called the degeneracy of the graph.

# Relationships
## Builds Upon
- **Greedy colouring** -- Achieved by optimal ordering

## Related
- **Chromatic number** -- chi(G) <= col(G)
- **Degeneracy** -- col(G) - 1 is the degeneracy

# Source Reference
Chapter 5, Section 5.2, Proposition 5.2.2, page 115.

# Verification Notes
- Proposition stated and proved on p. 115
- Confidence: HIGH -- named proposition
