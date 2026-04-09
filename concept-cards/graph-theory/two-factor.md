---
concept: 2-Factor
slug: two-factor
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
  - "2-regular factor"
prerequisites:
  - k-factor
extends:
  - k-factor
related:
  - one-factor
  - euler-tour
contrasts_with: []
answers_questions:
  - "What is a 2-factor?"
---

# Quick Definition
A 2-factor of a graph G is a 2-regular spanning subgraph, i.e., a union of vertex-disjoint cycles that together cover all vertices of G.

# Core Definition
A 2-factor is a 2-regular spanning subgraph of G. Since every connected 2-regular graph is a cycle, a 2-factor is a collection of vertex-disjoint cycles covering all vertices.

# Prerequisites
- **k-factor** — a 2-factor is the k=2 case

# Key Properties
1. Every vertex has degree exactly 2 in the 2-factor
2. The 2-factor is a disjoint union of cycles covering V
3. Every regular graph of positive even degree has a 2-factor (Corollary 2.1.5, Petersen 1891)
4. A Hamilton cycle is a 2-factor consisting of a single cycle

# Construction / Recognition
## Construction via Euler Tour (Corollary 2.1.5)
1. Given a 2k-regular graph G (k >= 1), find an Euler tour (exists by Theorem 1.8.1)
2. Replace each vertex v by a pair (v-, v+) using the Euler tour
3. The resulting bipartite graph is k-regular
4. Find a 1-factor (by Corollary 2.1.3)
5. Collapse vertex pairs back to obtain a 2-factor of G

# Context & Application
The existence of 2-factors in regular graphs of even degree is one of the earliest results in graph theory (Petersen 1891). It connects Euler tour theory with matching theory.

# Examples
**Example** (p. 49, Corollary 2.1.5): Every 2k-regular graph has a 2-factor. The proof uses vertex-splitting along an Euler tour and the 1-factor existence for regular bipartite graphs.

# Relationships
## Builds Upon
- **k-factor** (k=2)

## Enables
- **Hamilton cycle** — a Hamilton cycle is a connected 2-factor

## Related
- **One-factor** — the k=1 analog
- **Euler tour** — used in the construction proof

# Common Errors
- **Error**: Assuming a 2-factor is always a single cycle
  **Correction**: A 2-factor may consist of multiple disjoint cycles

# Common Confusions
- **Confusion**: Confusing 2-factor with Hamilton cycle
  **Clarification**: A Hamilton cycle is a 2-factor with exactly one cycle; a 2-factor may have multiple cycles

# Source Reference
Chapter 2, Section 2.1, Corollary 2.1.5, p. 49 (pdf p. 49).

# Verification Notes
- Concept synthesized from k-factor definition and Corollary 2.1.5
- Confidence: HIGH — directly defined and proved
