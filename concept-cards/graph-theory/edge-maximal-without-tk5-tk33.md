---
concept: Edge-Maximal Graph Without TK^5 or TK_{3,3}
slug: edge-maximal-without-tk5-tk33
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.4 Planar graphs: Kuratowski's theorem"
extraction_confidence: high
aliases:
  - "Lemma 4.4.4"
prerequisites:
  - planar-graph
  - topological-minor
extends: []
related:
  - kuratowski-theorem
  - edge-maximality-planarity
contrasts_with: []
answers_questions:
  - "What structure do edge-maximal graphs without TK^5 or TK_{3,3} have?"
---

# Quick Definition
Lemma 4.4.4 shows that if G has kappa(G) <= 2 and is edge-maximal without a topological minor from a set of 3-connected graphs X, then G decomposes along a K^2 separator, with both parts edge-maximal.

# Core Definition
**Lemma 4.4.4**: If G has kappa(G) <= 2, is edge-maximal without TK^5 or TK_{3,3}, and G_1, G_2 are proper induced subgraphs with G = G_1 U G_2 and |G_1 intersection G_2| = kappa(G), then G_1 and G_2 are also edge-maximal without such topological minors, and G_1 intersection G_2 = K^2 (Diestel, pp. 99-100).

# Prerequisites
- **Planar graph**, **Topological minor**

# Key Properties
1. The separator must be a K^2 (an edge)
2. Both parts inherit edge-maximality
3. Technical lemma enabling the reduction to the 3-connected case

# Relationships
## Enables
- **Edge-maximality and 3-connectedness** (Lemma 4.4.5)
- **Kuratowski's theorem** -- Part of the proof chain

# Source Reference
Chapter 4, Section 4.4, Lemma 4.4.4, pages 99-100.

# Verification Notes
- Full proof pp. 99-100
- Confidence: HIGH
