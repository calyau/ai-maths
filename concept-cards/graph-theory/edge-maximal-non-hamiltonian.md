---
concept: Edge-Maximal Non-Hamiltonian Graph
slug: edge-maximal-non-hamiltonian
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 289
section: "10.2 Hamilton cycles and degree sequences"
extraction_confidence: high
aliases:
  - "extremal non-Hamiltonian graph"
prerequisites:
  - hamiltonian-graph
extends: []
related:
  - chvatals-theorem
contrasts_with: []
answers_questions:
  - "What is an edge-maximal non-Hamiltonian graph?"
---

# Quick Definition
An edge-maximal non-Hamiltonian graph is a graph that is not Hamiltonian but becomes Hamiltonian upon the addition of any new edge.

# Core Definition
A graph G = (V, E) is **edge-maximal non-Hamiltonian** (or extremal non-Hamiltonian) if G has no Hamilton cycle but G + xy has a Hamilton cycle for every pair of non-adjacent vertices x, y. This means adding any edge creates a Hamilton cycle (Diestel, p. 289, proof of Theorem 10.2.1).

# Prerequisites
- **Hamiltonian graph** — the property being just barely missed

# Key Properties
1. Not Hamiltonian, but adding any edge makes it Hamiltonian
2. For any non-adjacent x, y: G + xy has a Hamilton cycle H through xy
3. H - xy is a Hamilton path from x to y in G
4. Used as a proof technique: assume graph is maximal non-Hamiltonian, derive structural properties
5. Key in the proof of Chvatal's theorem

# Context & Application
Edge-maximal non-Hamiltonian graphs are a standard proof technique. By assuming edge-maximality, one can derive strong structural properties that lead to contradictions with degree conditions.

# Examples
**Example** (p. 289-290): In the proof of Chvatal's theorem, G is chosen as an edge-maximal non-Hamiltonian graph with degree sequence >= (a1, ..., an).

# Relationships
## Related
- **Chvatal's theorem** — proof uses this technique
- **Hamiltonian closure** — related concept

# Source Reference
Chapter 10, Section 10.2, p. 289 (pdf p. 289).

# Verification Notes
- From proof of Theorem 10.2.1
- Confidence: HIGH — standard technique explicitly used
