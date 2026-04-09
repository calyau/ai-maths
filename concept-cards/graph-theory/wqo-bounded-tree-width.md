---
concept: WQO for Bounded Tree-Width
slug: wqo-bounded-tree-width
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 331
section: "12.3 Tree-decompositions"
extraction_confidence: high
aliases:
  - "Theorem 12.3.7"
prerequisites:
  - tree-width
  - well-quasi-ordering
  - kruskals-tree-theorem
extends:
  - kruskals-tree-theorem
related:
  - graph-minor-theorem
contrasts_with: []
answers_questions:
  - "Are graphs of bounded tree-width well-quasi-ordered?"
---

# Quick Definition
For every integer k > 0, the graphs of tree-width < k are well-quasi-ordered by the minor relation (Robertson-Seymour, 1990).

# Core Definition
**Theorem 12.3.7** (Robertson & Seymour 1990): For every integer k > 0, the graphs of tree-width < k are well-quasi-ordered by the minor relation (Diestel, p. 331).

# Prerequisites
- **Tree-width** — The bounding parameter
- **Well-quasi-ordering** — The property being established
- **Kruskal's tree theorem** — The proof generalizes Kruskal's approach

# Key Properties
1. The proof iterates the "minimal bad sequence" argument tw(G) times
2. This is a step towards the full graph minor theorem
3. Combined with the grid theorem, helps prove Corollary 12.5.3

# Context & Application
This theorem is a key intermediate result between Kruskal's tree theorem and the full graph minor theorem. It handles all graphs that are "almost tree-like" in the sense of bounded tree-width.

# Relationships
## Builds Upon
- **Kruskal's tree theorem** — The tree case (tw = 1)

## Enables
- **Corollary 12.5.3** — Finitely many forbidden minors for each surface
- **Graph minor theorem** — A step in the proof

# Source Reference
Chapter 12, Section 12.3, page 331 (Theorem 12.3.7).

# Verification Notes
- Statement from p. 331
- Confidence: HIGH — named theorem
