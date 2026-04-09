---
concept: Edge-Connectivity
slug: edge-connectivity

category: connectivity
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 21
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "l-edge-connected"
  - "lambda(G)"

prerequisites:
  - graph
  - edge
  - connected-graph
extends:
  - connected-graph
related:
  - k-connected
  - minimum-degree
contrasts_with:
  - k-connected

answers_questions:
  - "What is edge-connectivity?"
  - "What does lambda(G) mean?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
A graph G is l-edge-connected if |G| > 1 and G - F remains connected for every set F of fewer than l edges. The edge-connectivity lambda(G) is the greatest such l.

# Core Definition
If |G| > 1 and G - F is connected for every set F of edges with |F| < l, then G is called l-edge-connected. The greatest integer l such that G is l-edge-connected is the edge-connectivity lambda(G) of G. In particular, lambda(G) = 0 if G is disconnected (Diestel, p. 12).

# Prerequisites
- **Graph**, **edge**, **connected-graph**

# Key Properties
1. kappa(G) <= lambda(G) <= delta(G) (Proposition 1.4.2)
2. lambda(G) = 0 iff G is disconnected
3. lambda(G) <= delta(G) because deleting all edges at a vertex of minimum degree disconnects

# Context & Application
Edge-connectivity is an alternative measure of graph robustness. It is always at least as large as vertex connectivity but at most the minimum degree.

# Examples
**Example** (p. 12): Fig. 1.4.3 shows the octahedron G with kappa(G) = lambda(G) = 4, and a graph H with kappa(H) = 2 but lambda(H) = 4.

# Relationships
## Builds Upon
- **connected-graph**

## Contrasts With
- **k-connected** — vertex connectivity; kappa(G) <= lambda(G)

# Source Reference
Chapter 1: The Basics, Section 1.4, page 12 (pdf p. 22). See Fig. 1.4.3.

# Verification Notes
- Direct from p. 12
- Confidence: HIGH
