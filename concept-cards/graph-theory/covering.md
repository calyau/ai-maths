---
concept: Covering
slug: covering
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 43
section: "2.3 Packing and covering"
extraction_confidence: high
aliases:
  - "graph covering"
  - "vertex covering"
prerequisites:
  - graph
extends: []
related:
  - packing
  - vertex-cover
  - erdos-posa-property
contrasts_with:
  - packing
answers_questions:
  - "What is a covering problem in graph theory?"
---

# Quick Definition
A covering problem asks: given a graph G and a class H of graphs, find the fewest vertices of G that meet (cover) all subgraphs isomorphic to a graph in H.

# Core Definition
The **covering** problem asks how few vertices of G suffice to meet all its subgraphs isomorphic to a graph in a given class H: clearly, we need at least as many vertices for such a cover as the maximum number k of H-graphs that we can pack disjointly into G (Diestel, p. 43).

# Prerequisites
- **Graph** — covering is defined within a graph

# Key Properties
1. A cover is a set of vertices that meets (intersects) every H-subgraph
2. min cover >= max packing (trivially)
3. If min cover <= f(max packing) for some function f independent of G, then H has the Erdos-Posa property
4. For H = {K2}, covering means vertex cover; packing means matching

# Construction / Recognition
## To Find a Minimum Cover
1. Given G and class H
2. Find a set U of vertices such that every H-subgraph contains a vertex from U
3. Minimize |U|

# Context & Application
Covering is the dual of packing. The fundamental question is whether the covering number can be bounded by a function of the packing number, independently of the graph. This is the Erdos-Posa property, proved for cycles in Theorem 2.3.2.

# Examples
**Example**: For H = {K2}, a cover is a vertex cover (a set of vertices meeting every edge). Konig's theorem says min vertex cover = max matching in bipartite graphs.

# Relationships
## Builds Upon
- **Graph**

## Enables
- **Erdos-Posa property** — packing-covering duality

## Related
- **Vertex cover** — special case for edges
- **Packing** — the dual problem

## Contrasts With
- **Packing** — packing maximizes disjoint copies; covering minimizes vertices meeting all copies

# Common Errors
- **Error**: Confusing covering vertices with covering edges
  **Correction**: In the packing/covering framework, a cover is a vertex set meeting every H-subgraph

# Common Confusions
- **Confusion**: Assuming min cover = max packing always
  **Clarification**: Equality holds in bipartite graphs for H = {K2} (Konig), but not in general

# Source Reference
Chapter 2, p. 43 (pdf p. 43). Section 2.3 for detailed treatment.

# Verification Notes
- Definition from p. 43
- Confidence: HIGH — explicitly defined
