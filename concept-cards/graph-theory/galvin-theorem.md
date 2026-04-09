---
concept: "Galvin's Theorem"
slug: galvin-theorem
category: graph-colouring
subcategory: list-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.4 List colouring"
extraction_confidence: high
aliases:
  - "Theorem 5.4.4"
  - "Galvin 1995"
prerequisites:
  - list-chromatic-index
  - konig-edge-colouring-theorem
  - kernel
extends:
  - konig-edge-colouring-theorem
related:
  - list-colouring-conjecture
contrasts_with: []
answers_questions:
  - "Do bipartite graphs satisfy ch' = chi'?"
---

# Quick Definition
Galvin's theorem proves the List Colouring Conjecture for bipartite graphs: every bipartite graph G satisfies ch'(G) = chi'(G) = Delta(G).

# Core Definition
**Theorem 5.4.4** (Galvin 1995): "Every bipartite graph G satisfies ch'(G) = chi'(G)" (Diestel, p. 125).

# Prerequisites
- **List-chromatic index** -- The theorem determines ch'
- **Konig's edge colouring theorem** -- chi'(G) = Delta(G) for bipartite G
- **Kernel** -- The proof uses kernels in orientations of the line graph

# Key Properties
1. ch'(G) = chi'(G) = Delta(G) for bipartite G
2. Proof strategy: orient the line graph using a Delta-edge-colouring, then apply Lemma 5.4.3
3. The orientation uses the edge colouring to define preferences
4. The stable marriage theorem ensures every induced subgraph has a kernel

# Context & Application
Galvin's theorem is one of the most elegant results in list colouring theory. It confirms the List Colouring Conjecture for bipartite graphs using a surprising connection between orientations, kernels, and stable matchings.

# Relationships
## Builds Upon
- **Konig's theorem**, **Kernel concept**, **Stable marriage theorem**

## Related
- **List Colouring Conjecture** -- Galvin proves the bipartite case

# Source Reference
Chapter 5, Section 5.4, Theorem 5.4.4, pages 125-126.

# Verification Notes
- Full proof given pp. 125-126
- Confidence: HIGH -- named theorem with complete proof
