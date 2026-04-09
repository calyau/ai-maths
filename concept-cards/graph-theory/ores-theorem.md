---
concept: "Ore's Theorem"
slug: ores-theorem
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 289
section: "10.2 Hamilton cycles and degree sequences"
extraction_confidence: medium
aliases:
  - "Ore 1960"
prerequisites:
  - hamiltonian-graph
  - degree-sequence
extends:
  - diracs-theorem
related:
  - chvatals-theorem
contrasts_with: []
answers_questions:
  - "What is Ore's theorem?"
---

# Quick Definition
If G has n >= 3 vertices and d(x) + d(y) >= n for every pair of non-adjacent vertices x, y, then G has a Hamilton cycle.

# Core Definition
**Ore's theorem** states that a graph G on n >= 3 vertices is Hamiltonian if d(x) + d(y) >= n for every pair of non-adjacent vertices x, y. This is a special case of Chvatal's theorem (Diestel, p. 289-290, implicit in the development).

# Prerequisites
- **Hamiltonian graph** — the conclusion
- **Degree sequence** — Ore's condition is on degree sums

# Key Properties
1. Strictly generalizes Dirac's theorem (delta >= n/2 implies d(x)+d(y) >= n)
2. A special case of Chvatal's theorem
3. Used in the proof of Chvatal's theorem (the proof considers non-adjacent pairs with maximum d(x)+d(y))
4. The condition only applies to non-adjacent pairs

# Context & Application
Ore's theorem is intermediate between Dirac and Chvatal in generality. It considers pairs of non-adjacent vertices rather than just the minimum degree, providing a finer condition.

# Examples
**Example**: A graph where two non-adjacent vertices have degrees 2 and n-3 (sum n-1 < n) might not be Hamiltonian, even if all other pairs satisfy Ore's condition.

# Relationships
## Builds Upon
- **Dirac's theorem** — Ore generalizes Dirac

## Enables
- **Chvatal's theorem** — further generalization

# Source Reference
Chapter 10, Section 10.2 context. Ore's theorem is subsumed by Chvatal's Theorem 10.2.1.

# Verification Notes
- Implicit in the development of Section 10.2
- Confidence: MEDIUM — not separately stated as a theorem in this text
