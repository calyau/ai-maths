---
concept: Topological Isomorphism
slug: topological-isomorphism
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
  - plane-graph
extends: []
related:
  - combinatorial-isomorphism
  - graph-theoretical-isomorphism
  - equivalent-embeddings
contrasts_with:
  - combinatorial-isomorphism
  - graph-theoretical-isomorphism
answers_questions:
  - "What is a topological isomorphism between plane graphs?"
  - "When are two plane graphs topologically the same?"
---

# Quick Definition
A topological isomorphism between two plane graphs H and H' is an abstract isomorphism induced by a homeomorphism of the 2-sphere S^2 to itself.

# Core Definition
An isomorphism sigma between plane graphs H and H' is a topological isomorphism "if there exists a homeomorphism phi: S^2 -> S^2 such that psi := pi o phi o pi^{-1} induces sigma on V U E" (Diestel, p. 93), where pi is a fixed stereographic projection from S^2 to R^2.

# Prerequisites
- **Planar embedding** -- Applies to plane graph drawings
- **Plane graph** -- The objects being compared

# Key Properties
1. Strongest notion of isomorphism for plane graphs
2. Every topological isomorphism is also combinatorial
3. For 2-connected plane graphs, every combinatorial isomorphism is topological (Theorem 4.3.1)
4. Works on S^2 to avoid special status for the outer face

# Context & Application
Topological isomorphism is the strongest of three criteria Diestel defines for comparing plane graphs. For 2-connected graphs, it coincides with the weaker combinatorial and graph-theoretical isomorphisms (Theorem 4.3.1), showing that the simpler criteria suffice.

# Relationships
## Enables
- **Equivalent embeddings** -- Defined via topological isomorphism

## Contrasts With
- **Combinatorial isomorphism** -- Weaker: preserves incidence but not induced by a homeomorphism
- **Graph-theoretical isomorphism** -- Weakest: only preserves face boundary structure

# Source Reference
Chapter 4, Section 4.3 "Drawings," pages 93-94. Theorem 4.3.1.

# Verification Notes
- Definition adapted from p. 93
- Confidence: HIGH -- explicit definition with technical details
