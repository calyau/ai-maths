---
concept: Choice Number
slug: choice-number
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
  - "ch(G)"
  - "list-chromatic number"
  - "choosability"
prerequisites:
  - list-colouring
extends:
  - list-colouring
related:
  - chromatic-number
  - list-chromatic-index
contrasts_with:
  - chromatic-number
answers_questions:
  - "What is the choice number of a graph?"
  - "How does choosability relate to the chromatic number?"
---

# Quick Definition
The choice number ch(G) is the minimum k such that G is k-choosable (can be properly coloured from any lists of size k). Always ch(G) >= chi(G).

# Core Definition
"The least integer k for which G is k-choosable is the list-chromatic number, or choice number ch(G) of G" (Diestel, p. 121).

# Prerequisites
- **List colouring** -- ch(G) is the minimum k for list colourability

# Key Properties
1. ch(G) >= chi(G) for all graphs G
2. ch(G) <= col(G) (the colouring number upper bound holds for ch too)
3. ch(G) can be much larger than chi(G) (e.g., K_{n,n} has chi = 2 but ch grows)
4. Large average degree forces large ch(G) (Theorem 5.4.1, Alon 1993)
5. ch(G) <= 5 for planar graphs (Thomassen)

# Context & Application
The choice number captures a stronger form of colourability. While chi captures the minimum colours when all vertices have the same options, ch handles the worst case of heterogeneous constraints. The choice number is better behaved with respect to structural graph invariants (like minimum degree) than chi.

# Relationships
## Builds Upon
- **List colouring**

## Contrasts With
- **Chromatic number** -- chi(G) <= ch(G); chi uses uniform lists, ch handles all lists

## Related
- **List-chromatic index** -- The edge colouring analogue

# Source Reference
Chapter 5, Section 5.4, page 121.

# Verification Notes
- Definition from p. 121
- Confidence: HIGH -- explicit definition
