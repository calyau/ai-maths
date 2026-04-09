---
concept: Line Graph and Edge Colouring
slug: line-graph-colouring
category: graph-colouring
subcategory: edge-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: null
extraction_confidence: high
aliases: []
prerequisites:
  - edge-colouring
  - chromatic-index
extends: []
related:
  - vertex-colouring
  - list-chromatic-index
contrasts_with: []
answers_questions:
  - "How does edge colouring relate to vertex colouring of line graphs?"
---

# Quick Definition
Every edge colouring of G is a vertex colouring of its line graph L(G), and vice versa. Hence chi'(G) = chi(L(G)). This reduces edge colouring to vertex colouring of a special class of graphs.

# Core Definition
"Clearly, every edge colouring of G is a vertex colouring of its line graph L(G), and vice versa; in particular, chi'(G) = chi(L(G)). The problem of finding good edge colourings may thus be viewed as a restriction of the more general vertex colouring problem to this special class of graphs" (Diestel, p. 112).

# Prerequisites
- **Edge colouring**, **Chromatic index**

# Key Properties
1. chi'(G) = chi(L(G))
2. ch'(G) = ch(L(G))
3. Edge colouring is vertex colouring restricted to line graphs
4. The tighter bounds for chi' (Vizing's theorem) reflect the structural constraint of being a line graph

# Relationships
## Related
- **Vertex colouring** -- Generalizes edge colouring
- **List-chromatic index** -- ch'(G) = ch(L(G))

# Source Reference
Chapter 5, page 112.

# Verification Notes
- From p. 112
- Confidence: HIGH
