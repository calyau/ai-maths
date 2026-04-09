---
concept: Grid Theorem
slug: grid-theorem
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 338
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases:
  - "excluded grid theorem"
  - "grid minor theorem"
prerequisites:
  - tree-width
  - graph-minor
extends: []
related:
  - bramble
  - excluded-planar-minor-theorem
contrasts_with: []
answers_questions:
  - "What is the grid theorem?"
  - "How does tree-width relate to grid minors?"
---

# Quick Definition
The grid theorem (Robertson-Seymour, 1986) states that for every integer r, there is an integer k such that every graph of tree-width at least k has an r x r grid minor. Large tree-width forces large grid minors.

# Core Definition
**Theorem 12.4.4** (Robertson & Seymour 1986): For every integer r there is an integer k such that every graph of tree-width at least k has an r x r grid minor (Diestel, p. 338).

# Prerequisites
- **Tree-width** — The hypothesis is large tree-width
- **Graph minor** — The conclusion is a grid minor

# Key Properties
1. The converse is also true: the k x k grid has tree-width k, so graphs with large grid minors have large tree-width
2. Combined with tree-width duality, gives three equivalent forms of "tree-like": small tree-width, small bramble order, no large grid minor
3. Implies Theorem 12.4.3: forbidding any planar H as minor bounds tree-width
4. The proof uses k-meshes, externally k-connected sets, and Lemma 12.4.9

# Context & Application
The grid theorem is one of the deepest results in the theory of graph minors. It identifies large grid minors as a canonical obstruction to small tree-width, connecting tree-width to topological/structural properties.

# Examples
**Example 1** (pp. 338-348): The full proof constructs either a K^m minor (from disjoint path systems) or an r x r grid (from intersecting path systems).

# Relationships
## Builds Upon
- **Tree-width** — Large tree-width is the hypothesis

## Enables
- **Excluded planar minor theorem** (12.4.3) — Forbidding a planar minor bounds tree-width
- **Erdős-Pósa property** for planar minors (Corollary 12.4.10)

# Source Reference
Chapter 12, Section 12.4, pages 338-348 (Theorem 12.4.4).

# Verification Notes
- Statement from p. 338
- Confidence: HIGH — named theorem with full proof
