---
concept: Edge Colouring
slug: edge-colouring
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
aliases:
  - "edge coloring"
  - "k-edge-colouring"
prerequisites:
  - vertex-colouring
extends: []
related:
  - chromatic-index
  - vizing-theorem
  - konig-edge-colouring-theorem
contrasts_with:
  - vertex-colouring
answers_questions:
  - "What is an edge colouring?"
  - "What distinguishes vertex colouring from edge colouring?"
---

# Quick Definition
An edge colouring of G = (V, E) is a map c: E -> S such that c(e) != c(f) for any two adjacent edges (edges sharing an endpoint). The minimum number of colours needed is the chromatic index chi'(G).

# Core Definition
"An edge colouring of G = (V, E) is a map c: E -> S with c(e) != c(f) for any adjacent edges e, f. The smallest integer k for which a k-edge-colouring exists, i.e. an edge colouring c: E -> {1, ..., k}, is the edge-chromatic number, or chromatic index, of G; it is denoted by chi'(G)" (Diestel, p. 112).

# Prerequisites
- **Vertex colouring** -- Edge colouring is a parallel concept for edges

# Key Properties
1. Every edge colouring of G is a vertex colouring of L(G), and vice versa
2. chi'(G) = chi(L(G)), where L(G) is the line graph
3. chi'(G) is always Delta(G) or Delta(G) + 1 (Vizing's theorem)
4. For bipartite graphs, chi'(G) = Delta(G) (Konig's theorem)

# Context & Application
Edge colouring is the special case of vertex colouring applied to line graphs. Despite this relationship, edge colouring is more tractable: the chromatic index is always within 1 of the trivial lower bound Delta(G), a much tighter bound than exists for vertex colouring.

# Relationships
## Contrasts With
- **Vertex colouring** -- Colours vertices vs edges; chi can be far from Delta, but chi' is within 1

## Enables
- **Chromatic index** -- The main invariant of edge colouring
- **Vizing's theorem** -- chi'(G) in {Delta, Delta + 1}

# Source Reference
Chapter 5, page 112.

# Verification Notes
- Definition quoted from p. 112
- Confidence: HIGH -- explicit definition
