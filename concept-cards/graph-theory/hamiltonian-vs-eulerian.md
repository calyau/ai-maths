---
concept: Hamiltonian vs Eulerian
slug: hamiltonian-vs-eulerian
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 285
section: "10.1 Simple sufficient conditions"
extraction_confidence: high
aliases: []
prerequisites:
  - hamilton-cycle
  - euler-tour
extends: []
related:
  - hamiltonian-graph
contrasts_with: []
answers_questions:
  - "What distinguishes a Hamilton cycle from an Euler tour?"
---

# Quick Definition
An Euler tour visits every edge exactly once; a Hamilton cycle visits every vertex exactly once. Euler tours are completely characterized (all vertices even degree); Hamiltonicity has no good characterization.

# Core Definition
The distinction between Euler tours and Hamilton cycles is the opening theme of Chapter 10. An Euler tour is a closed walk traversing every edge exactly once (Theorem 1.8.1 gives a complete characterization). A Hamilton cycle is a cycle containing every vertex exactly once. To determine Hamiltonicity is much harder than deciding Eulerianity, and no good characterization is known (Diestel, p. 285).

# Prerequisites
- **Hamilton cycle** — visits every vertex
- **Euler tour** — visits every edge

# Key Properties
1. Euler tour: exists iff every vertex has even degree and G is connected (Theorem 1.8.1)
2. Hamilton cycle: no simple characterization; NP-complete decision problem
3. A graph can be Eulerian but not Hamiltonian (e.g., K_{2,4})
4. A graph can be Hamiltonian but not Eulerian (e.g., K4 with odd degrees)
5. The sharp contrast in characterizability is the motivation for Chapter 10

# Context & Application
The comparison between Euler tours and Hamilton cycles illustrates a fundamental dichotomy in graph theory: some problems have clean, polynomial-time solutions, while analogous-sounding problems are NP-hard.

# Examples
**Example**: K4 is Hamiltonian (has a Hamilton cycle) but not Eulerian (vertices have degree 3, which is odd). The graph K_{2,4} is Eulerian (all degrees even) but checking Hamiltonicity requires more work.

# Relationships
## Builds Upon
- **Hamilton cycle**, **Euler tour**

## Related
- **Hamiltonian graph** — defined by having a Hamilton cycle

# Common Errors
- **Error**: Confusing "visits every vertex" with "visits every edge"
  **Correction**: Hamilton cycles visit every vertex; Euler tours visit every edge

# Source Reference
Chapter 10, opening paragraph, p. 285 (pdf p. 285).

# Verification Notes
- From p. 285 opening discussion
- Confidence: HIGH — the contrast is explicitly drawn
