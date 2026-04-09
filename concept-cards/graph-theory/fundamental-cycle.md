---
concept: Fundamental Cycle
slug: fundamental-cycle

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
  - "C_e"

prerequisites:
  - graph
  - spanning-tree
  - cycle
  - cycle-space
extends: []
related:
  - fundamental-cut
contrasts_with:
  - fundamental-cut

answers_questions:
  - "What is a fundamental cycle?"
  - "How do fundamental cycles form a basis for the cycle space?"
---

# Quick Definition
For a spanning tree T of a connected graph G, each edge e not in T creates a unique cycle C_e in T + e. These are the fundamental cycles, and they form a basis for the cycle space.

# Core Definition
Consider a connected graph G with a spanning tree T. For every edge e in E minus E(T) there is a unique cycle C_e in T + e; these cycles C_e are the fundamental cycles of G with respect to T (Diestel, p. 26).

Theorem 1.9.6: The fundamental cycles form a basis of C(G), and dim C(G) = m - n + 1.

# Prerequisites
- **Graph**, **spanning-tree**, **cycle**, **cycle-space**

# Key Properties
1. There are m - n + 1 fundamental cycles (one for each non-tree edge)
2. Each fundamental cycle C_e contains exactly one non-tree edge e
3. The fundamental cycles are linearly independent
4. They form a basis for the cycle space

# Relationships
## Builds Upon
- **spanning-tree**, **cycle**, **cycle-space**

## Contrasts With
- **fundamental-cut** — defined for tree edges, forming a basis for the cut space

# Source Reference
Chapter 1: The Basics, Section 1.9, pages 26-27 (pdf pp. 36-37). Theorem 1.9.6.

# Verification Notes
- Direct from pp. 26-27
- Confidence: HIGH
