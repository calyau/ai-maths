---
concept: Graph Minor
slug: graph-minor
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 325
section: null
extraction_confidence: high
aliases:
  - "minor"
  - "H minor"
prerequisites:
  - graph
extends: []
related:
  - tree-width
  - graph-minor-theorem
  - forbidden-minor
  - minor-closed-property
contrasts_with: []
answers_questions:
  - "What is a graph minor?"
---

# Quick Definition
H is a minor of G (written H <= G) if H can be obtained from G by deleting vertices, deleting edges, and contracting edges. Equivalently, G contains vertex-disjoint connected subgraphs (branch sets) corresponding to V(H), with edges between branch sets corresponding to edges of H.

# Core Definition
A graph H is a *minor* of G if H can be obtained from a subgraph of G by contracting edges. The minor relation is a quasi-ordering on the class of all graphs. In every infinite set of graphs, there are two such that one is a minor of the other (the graph minor theorem). The minor relation plays a central role in structural graph theory (Diestel, p. 325).

# Prerequisites
- **Graph** — Minors are defined for graphs

# Key Properties
1. The minor relation is reflexive and transitive (a quasi-ordering)
2. If H <= G then tw(H) <= tw(G) (Proposition 12.3.6)
3. Every minor-closed property can be characterized by forbidden minors (Proposition 12.4.1)
4. Finite graphs are WQO by the minor relation (graph minor theorem, Theorem 12.5.1)

# Context & Application
Graph minors are the central ordering concept in Robertson-Seymour theory. The minor relation is weaker than the subgraph relation but stronger than having a minor model (which allows non-connected branch sets).

# Relationships
## Enables
- **Graph minor theorem** — Finite graphs are WQO under minors
- **Forbidden minor characterizations** — Every minor-closed property has finitely many forbidden minors
- **Tree-width** — Minor-monotone parameter

# Source Reference
Chapter 12, introduction and throughout, page 325.

# Verification Notes
- Concept from p. 325 and Chapter 1
- Confidence: HIGH — central concept of the chapter
