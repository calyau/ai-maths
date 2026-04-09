---
concept: k-Edge-Connected Graph
slug: k-edge-connected-graph
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
  - "k-edge-connected"
prerequisites:
  - graph
  - edge-connectivity
extends:
  - edge-connectivity
related:
  - k-connected-graph
  - mengers-theorem-edge-version
contrasts_with:
  - k-connected-graph
answers_questions:
  - "What is a k-edge-connected graph?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
A graph G is k-edge-connected if it remains connected after the removal of any set of fewer than k edges. Equivalently, lambda(G) >= k.

# Core Definition
A graph G is **k-edge-connected** if lambda(G) >= k, where lambda(G) is the minimum number of edges whose removal disconnects G (the edge-connectivity).

# Prerequisites
- **Graph** — k-edge-connectivity is a graph property
- **Edge-connectivity** — lambda(G) is the parameter

# Key Properties
1. lambda(G) >= k means at least k edges must be removed to disconnect G
2. G is k-edge-connected iff any two vertices are joined by k edge-disjoint paths (Theorem 3.3.6(ii))
3. kappa(G) <= lambda(G) <= delta(G)
4. k-edge-connected does not imply k-connected (e.g., a graph with a vertex of degree k may be k-edge-connected but not k-connected)
5. Every 2k-edge-connected graph has k edge-disjoint spanning trees (Corollary 2.4.2)

# Context & Application
Edge-connectivity is the "edge removal" analogue of vertex connectivity. It is always at least as large as vertex connectivity but can be strictly larger.

# Examples
**Example**: A cycle C_n is 2-edge-connected and 2-connected. A graph obtained from two K_4's sharing an edge is 3-edge-connected but not 3-connected.

# Relationships
## Builds Upon
- **Graph**, **edge-connectivity**

## Related
- **Menger's theorem (edge version)** — characterizes edge-connectivity via edge-disjoint paths
- **Edge-disjoint spanning trees** — 2k-edge-connected implies k edge-disjoint spanning trees

## Contrasts With
- **k-connected graph** — vertex removal vs. edge removal

# Source Reference
Chapter 3, context of Section 3.3 (Menger's theorem).

# Verification Notes
- Standard definition
- Confidence: HIGH
