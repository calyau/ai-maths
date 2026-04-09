---
concept: "Menger's Theorem"
slug: mengers-theorem
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 72
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases:
  - "Menger 1927"
  - "Menger's min-max theorem"
prerequisites:
  - graph
  - path
  - separator
extends: []
related:
  - konigs-theorem
  - mengers-theorem-edge-version
  - global-mengers-theorem
  - fan-version-mengers-theorem
  - k-connected-characterization
contrasts_with: []
answers_questions:
  - "How does connectivity relate to the existence of disjoint paths (Menger's theorem)?"
  - "What must I know before understanding Menger's theorem?"
---

# Quick Definition
The minimum number of vertices separating two vertex sets A and B in a graph equals the maximum number of disjoint A-B paths.

# Core Definition
**Theorem 3.3.1 (Menger 1927).** Let G = (V, E) be a graph and A, B contained in V. Then the minimum number of vertices separating A from B in G is equal to the maximum number of disjoint A-B paths in G (Diestel, p. 72).

# Prerequisites
- **Graph** — the setting
- **Path** — disjoint A-B paths are counted
- **Separator** — the minimum A-B separator is the dual quantity

# Key Properties
1. Min-max duality: min separator = max disjoint paths
2. k = k(G, A, B) denotes the minimum separator size
3. G cannot contain more than k disjoint A-B paths (trivial direction)
4. The theorem says exactly k such paths exist (deep direction)
5. Three proofs are given: by induction on edges, by induction on path sizes, and by alternating walks
6. Konig's theorem is the bipartite special case
7. One of the cornerstones of graph theory

# Construction / Recognition
## First Proof Strategy (induction on ||G||)
1. If G has no edge, |A intersect B| = k and we have k trivial paths
2. Otherwise, pick edge e = xy and contract it
3. Find separator Y in G/e, then X = (Y \ {v_e}) union {x, y}
4. Find k disjoint A-X paths and k disjoint X-B paths in G-e
5. Combine to get k disjoint A-B paths

## Third Proof Strategy (alternating walks)
1. Find a maximum set P of disjoint A-B paths
2. If an alternating walk reaches B \ V[P], augment (Lemma 3.3.2)
3. If not, construct an A-B separator on P (Lemma 3.3.3)

# Context & Application
Menger's theorem is one of the cornerstones of graph theory (Diestel, p. 72). It establishes that the two definitions of k-connectivity (at least k vertices to disconnect, and k independent paths between any two vertices) are equivalent. The theorem has numerous applications in network theory, combinatorial optimization, and algorithm design. It generalizes Konig's theorem and is generalized by Mader's theorem.

# Examples
**Example** (p. 73, Fig. 3.3.1): Paths and augmentation in the second proof, showing how P is replaced by a set exceeding P.

**Example** (p. 74, Fig. 3.3.2): An alternating walk from A to B in the third proof.

# Relationships
## Builds Upon
- **Graph**, **path**, **separator**

## Enables
- **Global Menger's theorem** — k-connectivity characterized
- **Fan version** — a-B fans
- **k-connected characterization** — k independent paths between any two vertices
- **Mader's theorem** — generalization to H-paths

## Related
- **Konig's theorem** — the bipartite special case
- **Max-flow min-cut theorem** — the network flow generalization

# Common Errors
- **Error**: Confusing vertex-disjoint paths with edge-disjoint paths
  **Correction**: The basic version (Theorem 3.3.1) uses vertex separators and vertex-disjoint paths; the edge version is Corollary 3.3.5(ii)

# Common Confusions
- **Confusion**: Thinking Menger's theorem requires a and b to be single vertices
  **Clarification**: The theorem works for sets A and B, not just individual vertices. Special cases for individual vertices are corollaries (3.3.4 and 3.3.5)

# Source Reference
Chapter 3, Section 3.3, Theorem 3.3.1, pp. 72-76 (pdf pp. 72-76). Three proofs given.

# Verification Notes
- Theorem statement from p. 72
- Three proofs spanning pp. 72-76
- Described as "one of the cornerstones of graph theory"
- Confidence: HIGH — central theorem with three full proofs
