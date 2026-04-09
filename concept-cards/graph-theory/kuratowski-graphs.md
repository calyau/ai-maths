---
concept: Kuratowski Graphs
slug: kuratowski-graphs
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.4 Planar graphs: Kuratowski's theorem"
extraction_confidence: high
aliases:
  - "K5"
  - "K33"
  - "K_{3,3}"
  - "forbidden minors for planarity"
prerequisites:
  - planar-graph
  - edge-bound-planar
extends: []
related:
  - kuratowski-theorem
contrasts_with: []
answers_questions:
  - "What are the Kuratowski graphs?"
  - "Why are K^5 and K_{3,3} not planar?"
---

# Quick Definition
The Kuratowski graphs are K^5 (complete graph on 5 vertices) and K_{3,3} (complete bipartite graph with parts of size 3). They are the two minimal non-planar graphs in the minor ordering.

# Core Definition
K^5 and K_{3,3} are the forbidden minors for planarity. K^5 has 5 vertices and 10 edges; K_{3,3} has 6 vertices and 9 edges. Neither can be drawn in the plane without edge crossings.

# Prerequisites
- **Planar graph** -- These graphs are the obstructions to planarity
- **Edge bound** -- Used to prove non-planarity

# Key Properties
1. K^5 has 10 edges; 10 > 3(5) - 6 = 9, so K^5 is non-planar
2. K_{3,3} has 9 edges and is triangle-free; 9 > 2(6) - 4 = 8, so K_{3,3} is non-planar
3. Both are minimal non-planar in the minor order
4. A graph is planar iff it contains neither as a minor (Kuratowski's theorem)
5. A graph contains K^5 or K_{3,3} as a minor iff it contains one as a topological minor (Lemma 4.4.2)

# Context & Application
K^5 and K_{3,3} are the two fundamental obstructions to planarity. They play an analogous role to odd cycles for bipartiteness -- they are the minimal "certificates of non-planarity." Every non-planar graph must contain at least one of them as a minor.

# Examples
**Example** (p. 92): K^5 non-planarity via edge count: 10 > 9.

**Example** (p. 92): K_{3,3} non-planarity via triangle-free edge count: 9 > 8.

# Relationships
## Enables
- **Kuratowski's theorem** -- These are the forbidden minors

# Source Reference
Chapter 4, Section 4.2 (non-planarity proofs, p. 92) and Section 4.4 (Kuratowski's theorem, pp. 97-101).

# Verification Notes
- Non-planarity proofs from p. 92
- Confidence: HIGH -- well-known classical objects
