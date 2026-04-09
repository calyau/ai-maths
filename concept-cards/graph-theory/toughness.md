---
concept: Toughness
slug: toughness
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
aliases:
  - "t-tough"
  - "graph toughness"
prerequisites:
  - graph
  - connectivity
extends: []
related:
  - hamiltonian-graph
  - toughness-conjecture
contrasts_with: []
answers_questions:
  - "What is toughness in graph theory?"
---

# Quick Definition
A graph G is t-tough if for every separator S, the graph G-S has at most |S|/t components. Hamiltonian graphs must be 1-tough.

# Core Definition
A graph G is called **t-tough**, where t > 0 is any real number, if for every separator S the graph G-S has at most |S|/t components (Diestel, p. 288).

# Prerequisites
- **Graph** — toughness is a graph property
- **Connectivity** — toughness relates to separating sets

# Key Properties
1. Hamiltonian graphs are 1-tough (necessary condition)
2. 1-toughness is not sufficient for Hamiltonicity (Exercise 5)
3. Chvatal conjectured that t-toughness for some t forces Hamiltonicity (Toughness Conjecture)
4. The conjecture was disproved for t=2 but remains open in general
5. G^2 of a k-connected graph G is k-tough (Exercise 9)

# Construction / Recognition
## To Check t-Toughness
1. For every separator S of G
2. Count the number of components of G-S
3. Verify: number of components <= |S|/t

# Context & Application
Toughness measures how resistant a graph is to being broken into many components. It is a necessary condition for Hamiltonicity (1-toughness) and the Toughness Conjecture proposes that some constant t suffices.

# Examples
**Example** (Exercise 5): There exist 1-tough non-Hamiltonian graphs, so 1-toughness alone is insufficient.

# Relationships
## Builds Upon
- **Graph**, **connectivity**

## Related
- **Hamiltonian graph** — Hamiltonian implies 1-tough
- **Toughness conjecture** — t-tough for large enough t implies Hamiltonian?

# Common Errors
- **Error**: Thinking 1-tough implies Hamiltonian
  **Correction**: 1-tough is necessary but not sufficient

# Source Reference
Chapter 10, Section 10.1, p. 288 (pdf p. 288).

# Verification Notes
- Definition from p. 288
- Confidence: HIGH — explicitly defined
