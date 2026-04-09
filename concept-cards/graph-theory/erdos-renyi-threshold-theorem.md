---
concept: "Erdős-Rényi Threshold Theorem"
slug: erdos-renyi-threshold-theorem
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
aliases:
  - "subgraph threshold theorem"
prerequisites:
  - second-moment-method
  - balanced-graph
  - threshold-function
extends: []
related:
  - random-graph-gnp
contrasts_with: []
answers_questions:
  - "What is the threshold for containing a balanced subgraph?"
---

# Quick Definition
For a balanced graph H with k vertices and l >= 1 edges, t(n) = n^{-k/l} is a threshold function for the property of containing H as a subgraph in G(n,p).

# Core Definition
**Theorem 11.4.3** (Erdős & Rényi 1960): If H is a balanced graph with k vertices and l >= 1 edges, then t(n) := n^{-k/l} is a threshold function for the property P_H of containing a copy of H as a subgraph (Diestel, p. 318).

# Prerequisites
- **Second moment method** — The proof uses the second moment method for the upper part
- **Balanced graph** — H must be balanced for the simple threshold formula
- **Threshold function** — The concept being computed

# Key Properties
1. Below the threshold (p/t -> 0): E(X) -> 0, so almost no G contains H (first moment)
2. Above the threshold (p/t -> infinity): sigma^2/mu^2 -> 0, so almost every G contains H (second moment)
3. The "balanced" condition ensures epsilon(H') <= epsilon(H) for all subgraphs H'
4. For unbalanced H, the threshold becomes t(n) = n^{-1/epsilon'(H)} where epsilon'(H) = max epsilon(F) over F subset H

# Context & Application
This theorem provides a unified way to compute thresholds for many natural graph properties. The proof illustrates the complete first-and-second-moment argument.

# Examples
**Example 1** (Corollary 11.4.4): Threshold for k-cycles is n^{-1} (independent of k!).

**Example 2** (Corollary 11.4.5): Threshold for trees of order k is n^{-k/(k-1)}.

**Example 3** (Corollary 11.4.6): Threshold for K^k is n^{-2/(k-1)}.

# Relationships
## Builds Upon
- **Second moment method** — The proof technique

## Related
- **Balanced graph** — The hypothesis on H

# Source Reference
Chapter 11, Section 11.4, pages 318-322 (Theorem 11.4.3).

# Verification Notes
- Statement and proof from pp. 318-322
- Confidence: HIGH — named theorem with complete proof
