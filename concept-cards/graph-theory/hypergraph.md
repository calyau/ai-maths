---
concept: Hypergraph
slug: hypergraph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 38
section: "1.10 Other notions of graphs"

extraction_confidence: high

aliases: []

prerequisites:
  - graph
extends:
  - graph
related:
  - multigraph
contrasts_with:
  - graph

answers_questions:
  - "What is a hypergraph?"
---

# Quick Definition
A hypergraph is a pair (V, E) where E consists of non-empty subsets of V of any cardinality (not just 2-element subsets). Graphs are special hypergraphs.

# Core Definition
A hypergraph is a pair (V, E) of disjoint sets, where the elements of E are non-empty subsets (of any cardinality) of V. Thus, graphs are special hypergraphs (Diestel, p. 28).

# Prerequisites
- **Graph** — a hypergraph generalizes a graph

# Key Properties
1. Edges (called hyperedges) can connect any number of vertices
2. Ordinary graphs are hypergraphs where every edge has exactly 2 elements
3. A k-uniform hypergraph has all edges of size k

# Relationships
## Builds Upon
- **graph**

## Contrasts With
- **graph** — graph edges connect exactly 2 vertices

# Source Reference
Chapter 1: The Basics, Section 1.10, page 28 (pdf p. 38).

# Verification Notes
- Direct from p. 28
- Confidence: HIGH
