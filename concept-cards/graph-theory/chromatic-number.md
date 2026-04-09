---
concept: Chromatic Number
slug: chromatic-number
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
  - "chi(G)"
  - "vertex chromatic number"
prerequisites:
  - vertex-colouring
extends:
  - vertex-colouring
related:
  - chromatic-index
  - clique-number
  - colouring-number
  - choice-number
contrasts_with:
  - chromatic-index
  - choice-number
answers_questions:
  - "What is the chromatic number of a graph?"
  - "How does the chromatic number relate to the clique number?"
  - "How do I compute the chromatic number of a graph?"
---

# Quick Definition
The chromatic number chi(G) of a graph G is the smallest integer k such that G has a k-colouring (a proper vertex colouring using k colours).

# Core Definition
"The smallest integer k such that G has a k-colouring, a vertex colouring c: V -> {1, ..., k}. This k is the (vertex-)chromatic number of G; it is denoted by chi(G). A graph G with chi(G) = k is called k-chromatic; if chi(G) <= k, we call G k-colourable" (Diestel, p. 111).

# Prerequisites
- **Vertex colouring** -- chi(G) is the minimum number of colours in a vertex colouring

# Key Properties
1. chi(G) >= omega(G) (clique number is a lower bound)
2. chi(G) <= Delta(G) + 1 (greedy algorithm bound)
3. chi(G) <= Delta(G) unless G is complete or an odd cycle (Brooks' theorem)
4. chi(G) <= col(G) = max{delta(H) : H subgraph of G} + 1
5. chi(G) <= 4 for planar graphs (four colour theorem)
6. chi(G) <= 1/2 + sqrt(2m + 1/4) (Proposition 5.2.1)
7. Graphs of arbitrarily large girth and chromatic number exist (Erdos, Theorem 5.2.5)
8. chi(G) >= |V|/alpha(G)

# Construction / Recognition
## To Bound chi(G) from Above
1. Greedy algorithm: chi(G) <= Delta(G) + 1
2. Better ordering: chi(G) <= col(G) = max_H delta(H) + 1
3. Brooks' theorem: chi(G) <= Delta(G) unless G = K^n or odd cycle
4. For planar graphs: chi(G) <= 4 (or <= 5 with elementary proof)

## To Bound chi(G) from Below
1. Find a large clique: chi(G) >= omega(G)
2. Use |V|/alpha(G) as a lower bound
3. For perfect graphs, chi(G) = omega(G)

# Context & Application
The chromatic number is the central invariant of colouring theory. Determining chi(G) is NP-hard in general. The gap between chi(G) and omega(G) can be arbitrarily large (Erdos's theorem), though for perfect graphs they coincide. Upper bounds come from greedy algorithms and structural results (Brooks, Vizing), while lower bounds typically require finding cliques or using algebraic methods.

# Examples
**Example** (p. 111): chi(K^n) = n (complete graph needs n colours).

**Example** (p. 111): chi(G) = 2 iff G is bipartite (and non-empty).

**Example** (p. 112): chi(C_{2k+1}) = 3 for odd cycles.

**Example** (Theorem 5.2.5): For every k, there exist graphs with girth > k and chi > k.

# Relationships
## Builds Upon
- **Vertex colouring**

## Enables
- **Four colour theorem** -- chi(G) <= 4 for planar G
- **Brooks' theorem** -- chi(G) <= Delta(G) for most G
- **Perfect graph** -- Defined by chi = omega for all induced subgraphs

## Related
- **Clique number** -- omega(G) <= chi(G)
- **Colouring number** -- col(G) upper bounds chi(G)

## Contrasts With
- **Chromatic index** -- chi'(G) for edge colouring
- **Choice number** -- ch(G) for list colouring (ch(G) >= chi(G))

# Common Errors
- **Error**: Assuming chi(G) = omega(G) for all graphs
  **Correction**: This holds only for perfect graphs; in general chi(G) can be much larger than omega(G)

# Common Confusions
- **Confusion**: Thinking high chromatic number requires a large clique
  **Clarification**: By Erdos's theorem, triangle-free graphs can have arbitrarily large chromatic number

# Source Reference
Chapter 5: Colouring, pages 111-118. Sections 5.1-5.2.

# Verification Notes
- Definition from p. 111
- Bounds from Propositions 5.2.1, 5.2.2, Theorems 5.2.4, 5.2.5
- Confidence: HIGH -- central definition of the chapter
