---
concept: "Tutte's Wheel Theorem"
slug: tuttes-wheel-theorem
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 68
section: "3.2 The structure of 3-connected graphs"
extraction_confidence: high
aliases:
  - "Tutte 1961"
  - "constructive characterization of 3-connected graphs"
prerequisites:
  - three-connected-graph
  - contractible-edge
extends: []
related:
  - ear-decomposition
contrasts_with: []
answers_questions:
  - "How can 3-connected graphs be constructed?"
---

# Quick Definition
A graph G is 3-connected if and only if there exists a sequence G0 = K4, G1, ..., Gn = G where each Gi+1 has an edge xy with d(x), d(y) >= 3 and Gi = Gi+1/xy.

# Core Definition
**Theorem 3.2.2 (Tutte 1961).** A graph G is 3-connected if and only if there exists a sequence G0, ..., Gn of graphs with: (i) G0 = K4 and Gn = G; (ii) Gi+1 has an edge xy with d(x), d(y) >= 3 and Gi = Gi+1/xy, for every i < n (Diestel, p. 69).

# Prerequisites
- **3-connected graph** — the graphs being characterized
- **Contractible edge** — Lemma 3.2.1 guarantees such edges exist

# Key Properties
1. K4 is the starting graph (smallest wheel, smallest 3-connected graph)
2. Each step is the reverse of contracting an edge: splitting a vertex
3. All graphs in the sequence are 3-connected
4. Both endpoints of the split edge must have degree >= 3
5. Based on Lemma 3.2.1: every 3-connected graph with |G| > 4 has a contractible edge

# Construction / Recognition
## Building 3-Connected Graphs
1. Start with K4
2. Pick a vertex v in the current graph
3. Split v into two adjacent vertices v', v''
4. Distribute neighbors: each gets at least 3 edges, every former neighbor goes to at least one
5. Repeat to get any desired 3-connected graph

# Context & Application
Tutte's wheel theorem is the 3-connected analogue of the ear decomposition for 2-connected graphs. It provides a complete constructive characterization using a simple local operation (vertex splitting) based on the minor relation.

Wheels C^n * K^1 give the theorem its name: K4 is the smallest wheel, and the construction can produce all wheels.

# Examples
**Example** (p. 69): Starting from K4, splitting one vertex yields a graph with 5 vertices that is 3-connected (provided degree conditions are met).

# Relationships
## Builds Upon
- **3-connected graph**, **contractible edge**

## Related
- **Ear decomposition** — the 2-connected analogue

# Common Errors
- **Error**: Splitting a vertex so that one part has degree < 3
  **Correction**: Both v' and v'' must have degree >= 3 for 3-connectivity to be preserved

# Common Confusions
- **Confusion**: Thinking the construction uses subgraphs, not minors
  **Clarification**: Unlike the ear decomposition (which uses subgraphs), Tutte's wheel theorem uses the minor relation (contraction)

# Source Reference
Chapter 3, Section 3.2, Theorem 3.2.2, pp. 68-70 (pdf pp. 68-70).

# Verification Notes
- Theorem from p. 69
- Based on Lemma 3.2.1 (p. 68)
- Confidence: HIGH — major named theorem with proof
