---
concept: Topological Spanning Tree
slug: topological-spanning-tree
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 241
section: "8.5 The topological end space"
extraction_confidence: high
aliases: []
prerequisites:
  - topological-end-space
  - normal-spanning-tree
extends: []
related:
  - topological-cycle-space
  - topological-circle
contrasts_with: []
answers_questions:
  - "What is a topological spanning tree?"
---

# Quick Definition
A topological spanning tree of G is an arc-connected standard subspace of |G| that contains every vertex and every end but contains no circle.

# Core Definition
A *topological spanning tree* of G is an arc-connected standard subspace of |G| that contains every vertex and every end but contains no circle. Such a subspace must be closed, and is both minimally arc-connected and maximally "acirclic." Any two points are joined by a unique arc (Diestel, p. 241).

# Prerequisites
- **Topological end space** — Topological spanning trees live in |G|
- **Normal spanning tree** — The closure of a normal spanning tree is a topological spanning tree

# Key Properties
1. Must contain every vertex and every end
2. Must be arc-connected and contain no circle
3. Adding any edge creates a unique circle (fundamental circuit)
4. Removing any edge creates exactly two arc-components (fundamental cut)
5. The closure of a normal spanning tree is always a topological spanning tree (Lemma 8.5.7)
6. Not every closure of an ordinary spanning tree is a topological spanning tree

# Context & Application
Topological spanning trees extend the concept of spanning trees to infinite graphs in a way that incorporates ends. They are essential for defining the topological cycle space.

# Examples
**Example 1** (p. 242, Fig. 8.5.2): T_1's closure is a topological spanning tree, but T_2's closure contains three circles.

# Relationships
## Builds Upon
- **Topological end space** — The ambient space
- **Normal spanning tree** — Closures yield topological spanning trees

## Enables
- **Topological cycle space** — Fundamental circuits generate it

# Source Reference
Chapter 8, Section 8.5, pages 241-242.

# Verification Notes
- Definition from p. 241
- Confidence: HIGH — explicit definition
