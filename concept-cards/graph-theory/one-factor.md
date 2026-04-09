---
concept: 1-Factor
slug: one-factor
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
  - "perfect matching"
  - "1-factor"
prerequisites:
  - k-factor
  - matching
extends:
  - k-factor
  - matching
related:
  - tuttes-theorem
  - halls-marriage-theorem
  - petersens-theorem-1-factor
contrasts_with: []
answers_questions:
  - "What is a 1-factor?"
  - "What is a perfect matching?"
---

# Quick Definition
A 1-factor of a graph G is a 1-regular spanning subgraph, equivalently a matching that covers every vertex. Also called a perfect matching.

# Core Definition
A subgraph H of G is a **1-factor** of G if and only if E(H) is a matching of V (Diestel, p. 43). Equivalently, a 1-factor is a set of independent edges such that every vertex of G is incident with exactly one edge.

# Prerequisites
- **k-factor** — a 1-factor is the k=1 case
- **Matching** — a 1-factor is a matching covering all vertices

# Key Properties
1. Every vertex is incident with exactly one edge of the 1-factor
2. The graph must have even order (|V| even) to have a 1-factor
3. In bipartite graphs, a 1-factor exists iff |A| = |B| and the marriage condition holds
4. In general graphs, Tutte's theorem characterizes 1-factor existence
5. Every bridgeless cubic graph has a 1-factor (Petersen's theorem, Corollary 2.2.2)

# Construction / Recognition
## To Verify a 1-Factor
1. Check that the edge set is a matching (no two edges share a vertex)
2. Verify every vertex of G is incident with exactly one edge

# Context & Application
The existence of 1-factors is the main theme of Sections 2.1 and 2.2. For bipartite graphs, Hall's theorem gives the criterion. For general graphs, Tutte's theorem provides the necessary and sufficient condition.

# Examples
**Example** (p. 43): In a bipartite graph with |A| = |B|, a matching of A (which exists by Hall's theorem when the marriage condition holds) is a 1-factor.

**Example** (Corollary 2.1.3, p. 48): Every k-regular bipartite graph (k >= 1) has a 1-factor.

# Relationships
## Builds Upon
- **k-factor** (k=1), **matching** covering all vertices

## Enables
- **Tutte's theorem** — characterizes graphs with 1-factors
- **Two-factor** — can sometimes be decomposed into 1-factors

## Related
- **Hall's marriage theorem** — characterizes bipartite 1-factors
- **Petersen's theorem** — bridgeless cubic graphs have 1-factors

# Common Errors
- **Error**: Looking for a 1-factor in a graph of odd order
  **Correction**: A 1-factor pairs all vertices, requiring even order

# Common Confusions
- **Confusion**: Confusing maximum matching with 1-factor
  **Clarification**: A 1-factor matches all vertices; a maximum matching may leave some unmatched

# Source Reference
Chapter 2, Section 2.1, p. 43 (pdf p. 43). Also Sections 2.1-2.2.

# Verification Notes
- Definition from p. 43
- Confidence: HIGH — explicitly defined
