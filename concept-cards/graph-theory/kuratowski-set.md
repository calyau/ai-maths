---
concept: Kuratowski Set
slug: kuratowski-set
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 352
section: "12.5 The graph minor theorem"
extraction_confidence: high
aliases:
  - "obstruction set"
  - "K_P"
prerequisites:
  - minor-closed-property
  - graph-minor-theorem
extends: []
related:
  - forbidden-minor
  - finite-basis-theorem
contrasts_with: []
answers_questions:
  - "What is the Kuratowski set for a minor-closed property?"
  - "What is the obstruction set?"
---

# Quick Definition
The Kuratowski set K_P for a minor-closed property P is the set of all graphs that are minimal (under the minor relation) in the complement of P. It is the unique smallest set of forbidden minors characterizing P.

# Core Definition
For a minor-closed property P, the *Kuratowski set* K_P := {H | H is <=-minimal in the complement of P} satisfies P = Forb(K_P) and is contained in every other set H such that P = Forb(H). By the graph minor theorem, K_P is always finite (Corollary 12.5.2) (Diestel, p. 352).

# Prerequisites
- **Minor-closed property** — K_P is defined for minor-closed properties
- **Graph minor theorem** — Guarantees K_P is finite

# Key Properties
1. K_P uniquely determines P
2. K_P is finite (by the graph minor theorem)
3. Elements of K_P are pairwise incomparable under the minor relation
4. Examples: K_{planarity} = {K^5, K_{3,3}}; K_{tw<3} = {K^4}; K_{tw<4} = {K^5, octahedron, 5-prism, Wagner graph}

# Context & Application
Kuratowski sets provide the most elegant characterizations of minor-closed properties. Finding the explicit Kuratowski set for a given surface is a major research problem; it has been done only for the sphere (Kuratowski's theorem) and the projective plane (35 forbidden minors).

# Examples
**Example 1** (p. 352): For planarity, K_P = {K^5, K_{3,3}}.

**Example 2** (p. 366): For the projective plane, K_P has 35 elements (Archdeacon, 1981).

# Relationships
## Builds Upon
- **Minor-closed property** and **Graph minor theorem**

## Related
- **Forbidden minor** — Elements of K_P

# Source Reference
Chapter 12, Section 12.5, pages 352-353.

# Verification Notes
- Definition from pp. 352-353
- Confidence: HIGH — explicit definition
