---
concept: k-Factor
slug: k-factor
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 43
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "regular factor"
  - "k-regular spanning subgraph"
prerequisites:
  - graph
  - spanning-subgraph
extends:
  - spanning-subgraph
related:
  - one-factor
  - two-factor
contrasts_with: []
answers_questions:
  - "What is a k-factor?"
---

# Quick Definition
A k-factor of a graph G is a k-regular spanning subgraph of G.

# Core Definition
A k-regular spanning subgraph is called a **k-factor** (Diestel, p. 43). A subgraph H of G is a k-factor if H spans G (contains all vertices) and every vertex of H has degree exactly k.

# Prerequisites
- **Graph** — k-factors are subgraphs of a graph
- **Spanning subgraph** — a k-factor must contain all vertices

# Key Properties
1. A k-factor contains all vertices of G
2. Every vertex has degree exactly k in the factor
3. A 1-factor is a perfect matching
4. A 2-factor is a union of vertex-disjoint cycles covering all vertices
5. A k-factor exists only if k|V| is even (since the sum of degrees must be even)

# Construction / Recognition
## To Verify a k-Factor
1. Check that H contains all vertices of G
2. Verify every vertex of H has degree exactly k
3. Confirm all edges of H are edges of G

# Context & Application
The concept of k-factor unifies several graph decomposition problems. The 1-factor problem (perfect matching) is the main theme of Sections 2.1-2.2. The 2-factor problem connects to Euler tours (Corollary 2.1.5).

# Examples
**Example** (p. 43): A 1-factor of G corresponds to a matching of V. A subgraph H is a 1-factor of G if and only if E(H) is a matching of V.

**Example** (Corollary 2.1.5, p. 49): Every regular graph of positive even degree has a 2-factor (Petersen 1891).

# Relationships
## Builds Upon
- **Spanning subgraph** — a k-factor is a regular spanning subgraph

## Enables
- **One-factor** — the k=1 case, equivalent to perfect matching
- **Two-factor** — the k=2 case, a union of vertex-disjoint cycles

# Common Errors
- **Error**: Forgetting that a k-factor must span the entire graph
  **Correction**: A k-factor must contain every vertex of G, not just a subset

# Common Confusions
- **Confusion**: Confusing k-factor with k-edge-coloring
  **Clarification**: A k-factor is a k-regular spanning subgraph; a k-edge-coloring partitions edges into matchings

# Source Reference
Chapter 2, p. 43 (pdf p. 43).

# Verification Notes
- Definition from p. 43
- Confidence: HIGH — explicitly defined
