---
concept: Bipartite Graph
slug: bipartite-graph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 26
section: "1.6 Bipartite graphs"

extraction_confidence: high

aliases:
  - "bipartite"
  - "2-partite"

prerequisites:
  - graph
  - adjacent
  - cycle
extends:
  - graph
related:
  - r-partite-graph
  - complete-multipartite-graph
  - odd-cycle
contrasts_with: []

answers_questions:
  - "What is a bipartite graph?"
  - "How do I recognize a bipartite graph?"
---

# Quick Definition
A graph is bipartite if its vertex set can be partitioned into two classes such that every edge connects vertices in different classes. Equivalently, a graph is bipartite if and only if it contains no odd cycle.

# Core Definition
A graph G = (V, E) is called 2-partite (bipartite) if V admits a partition into 2 classes such that every edge has its ends in different classes: vertices in the same partition class must not be adjacent (Diestel, p. 17).

Proposition 1.6.1: A graph is bipartite if and only if it contains no odd cycle (Diestel, p. 17).

# Prerequisites
- **Graph** — bipartiteness is a graph property
- **Adjacent** — partition classes must contain no adjacent vertices
- **Cycle** — characterized by absence of odd cycles

# Key Properties
1. A graph is bipartite iff it contains no odd cycle (Proposition 1.6.1)
2. Every tree is bipartite
3. Even cycles are bipartite; odd cycles are not
4. Every subgraph of a bipartite graph is bipartite

# Construction / Recognition
## To Test Bipartiteness
1. Find a spanning tree T with root r
2. Partition vertices into two classes based on whether their distance from r is even or odd
3. Check that no edge connects two vertices in the same class
4. If no such edge exists, G is bipartite; otherwise, G contains an odd cycle

# Context & Application
Bipartite graphs model many natural problems (matching, scheduling). The bipartition characterization by odd cycles is used throughout graph theory.

# Examples
**Example** (p. 17): Fig. 1.6.1 shows two 3-partite graphs (which are also bipartite).

# Relationships
## Builds Upon
- **graph**, **adjacent**, **cycle**

## Enables
- Matching theory (Chapter 2)

## Related
- **r-partite-graph** — bipartite is the case r = 2
- **odd-cycle** — absence characterizes bipartiteness

# Common Errors
- **Error**: Concluding a graph is bipartite because it has no triangle
  **Correction**: The graph must have no odd cycle of any length, not just triangles

# Source Reference
Chapter 1: The Basics, Section 1.6, pages 17-18 (pdf pp. 27-28). Proposition 1.6.1.

# Verification Notes
- Direct from pp. 17-18
- Confidence: HIGH
