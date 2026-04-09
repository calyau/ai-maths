---
concept: Excluded Planar Minor Theorem
slug: excluded-planar-minor-theorem
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
  - "Robertson-Seymour 1986"
prerequisites:
  - grid-theorem
  - tree-width
  - graph-minor
extends: []
related:
  - forbidden-minor
contrasts_with: []
answers_questions:
  - "When does forbidding a minor bound tree-width?"
---

# Quick Definition
Given a graph H, the graphs without an H minor have bounded tree-width if and only if H is planar (Robertson-Seymour, 1986).

# Core Definition
**Theorem 12.4.3** (Robertson & Seymour 1986): Given a graph H, the graphs without an H minor have bounded tree-width if and only if H is planar (Diestel, p. 338).

# Prerequisites
- **Grid theorem** — Used in the proof: every planar graph is a minor of some grid
- **Tree-width** — Bounded tree-width is the conclusion
- **Graph minor** — The excluded minor condition

# Key Properties
1. If H is non-planar, Forb(H) contains all grids (which are planar), so tree-width is unbounded
2. If H is planar, H is a minor of some grid, so excluding H limits grid size, which limits tree-width
3. The proof reduces to the grid theorem

# Context & Application
This theorem completely characterizes which excluded minor conditions bound tree-width. It is a key structural result used in the proof of the graph minor theorem.

# Relationships
## Builds Upon
- **Grid theorem** — The key ingredient

## Enables
- **Erdős-Pósa property** for planar minors (Corollary 12.4.10)

# Source Reference
Chapter 12, Section 12.4, page 338 (Theorem 12.4.3).

# Verification Notes
- Statement from p. 338
- Confidence: HIGH — named theorem
