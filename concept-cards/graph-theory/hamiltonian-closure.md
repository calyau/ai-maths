---
concept: Hamiltonian Closure
slug: hamiltonian-closure
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 289
section: "10.2 Hamilton cycles and degree sequences"
extraction_confidence: medium
aliases:
  - "Bondy-Chvatal closure"
prerequisites:
  - hamiltonian-graph
  - degree-sequence
extends: []
related:
  - chvatals-theorem
  - ores-theorem
contrasts_with: []
answers_questions:
  - "What is the Hamiltonian closure of a graph?"
---

# Quick Definition
The Hamiltonian closure of a graph G is obtained by repeatedly adding edges between non-adjacent vertices whose degree sum is at least n, until no more such pairs exist. G is Hamiltonian iff its closure is.

# Core Definition
The **Hamiltonian closure** (or Bondy-Chvatal closure) of a graph G is the graph obtained by iteratively adding edges between non-adjacent vertices u, v with d(u) + d(v) >= n until no more such pairs exist. A graph is Hamiltonian if and only if its closure is Hamiltonian.

# Prerequisites
- **Hamiltonian graph** — closure preserves Hamiltonicity
- **Degree sequence** — the closure is based on degree sums

# Key Properties
1. The closure is unique (independent of the order of edge additions)
2. G is Hamiltonian iff its closure is Hamiltonian
3. If the closure is complete (K_n), then G is Hamiltonian
4. Chvatal's theorem can be restated: degree sequences satisfying the Chvatal condition produce closures that are K_n
5. The proof of Chvatal's theorem uses edge-maximal non-Hamiltonian graphs, which relate to the closure concept

# Context & Application
The Hamiltonian closure provides an operational way to check Hamiltonicity: repeatedly add edges between non-adjacent vertices with high degree sum. If the process produces K_n, the original graph is Hamiltonian.

# Examples
**Example**: For a graph satisfying Dirac's condition (delta >= n/2), every non-adjacent pair has degree sum >= n, so the closure is K_n, confirming Hamiltonicity.

# Relationships
## Builds Upon
- **Hamiltonian graph**, **degree sequence**

## Related
- **Chvatal's theorem** — the closure concept underlies the proof
- **Ore's theorem** — if all non-adjacent pairs have degree sum >= n, closure is K_n

# Source Reference
Chapter 10, Section 10.2 context.

# Verification Notes
- Implicit in the proof of Theorem 10.2.1 (edge-maximal non-Hamiltonian graphs)
- Confidence: MEDIUM — concept is standard but not explicitly named in the text
