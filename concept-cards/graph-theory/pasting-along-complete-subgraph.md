---
concept: Pasting Along a Complete Subgraph
slug: pasting-along-complete-subgraph
category: graph-colouring
subcategory: perfect-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.5 Perfect graphs"
extraction_confidence: high
aliases:
  - "clique-sum"
prerequisites:
  - graph
extends: []
related:
  - chordal-graph
  - perfect-graph
contrasts_with: []
answers_questions:
  - "What does it mean to paste graphs along a complete subgraph?"
---

# Quick Definition
Pasting G_1 and G_2 along S means forming G = G_1 U G_2 where G_1 intersection G_2 = S and S is a complete subgraph (a clique). Used to characterize chordal graphs.

# Core Definition
"If G is a graph with induced subgraphs G_1, G_2 and S, such that G = G_1 U G_2 and S = G_1 intersection G_2, we say that G arises from G_1 and G_2 by pasting these graphs together along S" (Diestel, p. 127).

# Prerequisites
- **Graph**

# Key Properties
1. G_1 and G_2 share exactly the vertices and edges of S
2. S must be a complete subgraph for the chordal characterization
3. Preserves chordality when both G_1 and G_2 are chordal
4. Preserves perfection when both G_1 and G_2 are perfect and S is complete

# Context & Application
Pasting along complete subgraphs is the recursive construction for chordal graphs (Proposition 5.5.1) and provides the key step in proving chordal graphs are perfect.

# Relationships
## Enables
- **Chordal graph** -- Characterized by pasting construction
- **Perfect graph** -- Perfection preserved under pasting along cliques

# Source Reference
Chapter 5, Section 5.5, page 127. Proposition 5.5.1.

# Verification Notes
- Definition from p. 127
- Confidence: HIGH
