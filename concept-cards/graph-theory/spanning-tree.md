---
concept: Spanning Tree
slug: spanning-tree

category: trees-and-forests
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 23
section: "1.5 Trees and forests"

extraction_confidence: high

aliases: []

prerequisites:
  - tree
  - spanning-subgraph
  - connected-graph
extends:
  - tree
  - spanning-subgraph
related:
  - normal-spanning-tree
  - fundamental-cycle
  - fundamental-cut
contrasts_with: []

answers_questions:
  - "What is a spanning tree?"
  - "Does every connected graph have a spanning tree?"
---

# Quick Definition
A spanning tree of a connected graph G is a spanning subgraph that is a tree. Every connected graph contains a spanning tree.

# Core Definition
A frequently used application of Theorem 1.5.1 is that every connected graph contains a spanning tree: by the equivalence of (i) and (iii), any minimal connected spanning subgraph will be a tree (Diestel, p. 14).

# Prerequisites
- **Tree** — a spanning tree is a tree
- **Spanning subgraph** — it spans all vertices
- **Connected graph** — the graph must be connected

# Key Properties
1. A spanning tree of G has |G| - 1 edges (Corollary 1.5.3)
2. Every connected graph contains a spanning tree
3. A spanning tree is a minimal connected spanning subgraph (Theorem 1.5.1(iii))
4. Adding any edge to a spanning tree creates exactly one cycle (fundamental cycle)
5. Removing any edge from a spanning tree disconnects it (fundamental cut)

# Construction / Recognition
To find a spanning tree: take any minimal connected spanning subgraph, or repeatedly remove edges from cycles until none remain.

# Context & Application
Spanning trees are essential in graph theory and algorithms. They define fundamental cycles and cuts (Section 1.9), and normal spanning trees (Proposition 1.5.6) capture the structure of the host graph.

# Examples
**Example** (p. 11): Fig. 1.4.1 shows a spanning tree in each component of a graph.

# Relationships
## Builds Upon
- **tree**, **spanning-subgraph**, **connected-graph**

## Enables
- **fundamental-cycle**, **fundamental-cut** — defined with respect to a spanning tree
- **normal-spanning-tree** — a spanning tree with special properties

# Source Reference
Chapter 1: The Basics, Section 1.5, page 14 (pdf p. 24).

# Verification Notes
- From p. 14 and application of Theorem 1.5.1
- Confidence: HIGH
