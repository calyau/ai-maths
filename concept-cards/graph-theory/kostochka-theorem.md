---
concept: Kostochka's Theorem
slug: kostochka-theorem
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
  - "Theorem 7.2.2"
  - "Kostochka-Thomason theorem"
prerequisites:
  - graph
  - edge-density
related:
  - mader-theorem-topological-minors
  - hadwiger-conjecture
answers_questions:
  - "What average degree forces a K^r minor?"
---

# Quick Definition
There exists a constant c such that every graph of average degree d(G) >= cr*sqrt(log r) contains K^r as a minor; up to the constant c, this bound is best possible.

# Core Definition
**Theorem 7.2.2** (Kostochka 1982): There exists a constant c in R such that, for every r in N, every graph G of average degree d(G) >= cr*sqrt(log r) contains K^r as a minor. Up to the value of c, this bound is best possible as a function of r. Thomason (2001) determined the asymptotic value of c as alpha + o(1) where alpha = 0.53131... (Diestel, p. 170-171)

# Prerequisites
- **Graph** — Average degree is a graph parameter

# Key Properties
1. cr*sqrt(log r) is the threshold for K^r minors, optimal up to the constant
2. The lower bound (showing this is necessary) comes from random graphs
3. Significantly better than the cr^2 bound for topological minors
4. Thomason determined the precise asymptotic constant alpha = 0.53131...

# Context & Application
General minors are easier to force than topological minors: cr*sqrt(log r) vs cr^2. This gap is one reason Hadwiger's conjecture (which concerns general minors) is considered more tractable than Hajos's conjecture (about topological minors).

# Relationships
## Related
- **Hadwiger's conjecture** — Asks if chi(G) >= r suffices (much stronger than large average degree)
- **Mader theorem** — For topological minors, cr^2 is needed

# Source Reference
Chapter 7, Section 7.2, Theorem 7.2.2, pages 170-171 (pdf pages 180-181).

# Verification Notes
- Confidence: HIGH — named theorem, stated without proof but with precise reference
