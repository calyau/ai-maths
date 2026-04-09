---
concept: Fundamental Cut
slug: fundamental-cut

category: algebraic-graph-theory
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 36
section: "1.9 Some linear algebra"

extraction_confidence: high

aliases:
  - "D_e"

prerequisites:
  - graph
  - spanning-tree
  - cut
  - cut-space
extends: []
related:
  - fundamental-cycle
contrasts_with:
  - fundamental-cycle

answers_questions:
  - "What is a fundamental cut?"
  - "How do fundamental cuts form a basis for the cut space?"
---

# Quick Definition
For a spanning tree T of a connected graph G, removing a tree edge e splits T into two components; the set D_e of edges between these components is a fundamental cut. The fundamental cuts form a basis for the cut space.

# Core Definition
Given an edge e in T, the graph T - e has exactly two components. The set D_e of edges between these two components forms a bond in G. These bonds D_e are the fundamental cuts of G with respect to T (Diestel, p. 26).

Theorem 1.9.6: The fundamental cuts form a basis of C*(G), and dim C*(G) = n - 1.

# Prerequisites
- **Graph**, **spanning-tree**, **cut**, **cut-space**

# Key Properties
1. There are n - 1 fundamental cuts (one for each tree edge)
2. Each fundamental cut D_e contains exactly one tree edge e
3. The fundamental cuts are linearly independent
4. They form a basis for the cut space

# Relationships
## Builds Upon
- **spanning-tree**, **cut**, **cut-space**

## Contrasts With
- **fundamental-cycle** — defined for non-tree edges

# Source Reference
Chapter 1: The Basics, Section 1.9, pages 26-27 (pdf pp. 36-37). Theorem 1.9.6. See Fig. 1.9.3.

# Verification Notes
- Direct from pp. 26-27
- Confidence: HIGH
