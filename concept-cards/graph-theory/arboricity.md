---
concept: Arboricity
slug: arboricity
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 59
section: "2.4 Tree-packing and arboricity"
extraction_confidence: high
aliases: []
prerequisites:
  - tree
  - forest
extends: []
related:
  - nash-williams-arboricity-theorem
  - edge-disjoint-spanning-trees
contrasts_with: []
answers_questions:
  - "What is the arboricity of a graph?"
---

# Quick Definition
The arboricity of a graph G is the minimum number of forests needed to partition its edge set.

# Core Definition
The least number of forests forming a partition of a graph G is called the **arboricity** of G. By Theorem 2.4.4, the arboricity is a measure for the maximum local density: a graph has small arboricity if and only if it is "nowhere dense," i.e., has no subgraph H with epsilon(H) large (Diestel, p. 59).

# Prerequisites
- **Tree** / **forest** — arboricity counts forests

# Key Properties
1. Arboricity = min number of forests partitioning E(G)
2. Characterized by Nash-Williams' theorem: arboricity <= k iff ||G[U]|| <= k(|U|-1) for all non-empty U
3. Measures maximum local density
4. Arboricity 1 iff G is a forest
5. Planar graphs have arboricity at most 3

# Construction / Recognition
## Computing Arboricity
1. Find the maximum of ||G[U]|| / (|U|-1) over all non-empty U with |U| >= 2
2. Arboricity = ceiling of this maximum

# Context & Application
Arboricity is the dual of the spanning tree packing problem. Packing asks how many edge-disjoint spanning trees fit; arboricity asks how few forests suffice to cover all edges. Both are characterized by Nash-Williams-type conditions.

# Examples
**Example**: A tree has arboricity 1 (it is its own single forest). K4 has 6 edges and arboricity 2 (each forest has at most 3 edges). A planar graph has arboricity at most 3.

# Relationships
## Builds Upon
- **Tree**, **forest**

## Related
- **Nash-Williams arboricity theorem** — characterizes arboricity
- **Edge-disjoint spanning trees** — dual concept

# Common Errors
- **Error**: Confusing arboricity with chromatic number
  **Correction**: Arboricity partitions edges into forests; chromatic number partitions vertices into independent sets

# Common Confusions
- **Confusion**: Thinking arboricity is about spanning trees specifically
  **Clarification**: Arboricity uses forests (not necessarily spanning trees) to partition edges

# Source Reference
Chapter 2, Section 2.4, p. 59 (pdf p. 59). See Theorem 2.4.4.

# Verification Notes
- Definition from p. 59
- Confidence: HIGH — explicitly defined
