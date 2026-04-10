---
concept: "Menger's Theorem"
slug: mengers-theorem
category: connectivity
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "Theorem 5"
  - "Menger 1927"
prerequisites:
  - graph-connectivity
  - independent-paths
  - max-flow-min-cut-theorem
extends: []
related:
  - vertex-connectivity
  - edge-connectivity
  - halls-theorem
contrasts_with: []
answers_questions:
  - "What must I know before understanding Menger's theorem?"
  - "What is graph connectivity?"
---

# Quick Definition
Menger's theorem (1927) states that the minimum number of vertices (or edges) separating two vertices equals the maximum number of independent (or edge-disjoint) paths between them.

# Core Definition
**Theorem 5** (Menger, 1927):
(i) *Vertex form*: Let $s$ and $t$ be distinct nonadjacent vertices of a graph $G$. Then the minimal number of vertices separating $s$ from $t$ is equal to the maximal number of independent $s$-$t$ paths.
(ii) *Edge form*: Let $s$ and $t$ be distinct vertices of $G$. Then the minimal number of edges separating $s$ from $t$ is equal to the maximal number of edge-disjoint $s$-$t$ paths (Bollobás, pp. 82-83).

# Prerequisites
- **Graph connectivity** — Menger's theorem characterizes connectivity
- **Independent paths** — The objects being counted in the vertex form
- **Max-flow min-cut theorem** — One proof derives Menger from max-flow min-cut

# Key Properties
1. Two forms: vertex and edge
2. The vertex form requires $s$ and $t$ to be nonadjacent
3. The edge form has no adjacency requirement
4. Can be deduced from max-flow min-cut (first proof) or proved independently (second proof)
5. Implies: a graph is $k$-connected iff any two vertices can be joined by $k$ independent paths (Corollary 6)
6. Has a set-to-set generalization

# Construction / Recognition
## First Proof (via Max-Flow Min-Cut)
1. Replace each edge $xy$ by directed edges $\vec{xy}$ and $\vec{yx}$
2. For vertex form: give each vertex (except $s,t$) capacity 1
3. Apply Theorem 4 and the integrality theorem
4. Maximal flow decomposes into independent paths

## Second Proof (from first principles)
1. Induction on the minimal separator size $k$
2. Uses a minimum counterexample argument
3. Relies on contracting components and analyzing separating sets

# Context & Application
Menger's theorem is "the basic result in the theory of connectivity" (p. 82). It is the graph-theoretic analogue of the max-flow min-cut theorem and connects the local notion of separation to the global notion of path existence.

# Examples
**Example** (p. 82): In the proof via max-flow min-cut, edges are given capacity 1, and the integrality theorem ensures the maximal flow (with value 0 or 1 on each edge) decomposes into independent paths.

# Relationships
## Builds Upon
- **max-flow-min-cut-theorem** — One proof uses this
- **independent-paths** — The objects being counted

## Enables
- **halls-theorem** — Can be derived from Menger's theorem
- **k-connectivity-characterization** — Corollary 6

## Related
- **vertex-connectivity** — Minimum separator = $\kappa$-related value
- **edge-connectivity** — Edge form of Menger

# Common Errors
- **Error**: Applying the vertex form when $s$ and $t$ are adjacent
  **Correction**: The vertex form requires $s$ and $t$ to be nonadjacent; the edge form has no such restriction

# Common Confusions
- **Confusion**: Thinking Menger's theorem gives an algorithm for finding the paths
  **Clarification**: The theorem is existential; finding the paths constructively uses the max-flow algorithm

# Source Reference
Chapter III, Section III.2, pages 82-84. Theorem 5 with two proofs.

# Verification Notes
- Definition source: Direct theorem statement from pp. 82-83
- Confidence rationale: Major theorem with two complete proofs
- Uncertainties: None
- Cross-reference status: Verified
