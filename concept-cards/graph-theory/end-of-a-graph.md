---
concept: End of a Graph
slug: end-of-a-graph
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 213
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "end"
  - "graph end"
prerequisites:
  - ray
  - tail-of-a-ray
  - infinite-graph
extends: []
related:
  - end-degree
  - normal-spanning-tree
  - topological-end-space
  - freudenthal-compactification
contrasts_with: []
answers_questions:
  - "What is an end of a graph?"
  - "How are ends defined?"
---

# Quick Definition
An end of a graph G is an equivalence class of rays, where two rays are equivalent if for every finite set S of vertices, both have a tail in the same component of G - S.

# Core Definition
An *end* of a graph G is an equivalence class of rays in G, where two rays are considered equivalent if, for every finite set S of vertices of G, both have a tail in the same component of G - S. This is indeed an equivalence relation: since S is finite, there is exactly one such component for each ray. Two rays are equivalent if and only if they can be linked by infinitely many disjoint paths. The set of ends of G is denoted by Omega(G), and we write G = (V, E, Omega) to express that G has vertex, edge, and end sets V, E, Omega (Diestel, pp. 213-214).

# Prerequisites
- **Ray** — Ends are equivalence classes of rays
- **Tail of a ray** — Equivalence is defined via tails in components
- **Infinite graph** — Only infinite graphs can have ends

# Key Properties
1. Two rays are equivalent iff they can be linked by infinitely many disjoint paths
2. Every end contains exactly one normal ray of a normal spanning tree (Lemma 8.2.3)
3. A locally finite tree can have uncountably many ends (e.g., the binary tree T_2)
4. Ends can be thought of as "points at infinity" to which rays converge
5. The maximum number of disjoint rays in an end is its vertex-degree; for edge-disjoint rays, its edge-degree

# Construction / Recognition
## To Determine Ends
1. Find all rays in the graph
2. For each pair of rays, check if for every finite S, both have tails in the same component of G - S
3. Group equivalent rays into equivalence classes

## For Trees
- Two rays are equivalent iff they share a tail
- For every fixed vertex v, each end contains exactly one ray starting at v

# Context & Application
Ends are perhaps the most important concept unique to infinite graph theory, with no finite counterpart. They capture the "eventual behaviour" of infinite paths and serve as additional limit points in the topological space |G|. Diestel's treatment of ends is central to his approach to infinite graphs.

# Examples
**Example 1** (p. 213): The 2-way infinite ladder has exactly two ends: one on the left, one on the right.

**Example 2** (p. 213): The binary tree T_2 has continuum many ends, corresponding bijectively to infinite 0-1 sequences.

**Example 3** (p. 208): The N x N grid has exactly one end, which is thick.

# Relationships
## Builds Upon
- **Ray** — Ends are equivalence classes of rays

## Enables
- **End degree** — vertex-degree and edge-degree of an end
- **Topological end space** — ends as points in a topological space
- **Freudenthal compactification** — adding ends makes locally finite graphs compact

## Related
- **Normal spanning tree** — each end contains exactly one normal ray

# Common Errors
- **Error**: Confusing ends of a graph with endvertices of an edge
  **Correction**: In infinite graph theory, use "endvertices" for edge endpoints to avoid confusion

# Common Confusions
- **Confusion**: Thinking every graph has exactly one or two ends
  **Clarification**: A graph can have any number of ends, from zero to uncountably many

- **Confusion**: Thinking ends are defined only for locally finite graphs
  **Clarification**: Ends are defined for all graphs; locally finite graphs just have better-behaved end spaces

# Source Reference
Chapter 8, Section 8.1, pages 213-214; Section 8.2, pages 214-218.

# Verification Notes
- Definition directly from pp. 213-214
- Properties from Lemma 8.2.3 and surrounding discussion
- Confidence: HIGH — central concept with explicit definition
