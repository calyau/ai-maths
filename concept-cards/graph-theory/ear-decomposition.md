---
concept: Ear Decomposition
slug: ear-decomposition
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 67
section: "3.1 2-Connected graphs and subgraphs"
extraction_confidence: high
aliases:
  - "Whitney's ear decomposition"
  - "open ear decomposition"
prerequisites:
  - two-connected-graph
  - h-path
  - cycle
extends: []
related:
  - block
contrasts_with: []
answers_questions:
  - "How can 2-connected graphs be constructed?"
---

# Quick Definition
An ear decomposition builds a 2-connected graph by starting from a cycle and successively adding H-paths (ears) to the graph already constructed.

# Core Definition
**Proposition 3.1.3.** A graph is 2-connected if and only if it can be constructed from a cycle by successively adding H-paths to graphs H already constructed (Diestel, p. 67).

# Prerequisites
- **2-connected graph** — the graphs characterized by ear decomposition
- **H-path** — each "ear" is an H-path
- **Cycle** — the starting graph

# Key Properties
1. Start with any cycle
2. Each step adds an H-path (a path whose internal vertices are new, endpoints in H)
3. Every intermediate graph is 2-connected
4. Every 2-connected graph can be built this way
5. The proof uses maximality: if a 2-connected graph G has a maximal constructible subgraph H != G, then G-w for some w in H has a v-H path P, and H union wvP extends H

# Construction / Recognition
## To Build a 2-Connected Graph via Ear Decomposition
1. Start with a cycle C (this is G0)
2. Find an H-path P in G (a path with endpoints in H, internal vertices outside H)
3. Set H := H union P
4. Repeat until H = G

## To Verify Ear Decomposition Exists
1. Start with any cycle in G
2. Repeatedly find H-paths
3. If the process constructs all of G, the ear decomposition exists (and G is 2-connected)

# Context & Application
Ear decomposition is a constructive characterization of 2-connected graphs, providing an inductive approach to proving properties of such graphs. It is used in algorithms for biconnected components and in proofs about 2-connected graph structure.

# Examples
**Example** (p. 67, Fig. 3.1.2): Successive addition of H-paths to build a 2-connected graph from a cycle.

# Relationships
## Builds Upon
- **2-connected graph**, **H-path**, **cycle**

## Related
- **Tutte's wheel theorem** (Theorem 3.2.2) — analogous construction for 3-connected graphs

# Common Errors
- **Error**: Starting with a graph other than a cycle
  **Correction**: The base case must be a cycle, which is the simplest 2-connected graph

# Common Confusions
- **Confusion**: Confusing H-paths (ears) with arbitrary paths
  **Clarification**: An H-path has both endpoints in H but all internal vertices outside H

# Source Reference
Chapter 3, Section 3.1, Proposition 3.1.3, p. 67 (pdf p. 67).

# Verification Notes
- Proposition from p. 67
- Confidence: HIGH — explicitly stated and proved
