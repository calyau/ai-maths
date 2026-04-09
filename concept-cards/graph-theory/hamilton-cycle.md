---
concept: Hamilton Cycle
slug: hamilton-cycle
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
  - "Hamiltonian cycle"
prerequisites:
  - graph
  - cycle
  - path
extends:
  - cycle
related:
  - hamilton-path
  - hamiltonian-graph
  - euler-tour
  - diracs-theorem
contrasts_with:
  - euler-tour
answers_questions:
  - "What is a Hamilton cycle?"
  - "What distinguishes a Hamilton cycle from an Euler tour?"
---

# Quick Definition
A Hamilton cycle of a graph G is a cycle that contains every vertex of G exactly once. A graph with a Hamilton cycle is called Hamiltonian.

# Core Definition
If |G| >= 3, then any closed walk that contains every vertex of G exactly once is a cycle: a **Hamilton cycle** of G. If G has a Hamilton cycle, it is called **hamiltonian** (Diestel, p. 285).

# Prerequisites
- **Graph** — Hamilton cycles are defined in graphs
- **Cycle** — a Hamilton cycle is a specific type of cycle
- **Path** — Hamilton paths are related

# Key Properties
1. Contains every vertex of G exactly once
2. Is a 2-factor consisting of a single cycle
3. G must have |G| >= 3 for a Hamilton cycle to exist
4. No good characterization of Hamiltonian graphs is known (and likely none exists, as the problem is NP-complete)
5. Sufficient conditions include: delta(G) >= n/2 (Dirac), d(x)+d(y) >= n for non-adjacent x,y (Ore)
6. A Hamiltonian graph must be 2-connected (necessary but not sufficient)

# Construction / Recognition
## To Verify a Hamilton Cycle
1. Check that the cycle visits every vertex of G exactly once
2. Verify it returns to the starting vertex
3. Confirm all edges used are edges of G

# Context & Application
Determining whether a graph is Hamiltonian is NP-hard and was one of the early prototypes of NP-complete problems. No good characterization analogous to Euler's theorem (for Euler tours) is known. The study of sufficient conditions (Dirac, Ore, Chvatal) is the main theme of Chapter 10.

The travelling salesman problem is a weighted version of the Hamilton cycle problem: find a minimum-weight Hamilton cycle.

# Examples
**Example** (p. 285): A complete graph K_n (n >= 3) is Hamiltonian. The Petersen graph is not Hamiltonian.

**Example** (p. 286): If n is odd and G is the union of two copies of K^{ceil(n/2)} meeting in one vertex, then delta(G) = floor(n/2) but G is not Hamiltonian (showing Dirac's bound n/2 is tight).

# Relationships
## Builds Upon
- **Cycle** — a Hamilton cycle is a spanning cycle

## Enables
- **Dirac's theorem** — sufficient condition for Hamiltonicity
- **Ore's theorem** — another sufficient condition
- **Chvatal's theorem** — characterizes Hamiltonian degree sequences

## Related
- **Hamilton path** — a path visiting every vertex
- **Hamiltonian graph** — a graph possessing a Hamilton cycle

## Contrasts With
- **Euler tour** — visits every edge exactly once (vs. every vertex for Hamilton)

# Common Errors
- **Error**: Confusing Hamilton cycle with Euler tour
  **Correction**: Hamilton cycle visits every vertex once; Euler tour visits every edge once. A graph can have one without the other.

# Common Confusions
- **Confusion**: Thinking Hamiltonicity has a simple characterization like Euler tours
  **Clarification**: Unlike Euler tours (characterized by all vertices having even degree), no simple necessary and sufficient condition for Hamiltonicity is known

# Source Reference
Chapter 10, p. 285 (pdf p. 285). Opening definition of the chapter.

# Verification Notes
- Definition from p. 285
- Confidence: HIGH — explicitly defined
