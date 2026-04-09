---
concept: Balanced Graph
slug: balanced-graph
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 318
section: "11.4 Threshold functions and second moments"
extraction_confidence: high
aliases: []
prerequisites:
  - graph
extends: []
related:
  - erdos-renyi-threshold-theorem
contrasts_with: []
answers_questions:
  - "What is a balanced graph?"
---

# Quick Definition
A graph H is balanced if epsilon(H') <= epsilon(H) for all subgraphs H' of H, where epsilon denotes the edge density (number of edges divided by number of vertices).

# Core Definition
A graph H is *balanced* if epsilon(H') <= epsilon(H) for all subgraphs H' of H, where epsilon(H) = ||H||/|H| is the edge density (Diestel, p. 318).

# Prerequisites
- **Graph** — Balanced is a property of graphs

# Key Properties
1. Complete graphs K^k are balanced: epsilon(K^i) = (i-1)/2 < (k-1)/2 = epsilon(K^k) for i < k
2. Cycles C^k are balanced
3. Trees of order k are balanced
4. For balanced H, the threshold for P_H has the simple form t(n) = n^{-k/l}

# Examples
**Example 1** (Corollary 11.4.6): K^k is balanced because epsilon(K^i) < epsilon(K^k) for i < k.

# Relationships
## Enables
- **Erdős-Rényi threshold theorem** — Requires balanced H for the simple formula

# Source Reference
Chapter 11, Section 11.4, page 318.

# Verification Notes
- Definition from p. 318
- Confidence: HIGH — explicit definition
