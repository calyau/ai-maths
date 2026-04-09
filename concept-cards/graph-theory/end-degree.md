---
concept: End Degree
slug: end-degree
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 214
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "vertex-degree of an end"
  - "edge-degree of an end"
  - "thick end"
  - "thin end"
prerequisites:
  - end-of-a-graph
  - ray
extends:
  - end-of-a-graph
related:
  - topological-end-space
contrasts_with: []
answers_questions:
  - "What is the degree of an end?"
  - "What distinguishes thick ends from thin ends?"
---

# Quick Definition
The vertex-degree of an end is the maximum number of disjoint rays it contains; the edge-degree is the maximum number of edge-disjoint rays. Ends of infinite vertex-degree are thick; those of finite vertex-degree are thin.

# Core Definition
The maximum number of disjoint rays in an end is the (combinatorial) vertex-degree of that end; the maximum number of edge-disjoint rays in it is its (combinatorial) edge-degree. These maxima are indeed attained: if an end contains k (edge-)disjoint rays for every integer k, it also contains an infinite set of (edge-)disjoint rays. Thus, every end has a vertex-degree and an edge-degree in N union {infinity}. Ends of infinite vertex-degree are called *thick*; ends of finite vertex-degree are *thin* (Diestel, pp. 214, 218).

# Prerequisites
- **End of a graph** — Degrees are measured for ends
- **Ray** — Degrees count disjoint rays within an end

# Key Properties
1. The maxima defining degrees are always attained (Theorem 8.2.5)
2. Every end has both a vertex-degree and an edge-degree in N union {infinity}
3. A graph with a thick end contains the N x N grid as a minor (Theorem 8.2.6)
4. The N x N grid has one thick end

# Examples
**Example 1** (p. 218): The N x N grid has a single thick end.

**Example 2**: A ray has one end of vertex-degree 1 (thin).

# Relationships
## Builds Upon
- **End of a graph** — Degree is a property of an end

## Enables
- **Halin's theorem** (8.2.6) — Thick ends contain grid subdivisions

# Source Reference
Chapter 8, Sections 8.1-8.2, pages 214, 218.

# Verification Notes
- Definition from pp. 214, 218
- Confidence: HIGH — explicit definitions
