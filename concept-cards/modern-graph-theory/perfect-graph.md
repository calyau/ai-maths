---
concept: Perfect Graph
slug: perfect-graph
category: perfect-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 175
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "perfect graphs"
prerequisites:
  - chromatic-number
  - clique-number
extends: []
related:
  - perfect-graph-theorem
  - imperfect-graph
  - perfect-graph-conjecture
contrasts_with:
  - imperfect-graph
answers_questions:
  - "What is a perfect graph?"
---

# Quick Definition
A graph G is perfect if χ(H) = ω(H) for every induced subgraph H of G, including G itself. Perfect graphs include bipartite graphs, their complements, comparability graphs, and line graphs of bipartite graphs.

# Core Definition
A graph G is **perfect** if χ(H) = ω(H) for every induced subgraph H of G. The concept was explicitly defined by Berge in 1960, though the first result (complements of bipartite graphs are perfect) was proved by Gallai and König in 1932. The graph must satisfy equality for ALL induced subgraphs, not just for G itself (Bollobás, p. 175).

# Prerequisites
- **Chromatic number** — one side of the defining equality
- **Clique number** — the other side

# Key Properties
1. χ(H) = ω(H) for every induced subgraph H ⊆ G
2. Every induced subgraph of a perfect graph is perfect
3. Bipartite graphs are perfect
4. Complements of bipartite graphs are perfect (Theorem 15)
5. Comparability graphs and their complements are perfect (Theorem 17)
6. Line graphs of bipartite graphs and their complements are perfect (Theorem 16)
7. A graph is perfect iff |H| ≤ ω(H)·ω(H̅) for all induced H (Lovász)

# Construction / Recognition
## Classes of Perfect Graphs
1. Bipartite graphs
2. Complements of bipartite graphs
3. Comparability graphs
4. Line graphs of bipartite graphs
5. Complements of all the above
6. Any graph obtained by vertex substitution from perfect graphs (Theorem 19)

## Recognition
- A graph is perfect iff it contains no odd hole or odd antihole of length ≥ 5 (Strong Perfect Graph Theorem, proved by Chudnovsky et al. 2006, conjectured by Berge 1960)

# Context & Application
Perfect graphs are important not only in graph theory but also in optimization, linear programming, and polyhedral combinatorics. The fractional relaxation of the independence number equals the independence number for perfect graphs.

# Examples
**Example** (p. 175): Bipartite graphs are perfect (χ = 2 = ω for non-trivial cases).

**Example** (p. 175): An odd cycle of length ≥ 5 is NOT perfect: ω = 2 but χ = 3.

**Example** (p. 176): Complements of bipartite graphs are perfect (by König's theorem / Theorem 15).

# Relationships
## Builds Upon
- **Chromatic number** and **clique number** — defining equality

## Enables
- **Perfect graph theorem** — complement of a perfect graph is perfect
- Optimization: χ, ω, α can all be computed in polynomial time for perfect graphs

## Contrasts With
- **Imperfect graph** — χ(G) > ω(G) for some induced subgraph

# Common Errors
- **Error**: Checking only χ(G) = ω(G) and concluding G is perfect
  **Correction**: Must verify χ(H) = ω(H) for ALL induced subgraphs H

# Common Confusions
- **Confusion**: Thinking every graph with χ = ω is perfect
  **Clarification**: Perfection requires the equality for every induced subgraph, not just G itself

# Source Reference
Chapter V: Colouring, Section V.5, pages 175–180.

# Verification Notes
- Definition source: Direct from p. 175
- Confidence rationale: Explicitly defined with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
