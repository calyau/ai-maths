---
concept: Ray
slug: ray
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 206
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "one-way infinite path"
prerequisites:
  - graph
  - infinite-graph
extends: []
related:
  - double-ray
  - tail-of-a-ray
  - end-of-a-graph
  - comb
contrasts_with:
  - double-ray
answers_questions:
  - "What is a ray in graph theory?"
---

# Quick Definition
A ray is a one-way infinite path: an infinite graph with vertices x_0, x_1, x_2, ... and edges x_0x_1, x_1x_2, x_2x_3, .... Up to isomorphism, there is only one ray.

# Core Definition
An infinite graph (V, E) of the form V = {x_0, x_1, x_2, ...}, E = {x_0x_1, x_1x_2, x_2x_3, ...}, where the x_n are assumed to be distinct, is called a *ray* (Diestel, p. 206). In the context of infinite graphs, finite paths, rays, and double rays are all called *paths*.

# Prerequisites
- **Graph** — A ray is a type of graph
- **Infinite graph** — Rays are infinite graphs

# Key Properties
1. Up to isomorphism, there is exactly one ray
2. A ray has one vertex of degree 1 (its starting vertex) and all others have degree 2
3. Every ray is locally finite
4. The subrays of a ray are its tails
5. Rays are the fundamental objects whose equivalence classes define ends

# Construction / Recognition
## To Construct a Ray
1. Start with vertex x_0
2. Add vertex x_1 and edge x_0x_1
3. Continue inductively: add x_{n+1} and edge x_nx_{n+1}

# Context & Application
Rays are the most basic infinite paths and play a role in infinite graph theory analogous to that of paths in finite graph theory. They are central to the definition of ends and to the topological study of infinite graphs.

# Examples
**Example 1** (p. 206): The graph with V = {x_0, x_1, x_2, ...} and E = {x_0x_1, x_1x_2, ...} is the standard ray.

# Relationships
## Enables
- **End of a graph** — defined via equivalence classes of rays
- **Tail of a ray** — subrays of a ray
- **Comb** — built from a ray and disjoint paths

## Contrasts With
- **Double ray** — infinite in both directions

# Common Errors
- **Error**: Confusing a ray with a path
  **Correction**: In infinite graph theory, "path" includes finite paths, rays, and double rays

# Common Confusions
- **Confusion**: Thinking two rays in a graph must be equivalent
  **Clarification**: Rays are equivalent only if they cannot be separated by finite vertex sets

# Source Reference
Chapter 8, Section 8.1, page 206.

# Verification Notes
- Definition directly from p. 206
- Confidence: HIGH — explicit formal definition given
