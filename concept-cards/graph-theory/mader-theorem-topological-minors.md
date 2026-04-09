---
concept: "Average Degree Forcing Topological Minors"
slug: mader-theorem-topological-minors
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 180
section: "7.2 Minors"
extraction_confidence: high
aliases:
  - "Theorem 7.2.1"
  - "topological minor forcing"
prerequisites:
  - graph
  - edge-density
related:
  - kostochka-theorem
  - hadwiger-conjecture
answers_questions:
  - "How many edges force a topological K^r minor?"
---

# Quick Definition
There is a constant c such that every graph of average degree d(G) >= cr^2 contains K^r as a topological minor (Theorem 7.2.1).

# Core Definition
**Theorem 7.2.1**: There is a constant c in R such that, for every r in N, every graph G of average degree d(G) >= cr^2 contains K^r as a topological minor. The proof works with c = 10: a graph of average degree at least 10r^2 has an r^2-connected subgraph H by Theorem 1.4.3. Pick r branch vertices and r-1 neighbours each; since H is (1/2)r^2-linked by Theorem 3.5.3, the required disjoint paths exist. (Diestel, p. 170)

The lower bound h(r) > (1/8)r^2 shows this is best possible up to the constant.

# Prerequisites
- **Graph** — The theorem is about graphs of large average degree

# Key Properties
1. cr^2 edges per vertex suffice for a topological K^r
2. Best possible up to the constant c (lower bound (1/8)r^2)
3. For small r: 2n-2 edges force TK^4; 3n-5 edges force TK^5
4. Sparse extremal theory: linear number of edges (in n) suffices

# Relationships
## Related
- **Kostochka's theorem** — For general minors, cr*sqrt(log r) suffices
- **Hadwiger's conjecture** — Asks whether chi(G) >= r forces K^r minor

# Source Reference
Chapter 7, Section 7.2, Theorem 7.2.1, page 170 (pdf page 180).

# Verification Notes
- Confidence: HIGH — theorem with proof
