---
concept: Hamilton Cycle
slug: hamilton-cycle
category: paths-and-cycles
subcategory: hamilton-euler
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.3 Hamilton Cycles and Euler Circuits"
extraction_confidence: high
aliases:
  - Hamiltonian cycle
  - Hamiltonian graph
prerequisites:
  - graph
  - cycle
  - complete-graph
extends:
  - cycle
related:
  - hamilton-path
  - euler-circuit
contrasts_with:
  - euler-circuit
answers_questions:
  - "What is a Hamilton cycle?"
  - "What distinguishes Hamilton cycles from Euler circuits?"
---

# Quick Definition

A Hamilton cycle is a cycle containing all vertices of a graph. A graph containing a Hamilton cycle is called Hamiltonian.

# Core Definition

"A cycle containing all the vertices of a graph is said to be a Hamilton cycle of the graph. [...] A graph containing a Hamilton cycle is said to be Hamiltonian" (Bollobás, p. 23). The term originates from a game invented in 1857 by Sir William Rowan Hamilton involving cycles through all vertices of the dodecahedron graph.

# Prerequisites

- **Graph** — Hamilton cycles are defined within graphs
- **Cycle** — A Hamilton cycle is a specific cycle
- **Complete graph** — $K_n$ decomposition into Hamilton cycles is studied

# Key Properties

1. A Hamilton cycle visits every vertex exactly once (and returns to start)
2. For odd $n \ge 3$, $K_n$ decomposes into $\frac{1}{2}(n-1)$ edge-disjoint Hamilton cycles (Theorem 11)
3. No efficient algorithm is known for finding Hamilton cycles
4. Even deciding if a graph is Hamiltonian is computationally hard
5. The knight's tour puzzle asks for a Hamilton cycle in the knight's graph

# Construction / Recognition

No efficient general algorithm is known. The travelling salesman problem (finding a minimum-cost Hamilton cycle) is one of the most famous unsolved algorithmic problems.

# Context & Application

Hamilton cycles connect to the travelling salesman problem, one of the most important optimization problems. The concept originated from Hamilton's 1857 game on the dodecahedron. The knight's tour, studied by Euler in 1759, is an earlier example.

# Examples

**Example** (p. 23): Fig. I.11 shows a Hamilton cycle in the graph of the dodecahedron.

**Example** (p. 23): Fig. I.12 shows two knight's tours (Hamilton cycles in the knight's graph on a chessboard).

**Example** (Theorem 11, p. 24): For odd $n \ge 3$, $K_n$ is decomposable into $\frac{1}{2}(n-1)$ edge-disjoint Hamilton cycles.

# Relationships

## Builds Upon
- **Cycle** — A Hamilton cycle is a cycle through all vertices

## Enables
- Travelling salesman problem
- Graph decomposition theory

## Related
- **Hamilton path** — A path through all vertices (not necessarily closed)

## Contrasts With
- **Euler circuit** — An Euler circuit traverses every edge; a Hamilton cycle visits every vertex

# Common Errors

- **Error**: Confusing Hamilton cycle (visits all vertices) with Euler circuit (traverses all edges)
  **Correction**: Hamilton = all vertices once; Euler = all edges once

# Common Confusions

- **Confusion**: Thinking every graph with enough edges must be Hamiltonian
  **Clarification**: Hamiltonicity is not determined by edge count alone; no simple characterization exists

# Source Reference

Chapter I: Fundamentals, Section I.3, pages 22-24; Theorem 11, page 24.

# Verification Notes

- Definition source: Direct from p. 23
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
