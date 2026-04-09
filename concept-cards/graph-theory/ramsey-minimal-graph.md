---
concept: Ramsey-Minimal Graph
slug: ramsey-minimal-graph
category: ramsey-theory
subcategory: graph-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 267
section: "9.2 Ramsey numbers"
extraction_confidence: high
aliases:
  - "Ramsey minimal"
prerequisites:
  - graph-ramsey-number
  - monochromatic-subgraph
related:
  - ramsey-number-bounded-degree
answers_questions:
  - "What is a Ramsey-minimal graph?"
---

# Quick Definition
A graph G is Ramsey-minimal for H if G is minimal (w.r.t. subgraph relation) with the property that every 2-colouring of its edges yields a monochromatic copy of H.

# Core Definition
Given a graph H, a graph G is **Ramsey-minimal** for H if G is minimal with the property that every 2-colouring of E(G) yields a monochromatic copy of H. That is, no proper subgraph of G has this property.

**Proposition 9.2.3**: If T is a tree but not a star, then infinitely many graphs are Ramsey-minimal for T. (Diestel, pp. 257-258)

# Prerequisites
- **Graph Ramsey number** — Ramsey-minimal graphs exist by Ramsey's theorem
- **Monochromatic subgraph** — The property defining Ramsey-minimality

# Key Properties
1. Removing any edge from G allows a 2-colouring without monochromatic H
2. Not unique for most H
3. For trees that are not stars: infinitely many Ramsey-minimal graphs exist

# Relationships
## Builds Upon
- **Graph Ramsey number**

# Source Reference
Chapter 9, Section 9.2, pages 257-258 (pdf pages 267-268). Proposition 9.2.3.

# Verification Notes
- Confidence: HIGH — explicitly defined with a result about trees
