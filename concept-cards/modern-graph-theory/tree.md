---
concept: Tree
slug: tree
category: paths-and-cycles
subcategory: trees-and-forests
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases: []
prerequisites:
  - graph
  - connected-graph
  - forest
extends:
  - forest
related:
  - spanning-tree
  - bridge
contrasts_with:
  - cycle
answers_questions:
  - "What is a tree?"
  - "What are the equivalent characterizations of a tree?"
---

# Quick Definition

A tree is a connected forest — a connected graph with no cycles. Equivalently, a tree is a minimal connected graph or a maximal acyclic graph.

# Core Definition

"A tree is a connected forest" (Bollobás, p. 14). Theorem 6 gives three equivalent characterizations:
- (i) $G$ is a tree
- (ii) $G$ is a minimal connected graph (connected and every edge is a bridge)
- (iii) $G$ is a maximal acyclic graph (acyclic and adding any edge creates a cycle)

A tree of order $n$ has exactly $n - 1$ edges (Corollary 8).

# Prerequisites

- **Graph** — A tree is a graph
- **Connected graph** — A tree must be connected
- **Forest** — A tree is a connected forest

# Key Properties

1. Connected and acyclic
2. Has exactly $n - 1$ edges for $n$ vertices (Corollary 8)
3. Every edge is a bridge (Theorem 6)
4. Adding any edge creates exactly one cycle (Theorem 6)
5. Between any two vertices there is a unique path (Theorem 5)
6. A tree of order $\ge 2$ has at least 2 vertices of degree 1 (Corollary 9)

# Construction / Recognition

## To recognize a tree
1. Verify connectivity and $e(G) = n - 1$
2. Or: verify connectivity and absence of cycles
3. Or: verify that between any two vertices there is exactly one path

# Context & Application

Trees are among the most fundamental structures in graph theory and computer science. They appear as spanning trees, in optimization (economical spanning trees), and as the structural backbone in electrical network analysis (Kirchhoff's theorem). Every connected graph contains a spanning tree (Corollary 7).

# Examples

**Example** (p. 14): Fig. I.5 shows a forest; each of its components is a tree.

**Example** (p. 17): Theorem 6 proves the equivalence of three characterizations of trees.

# Relationships

## Builds Upon
- **Forest** — A tree is a connected forest
- **Connected graph** — A tree must be connected

## Enables
- **Spanning tree** — A tree that spans all vertices of a graph
- **Matrix-tree theorem** — Counts spanning trees using the Laplacian

## Related
- **Bridge** — Every edge of a tree is a bridge

## Contrasts With
- **Cycle** — A tree is acyclic; adding any edge creates a unique cycle

# Common Errors

- **Error**: Assuming a tree must have a designated root
  **Correction**: Trees in graph theory are unrooted by default; rooted trees are a separate concept

# Common Confusions

- **Confusion**: Confusing "tree" with "spanning tree"
  **Clarification**: A tree is any connected acyclic graph; a spanning tree is a tree that is a spanning subgraph of a given graph

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 14; Theorems 5-6, pages 17-18; Corollaries 7-9, pages 18-19.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined with multiple equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
