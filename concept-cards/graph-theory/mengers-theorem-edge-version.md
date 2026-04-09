---
concept: "Menger's Theorem (Edge Version)"
slug: mengers-theorem-edge-version
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 76
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases:
  - "edge version of Menger's theorem"
prerequisites:
  - mengers-theorem
  - edge-connectivity
extends:
  - mengers-theorem
related:
  - global-mengers-theorem
contrasts_with:
  - mengers-theorem
answers_questions:
  - "What is the edge version of Menger's theorem?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
The minimum number of edges separating two vertices a and b in G equals the maximum number of edge-disjoint a-b paths.

# Core Definition
**Corollary 3.3.5(ii).** The minimum number of edges separating a from b in G is equal to the maximum number of edge-disjoint a-b paths in G (Diestel, p. 76).

# Prerequisites
- **Menger's theorem** — the vertex version from which this is derived
- **Edge-connectivity** — the minimum edge cut

# Key Properties
1. Dual to the vertex version: edges play the role of separators
2. Derived by applying the vertex version to the line graph of G
3. No restriction on whether a and b are adjacent
4. lambda(G) = min edge-connectivity = max edge-disjoint paths between worst-case pair

# Construction / Recognition
## Derivation from Vertex Version
1. Take the line graph L(G) of G
2. Set A := E(a) (edges at a) and B := E(b) (edges at b)
3. A vertex separator in L(G) corresponds to an edge set separating a from b in G
4. Disjoint A-B paths in L(G) correspond to edge-disjoint a-b paths in G
5. Apply Theorem 3.3.1

# Context & Application
The edge version of Menger's theorem provides the min-max duality for edge-connectivity. Together with the vertex version, it establishes that connectivity (both vertex and edge) is dual to the existence of disjoint paths.

# Examples
**Example**: In a graph with lambda_G(a,b) = 3, there exist exactly 3 edge-disjoint paths from a to b, and any edge cut separating a from b has at least 3 edges.

# Relationships
## Builds Upon
- **Menger's theorem** (vertex version)

## Related
- **Global Menger's theorem** — edge version: k-edge-connected iff k edge-disjoint paths between any two vertices

## Contrasts With
- **Menger's theorem** (vertex version) — uses vertex separators and vertex-disjoint paths

# Common Errors
- **Error**: Confusing edge-disjoint with vertex-disjoint paths
  **Correction**: Edge-disjoint paths may share vertices; vertex-disjoint paths share nothing

# Source Reference
Chapter 3, Section 3.3, Corollary 3.3.5(ii), p. 76 (pdf p. 76).

# Verification Notes
- Statement from p. 76
- Confidence: HIGH — explicit corollary
