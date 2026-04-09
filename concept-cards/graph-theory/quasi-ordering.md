---
concept: Quasi-Ordering
slug: quasi-ordering
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 326
section: "12.1 Well-quasi-ordering"
extraction_confidence: high
aliases:
  - "quasi-order"
  - "preorder"
prerequisites:
  - graph
extends: []
related:
  - well-quasi-ordering
contrasts_with: []
answers_questions:
  - "What is a quasi-ordering?"
---

# Quick Definition
A quasi-ordering is a reflexive and transitive relation. It generalizes partial orderings by not requiring antisymmetry.

# Core Definition
A reflexive and transitive relation is called a *quasi-ordering* (Diestel, p. 326).

# Prerequisites
- **Graph** — Quasi-orderings are used to compare graphs

# Key Properties
1. Reflexive: x <= x for all x
2. Transitive: x <= y and y <= z implies x <= z
3. Not necessarily antisymmetric: x <= y and y <= x does not imply x = y

# Context & Application
Quasi-orderings arise naturally in graph theory: the minor relation, the subgraph relation, and the topological minor relation are all quasi-orderings on graphs.

# Relationships
## Enables
- **Well-quasi-ordering** — A quasi-ordering with an additional finiteness condition

# Source Reference
Chapter 12, Section 12.1, page 326.

# Verification Notes
- Definition from p. 326
- Confidence: HIGH — explicit definition
