---
concept: Marriage Condition
slug: marriage-condition
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 46
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "Hall's condition"
  - "neighbourhood condition"
prerequisites:
  - bipartite-graph
  - neighbourhood
extends: []
related:
  - halls-marriage-theorem
  - matching
contrasts_with:
  - tuttes-condition
answers_questions:
  - "What is the marriage condition?"
---

# Quick Definition
The marriage condition for a bipartite graph G = (A, B; E) states that |N(S)| >= |S| for every subset S of A; equivalently, every set of vertices in A has enough neighbours in B.

# Core Definition
A condition clearly necessary for the existence of a matching of A is that every subset of A has enough neighbours in B, i.e., that |N(S)| >= |S| for all S contained in A. This is called the **marriage condition** (Diestel, p. 46).

# Prerequisites
- **Bipartite graph** — the condition is stated for bipartite graphs with bipartition {A, B}
- **Neighbourhood** — N(S) denotes the set of neighbours of S

# Key Properties
1. Necessary condition for a matching of A (obvious: each vertex in S must be matched to a distinct neighbour)
2. Also sufficient for a matching of A (Hall's theorem)
3. Involves checking an exponential number of subsets in general
4. For k-regular bipartite graphs, the marriage condition is automatically satisfied
5. When |A| = |B|, the marriage condition ensures a 1-factor exists

# Construction / Recognition
## To Verify the Marriage Condition
1. For every subset S of A (there are 2^|A| subsets)
2. Compute N(S) = union of neighbourhoods of vertices in S within B
3. Check |N(S)| >= |S|
4. If any subset fails, the marriage condition does not hold

# Context & Application
The marriage condition captures the intuitive requirement that no set of vertices in A is "over-demanding" relative to the available partners in B. If some subset S of A has fewer than |S| neighbours in B, it is clearly impossible to match all of S. Hall's theorem says this is the only obstruction.

# Examples
**Example**: In a k-regular bipartite graph with k >= 1, any set S in A sends exactly k|S| edges to B, all incident with N(S). Since N(S) has at most k|N(S)| edges from S, we get k|S| <= k|N(S)|, so |N(S)| >= |S|.

# Relationships
## Builds Upon
- **Bipartite graph**, **neighbourhood**

## Enables
- **Hall's marriage theorem** — the marriage condition is both necessary and sufficient

## Contrasts With
- **Tutte's condition** — the analogous condition for 1-factors in general graphs: q(G-S) <= |S|

# Common Errors
- **Error**: Checking only single vertices (|N({a})| >= 1) and concluding the marriage condition holds
  **Correction**: All subsets must be checked, not just singletons

# Common Confusions
- **Confusion**: Thinking the marriage condition is only necessary
  **Clarification**: Hall's theorem proves it is both necessary and sufficient for a matching of A

# Source Reference
Chapter 2, Section 2.1, p. 46 (pdf p. 46).

# Verification Notes
- Definition from p. 46
- Confidence: HIGH — explicitly named and defined
