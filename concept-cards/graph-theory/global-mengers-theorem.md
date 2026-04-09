---
concept: "Global Version of Menger's Theorem"
slug: global-mengers-theorem
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 77
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases:
  - "Whitney's theorem"
  - "k-connected path characterization"
prerequisites:
  - mengers-theorem
  - k-connected-graph
extends:
  - mengers-theorem
related:
  - k-connected-characterization
  - mengers-theorem-edge-version
contrasts_with: []
answers_questions:
  - "How does connectivity relate to the existence of disjoint paths?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
A graph is k-connected if and only if any two vertices are joined by k independent paths. A graph is k-edge-connected if and only if any two vertices are joined by k edge-disjoint paths.

# Core Definition
**Theorem 3.3.6 (Global Version of Menger's Theorem).**
(i) A graph is k-connected if and only if it contains k independent paths between any two vertices.
(ii) A graph is k-edge-connected if and only if it contains k edge-disjoint paths between any two vertices (Diestel, p. 77).

# Prerequisites
- **Menger's theorem** — the local version
- **k-connected graph** — one of the equivalent characterizations

# Key Properties
1. k-connected = k independent paths between every pair of vertices
2. k-edge-connected = k edge-disjoint paths between every pair of vertices
3. Part (i) was first stated by Whitney (1932)
4. Part (i) proof handles adjacent vertices specially: if ab is an edge, then G-ab has only k-2 independent a-b paths, but kappa(G) >= k ensures k paths in G
5. Part (ii) follows directly from Corollary 3.3.5(ii)

# Construction / Recognition
## Proof of Part (i)
1. Forward: if k independent paths between any two vertices, then |G| > k and G is k-connected
2. Backward: assume G is k-connected but some pair a, b lacks k independent paths
3. By Corollary 3.3.5(i), a and b must be adjacent
4. In G- = G-ab, there are at most k-2 independent a-b paths
5. So G- has a separator X of size <= k-2 between a and b
6. Find a vertex v not in X union {a,b}; then X union {b} separates v from a in G
7. This contradicts kappa(G) >= k

# Context & Application
This theorem resolves the tension between the two definitions of k-connectivity: removing k-1 vertices does not disconnect, and there are k independent paths between any two vertices. These are equivalent, making connectivity a robust and natural concept.

# Examples
**Example**: K4 is 3-connected; between any two vertices there are 3 independent paths. For a triangle K3, which is 2-connected, any two vertices are joined by 2 independent paths.

# Relationships
## Builds Upon
- **Menger's theorem**

## Enables
- Understanding of connectivity as both a "resilience" and "richness" property

## Related
- **k-connected characterization** — this theorem provides it

# Common Errors
- **Error**: Forgetting to handle adjacent vertices in the vertex version
  **Correction**: Adjacent vertices require special treatment: they have k-1 independent paths in G-ab, but k in G (including the direct edge)

# Common Confusions
- **Confusion**: Thinking k-connected and k-edge-connected are the same
  **Clarification**: k-connected (vertex) implies k-edge-connected, but not vice versa. The vertex version requires independent paths (sharing no vertices); the edge version requires only edge-disjoint paths.

# Source Reference
Chapter 3, Section 3.3, Theorem 3.3.6, p. 77 (pdf p. 77).

# Verification Notes
- Theorem from p. 77
- First stated by Whitney (1932), noted in the chapter notes
- Confidence: HIGH — major theorem with proof
