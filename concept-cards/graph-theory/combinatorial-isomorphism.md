---
concept: Combinatorial Isomorphism
slug: combinatorial-isomorphism
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
  - face
extends: []
related:
  - topological-isomorphism
  - graph-theoretical-isomorphism
  - equivalent-embeddings
contrasts_with:
  - topological-isomorphism
  - graph-theoretical-isomorphism
answers_questions:
  - "What is a combinatorial isomorphism between plane graphs?"
---

# Quick Definition
A combinatorial isomorphism between plane graphs H and H' is an abstract isomorphism that extends to a bijection preserving incidence of vertices, edges, and faces.

# Core Definition
An isomorphism sigma is a "combinatorial isomorphism of the plane graphs H and H' if it can be extended to a bijection sigma: V U E U F -> V' U E' U F' that preserves incidence not only of vertices with edges but also of vertices and edges with faces" (Diestel, p. 93).

# Prerequisites
- **Planar embedding** -- Applies to plane graph drawings
- **Face** -- Must preserve face incidence

# Key Properties
1. Intermediate strength between topological and graph-theoretical isomorphism
2. Maps face boundaries of H to face boundaries of H'
3. For 2-connected plane graphs, equivalent to topological isomorphism (Theorem 4.3.1)
4. Every graph-theoretical isomorphism is combinatorial (Theorem 4.3.1(i))

# Context & Application
This is the practically most useful notion, as it has a purely combinatorial description (no homeomorphism needed) yet coincides with topological isomorphism for 2-connected graphs. Two embeddings of a 2-connected graph are equivalent if and only if they are combinatorially isomorphic.

# Relationships
## Contrasts With
- **Topological isomorphism** -- Stronger (induced by homeomorphism)
- **Graph-theoretical isomorphism** -- Weaker (only face boundary sets must match)

# Source Reference
Chapter 4, Section 4.3, page 93. Theorem 4.3.1.

# Verification Notes
- Definition quoted from p. 93
- Confidence: HIGH -- explicit definition
