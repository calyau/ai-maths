---
concept: "Erdos's Theorem (Girth and Chromatic Number)"
slug: erdos-girth-chromatic
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
  - "Theorem 5.2.5"
  - "Erdos 1959"
prerequisites:
  - chromatic-number
extends: []
related:
  - clique-number
contrasts_with: []
answers_questions:
  - "Can triangle-free graphs have large chromatic number?"
  - "Is large chromatic number caused by dense local structure?"
---

# Quick Definition
For every integer k, there exists a graph G with girth g(G) > k and chromatic number chi(G) > k. Thus, large chromatic number can occur without short cycles.

# Core Definition
**Theorem 5.2.5** (Erdos 1959): "For every integer k there exists a graph G with girth g(G) > k and chromatic number chi(G) > k" (Diestel, p. 117).

# Prerequisites
- **Chromatic number** -- The theorem involves chi(G)

# Key Properties
1. High chromatic number can occur purely as a global phenomenon
2. Locally (around each vertex), a graph of large girth looks like a tree (2-colourable)
3. First proved non-constructively using random graphs
4. The proof is given in Chapter 11.2 (random graphs)

# Context & Application
This theorem demolishes the naive intuition that large chromatic number requires dense local structure (like cliques). It shows that chi(G) can be arbitrarily large even when omega(G) = 2 (no triangles), making the gap between chi and omega arbitrarily large.

# Relationships
## Related
- **Clique number** -- omega(G) does not bound chi(G)
- **Perfect graph** -- Perfect graphs are precisely those where chi = omega always holds

# Source Reference
Chapter 5, Section 5.2, Theorem 5.2.5, page 117.

# Verification Notes
- Theorem stated; proof deferred to Chapter 11.2
- Confidence: HIGH -- named classical theorem
