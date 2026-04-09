---
concept: Hamilton Path
slug: hamilton-path
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
  - "Hamiltonian path"
prerequisites:
  - path
  - graph
extends:
  - path
related:
  - hamilton-cycle
  - hamiltonian-graph
contrasts_with: []
answers_questions:
  - "What is a Hamilton path?"
---

# Quick Definition
A Hamilton path is a path in G that contains every vertex of G exactly once.

# Core Definition
A path in G containing every vertex of G is a **Hamilton path** (Diestel, p. 285).

# Prerequisites
- **Path** — a Hamilton path is a spanning path
- **Graph** — defined within a graph

# Key Properties
1. Visits every vertex exactly once but does not return to the start
2. A Hamilton cycle minus one edge gives a Hamilton path
3. A graph with a Hamilton path may not have a Hamilton cycle
4. Corollary 10.2.2 characterizes path-Hamiltonian degree sequences
5. G^3 of a connected graph G has a Hamilton path between any two vertices (Exercise 12)

# Context & Application
Hamilton paths are closely related to Hamilton cycles. A graph with a Hamilton cycle always has a Hamilton path, but the converse is false. Degree sequence conditions for Hamilton paths are given in Corollary 10.2.2.

# Examples
**Example**: Every tournament (complete oriented graph) has a Hamilton path (Exercise 1, p. 299).

# Relationships
## Builds Upon
- **Path** — a Hamilton path is a spanning path

## Related
- **Hamilton cycle** — a Hamilton cycle minus one edge is a Hamilton path
- **Hamiltonian graph** — having a Hamilton path is weaker than being Hamiltonian

# Common Errors
- **Error**: Assuming a Hamilton path implies a Hamilton cycle
  **Correction**: The path need not close into a cycle

# Source Reference
Chapter 10, p. 285 (pdf p. 285).

# Verification Notes
- Definition from p. 285
- Confidence: HIGH — explicitly defined
