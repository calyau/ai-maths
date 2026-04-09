---
concept: "Petersen's 2-Factor Theorem"
slug: petersens-2-factor-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 49
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "Petersen 1891 (2-factor)"
  - "Corollary 2.1.5"
prerequisites:
  - two-factor
  - regular-graph
  - euler-tour
  - halls-marriage-theorem
extends:
  - halls-marriage-theorem
related:
  - petersens-theorem-1-factor
contrasts_with: []
answers_questions:
  - "Does every regular graph of positive even degree have a 2-factor?"
---

# Quick Definition
Every regular graph of positive even degree has a 2-factor.

# Core Definition
**Corollary 2.1.5 (Petersen 1891).** Every regular graph of positive even degree has a 2-factor (Diestel, p. 49).

# Prerequisites
- **2-factor** — a 2-regular spanning subgraph
- **Regular graph** — all vertices have the same degree
- **Euler tour** — used in the proof
- **Hall's marriage theorem** — Corollary 2.1.3 is applied

# Key Properties
1. Applies to 2k-regular graphs for k >= 1
2. Proof: find an Euler tour, split vertices, get a k-regular bipartite graph, find a 1-factor, collapse back
3. The 1-factor of the bipartite graph becomes a 2-factor of the original graph
4. One of the earliest results in graph theory

# Construction / Recognition
## Proof Strategy
1. G is 2k-regular (k >= 1), WLOG connected
2. Find an Euler tour (Theorem 1.8.1)
3. Replace each vertex v by (v-, v+) using the tour
4. The bipartite graph G' is k-regular
5. By Corollary 2.1.3, G' has a 1-factor
6. Collapse pairs (v-, v+) back to get a 2-factor of G

# Context & Application
This theorem shows how matching theory in bipartite graphs can be applied to solve structural problems in general graphs via the Euler tour decomposition technique.

# Examples
**Example** (p. 49, Fig. 2.1.4): Vertex splitting along an Euler tour transforms a 2k-regular graph into a k-regular bipartite graph.

# Relationships
## Builds Upon
- **Hall's marriage theorem** (via Corollary 2.1.3), **Euler tour**

## Related
- **Petersen's 1-factor theorem** — bridgeless cubic graphs have 1-factors

# Source Reference
Chapter 2, Section 2.1, Corollary 2.1.5, p. 49 (pdf p. 49).

# Verification Notes
- Statement and proof from p. 49
- Confidence: HIGH — explicit corollary with proof
