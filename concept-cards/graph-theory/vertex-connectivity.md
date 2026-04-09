---
concept: Vertex Connectivity
slug: vertex-connectivity
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 65
section: null
extraction_confidence: high
aliases:
  - "kappa(G)"
  - "connectivity number"
prerequisites:
  - graph
extends: []
related:
  - edge-connectivity
  - k-connected-graph
  - mengers-theorem
contrasts_with:
  - edge-connectivity
answers_questions:
  - "What is vertex connectivity?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
The vertex connectivity kappa(G) is the minimum number of vertices whose removal disconnects G (or |G|-1 if G is complete).

# Core Definition
The (vertex) **connectivity** kappa(G) of a graph G is the minimum size of a vertex set S such that G-S is disconnected or has only one vertex. For complete graphs K_n, kappa(K_n) = n-1 (Diestel, Ch. 1.4).

# Prerequisites
- **Graph** — kappa(G) is a graph parameter

# Key Properties
1. kappa(G) >= k iff G is k-connected
2. kappa(G) <= lambda(G) <= delta(G)
3. kappa(G) = max k such that G is k-connected
4. kappa(K_n) = n-1
5. By Menger's theorem, kappa(G) equals the maximum number of independent paths between the worst-case pair of vertices

# Context & Application
Vertex connectivity is the primary connectivity measure in Chapter 3. The chapter opens by noting that the definition (minimum vertices to disconnect) is unintuitive, but Menger's theorem shows it equals the maximum number of independent paths between any two vertices.

# Examples
**Example**: kappa(K_4) = 3. kappa(C_n) = 2. kappa(path P_n) = 1 for n >= 3.

# Relationships
## Builds Upon
- **Graph**

## Related
- **k-connected graph** — kappa(G) >= k
- **Menger's theorem** — kappa(G) = min separator = max independent paths

## Contrasts With
- **Edge connectivity** — lambda(G), minimum edges to disconnect

# Source Reference
Chapter 1.4 and Chapter 3.

# Verification Notes
- Standard definition
- Confidence: HIGH
