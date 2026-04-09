---
concept: "kappa_G(H)"
slug: kappa-g-h
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
  - "H-path vertex separator"
prerequisites:
  - h-path
extends: []
related:
  - maders-theorem
  - lambda-g-h
contrasts_with:
  - lambda-g-h
answers_questions:
  - "What is kappa_G(H)?"
---

# Quick Definition
kappa_G(H) is the least cardinality of a vertex set X in V(G-H) that meets every H-path in G.

# Core Definition
Given an induced subgraph H of G, **kappa_G(H)** denotes the least cardinality of a vertex set X contained in V(G-H) that meets every H-path in G (Diestel, p. 78).

# Prerequisites
- **H-path** — the paths being blocked

# Key Properties
1. X must lie outside H (in V(G-H))
2. Every H-path must contain a vertex from X
3. G has at least kappa_G(H)/2 independent H-paths (Corollary 3.4.2)
4. The factor of 1/2 is best possible (Exercise 19)

# Context & Application
kappa_G(H) is the vertex analogue of lambda_G(H) for H-paths. It measures how many vertices outside H are needed to block all H-paths.

# Examples
**Example** (Exercise 19): There exist graphs where the maximum number of independent H-paths is exactly kappa_G(H)/2.

# Relationships
## Related
- **Mader's theorem** — gives the exact maximum number of H-paths
- **lambda_G(H)** — the edge analogue

## Contrasts With
- **lambda_G(H)** — uses edges instead of vertices to block H-paths

# Source Reference
Chapter 3, Section 3.4, p. 78 (pdf p. 78).

# Verification Notes
- Definition from p. 78
- Confidence: HIGH — explicitly defined
