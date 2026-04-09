---
concept: Complete Graph
slug: complete-graph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "K^n"
  - "clique"

prerequisites:
  - graph
  - adjacent
extends:
  - graph
related:
  - independent-set
  - complement
  - complete-multipartite-graph
contrasts_with:
  - independent-set
  - empty-graph

answers_questions:
  - "What is a complete graph?"
  - "What is K^n?"
---

# Quick Definition
A graph is complete if all its vertices are pairwise adjacent. A complete graph on n vertices is denoted K^n; a K^3 is called a triangle.

# Core Definition
If all the vertices of G are pairwise adjacent, then G is complete. A complete graph on n vertices is a K^n; a K^3 is called a triangle (Diestel, p. 3).

# Prerequisites
- **Graph** — a complete graph is a special type of graph
- **Adjacent** — completeness is defined in terms of adjacency

# Key Properties
1. K^n has n vertices and n(n-1)/2 edges
2. K^n is unique up to isomorphism for each n
3. Every graph on n vertices is a subgraph of K^n
4. The complement of K^n is the empty graph on n vertices
5. K^3 is called a triangle

# Construction / Recognition
## To Construct K^n
1. Create n vertices
2. Add an edge between every pair of distinct vertices

## To Recognize
A graph on n vertices is complete if and only if it has n(n-1)/2 edges.

# Context & Application
Complete graphs are among the most important graphs. Diestel uses the notation K^n (with superscript) rather than the more common K_n (with subscript), to free subscripts for ad-hoc use.

# Examples
**Example** (p. 3): K^3 is a triangle. K^2 * K^3 = K^5.

# Relationships
## Builds Upon
- **graph**, **adjacent**

## Enables
- **complete-multipartite-graph** — generalization of complete graphs
- **minor** — K^n minors are central to graph structure theory

## Contrasts With
- **empty-graph** — no edges at all
- **independent-set** — no two vertices adjacent

# Common Confusions
- **Confusion**: Confusing K^n with K_n notation
  **Clarification**: Diestel uses superscript (K^n) to keep subscripts free for indexing

# Source Reference
Chapter 1: The Basics, Section 1.1, page 3 (pdf p. 13).

# Verification Notes
- Direct from p. 3
- Confidence: HIGH
