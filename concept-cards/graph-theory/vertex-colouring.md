---
concept: Vertex Colouring
slug: vertex-colouring
category: graph-colouring
subcategory: vertex-colouring
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
  - "graph colouring"
  - "proper colouring"
  - "k-colouring"
  - "vertex coloring"
prerequisites:
  - graph
extends: []
related:
  - chromatic-number
  - colour-class
  - edge-colouring
  - list-colouring
contrasts_with:
  - edge-colouring
  - list-colouring
answers_questions:
  - "What is a graph colouring?"
  - "What distinguishes vertex colouring from edge colouring?"
---

# Quick Definition
A vertex colouring of a graph G = (V, E) is a map c: V -> S such that c(v) != c(w) whenever v and w are adjacent. The smallest k for which a k-colouring exists is the chromatic number chi(G).

# Core Definition
"A vertex colouring of a graph G = (V, E) is a map c: V -> S such that c(v) != c(w) whenever v and w are adjacent. The elements of the set S are called the available colours" (Diestel, p. 111). A k-colouring is a vertex colouring c: V -> {1, ..., k}. A graph G with chi(G) = k is called k-chromatic; if chi(G) <= k, it is k-colourable.

# Prerequisites
- **Graph** -- Colouring is a property of graphs

# Key Properties
1. A k-colouring is a partition of V into k independent sets (colour classes)
2. The non-trivial 2-colourable graphs are precisely the bipartite graphs
3. Every graph G satisfies chi(G) <= Delta(G) + 1 (greedy bound)
4. chi(G) >= omega(G) (clique number provides a lower bound)
5. chi(G) >= |V|/alpha(G) (independence number provides a bound)

# Construction / Recognition
## To Find a Vertex Colouring
1. Apply the greedy algorithm: enumerate vertices, assign each the smallest available colour
2. This uses at most Delta(G) + 1 colours
3. With a good vertex ordering, the colouring number col(G) may be achieved
4. Finding the minimum number of colours (chi(G)) is NP-hard in general

# Context & Application
Vertex colouring is one of the most studied problems in graph theory. It arises from map colouring (the four colour problem), scheduling (committee meetings, timetabling), and resource allocation. The chromatic number captures the minimum resources needed when conflicting items cannot share a resource.

# Examples
**Example** (p. 111, Fig. 5.0.1): A graph with a 4-colouring c: V -> {1, 2, 3, 4} is shown.

**Example** (p. 111): The complete graph K^k requires exactly k colours: chi(K^k) = k.

**Example** (p. 111): Bipartite graphs are exactly the 2-colourable graphs.

# Relationships
## Builds Upon
- **Graph** -- Colouring is defined for graphs

## Enables
- **Chromatic number** -- The minimum k for a k-colouring
- **Four colour theorem** -- chi(G) <= 4 for planar G
- **Brooks' theorem** -- chi(G) <= Delta(G) for most graphs

## Related
- **Colour class** -- The independent sets in a colouring

## Contrasts With
- **Edge colouring** -- Colours edges instead of vertices
- **List colouring** -- Each vertex has its own list of available colours

# Common Errors
- **Error**: Allowing adjacent vertices to share a colour
  **Correction**: A proper colouring requires c(v) != c(w) for every edge vw

# Common Confusions
- **Confusion**: Thinking "colouring" can refer to any assignment of colours
  **Clarification**: In graph theory, "colouring" always means "proper colouring" unless stated otherwise -- adjacent elements must receive different colours

# Source Reference
Chapter 5: Colouring, introductory section, pages 111-112.

# Verification Notes
- Definition directly quoted from p. 111
- Confidence: HIGH -- explicit foundational definition
