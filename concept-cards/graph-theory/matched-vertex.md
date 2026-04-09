---
concept: Matched Vertex
slug: matched-vertex
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
  - "saturated vertex"
  - "M-saturated vertex"
prerequisites:
  - matching
extends:
  - matching
related:
  - unmatched-vertex
  - m-augmenting-path
contrasts_with:
  - unmatched-vertex
answers_questions:
  - "What is a matched vertex?"
  - "What does it mean for a vertex to be saturated by a matching?"
---

# Quick Definition
A vertex is matched (or saturated) by a matching M if it is incident with an edge in M. A vertex not incident with any edge of M is unmatched.

# Core Definition
Given a matching M in a graph G = (V, E), the vertices incident with edges of M are called **matched** (by M). Vertices not incident with any edge of M are **unmatched** (Diestel, p. 43).

# Prerequisites
- **Matching** — matched/unmatched status is defined relative to a matching M

# Key Properties
1. A matched vertex is incident with exactly one edge of M (since M is a matching)
2. Every edge of M contributes exactly two matched vertices
3. The number of matched vertices equals 2|M|
4. Whether a vertex is matched depends on the particular matching M under consideration

# Construction / Recognition
## To Determine if a Vertex is Matched
1. Given a matching M and a vertex v
2. Check if any edge in M is incident with v
3. If yes, v is matched; if no, v is unmatched

# Context & Application
The distinction between matched and unmatched vertices is fundamental to matching theory. Augmenting paths begin and end at unmatched vertices, and the goal of maximum matching is to minimize the number of unmatched vertices.

# Examples
**Example** (p. 44, Fig. 2.1.1): In the depicted bipartite graph, bold edges form the matching M. Vertices at the endpoints of bold edges are matched; the remaining vertices are unmatched. The augmenting path P starts and ends at unmatched vertices.

# Relationships
## Builds Upon
- **Matching** — defines the context for matched/unmatched status

## Enables
- **M-augmenting path** — starts and ends at unmatched vertices
- **Maximum matching** — minimizes unmatched vertices

## Contrasts With
- **Unmatched vertex** — a vertex not incident with any edge of M

# Common Errors
- **Error**: Assuming a vertex can be matched by two edges simultaneously
  **Correction**: Since M is a matching (independent edges), each matched vertex is incident with exactly one edge of M

# Common Confusions
- **Confusion**: Thinking "matched" is an absolute property of a vertex
  **Clarification**: Whether a vertex is matched depends on the specific matching M; a vertex matched by one matching may be unmatched by another

# Source Reference
Chapter 2, Section 2.1, p. 43 (pdf p. 43).

# Verification Notes
- Definition directly from p. 43
- Confidence: HIGH — explicitly defined terms
