---
concept: Tree-Width
slug: tree-width
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 331
section: "12.3 Tree-decompositions"
extraction_confidence: high
aliases:
  - "treewidth"
  - "tw(G)"
prerequisites:
  - tree-decomposition
extends:
  - tree-decomposition
related:
  - bramble
  - grid-theorem
  - graph-minor
  - path-decomposition
contrasts_with: []
answers_questions:
  - "What is tree-width?"
  - "How does tree-width relate to forbidden minors?"
---

# Quick Definition
The width of a tree-decomposition (T, V) is max{|V_t| - 1 : t in T}. The tree-width tw(G) of G is the least width of any tree-decomposition of G. Trees have tree-width 1.

# Core Definition
The *width* of a tree-decomposition (T, V) is the number max{|V_t| - 1 : t in T}, and the *tree-width* tw(G) of G is the least width of any tree-decomposition of G. Trees have tree-width 1 (the "-1" in the definition serves precisely to make this true) (Diestel, p. 331).

# Prerequisites
- **Tree-decomposition** — Tree-width is the minimum width over all tree-decompositions

# Key Properties
1. Trees have tree-width 1
2. tw(H) <= tw(G) whenever H is a minor of G (Proposition 12.3.6)
3. Graphs of tree-width < k are WQO by the minor relation (Theorem 12.3.7)
4. tw(G) = k iff G has a bramble of order k+1 but none of order k+2 (Theorem 12.3.9)
5. tw(G) = min{omega(H) - 1 : G subset H, H chordal} (Corollary 12.3.12)
6. Large tree-width implies large grid minors (Theorem 12.4.4)

# Construction / Recognition
## To Determine Tree-Width
1. Find a tree-decomposition of minimum width
2. Lower bound: find a bramble of order k+1 (proves tw >= k)
3. Upper bound: exhibit a tree-decomposition of width k (proves tw <= k)
4. For the k x k grid: tree-width is exactly k

# Context & Application
Tree-width is arguably the most important parameter in structural graph theory. It measures how "tree-like" a graph is. Graphs of bounded tree-width admit efficient algorithms for many NP-hard problems. The graph minor theorem fundamentally relies on tree-width analysis.

# Examples
**Example 1** (p. 332): The k x k grid has tree-width k (shown using brambles of crosses).

**Example 2** (p. 337): Graphs of tree-width < 2 are forests (H = {K^3}); tree-width < 3 iff no K^4 minor (Proposition 12.4.2).

# Relationships
## Builds Upon
- **Tree-decomposition** — Tree-width is defined via tree-decompositions

## Enables
- **WQO for bounded tree-width** (Theorem 12.3.7)
- **Grid theorem** (Theorem 12.4.4)
- **Excluded minor characterizations** (Section 12.4)

## Related
- **Bramble** — Dual characterization of tree-width
- **Graph minor** — Tree-width is minor-monotone

# Common Errors
- **Error**: Computing tree-width as max|V_t| instead of max|V_t| - 1
  **Correction**: The "-1" is part of the definition, ensuring trees have tree-width 1

# Common Confusions
- **Confusion**: Thinking tree-width 0 means the graph is a tree
  **Clarification**: Tree-width 0 means no edges; tree-width 1 means forest

# Source Reference
Chapter 12, Section 12.3, pages 331-336; Section 12.4, pages 337-351.

# Verification Notes
- Definition from p. 331
- Duality theorem from Theorem 12.3.9
- Confidence: HIGH — central concept with extensive treatment
