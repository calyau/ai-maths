---
concept: Total Chromatic Number
slug: total-chromatic-number
category: graph-colouring
subcategory: edge-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "Exercises"
extraction_confidence: medium
aliases:
  - "chi_T(G)"
  - "total colouring"
prerequisites:
  - vertex-colouring
  - edge-colouring
extends: []
related:
  - chromatic-number
  - chromatic-index
  - list-colouring-conjecture
contrasts_with: []
answers_questions:
  - "What is the total chromatic number?"
  - "What is the total colouring conjecture?"
---

# Quick Definition
The total chromatic number chi_T(G) is the least number of colours needed to colour both vertices and edges simultaneously so that adjacent or incident elements get different colours. The total colouring conjecture asserts chi_T(G) <= Delta(G) + 2.

# Core Definition
"The total chromatic number chi_T(G) of a graph G = (V,E) is the least number of colours needed to colour the vertices and edges of G simultaneously so that any adjacent or incident elements of V U E are coloured differently" (Diestel, p. 136, Exercise 29).

# Prerequisites
- **Vertex colouring** and **Edge colouring** -- Combines both

# Key Properties
1. chi_T(G) >= Delta(G) + 1 (trivially)
2. Total colouring conjecture: chi_T(G) <= Delta(G) + 2
3. Conjecture proposed by Vizing and Behzad (~1965)

# Relationships
## Related
- **Chromatic number** and **Chromatic index** -- Both contribute
- **List colouring conjecture** -- Related via Exercise 29

# Source Reference
Chapter 5, Exercise 29, page 136.

# Verification Notes
- Exercise definition
- Confidence: MEDIUM
