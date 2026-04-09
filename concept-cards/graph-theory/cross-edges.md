---
concept: Cross-Edges
slug: cross-edges
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 56
section: "2.4 Tree-packing and arboricity"
extraction_confidence: high
aliases:
  - "partition cross-edges"
prerequisites:
  - graph
extends: []
related:
  - nash-williams-tutte-theorem
  - edge-disjoint-spanning-trees
contrasts_with: []
answers_questions:
  - "What are cross-edges with respect to a vertex partition?"
---

# Quick Definition
Cross-edges of a graph G with respect to a vertex partition P are edges whose endpoints lie in different partition sets.

# Core Definition
With respect to a partition of V(G) into sets, **cross-edges** are edges whose ends lie in different partition sets (Diestel, p. 56).

# Prerequisites
- **Graph** — cross-edges are edges of a graph

# Key Properties
1. Each spanning tree has at least r-1 cross-edges for a partition into r sets
2. k edge-disjoint spanning trees require at least k(r-1) cross-edges (for any partition into r sets)
3. This necessary condition is also sufficient (Nash-Williams-Tutte theorem)

# Context & Application
Cross-edges are the key quantity in the Nash-Williams-Tutte theorem characterizing edge-disjoint spanning trees.

# Examples
**Example** (p. 56): For the partition of V into single vertices, every edge is a cross-edge, giving total cross-edges = ||G||.

# Relationships
## Related
- **Nash-Williams-Tutte theorem** — characterization via cross-edges
- **Edge-disjoint spanning trees**

# Source Reference
Chapter 2, Section 2.4, p. 56 (pdf p. 56).

# Verification Notes
- Definition from p. 56
- Confidence: HIGH — explicitly defined
