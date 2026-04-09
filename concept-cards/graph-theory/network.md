---
concept: Network
slug: network
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 151
section: "6.2 Flows in networks"
extraction_confidence: high
aliases:
  - "flow network"
prerequisites:
  - graph
  - edge
  - vertex
related:
  - flow-in-network
  - capacity-function
  - cut-in-network
answers_questions:
  - "What is a network in graph theory?"
---

# Quick Definition
A network is a multigraph G equipped with two distinguished vertices s (source) and t (sink) and a capacity function c on its directed edges.

# Core Definition
Let G = (V, E) be a multigraph, s, t in V two fixed vertices, and c: E-arrow -> N a map. We call c a **capacity function** on G, and the tuple N := (G, s, t, c) a **network**. Note that c is defined independently for the two directions of an edge. (Diestel, p. 141, Section 6.2)

# Prerequisites
- **Graph (multigraph)** — The underlying structure
- **Vertex** — Source and sink are distinguished vertices

# Key Properties
1. Has a designated source s and sink t
2. Capacity function c assigns non-negative integer capacities to each directed edge
3. Capacities for the two directions of an edge may differ
4. Forms the setting for the max-flow min-cut theorem

# Context & Application
Networks formalize the intuitive notion of a system with a source producing flow and a sink consuming it, where links have limited capacity. This is the standard framework for network flow algorithms.

# Examples
**Example** (p. 142, Fig. 6.2.1): A network with source s, sink t, and integer capacities on each edge, shown with a flow of total value 3.

# Relationships
## Builds Upon
- **Graph** — A network is a graph with additional structure

## Enables
- **Flow in network** — Flows are defined within networks
- **Cut in network** — Cuts separate source from sink
- **Max-flow min-cut theorem** — The fundamental theorem about networks

# Source Reference
Chapter 6: Flows, Section 6.2 "Flows in networks," page 141 (pdf page 151).

# Verification Notes
- Definition: Directly from p. 141
- Confidence: HIGH — explicit formal definition
