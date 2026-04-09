---
concept: Rooted Tree
slug: rooted-tree

category: trees-and-forests
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 24
section: "1.5 Trees and forests"

extraction_confidence: high

aliases:
  - "root"
  - "tree-order"

prerequisites:
  - tree
extends:
  - tree
related:
  - normal-spanning-tree
contrasts_with: []

answers_questions:
  - "What is a rooted tree?"
  - "What is the tree-order?"
---

# Quick Definition
A rooted tree is a tree T with a designated vertex r called the root. Writing x <= y for x in rTy defines a partial ordering on V(T), the tree-order.

# Core Definition
Sometimes it is convenient to consider one vertex of a tree as special; such a vertex is then called the root of this tree. A tree T with a fixed root r is a rooted tree. Writing x <= y for x in rTy then defines a partial ordering on V(T), the tree-order associated with T and r (Diestel, p. 15).

# Prerequisites
- **Tree** — a rooted tree is a tree with additional structure

# Key Properties
1. The root r is the least element in the tree-order
2. Leaves are the maximal elements
3. The ends of any edge are comparable (one is above the other)
4. The down-closure of every vertex is a chain
5. Vertices at distance k from r have height k and form the kth level
6. The up-closure of x is the set of all vertices y >= x
7. The down-closure of y is the set of all vertices x <= y

# Context & Application
Rooted trees provide a natural hierarchy. The tree-order is used extensively in the theory of infinite graphs (Chapter 8) and in normal spanning trees.

# Relationships
## Builds Upon
- **tree**

## Enables
- **normal-spanning-tree** — a rooted spanning tree with special properties

# Source Reference
Chapter 1: The Basics, Section 1.5, page 15 (pdf p. 25).

# Verification Notes
- Direct from p. 15
- Confidence: HIGH
