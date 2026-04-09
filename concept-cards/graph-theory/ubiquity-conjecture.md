---
concept: Ubiquity Conjecture
slug: ubiquity-conjecture
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 217
section: "8.2 Paths, trees, and ends"
extraction_confidence: high
aliases:
  - "Andreae 2002"
prerequisites:
  - graph-minor
  - locally-finite-graph
extends: []
related:
  - well-quasi-ordering
contrasts_with: []
answers_questions:
  - "What is ubiquity in graph theory?"
---

# Quick Definition
A graph H is ubiquitous with respect to a relation if nH <= G for all n implies aleph_0 H <= G. The ubiquity conjecture (Andreae 2002) states that every locally finite connected graph is ubiquitous with respect to the minor relation.

# Core Definition
A graph H is called *ubiquitous* with respect to a relation <= if nH <= G for all n implies aleph_0 H <= G, where nH denotes n disjoint copies. The *ubiquity conjecture* (Andreae 2002): every locally finite connected graph is ubiquitous with respect to the minor relation (Diestel, p. 217).

# Prerequisites
- **Graph minor** — The relation in the conjecture
- **Locally finite graph** — The hypothesis on H

# Key Properties
1. Rays are ubiquitous (Theorem 8.2.5)
2. Non-ubiquitous graphs exist for the subgraph relation (Exercise 36)
3. Ubiquity is related to well-quasi-ordering

# Source Reference
Chapter 8, Section 8.2, page 217.

# Verification Notes
- Definition from p. 217
- Confidence: HIGH — explicitly stated conjecture
