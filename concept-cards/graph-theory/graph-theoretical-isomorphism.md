---
concept: Graph-Theoretical Isomorphism
slug: graph-theoretical-isomorphism
category: planar-graphs
subcategory: drawings
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.3 Drawings"
extraction_confidence: high
aliases: []
prerequisites:
  - planar-embedding
  - face-boundary
extends: []
related:
  - combinatorial-isomorphism
  - topological-isomorphism
contrasts_with:
  - combinatorial-isomorphism
  - topological-isomorphism
answers_questions:
  - "What is a graph-theoretical isomorphism between plane graphs?"
---

# Quick Definition
A graph-theoretical isomorphism between plane graphs H and H' is an abstract isomorphism sigma such that sigma maps the set of face boundaries of H onto the set of face boundaries of H'. This is the weakest of the three types of isomorphism for plane graphs.

# Core Definition
sigma is "a graph-theoretical isomorphism of the plane graphs H and H'" if the sets of face boundaries are mapped onto each other: {sigma(H[f]) : f in F} = {H'[f'] : f' in F'} (Diestel, pp. 93-94).

# Prerequisites
- **Planar embedding**, **Face boundary**

# Key Properties
1. Weakest notion -- only requires face boundary sets to match (not individual face-boundary correspondence)
2. Easier to verify than combinatorial or topological isomorphism
3. For 3-connected graphs, equivalent to the other two types (Theorem 4.3.1)

# Relationships
## Contrasts With
- **Combinatorial isomorphism** -- Stronger: preserves individual face-vertex-edge incidence
- **Topological isomorphism** -- Strongest: induced by homeomorphism

# Source Reference
Chapter 4, Section 4.3, pages 93-94. Theorem 4.3.1.

# Verification Notes
- Definition from pp. 93-94
- Confidence: HIGH
