---
concept: "Mader's Theorem"
slug: maders-theorem
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 78
section: "3.4 Mader's theorem"
extraction_confidence: high
aliases:
  - "Mader 1978"
  - "H-path theorem"
prerequisites:
  - mengers-theorem
  - h-path
extends:
  - mengers-theorem
related:
  - tuttes-theorem
contrasts_with: []
answers_questions:
  - "How many independent H-paths can be found in a graph?"
---

# Quick Definition
Given a graph G with induced subgraph H, the maximum number of independent H-paths equals M_G(H), a min-max quantity involving vertex sets and edge sets that meet all H-paths.

# Core Definition
**Theorem 3.4.1 (Mader 1978).** Given a graph G with an induced subgraph H, there are always M_G(H) independent H-paths in G, where M_G(H) is the minimum over all X and F of (|X| + sum of floor(|partial C|/2)) (Diestel, p. 78).

Here X is a subset of V(G-H) and F is a subset of E(G-H-X) such that every H-path has a vertex in X or an edge in F.

# Prerequisites
- **Menger's theorem** — Mader's theorem is a common generalization
- **H-path** — the objects being counted

# Key Properties
1. Generalizes both Menger's theorem (vertex version) and Tutte's 1-factor theorem
2. The separator involves both vertices (X) and edges (F)
3. Components of (V(G-H) \ X, F) contribute floor(|partial C|/2) to the bound
4. Presented without proof (the proof is deep)
5. Corollary 3.4.2: at least kappa_G(H)/2 independent H-paths and lambda_G(H)/2 edge-disjoint H-paths

# Construction / Recognition
## The Upper Bound M_G(H)
1. Choose X in V(G-H) and F in E(G-H-X) meeting all H-paths
2. For each component C of (Y, F), compute |partial C| (vertices with neighbors outside X union C)
3. M_G(H) = min(|X| + sum floor(|partial C|/2))

# Context & Application
Mader's theorem unifies Menger's theorem and Tutte's 1-factor theorem as special cases. It answers the natural question of how many independent H-paths exist in G, for an arbitrary induced subgraph H.

# Examples
**Example** (p. 78, Fig. 3.4.1): An H-path in G-X must have at least two vertices in partial C for some component C, since it enters and exits C.

# Relationships
## Builds Upon
- **Menger's theorem**, **H-path**

## Enables
- **Corollary 3.4.2** — bounds using kappa_G(H) and lambda_G(H)
- Derives Tutte's 1-factor theorem (Exercise 21)

## Related
- **Tutte's theorem** — can be derived as a special case

# Common Errors
- **Error**: Expecting kappa_G(H) independent H-paths
  **Correction**: Only kappa_G(H)/2 independent H-paths are guaranteed (Corollary 3.4.2)

# Source Reference
Chapter 3, Section 3.4, Theorem 3.4.1, pp. 78-79 (pdf pp. 78-79).

# Verification Notes
- Theorem stated without proof
- Confidence: HIGH — explicitly stated theorem
