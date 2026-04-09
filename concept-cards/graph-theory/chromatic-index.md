---
concept: Chromatic Index
slug: chromatic-index
category: graph-colouring
subcategory: edge-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.3 Colouring edges"
extraction_confidence: high
aliases:
  - "chi'(G)"
  - "edge-chromatic number"
prerequisites:
  - edge-colouring
extends:
  - edge-colouring
related:
  - vizing-theorem
  - konig-edge-colouring-theorem
  - class-one-class-two
contrasts_with:
  - chromatic-number
answers_questions:
  - "What is the chromatic index of a graph?"
---

# Quick Definition
The chromatic index chi'(G) is the minimum number of colours needed in a proper edge colouring of G. By Vizing's theorem, chi'(G) is always Delta(G) or Delta(G) + 1.

# Core Definition
The chromatic index chi'(G) is the smallest k such that a k-edge-colouring exists (Diestel, p. 112). The fundamental result is Vizing's theorem: Delta(G) <= chi'(G) <= Delta(G) + 1.

# Prerequisites
- **Edge colouring** -- chi'(G) is the minimum for edge colouring

# Key Properties
1. chi'(G) >= Delta(G) (trivially, since edges at a vertex of max degree need distinct colours)
2. chi'(G) <= Delta(G) + 1 (Vizing's theorem)
3. chi'(G) = Delta(G) for bipartite graphs (Konig's theorem)
4. Determines whether G is class 1 (chi' = Delta) or class 2 (chi' = Delta + 1)
5. chi'(G) = chi(L(G))

# Relationships
## Builds Upon
- **Edge colouring**

## Enables
- **Class one/class two** classification
- **List-chromatic index** comparison

## Contrasts With
- **Chromatic number** -- chi can be far from Delta; chi' is always within 1

# Source Reference
Chapter 5, pages 112, 119-120. Sections 5.3.

# Verification Notes
- Definition from p. 112
- Confidence: HIGH
