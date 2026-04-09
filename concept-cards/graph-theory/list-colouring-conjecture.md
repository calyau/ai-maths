---
concept: List Colouring Conjecture
slug: list-colouring-conjecture
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
  - "edge list colouring conjecture"
prerequisites:
  - list-chromatic-index
  - chromatic-index
extends: []
related:
  - galvin-theorem
  - vizing-theorem
contrasts_with: []
answers_questions:
  - "Is ch'(G) always equal to chi'(G)?"
---

# Quick Definition
The List Colouring Conjecture asserts that ch'(G) = chi'(G) for every graph G -- that is, the list-chromatic index always equals the ordinary chromatic index.

# Core Definition
"List Colouring Conjecture. Every graph G satisfies ch'(G) = chi'(G)" (Diestel, p. 124).

# Prerequisites
- **List-chromatic index** and **Chromatic index**

# Key Properties
1. Proved for bipartite graphs (Galvin's theorem)
2. Asymptotically correct: ch'(G) <= (1 + epsilon)Delta(G) for large Delta (Kahn 1994)
3. Would imply ch'(G) in {Delta, Delta + 1} for all G
4. Open in general (as of the text)

# Context & Application
This conjecture suggests that for edge colouring, the list version is no harder than the ordinary version -- a striking contrast with vertex colouring where chi and ch can differ widely.

# Relationships
## Related
- **Galvin's theorem** -- Proves the bipartite case

# Source Reference
Chapter 5, Section 5.4, page 124.

# Verification Notes
- Conjecture stated on p. 124
- Confidence: HIGH -- explicitly stated conjecture
