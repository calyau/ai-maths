---
concept: Degeneracy
slug: degeneracy
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.2 Colouring vertices"
extraction_confidence: high
aliases:
  - "k-degenerate"
prerequisites:
  - graph
extends: []
related:
  - colouring-number
  - chromatic-number
contrasts_with: []
answers_questions:
  - "What is the degeneracy of a graph?"
---

# Quick Definition
The degeneracy of G is col(G) - 1 = max{delta(H) : H subgraph of G}. A graph is k-degenerate if every subgraph has minimum degree at most k.

# Core Definition
The degeneracy equals max{delta(H) | H subgraph of G}, which is col(G) - 1 (Proposition 5.2.2). A graph of large chromatic number must have a subgraph of large minimum degree (Corollary 5.2.3).

# Prerequisites
- **Graph**

# Key Properties
1. col(G) = degeneracy + 1
2. chi(G) <= degeneracy + 1
3. Every graph G has a subgraph with minimum degree >= chi(G) - 1

# Relationships
## Related
- **Colouring number** -- col(G) = degeneracy + 1

# Source Reference
Chapter 5, Section 5.2, Proposition 5.2.2, page 115.

# Verification Notes
- Implicit in Proposition 5.2.2
- Confidence: HIGH
