---
concept: Path Cover
slug: path-cover
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 60
section: "2.5 Path covers"
extraction_confidence: high
aliases:
  - "directed path cover"
prerequisites:
  - directed-graph
  - path
extends: []
related:
  - gallai-milgram-theorem
  - dilworths-theorem
contrasts_with: []
answers_questions:
  - "What is a path cover?"
---

# Quick Definition
A path cover of a directed graph G is a set of disjoint directed paths that together contain all vertices of G.

# Core Definition
A **path cover** of a directed graph G is a set of disjoint paths in G which together contain all the vertices of G (Diestel, p. 60).

# Prerequisites
- **Directed graph** — path covers are defined for directed graphs in this section
- **Path** — directed paths form the cover

# Key Properties
1. The paths are vertex-disjoint
2. Every vertex belongs to exactly one path
3. A single vertex counts as a trivial path
4. The minimum number of paths in a path cover is at least the maximum antichain size
5. Gallai-Milgram theorem: there exists a path cover with an independent set of representatives

# Construction / Recognition
## To Construct a Path Cover
1. Find disjoint directed paths in G
2. Assign remaining vertices as trivial paths
3. Ensure every vertex is covered exactly once

# Context & Application
Path covers connect directed graph theory to partial order theory via Dilworth's theorem. The number of paths needed to cover all vertices of G equals the maximum antichain size when G is the comparability graph of a partial order.

# Examples
**Example** (p. 60): The minimum path cover problem for a directed graph asks for the fewest directed paths covering all vertices. König's duality (Theorem 2.1.1) is the special case where all paths have length 0 or 1.

# Relationships
## Builds Upon
- **Directed graph**, **path**

## Enables
- **Gallai-Milgram theorem** — path cover with independent representatives
- **Dilworth's theorem** — minimum chain cover = maximum antichain

# Common Errors
- **Error**: Allowing paths to share vertices
  **Correction**: Path cover paths must be vertex-disjoint

# Common Confusions
- **Confusion**: Confusing path cover with edge cover
  **Clarification**: A path cover covers vertices with paths; an edge cover covers vertices with edges

# Source Reference
Chapter 2, Section 2.5, p. 60 (pdf p. 60).

# Verification Notes
- Definition from p. 60
- Confidence: HIGH — explicitly defined
