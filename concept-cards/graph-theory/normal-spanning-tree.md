---
concept: Normal Spanning Tree
slug: normal-spanning-tree
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 214
section: "8.2 Paths, trees, and ends"
extraction_confidence: high
aliases:
  - "normal tree"
prerequisites:
  - infinite-graph
  - end-of-a-graph
extends: []
related:
  - star-comb-lemma
  - topological-spanning-tree
contrasts_with: []
answers_questions:
  - "What is a normal spanning tree?"
  - "Why are normal spanning trees important in infinite graph theory?"
---

# Quick Definition
A rooted spanning tree T of G is normal if the endvertices of every edge of G not in T are comparable in the tree-order of T. Normal spanning trees are the single most important structural tool in infinite graph theory.

# Core Definition
A rooted tree T contained in G is *normal* in G if the endvertices of every T-path in G are comparable in the tree-order of T. If T is a spanning tree, the only T-paths are edges of G that are not edges of T. Normal spanning trees exhibit the separation properties of the graph they span (Diestel, p. 214).

# Prerequisites
- **Infinite graph** — Normal spanning trees are primarily a tool for infinite graphs
- **End of a graph** — Normal spanning trees reflect the end structure

# Key Properties
1. Every end of G contains exactly one normal ray of T (Lemma 8.2.3)
2. Every countable connected graph has a normal spanning tree (Theorem 8.2.4, Jung 1967)
3. The down-closure of any vertex in the tree-order is finite and separates its up-closure from the rest
4. Not all connected graphs have a normal spanning tree (e.g., uncountable complete graphs)
5. A graph has a normal spanning tree iff it has no topological K^{aleph_0} subgraph (Theorem 12.4.13)

# Construction / Recognition
## To Construct a Normal Spanning Tree (Countable Case)
1. Start with a single vertex as T_0
2. At step n+1: if v_{n+1} is not in T_n, find the component C of G - T_n containing it
3. Let x be the greatest element of N(C) in T_n
4. Add an x-v_{n+1} path through C to extend T_n to T_{n+1}
5. The union T of all T_n is a normal spanning tree

# Context & Application
Normal spanning trees are perhaps the single most important structural tool in infinite graph theory. They simultaneously encode the separation properties and end structure of a graph. The closure of a normal spanning tree is always a topological spanning tree (Lemma 8.5.7).

# Examples
**Example 1** (p. 215-216): Construction of a normal spanning tree for a countable connected graph by iteratively adding vertices.

# Relationships
## Enables
- **Topological spanning tree** — Closure of a normal spanning tree is a topological spanning tree
- End structure analysis — Each end has exactly one normal ray

## Related
- **Star-comb lemma** — Used in the proof that normal rays reflect ends

# Source Reference
Chapter 8, Section 8.2, pages 214-216 (Lemma 8.2.3, Theorem 8.2.4).

# Verification Notes
- Properties from Lemma 8.2.3 and Theorem 8.2.4
- Confidence: HIGH — explicitly defined and proved
