---
concept: "Erdős-Pósa Property"
slug: erdos-posa-property
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 348
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases: []
prerequisites:
  - graph-minor
  - tree-decomposition
  - excluded-planar-minor-theorem
extends: []
related:
  - grid-theorem
contrasts_with: []
answers_questions:
  - "What is the Erdős-Pósa property?"
---

# Quick Definition
A class H of graphs has the Erdős-Pósa property if the number of vertices needed to cover all subgraphs from H in any graph is bounded by a function of the maximum number of disjoint such subgraphs.

# Core Definition
A class H of graphs has the *Erdős-Pósa property* if there is a function f: N -> N such that, given k and a graph G, either G has k disjoint subgraphs in H or there is a set of at most f(k) vertices hitting all subgraphs of G in H (Diestel, p. 348).

# Prerequisites
- **Graph minor** — The property applies to classes MH
- **Tree-decomposition** — Used in the proof
- **Excluded planar minor theorem** — Key ingredient

# Key Properties
1. If H is planar and connected, then MH has the Erdős-Pósa property (Corollary 12.4.10)
2. If H is non-planar, then MH does NOT have the Erdős-Pósa property (Exercise 39)
3. The Erdős-Pósa theorem (Theorem 2.3.2) is the special case H = K^3 (cycles)

# Relationships
## Builds Upon
- **Excluded planar minor theorem** and **Tree-decomposition**

# Source Reference
Chapter 12, Section 12.4, pages 348-349 (Corollary 12.4.10).

# Verification Notes
- Definition from p. 348
- Confidence: HIGH — explicit definition
