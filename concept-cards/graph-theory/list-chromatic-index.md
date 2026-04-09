---
concept: List-Chromatic Index
slug: list-chromatic-index
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
  - "ch'(G)"
prerequisites:
  - list-colouring
  - chromatic-index
extends:
  - list-colouring
related:
  - choice-number
  - list-colouring-conjecture
  - galvin-theorem
contrasts_with: []
answers_questions:
  - "What is the list-chromatic index?"
---

# Quick Definition
The list-chromatic index ch'(G) is the minimum k such that G has an edge colouring from any lists of size k. The List Colouring Conjecture asserts ch'(G) = chi'(G) for all graphs.

# Core Definition
"The least integer k such that G has an edge colouring from any family of lists of size k is the list-chromatic index ch'(G) of G; formally, we just set ch'(G) := ch(L(G))" (Diestel, p. 121).

# Prerequisites
- **List colouring** -- Applied to edges
- **Chromatic index** -- ch'(G) >= chi'(G)

# Key Properties
1. ch'(G) >= chi'(G) for all G
2. ch'(G) = chi'(G) = Delta(G) for bipartite G (Galvin's theorem)
3. The List Colouring Conjecture: ch'(G) = chi'(G) for all G
4. Kahn (1994) proved the conjecture is asymptotically correct

# Relationships
## Related
- **List Colouring Conjecture** -- ch' = chi'?
- **Galvin's theorem** -- Proved for bipartite graphs

# Source Reference
Chapter 5, Section 5.4, page 121.

# Verification Notes
- Definition from p. 121
- Confidence: HIGH -- explicit definition
