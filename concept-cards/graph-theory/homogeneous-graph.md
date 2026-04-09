---
concept: Homogeneous Graph
slug: homogeneous-graph
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 225
section: "8.3 Homogeneous and universal graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - infinite-graph
  - graph-isomorphism
extends: []
related:
  - rado-graph
  - universal-graph
contrasts_with: []
answers_questions:
  - "What is a homogeneous graph?"
---

# Quick Definition
A countable graph is homogeneous if every isomorphism between two finite induced subgraphs can be extended to an automorphism of the entire graph.

# Core Definition
A countable graph is *homogeneous* if every isomorphism between two finite induced subgraphs can be extended to an automorphism of the entire graph (Diestel, p. 225). The Rado graph R is homogeneous, as is K^{aleph_0} and its complement.

# Prerequisites
- **Infinite graph** — Homogeneity is defined for countable infinite graphs
- **Graph isomorphism** — Partial isomorphisms must extend to full automorphisms

# Key Properties
1. Homogeneous graphs have large automorphism groups
2. The Rado graph, K^{aleph_0}, and their complements are homogeneous
3. For every r >= 3, there is a homogeneous K^r-free graph R^r
4. These are essentially all countable homogeneous graphs (Lachlan-Woodrow theorem)

# Context & Application
Homogeneity represents an extreme form of symmetry. The Lachlan-Woodrow classification (Theorem 8.3.3, 1980) classifies all countably infinite homogeneous graphs.

# Examples
**Example 1** (p. 225): The Rado graph R is homogeneous.

**Example 2** (p. 225): For r >= 3, the graph R^r (universal K^r-free graph) is homogeneous.

# Relationships
## Related
- **Rado graph** — The most important homogeneous graph
- **Universal graph** — Homogeneous graphs tend to be universal

# Source Reference
Chapter 8, Section 8.3, pages 225-226 (Theorem 8.3.3).

# Verification Notes
- Definition from p. 225
- Confidence: HIGH — explicit definition
