---
concept: Travelling Salesman Problem
slug: travelling-salesman-problem
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 300
section: null
extraction_confidence: high
aliases:
  - "TSP"
prerequisites:
  - hamilton-cycle
extends:
  - hamilton-cycle
related:
  - npc-hamiltonicity
contrasts_with: []
answers_questions:
  - "What is the travelling salesman problem?"
---

# Quick Definition
The travelling salesman problem (TSP) asks for a minimum-weight Hamilton cycle in a weighted graph: a salesman must visit all cities exactly once and return home, minimizing total travel distance.

# Core Definition
The **travelling salesman problem** asks: given a weighted graph, find a Hamilton cycle of minimum total weight. This is a weighted generalization of the Hamilton cycle existence problem. Much of the motivation for considering Hamilton cycles comes from variations of this algorithmic problem (Diestel, p. 300, notes).

# Prerequisites
- **Hamilton cycle** — TSP seeks a minimum-weight one

# Key Properties
1. NP-hard optimization problem
2. One of the most-studied problems in combinatorial optimization
3. The decision version (does a Hamilton cycle of weight <= W exist?) is NP-complete
4. Many heuristic and approximation algorithms exist
5. Historical origin: W.R. Hamilton's 1857 game on the dodecahedron

# Context & Application
The TSP is mentioned in the chapter notes as the primary practical motivation for studying Hamilton cycles. What began as a mathematical puzzle became a fundamental problem in operations research and theoretical computer science.

# Examples
**Example**: A salesman must visit n cities, each pair connected by a road with a distance. The TSP asks for the shortest route visiting all cities exactly once and returning home.

# Relationships
## Builds Upon
- **Hamilton cycle** — TSP optimizes over Hamilton cycles

## Related
- **NP-completeness of Hamiltonicity** — TSP is NP-hard

# Source Reference
Chapter 10, notes, p. 300 (pdf p. 300).

# Verification Notes
- From chapter notes, p. 300
- Confidence: HIGH — explicitly mentioned
