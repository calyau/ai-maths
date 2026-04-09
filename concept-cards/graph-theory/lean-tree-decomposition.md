---
concept: Lean Tree-Decomposition
slug: lean-tree-decomposition
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 335
section: "12.3 Tree-decompositions"
extraction_confidence: high
aliases:
  - "linked tree-decomposition"
prerequisites:
  - tree-decomposition
  - tree-width
extends:
  - tree-decomposition
related: []
contrasts_with: []
answers_questions:
  - "What is a lean tree-decomposition?"
---

# Quick Definition
A tree-decomposition is lean (or linked) if for any t1, t2 in T and subsets Z1 of V_{t1}, Z2 of V_{t2} with |Z1| = |Z2| = k, either G has k disjoint Z1-Z2 paths or some edge tt' on the t1-t2 path in T has |V_t cap V_{t'}| < k.

# Core Definition
A tree-decomposition (T, V) of G is *lean* (or *linked*) if it satisfies: (T4) Given t1, t2 in T and Z1 subset V_{t1}, Z2 subset V_{t2} with |Z1| = |Z2| = k, either G has k disjoint Z1-Z2 paths, or some edge tt' on the t1-t2 path in T has |V_t cap V_{t'}| < k (Diestel, p. 335).

# Prerequisites
- **Tree-decomposition** — Lean is a strengthening property
- **Tree-width** — Lean decompositions of optimal width always exist

# Key Properties
1. Every graph has a lean tree-decomposition of width tw(G) (Theorem 12.3.10, Thomas 1990)
2. Parts are no larger than required by external connectivity
3. Branches are "stripped of unnecessary bulk"
4. This gives optimal tree-decompositions a useful extra property "for free"

# Context & Application
Lean tree-decompositions are a valuable tool: they combine optimal width with local connectivity guarantees.

# Relationships
## Builds Upon
- **Tree-decomposition** — Lean adds condition (T4)

# Source Reference
Chapter 12, Section 12.3, pages 335-336 (Theorem 12.3.10).

# Verification Notes
- Definition from p. 335
- Confidence: HIGH — explicit definition
