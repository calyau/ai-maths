---
concept: Nonvanishing Coefficients of the Tutte Polynomial
slug: nonvanishing-coefficients-tutte
category: tutte-polynomial
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 363
section: "X.5 A Spanning Tree Expansion of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - spanning-tree-expansion
extends: []
related:
  - chromatic-invariant
  - tait-conjecture-crossing-number
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
For a 2-connected loopless graph $G$ with $n$ vertices and $m$ edges: $t_{i0} > 0$ for $1 \leq i \leq n-1$, $t_{0j} > 0$ for $1 \leq j \leq m-n+1$, and $t_{11} > 0$ unless $G$ is a cycle or thick edge.

# Core Definition
Theorem 14 (p. 363): "Let $G$ be a 2-connected loopless graph with $n$ vertices and $m$ edges, and let $T_G(x,y) = \sum t_{ij} x^i y^j$. Then $t_{i0} > 0$ for each $i, 1 \leq i \leq n-1$, and $t_{0j} > 0$ for each $j, 1 \leq j \leq m-n+1$." Theorem 15: $t_{11} > 0$ unless $G$ is a cycle or thick edge.

# Prerequisites
- **Spanning tree expansion** — The coefficients $t_{ij}$ come from this expansion

# Key Properties
1. $t_{i0} > 0$ for $1 \leq i \leq n-1$ (2-connected loopless)
2. $t_{0j} > 0$ for $1 \leq j \leq m-n+1$ (2-connected loopless)
3. $t_{11} > 0$ unless $G$ is a cycle $C_n$ or thick edge $I_k$ (Theorem 15)
4. Brylawski's identity: $\sum_{i=0}^h \sum_{j=0}^{h-i} (-1)^j \binom{h-i}{j} t_{ij} = 0$ for $e(G) > h$

# Context & Application
These results are used in the proof of Tait's conjecture (Theorem 22): the breadth of the Jones polynomial equals the number of crossings because all boundary coefficients are nonzero.

# Relationships
## Builds Upon
- **spanning-tree-expansion**

## Enables
- **tait-conjecture-crossing-number** — Uses Theorem 14

## Related
- **chromatic-invariant** — $\theta(G) = t_{10}$

# Source Reference
Chapter X, Section X.5, Theorems 14-15, pages 363-364.

# Verification Notes
- Definition source: Direct from Theorems 14-15
- Confidence rationale: Explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
