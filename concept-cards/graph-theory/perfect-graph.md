---
concept: Perfect Graph
slug: perfect-graph
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
  - "Berge graph"
prerequisites:
  - chromatic-number
  - clique-number
extends: []
related:
  - strong-perfect-graph-theorem
  - perfect-graph-theorem
  - chordal-graph
  - comparability-graph
  - interval-graph
contrasts_with: []
answers_questions:
  - "What is a perfect graph?"
  - "When does chi(G) = omega(G)?"
---

# Quick Definition
A graph G is perfect if every induced subgraph H of G satisfies chi(H) = omega(H). That is, the clique number always determines the chromatic number in perfect graphs.

# Core Definition
"A graph is called perfect if every induced subgraph H of G has chromatic number chi(H) = omega(H), i.e. if the trivial lower bound of omega(H) colours always suffices to colour the vertices of H" (Diestel, p. 126).

# Prerequisites
- **Chromatic number** -- Perfect graphs satisfy chi = omega
- **Clique number** -- omega provides the lower bound

# Key Properties
1. chi(H) = omega(H) for ALL induced subgraphs H, not just G itself
2. Closed under taking induced subgraphs (by definition)
3. NOT closed under general subgraphs, supergraphs, or minors
4. Bipartite graphs are perfect
5. Complements of bipartite graphs are perfect (equivalent to Konig's duality theorem)
6. Chordal graphs are perfect (Proposition 5.5.2)
7. Comparability graphs and interval graphs are perfect
8. G is perfect iff complement(G) is perfect (Lovasz's perfect graph theorem)

# Construction / Recognition
## To Verify Perfection
1. For every induced subgraph H, check chi(H) = omega(H)
2. Equivalently: check that neither G nor complement(G) contains an odd cycle of length >= 5 as an induced subgraph (strong perfect graph theorem)

# Context & Application
Perfect graphs form a large and important class where colouring is well-behaved: high chromatic number always has a local explanation (a large clique). Many fundamental classes (bipartite, chordal, comparability, interval) are perfect. The strong perfect graph theorem (2002) gives a complete forbidden-subgraph characterization.

# Examples
**Example** (p. 126-127): Bipartite graphs are perfect (chi = omega for all induced subgraphs).

**Example** (p. 127): C_5 (5-cycle) is NOT perfect: chi(C_5) = 3 but omega(C_5) = 2.

**Example** (p. 127): Chordal graphs are perfect (Proposition 5.5.2).

# Relationships
## Builds Upon
- **Chromatic number**, **Clique number**

## Enables
- **Strong perfect graph theorem** -- Characterizes perfect graphs
- **Perfect graph theorem** -- G perfect iff complement(G) perfect

## Related
- **Chordal graph** -- Important subclass of perfect graphs
- **Comparability graph** -- Another perfect class
- **Interval graph** -- Another perfect class

# Common Errors
- **Error**: Checking chi = omega only for G itself
  **Correction**: Must hold for ALL induced subgraphs

# Common Confusions
- **Confusion**: Thinking perfection is hereditary under all subgraphs
  **Clarification**: Perfection is closed under induced subgraphs, but NOT under general subgraphs or supergraphs

# Source Reference
Chapter 5, Section 5.5, pages 126-133.

# Verification Notes
- Definition from p. 126
- Confidence: HIGH -- explicit definition, central to Section 5.5
