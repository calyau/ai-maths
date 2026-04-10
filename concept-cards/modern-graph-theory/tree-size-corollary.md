---
concept: Tree Size Corollary
slug: tree-size-corollary
category: paths-and-cycles
subcategory: trees-and-forests
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.2 Paths, Cycles, and Trees"
extraction_confidence: high
aliases:
  - tree edge count
  - forest edge count
prerequisites:
  - tree
  - forest
  - spanning-tree
extends: []
related:
  - handshaking-lemma
contrasts_with: []
answers_questions:
  - "How many edges does a tree have?"
  - "How many edges does a forest have?"
---

# Quick Definition

A tree of order $n$ has exactly $n - 1$ edges (Corollary 8). A forest of order $n$ with $k$ components has exactly $n - k$ edges. A tree of order $\ge 2$ has at least two leaves (vertices of degree 1).

# Core Definition

"**Corollary 8.** A tree of order $n$ has size $n - 1$; a forest of order $n$ with $k$ components has size $n - k$" (Bollobás, p. 19). This follows from the spanning tree construction where each non-root vertex contributes exactly one edge.

"**Corollary 9.** A tree of order at least 2 contains at least 2 vertices of degree 1" (p. 19). Proof: if at most one vertex had degree 1, the degree sum would be $\ge 1 + 2(n-1) = 2n - 1 > 2(n-1) = 2e(T)$, contradicting the handshaking lemma.

# Prerequisites

- **Tree** — The corollary applies to trees
- **Forest** — Extends to forests
- **Spanning tree** — The proof uses spanning tree constructions

# Key Properties

1. $e(T) = n - 1$ for a tree $T$ of order $n$
2. $e(F) = n - k$ for a forest $F$ with $n$ vertices and $k$ components
3. A graph of order $n$ is a tree iff it is connected and has $n - 1$ edges
4. A tree of order $\ge 2$ has $\ge 2$ leaves (degree-1 vertices)

# Construction / Recognition

A connected graph with $n$ vertices and $n - 1$ edges is a tree. An acyclic graph with $n$ vertices and $n - 1$ edges is also a tree.

# Context & Application

The formula $e = n - 1$ for trees is one of the most frequently used facts in graph theory. It appears in Euler's formula, the matrix-tree theorem, and the dimension formulas for cycle and cut spaces.

# Examples

**Example** (p. 19): The degree sequence of a tree of order $n \ge 2$ satisfies $d_1 \ge 1$ and $\sum d_i = 2(n-1)$, forcing at least two vertices of degree 1.

# Relationships

## Builds Upon
- **Tree**, **Forest**, **Spanning tree**

## Enables
- Euler's formula: $n - m + f = 2$ (base case is a tree with $f = 1$)
- Dimension formulas for cycle space ($m - n + k$) and cut space ($n - k$)

## Related
- **Handshaking lemma** — Used in the proof of Corollary 9

# Common Errors

- **Error**: Stating a tree of order $n$ has $n$ edges
  **Correction**: A tree of order $n$ has $n - 1$ edges

# Common Confusions

- **Confusion**: Thinking the formula $e = n - 1$ characterizes trees
  **Clarification**: It characterizes trees only when combined with connectivity or acyclicity; $e = n - 1$ alone is not sufficient

# Source Reference

Chapter I: Fundamentals, Section I.2, Corollaries 8 and 9, page 19.

# Verification Notes

- Definition source: Direct from p. 19
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
