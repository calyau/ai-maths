---
concept: Finite Tree-Width (Infinite Graphs)
slug: finite-tree-width-infinite
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 351
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases: []
prerequisites:
  - tree-width
  - tree-decomposition
extends:
  - tree-width
related:
  - normal-spanning-tree
contrasts_with: []
answers_questions:
  - "What does finite tree-width mean for infinite graphs?"
---

# Quick Definition
An infinite graph G has finite tree-width if G admits a tree-decomposition into finite parts such that for every infinite path in T, the "limsup" of the intersections is finite. Theorem 12.4.13: equivalent to having no topological K^{aleph_0} minor and to having a normal spanning tree with bounded ray linking.

# Core Definition
G has *finite tree-width* if G admits a tree-decomposition (T, (V_t)) into finite parts such that for every infinite path t_1t_2... in T, the set union_{i>=1} intersection_{j>=i} V_{t_j} is finite. **Theorem 12.4.13** (Diestel, Robertson, Seymour & Thomas): For connected G, the following are equivalent: (i) no topological K^{aleph_0} minor; (ii) finite tree-width; (iii) normal spanning tree with bounded ray-linking (Diestel, p. 351).

# Source Reference
Chapter 12, Section 12.4, pages 351-352 (Theorem 12.4.13).

# Verification Notes
- Definition from p. 351
- Confidence: HIGH — named theorem
