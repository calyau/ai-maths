---
concept: Hamiltonian Graph
slug: hamiltonian-graph
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
aliases:
  - "Hamiltonian"
prerequisites:
  - hamilton-cycle
extends: []
related:
  - diracs-theorem
  - ores-theorem
  - chvatals-theorem
  - toughness
contrasts_with:
  - eulerian-graph
answers_questions:
  - "What is a Hamiltonian graph?"
---

# Quick Definition
A graph is Hamiltonian if it contains a Hamilton cycle.

# Core Definition
If G has a Hamilton cycle, it is called **hamiltonian** (Diestel, p. 285).

# Prerequisites
- **Hamilton cycle** — a graph is Hamiltonian iff it has one

# Key Properties
1. No good characterization is known (NP-complete decision problem)
2. Necessary conditions: 2-connected, not too sparse
3. Sufficient conditions: Dirac (delta >= n/2), Ore (d(x)+d(y) >= n for non-adjacent pairs), Chvatal (degree sequence condition)
4. Hamiltonian implies 1-tough
5. Determining Hamiltonicity is NP-hard

# Construction / Recognition
## Known Sufficient Conditions
1. delta(G) >= n/2 (Dirac's theorem)
2. d(x) + d(y) >= n for all non-adjacent x, y (Ore's theorem)
3. Degree sequence satisfies Chvatal's condition (Theorem 10.2.1)
4. alpha(G) <= kappa(G) (Proposition 10.1.2)
5. G is 4-connected and planar (Tutte's theorem, Theorem 10.1.3)

# Context & Application
The Hamiltonicity problem originated from a game invented by W.R. Hamilton in 1857. It later became the travelling salesman problem in combinatorial optimization. The NP-completeness means no efficient algorithm is expected, motivating the search for sufficient conditions.

# Examples
**Example**: All complete graphs K_n (n >= 3) are Hamiltonian. The Petersen graph is not Hamiltonian despite being 3-connected and 3-regular.

# Relationships
## Builds Upon
- **Hamilton cycle**

## Related
- **Dirac's theorem**, **Ore's theorem**, **Chvatal's theorem** — sufficient conditions
- **Toughness** — related structural property

## Contrasts With
- **Eulerian graph** — has an Euler tour (every edge once); different from Hamiltonian (every vertex once)

# Source Reference
Chapter 10, p. 285 (pdf p. 285).

# Verification Notes
- Definition from p. 285
- Confidence: HIGH — standard term
