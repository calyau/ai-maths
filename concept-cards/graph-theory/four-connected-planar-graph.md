---
concept: 4-Connected Planar Graph
slug: four-connected-planar-graph
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 288
section: "10.1 Simple sufficient conditions"
extraction_confidence: high
aliases: []
prerequisites:
  - k-connected-graph
  - planar-graph
extends:
  - k-connected-graph
related:
  - tuttes-hamiltonicity-theorem
  - hamiltonian-graph
contrasts_with: []
answers_questions:
  - "Are all 4-connected planar graphs Hamiltonian?"
---

# Quick Definition
A 4-connected planar graph is a planar graph with vertex connectivity at least 4. Tutte proved that every such graph has a Hamilton cycle.

# Core Definition
A graph G is a **4-connected planar graph** if it is planar (embeddable in the plane without edge crossings) and 4-connected (kappa(G) >= 4). Tutte's theorem (10.1.3) states that every 4-connected planar graph is Hamiltonian (Diestel, p. 288).

# Prerequisites
- **k-connected graph** — kappa(G) >= 4
- **Planar graph** — embeddable in the plane

# Key Properties
1. Every 4-connected planar graph has a Hamilton cycle (Tutte 1956)
2. 3-connectedness does not suffice for cubic planar graphs (Tutte 1946 counterexample)
3. The result connects planarity and connectivity to Hamiltonicity
4. Related to the four colour theorem via cubic planar graphs and 4-flows

# Context & Application
The Hamiltonicity of 4-connected planar graphs is one of the deepest results connecting planarity with Hamiltonicity. If every 3-connected cubic planar graph were Hamiltonian, the four colour theorem would follow as a corollary.

# Examples
**Example**: The icosahedron is 5-connected and planar, hence Hamiltonian by Tutte's theorem. The Tutte graph is a 3-connected cubic planar graph without a Hamilton cycle.

# Relationships
## Builds Upon
- **k-connected graph**, **planar graph**

## Related
- **Tutte's Hamiltonicity theorem** — the key result
- **Hamiltonian graph** — 4-connected planar graphs are Hamiltonian

# Source Reference
Chapter 10, Section 10.1, Theorem 10.1.3, p. 288 (pdf p. 288).

# Verification Notes
- From Theorem 10.1.3
- Confidence: HIGH
