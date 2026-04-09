---
concept: Edge-Maximality and 3-Connectedness
slug: edge-maximality-planarity
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
  - "Lemma 4.4.5"
prerequisites:
  - planar-graph
extends: []
related:
  - kuratowski-theorem
  - three-connected-planarity
contrasts_with: []
answers_questions:
  - "Why can the general Kuratowski theorem be reduced to the 3-connected case?"
---

# Quick Definition
If |G| >= 4 and G is edge-maximal with TK^5, TK_{3,3} not subgraphs of G, then G is 3-connected (Lemma 4.4.5). This reduces the general Kuratowski theorem to the 3-connected case.

# Core Definition
**Lemma 4.4.5**: "If |G| >= 4 and G is edge-maximal with TK^5, TK_{3,3} not subgraphs of G, then G is 3-connected" (Diestel, p. 100).

# Prerequisites
- **Planar graph**

# Key Properties
1. Edge-maximal without TK^5 or TK_{3,3} implies 3-connected
2. Uses Lemma 4.4.4 to handle the kappa(G) <= 2 case
3. The 3-connected case is then handled by Lemma 4.4.3
4. Together with 4.4.3, completes the proof of Kuratowski's theorem

# Relationships
## Enables
- **Kuratowski's theorem** -- Reduction to 3-connected case

# Source Reference
Chapter 4, Section 4.4, Lemma 4.4.5, pages 100-101.

# Verification Notes
- Full proof pp. 100-101
- Confidence: HIGH
