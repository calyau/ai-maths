---
concept: Gallai-Edmonds Structure Theorem
slug: gallai-edmonds-structure
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 51
section: "2.2 Matching in general graphs"
extraction_confidence: medium
aliases:
  - "Gallai-Edmonds matching theorem"
  - "matching structure theorem"
prerequisites:
  - tuttes-theorem
  - factor-critical-graph
  - halls-marriage-theorem
extends:
  - tuttes-theorem
related:
  - tutte-berge-formula
  - maximum-matching
contrasts_with: []
answers_questions:
  - "What is the structure of maximum matchings in a graph?"
---

# Quick Definition
Every graph G has a vertex set S such that (i) S is matchable to the components of G-S, and (ii) every component of G-S is factor-critical. This determines the structure of all maximum matchings.

# Core Definition
**Theorem 2.2.3.** Every graph G = (V, E) contains a vertex set S with the following two properties: (i) S is matchable to the set of components of G-S; (ii) Every component of G-S is factor-critical. Given any such set S, the graph G contains a 1-factor if and only if |S| = |components of G-S| (Diestel, p. 51).

# Prerequisites
- **Tutte's theorem** — the structure theorem implies Tutte's theorem
- **Factor-critical graph** — components of G-S are factor-critical
- **Hall's marriage theorem** — used in the proof (matching S to components)

# Key Properties
1. S is matchable to the components: the bipartite graph G_S (contracting components) has a matching of S
2. Every component of G-S is factor-critical (odd order, removing any vertex gives a 1-factor)
3. The theorem determines the maximum matching size: |M| = |S| + (|V| - |S| - |C|)/2
4. All maximum matchings have the same structure: |S| edges to components, (|C|-1)/2 edges in each component C
5. This is a lean version of the full Gallai-Edmonds matching theorem

# Construction / Recognition
## Finding S (from the proof)
1. Consider sets T maximizing d(T) = q(G-T) - |T|
2. Let S be a largest such T
3. Show all components of G-S are odd and factor-critical
4. Show S is matchable to the components

# Context & Application
Theorem 2.2.3 reveals the deep structure underlying matchings in arbitrary graphs. It places a canonical decomposition on any graph that simultaneously determines the maximum matching size and describes the structure of all maximum matchings. The full version is the Gallai-Edmonds matching theorem (Gallai 1964, Edmonds 1965).

# Examples
**Example** (p. 50, Fig. 2.2.1): The contracted graph G_S shows the bipartite structure between S and the components of G-S.

# Relationships
## Builds Upon
- **Tutte's theorem**, **factor-critical graph**, **Hall's marriage theorem**

## Enables
- **Tutte-Berge formula** — the maximum matching size
- Structural description of all maximum matchings

## Related
- **Maximum matching** — size and structure determined by this theorem

# Common Errors
- **Error**: Assuming S is unique
  **Correction**: The theorem guarantees existence of such an S; uniqueness is not claimed (though the deficiency d(S) is maximized)

# Common Confusions
- **Confusion**: Thinking this only applies to graphs without 1-factors
  **Clarification**: It applies to all graphs; when |S| = |C|, the graph has a 1-factor

# Source Reference
Chapter 2, Section 2.2, Theorem 2.2.3, pp. 51-53 (pdf pp. 51-53).

# Verification Notes
- Theorem statement from p. 51
- Proof from pp. 51-53
- Reference to full Gallai-Edmonds theorem in notes, p. 53
- Confidence: MEDIUM — the theorem is explicitly stated, but it is described as a lean version of the full result
