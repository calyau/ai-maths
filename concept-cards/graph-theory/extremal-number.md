---
concept: Extremal Number
slug: extremal-number
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 175
section: "7.1 Subgraphs"
extraction_confidence: high
aliases:
  - "ex(n, H)"
  - "extremal function"
prerequisites:
  - graph
  - edge
related:
  - turan-theorem
  - turan-graph
  - erdos-stone-theorem
  - edge-density
answers_questions:
  - "How many edges can a graph have without containing a given subgraph?"
  - "What is the extremal number ex(n, H)?"
---

# Quick Definition
The extremal number ex(n, H) is the maximum number of edges that a graph on n vertices can have without containing H as a subgraph.

# Core Definition
A graph G not containing H (G not superset H) on n vertices with the largest possible number of edges is called **extremal** for n and H; its number of edges is denoted by **ex(n, H)**. An extremal graph is edge-maximal with H not subset G, but edge-maximality does not imply extremality: a graph may be edge-maximal without H while having fewer than ex(n, H) edges. (Diestel, p. 164-165)

# Prerequisites
- **Graph** — ex(n, H) counts edges in graphs
- **Edge** — The quantity being maximized

# Key Properties
1. ex(n, H) is well-defined for all graphs H and integers n >= |H|
2. Extremal graphs are edge-maximal, but not conversely
3. For H = K^r: ex(n, K^r) = t_{r-1}(n), the number of edges in the Turan graph (Theorem 7.1.1)
4. For bipartite H: ex(n, H) grows subquadratically
5. For forests H: ex(n, H) is at most linear in n
6. lim ex(n,H)/C(n,2) = (chi(H)-2)/(chi(H)-1) as n -> infinity (Corollary 7.1.3)

# Context & Application
The extremal number is the central quantity in extremal graph theory. Determining ex(n, H) for various H is the archetypal extremal graph problem. The Erdos-Stone theorem provides asymptotic information for all H simultaneously.

# Examples
**Example** (p. 165, Fig. 7.1.1): Two graphs edge-maximal without a P^3 subgraph; only one is extremal.

# Relationships
## Enables
- **Turan's theorem** — Determines ex(n, K^r) exactly
- **Erdos-Stone theorem** — Gives asymptotic ex(n, H) for all H

## Related
- **Edge density** — ex(n, H)/C(n,2) is the critical edge density for forcing H

# Source Reference
Chapter 7: Extremal Graph Theory, Section 7.1, pages 164-165 (pdf page 175).

# Verification Notes
- Confidence: HIGH — explicitly defined with notation
