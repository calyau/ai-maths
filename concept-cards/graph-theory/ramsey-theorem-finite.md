---
concept: "Ramsey's Theorem (Finite, for Graphs)"
slug: ramsey-theorem-finite
category: ramsey-theory
subcategory: classical-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 262
section: "9.1 Ramsey's original theorems"
extraction_confidence: high
aliases:
  - "Ramsey's theorem"
  - "Theorem 9.1.1"
prerequisites:
  - graph
  - vertex
  - edge
related:
  - ramsey-number
  - ramsey-theorem-infinite
  - ramsey-theorem-general
  - monochromatic-subgraph
  - c-colouring
answers_questions:
  - "What is Ramsey's theorem?"
  - "What must I know before studying Ramsey theory?"
---

# Quick Definition
For every r in N there exists an n in N such that every graph of order at least n contains either K^r or K-bar^r as an induced subgraph.

# Core Definition
**Theorem 9.1.1** (Ramsey 1930): For every r in N there exists an n in N such that every graph of order at least n contains either K^r or K-bar^r (the edgeless graph on r vertices) as an induced subgraph.

The proof constructs a sequence V_1, ..., V_{2r-2} of sets, choosing vertices v_i in V_i so that v_{i-1} is adjacent to all of V_i or to none. Among v_1, ..., v_{2r-3}, at least r-1 show the same adjacency behaviour; these plus v_{2r-2} form K^r or K-bar^r. This gives R(r) <= 2^{2r-3}. (Diestel, pp. 252-253)

# Prerequisites
- **Graph**, **Vertex**, **Edge** — The theorem is about graphs

# Key Properties
1. The simplest version of Ramsey's theorem for graphs
2. The proof gives the bound n = 2^{2r-3}
3. At first surprising: forcing K^r requires about (r-2)/(r-1) of all edges (Turan), but neither G nor G-bar has more than half
4. The Turan graphs show that avoiding K^r imposes structure helpful for finding K-bar^r

# Construction / Recognition
## Proof Strategy
1. Pick vertex v_1 from a large set V_1
2. Partition V_1 \ {v_1} into "all-adjacent" or "all-non-adjacent" to v_1; choose the larger half as V_2
3. Repeat: pick v_2 from V_2, partition into all-adj/all-non-adj; continue
4. After 2r-3 steps, pigeonhole: r-1 vertices show the same behaviour
5. These r-1 vertices plus the last chosen vertex form K^r or K-bar^r

# Context & Application
Ramsey's theorem is the founding result of Ramsey theory. Despite its simple statement, it leads to a distinctive mathematical theory with connections to algebra, geometry, and combinatorial number theory.

# Examples
**Example** (p. 252, Fig. 9.1.1): Illustration of the vertex selection process v_1, v_2, ... with diminishing sets V_1, V_2, ...

# Relationships
## Enables
- **Ramsey number** — R(r) is the least n for which the theorem holds
- **Ramsey theorem (general)** — Generalizes to c-colourings of k-sets
- **Theorem 9.2.2** — Ramsey numbers of bounded-degree graphs

## Related
- **Monochromatic subgraph** — Ramsey's theorem guarantees monochromatic complete/empty subgraphs
- **Turan's theorem** — Provides context for the surprising nature of Ramsey's theorem

# Source Reference
Chapter 9, Section 9.1, Theorem 9.1.1, pages 252-253 (pdf pages 262-263).

# Verification Notes
- Confidence: HIGH — foundational theorem with complete proof
