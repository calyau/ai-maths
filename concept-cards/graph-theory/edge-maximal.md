---
concept: Edge-Maximal
slug: edge-maximal

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "minimal"
  - "maximal"

prerequisites:
  - graph
  - subgraph
extends: []
related:
  - graph-property
contrasts_with: []

answers_questions:
  - "What does edge-maximal mean?"
  - "What does minimal/maximal mean for graphs?"
---

# Quick Definition
A graph G is edge-maximal with a given property if G has the property but no graph G + xy does, for any non-adjacent vertices x, y. When minimal or maximal is used without specifying an ordering, it refers to the subgraph relation.

# Core Definition
We call G edge-maximal with a given graph property if G itself has the property but no graph G + xy does, for non-adjacent vertices x, y in G. More generally, when we call a graph minimal or maximal with some property but have not specified any particular ordering, we are referring to the subgraph relation (Diestel, p. 4).

# Prerequisites
- **Graph** — edge-maximality is a property of graphs
- **Subgraph** — minimal/maximal refers to the subgraph ordering by default

# Key Properties
1. Edge-maximal: adding any edge destroys the property
2. Minimal (with respect to subgraph relation): removing any vertex or edge destroys the property
3. Maximal: no supergraph has the property

# Context & Application
These concepts are used when studying extremal properties of graphs. For example, trees are minimally connected graphs.

# Relationships
## Builds Upon
- **graph**, **subgraph**

# Source Reference
Chapter 1: The Basics, Section 1.1, page 4 (pdf p. 14).

# Verification Notes
- Direct from p. 4
- Confidence: HIGH
