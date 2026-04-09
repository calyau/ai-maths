---
concept: Unmatched Vertex
slug: unmatched-vertex
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 43
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "unsaturated vertex"
  - "M-unsaturated vertex"
  - "free vertex"
prerequisites:
  - matching
extends:
  - matching
related:
  - matched-vertex
  - m-augmenting-path
contrasts_with:
  - matched-vertex
answers_questions:
  - "What is an unmatched vertex?"
---

# Quick Definition
A vertex is unmatched (or unsaturated, or free) with respect to a matching M if it is not incident with any edge of M.

# Core Definition
Given a matching M in a graph G = (V, E), vertices not incident with any edge of M are called **unmatched** (Diestel, p. 43).

# Prerequisites
- **Matching** — unmatched status is defined relative to a specific matching

# Key Properties
1. An unmatched vertex has no edge of M incident to it
2. The number of unmatched vertices equals |V| - 2|M|
3. A matching is a 1-factor (perfect matching) if and only if there are no unmatched vertices
4. Augmenting paths start and end at unmatched vertices

# Construction / Recognition
## To Identify Unmatched Vertices
1. Given a matching M in G = (V, E)
2. For each vertex v in V, check whether any edge of M is incident with v
3. If no edge of M touches v, then v is unmatched

# Context & Application
Unmatched vertices are the starting and ending points for augmenting paths. The existence of an augmenting path (which connects two unmatched vertices) means the current matching is not maximum. Finding a maximum matching is equivalent to minimizing the number of unmatched vertices.

# Examples
**Example** (p. 44, Fig. 2.1.1): The unmatched vertices a0 in A and bk in B are the endpoints of the augmenting path P.

# Relationships
## Builds Upon
- **Matching** — defines unmatched status

## Enables
- **M-augmenting path** — connects two unmatched vertices

## Contrasts With
- **Matched vertex** — a vertex incident with an edge of M

# Common Errors
- **Error**: Assuming an unmatched vertex has no edges in the graph
  **Correction**: Unmatched means no edge of M is incident; the vertex may still have edges in E \ M

# Common Confusions
- **Confusion**: Thinking a vertex is permanently unmatched
  **Clarification**: A vertex unmatched by M may be matched by a different matching M'

# Source Reference
Chapter 2, Section 2.1, p. 43 (pdf p. 43).

# Verification Notes
- Definition from p. 43
- Confidence: HIGH — explicitly defined
