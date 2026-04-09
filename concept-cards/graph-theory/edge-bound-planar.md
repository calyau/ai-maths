---
concept: Edge Bound for Planar Graphs
slug: edge-bound-planar
category: planar-graphs
subcategory: plane-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.2 Plane graphs"
extraction_confidence: high
aliases:
  - "Corollary 4.2.10"
  - "3n - 6 bound"
  - "m <= 3n - 6"
prerequisites:
  - euler-formula
  - plane-triangulation
extends:
  - euler-formula
related:
  - maximal-planar-graph
  - kuratowski-theorem
contrasts_with: []
answers_questions:
  - "How many edges can a planar graph have?"
  - "What is the maximum number of edges in a planar graph?"
---

# Quick Definition
A plane graph with n >= 3 vertices has at most 3n - 6 edges, with equality if and only if it is a plane triangulation.

# Core Definition
**Corollary 4.2.10**: "A plane graph with n >= 3 vertices has at most 3n - 6 edges. Every plane triangulation with n vertices has 3n - 6 edges" (Diestel, p. 91).

# Prerequisites
- **Euler's formula** -- The bound is derived from n - m + l = 2
- **Plane triangulation** -- Achieves the bound exactly

# Key Properties
1. m <= 3n - 6 for any plane graph with n >= 3
2. Equality holds iff the graph is a plane triangulation
3. For triangle-free plane graphs: m <= 2n - 4
4. These bounds are tight

# Construction / Recognition
## To Use This Bound for Non-Planarity
1. Count vertices n and edges m of the graph
2. If m > 3n - 6, the graph is not planar
3. For triangle-free graphs, if m > 2n - 4, it is not planar

# Context & Application
This corollary is the primary tool for quick non-planarity proofs. It immediately shows K^5 (10 > 9) and K_{3,3} (9 > 8, using the triangle-free bound) are non-planar. It also establishes that planar graphs are sparse: the average degree is less than 6, which is essential for the five colour theorem proof.

# Examples
**Example** (p. 92): K^5 has 10 edges and 5 vertices. Since 10 > 3(5) - 6 = 9, K^5 is not planar.

**Example** (p. 92): K_{3,3} has 9 edges and 6 vertices, and is triangle-free. Since 9 > 2(6) - 4 = 8, K_{3,3} is not planar.

# Relationships
## Builds Upon
- **Euler's formula** -- Derived by substituting face count constraints

## Enables
- **Non-planarity of K^5 and K_{3,3}** -- Immediate corollary
- **Five colour theorem** -- Uses d(G) < 6
- **Kuratowski's theorem** -- Builds on these non-planarity results

# Source Reference
Chapter 4, Section 4.2, Corollary 4.2.10, pages 91-92.

# Verification Notes
- Statement directly quoted from p. 91
- Confidence: HIGH -- named corollary with proof
