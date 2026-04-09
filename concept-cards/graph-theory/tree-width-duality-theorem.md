---
concept: Tree-Width Duality Theorem
slug: tree-width-duality-theorem
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 332
section: "12.3 Tree-decompositions"
extraction_confidence: high
aliases:
  - "Seymour-Thomas theorem"
prerequisites:
  - tree-width
  - bramble
extends: []
related:
  - tree-decomposition
contrasts_with: []
answers_questions:
  - "What is the duality between tree-width and brambles?"
---

# Quick Definition
The tree-width duality theorem (Seymour-Thomas, 1993) states that a graph has tree-width >= k if and only if it contains a bramble of order > k. Equivalently, tree-width equals one less than the maximum bramble order.

# Core Definition
**Theorem 12.3.9** (Seymour & Thomas 1993): Let k >= 0 be an integer. A graph has tree-width >= k if and only if it contains a bramble of order > k (Diestel, p. 332).

# Prerequisites
- **Tree-width** — One side of the duality
- **Bramble** — The other side of the duality

# Key Properties
1. Backward direction: any bramble in G is covered by some part of any tree-decomposition
2. Forward direction: if no bramble has order > k, construct a tree-decomposition of width <= k
3. The proof of the forward direction uses induction on bramble size
4. The bramble number (max bramble order) equals tw(G) + 1

# Context & Application
This min-max theorem is analogous to other dualities in graph theory (max-flow min-cut, etc.). It provides both a certificate for large tree-width (a large bramble) and for small tree-width (a narrow decomposition).

# Relationships
## Builds Upon
- **Tree-width** and **Bramble**

# Source Reference
Chapter 12, Section 12.3, pages 332-334 (Theorem 12.3.9).

# Verification Notes
- Statement from p. 332
- Confidence: HIGH — named theorem with full proof
