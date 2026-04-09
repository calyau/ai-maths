---
concept: k-Connected Graph
slug: k-connected-graph
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
  - "k-connected"
  - "k-vertex-connected"
prerequisites:
  - graph
  - connectivity
extends:
  - connectivity
related:
  - global-mengers-theorem
  - two-connected-graph
  - three-connected-graph
  - k-edge-connected-graph
contrasts_with:
  - k-edge-connected-graph
answers_questions:
  - "What is a k-connected graph?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
A graph G is k-connected if |G| > k and G-X is connected for every set X of fewer than k vertices. Equivalently, kappa(G) >= k.

# Core Definition
A graph G is **k-connected** if |G| > k and G remains connected after the removal of any set of fewer than k vertices. The maximum k for which G is k-connected is kappa(G), the (vertex) connectivity of G (Diestel, Ch. 1.4, elaborated in Ch. 3).

# Prerequisites
- **Graph** — k-connectivity is a graph property
- **Connectivity** — kappa(G) is the connectivity parameter

# Key Properties
1. kappa(G) >= k means at least k vertices must be removed to disconnect G
2. G is k-connected iff any two vertices are joined by k independent paths (Theorem 3.3.6)
3. k-connected implies k-edge-connected, but not vice versa
4. k-connected implies (k-1)-connected
5. kappa(G) <= lambda(G) <= delta(G) (connectivity <= edge-connectivity <= minimum degree)

# Construction / Recognition
## To Verify k-Connectivity
1. Check |G| > k
2. For every set X of k-1 vertices, verify G-X is connected
3. Alternatively, verify k independent paths exist between every pair of vertices

# Context & Application
k-connectivity is the central topic of Chapter 3. It measures how resilient a graph is to vertex removal. The global version of Menger's theorem shows the equivalence of the "removal" and "paths" characterizations.

# Examples
**Example**: K_n is (n-1)-connected. The Petersen graph is 3-connected. C_n (cycle on n vertices) is 2-connected.

# Relationships
## Builds Upon
- **Graph**, **connectivity**

## Enables
- **Menger's theorem** — min separator = max disjoint paths
- **k-linked graph** — high connectivity forces k-linkedness

## Contrasts With
- **k-edge-connected graph** — uses edge removal instead of vertex removal

# Common Errors
- **Error**: Forgetting the condition |G| > k
  **Correction**: K_k is not k-connected; we need |G| > k

# Source Reference
Chapter 1.4 and Chapter 3 (pdf p. 65 onwards).

# Verification Notes
- Standard definition from Ch. 1.4
- Confidence: HIGH
