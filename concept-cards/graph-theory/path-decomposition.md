---
concept: Path-Decomposition
slug: path-decomposition
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 349
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases:
  - "path decomposition"
  - "linear decomposition"
prerequisites:
  - tree-decomposition
extends:
  - tree-decomposition
related:
  - tree-width
contrasts_with:
  - tree-decomposition
answers_questions:
  - "What is a path-decomposition?"
  - "What distinguishes a tree-decomposition from a path-decomposition?"
---

# Quick Definition
A path-decomposition of a finite graph is a tree-decomposition whose decomposition tree is a path. Its width is defined analogously: max|V_i| - 1. The path-width pw(G) is the least width of any path-decomposition.

# Core Definition
A *linear decomposition* of G is a family (V_i)_{i in I} of vertex sets indexed by some linear order I such that union V_i = V(G), every edge has both ends in some V_i, and V_i cap V_k subset V_j whenever i < j < k. For finite graphs, this is a tree-decomposition whose tree is a path, usually called a *path-decomposition*. The *path-width* pw(G) is the minimum width of any path-decomposition (Diestel, p. 349).

# Prerequisites
- **Tree-decomposition** — Path-decompositions are a special case

# Key Properties
1. pw(G) >= tw(G) always (path-decomposition is more restrictive)
2. Trees have unbounded path-width (Exercise 31)
3. G has path-decomposition into complete parts iff G is an interval graph
4. Excluding a forest H as minor bounds path-width (Robertson-Seymour Graph Minors I)

# Context & Application
Path-decompositions are used in the excluded K^n structure theorem (Theorem 12.4.11) as "vortices" attached to surface embeddings.

# Relationships
## Builds Upon
- **Tree-decomposition** — Path-decomposition is a special case

## Contrasts With
- **Tree-decomposition** — Tree T can be any tree; path-decomposition requires T to be a path

# Source Reference
Chapter 12, Section 12.4, page 349.

# Verification Notes
- Definition from p. 349
- Confidence: HIGH — explicit definition
