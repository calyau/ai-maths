---
concept: Girth
slug: girth
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases:
  - "g(G)"
  - minimum cycle length
prerequisites:
  - graph
  - cycle
extends: []
related:
  - eulers-formula
  - planar-graph
contrasts_with: []
answers_questions:
  - "What is the girth of a graph?"
---

# Quick Definition

The girth of a graph is the length of its shortest cycle. An acyclic graph has girth $\infty$.

# Core Definition

"The girth of the graph, that is the number of edges in a shortest cycle, is large. (The girth of an acyclic graph is defined to be $\infty$.)" (Bollobás, p. 30). The girth provides refined edge bounds for planar graphs via Theorem 16.

# Prerequisites

- **Graph** — Girth is a property of graphs
- **Cycle** — Girth measures the shortest cycle

# Key Properties

1. Girth $\ge 3$ for graphs with cycles (since cycles have length $\ge 3$)
2. Girth $= \infty$ for forests
3. A planar graph of girth $g$ has at most $\frac{g}{g-2}(n-2)$ edges (Theorem 16)
4. Triangle-free graphs have girth $\ge 4$
5. Bipartite graphs have even girth (if finite)

# Construction / Recognition

Find the shortest cycle in the graph. For each vertex, a BFS can detect shortest cycles.

# Context & Application

Girth is essential for proving nonplanarity. For instance, $K_{3,3}$ has girth 4, and the girth-based bound shows it is nonplanar since $9 > \frac{4}{2}(6-2) = 8$. Girth also appears in extremal graph theory (Chapter IV).

# Examples

**Example** (p. 31): $K_{3,3}$ has girth 4 and $e(K_{3,3}) = 9 > (4/(4-2))(6-2) = 8$, proving nonplanarity.

# Relationships

## Builds Upon
- **Graph**, **Cycle**

## Enables
- Refined edge bounds for planar graphs (Theorem 16)
- Nonplanarity proofs

## Related
- **Euler's formula** — Combined with girth bounds face sizes

# Common Errors

- **Error**: Defining girth as the length of the longest cycle
  **Correction**: Girth is the length of the shortest cycle

# Common Confusions

- **Confusion**: Assuming all planar graphs have girth 3
  **Clarification**: Planar graphs can have any girth; higher girth means fewer edges are allowed

# Source Reference

Chapter I: Fundamentals, Section I.4, Theorem 16, pages 30-31.

# Verification Notes

- Definition source: Direct from p. 30
- Confidence rationale: Explicitly defined in context of planar graph bounds
- Uncertainties: None
- Cross-reference status: Verified
