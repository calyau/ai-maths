---
concept: Matchable to Components
slug: matchable-to-components
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 51
section: "2.2 Matching in general graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - matching
  - component
extends: []
related:
  - gallai-edmonds-structure
  - tuttes-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for S to be matchable to the components of G-S?"
---

# Quick Definition
A vertex set S is matchable to the components C_{G-S} if the bipartite graph G_S (formed by contracting components and keeping only S-to-component edges) contains a matching of S.

# Core Definition
A vertex set S is **matchable** to C_{G-S} if the bipartite graph G_S, which arises from G by contracting the components C of G-S to single vertices and deleting all edges inside S, contains a matching of S. Formally, G_S has vertex set S union C_{G-S} and edge set {sC : there exists c in C with sc in E} (Diestel, p. 51).

# Prerequisites
- **Matching** — matchable means a matching of S exists in G_S
- **Component** — the components of G-S are contracted

# Key Properties
1. The bipartite graph G_S has S on one side and contracted components on the other
2. S is matchable iff each vertex in S can be "assigned" to a distinct component
3. Part of the Gallai-Edmonds structure (Theorem 2.2.3, property (i))
4. When all components are factor-critical and |S| = |C|, the graph has a 1-factor

# Context & Application
This concept is central to Theorem 2.2.3, which decomposes any graph into a set S matchable to factor-critical components. It provides the structural foundation for understanding maximum matchings.

# Examples
**Example** (p. 50, Fig. 2.2.1): The contracted graph G_S shows S matched to the three odd components.

# Relationships
## Builds Upon
- **Matching**, **component**

## Related
- **Gallai-Edmonds structure** — uses matchability
- **Tutte's theorem** — follows from the structure theorem

# Source Reference
Chapter 2, Section 2.2, p. 51 (pdf p. 51).

# Verification Notes
- Definition from p. 51
- Confidence: HIGH — explicitly defined
