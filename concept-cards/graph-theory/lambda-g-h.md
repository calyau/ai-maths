---
concept: "lambda_G(H)"
slug: lambda-g-h
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
  - "H-path edge separator"
prerequisites:
  - h-path
extends: []
related:
  - maders-theorem
  - kappa-g-h
contrasts_with:
  - kappa-g-h
answers_questions:
  - "What is lambda_G(H)?"
---

# Quick Definition
lambda_G(H) is the least cardinality of an edge set F in E(G) that meets every H-path in G.

# Core Definition
Given an induced subgraph H of G, **lambda_G(H)** denotes the least cardinality of an edge set F contained in E(G) that meets every H-path in G (Diestel, p. 78).

# Prerequisites
- **H-path** — the paths being blocked

# Key Properties
1. F is a set of edges (not vertices) blocking all H-paths
2. G has at least lambda_G(H)/2 edge-disjoint H-paths (Corollary 3.4.2)
3. The factor of 1/2 is best possible (Exercise 20)

# Context & Application
lambda_G(H) is the edge analogue of kappa_G(H). It measures how many edges are needed to block all H-paths.

# Relationships
## Related
- **Mader's theorem** — gives the exact number of H-paths
- **kappa_G(H)** — the vertex analogue

## Contrasts With
- **kappa_G(H)** — uses vertices instead of edges

# Source Reference
Chapter 3, Section 3.4, p. 78 (pdf p. 78).

# Verification Notes
- Definition from p. 78
- Confidence: HIGH — explicitly defined
