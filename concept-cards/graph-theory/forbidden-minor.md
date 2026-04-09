---
concept: Forbidden Minor
slug: forbidden-minor
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 337
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases:
  - "excluded minor"
  - "obstruction"
prerequisites:
  - graph-minor
  - minor-closed-property
extends: []
related:
  - kuratowski-set
  - graph-minor-theorem
contrasts_with: []
answers_questions:
  - "What is a forbidden minor?"
  - "How does tree-width relate to forbidden minors?"
---

# Quick Definition
For a set H of graphs, Forb(H) is the class of all graphs containing no minor from H. A graph property expressed by specifying forbidden minors is minor-closed, and conversely every minor-closed property can be so expressed.

# Core Definition
If H is any set of graphs, the class Forb_<=(H) := {G | G does not have H as minor for all H in H} is a graph property closed under isomorphism. When written this way, we say the property is expressed by specifying the graphs H in H as *forbidden* (or *excluded*) minors (Diestel, p. 337).

# Prerequisites
- **Graph minor** — Forbidden minors are excluded under the minor relation
- **Minor-closed property** — Properties expressible by forbidden minors

# Key Properties
1. Forb(H) is minor-closed (Proposition 1.7.3)
2. Every minor-closed property can be expressed by forbidden minors (Proposition 12.4.1)
3. By the graph minor theorem, every minor-closed property needs only finitely many forbidden minors
4. Examples: forests = Forb(K^3); tw < 3 = Forb(K^4); planar = Forb(K^5, K_{3,3})

# Context & Application
Forbidden minor characterizations are among the most attractive results in graph theory. Kuratowski's theorem (planarity), Wagner's theorem, and the tree-width characterizations are all examples.

# Examples
**Example 1** (p. 337): tw < 2 iff Forb(K^3) iff forest.

**Example 2** (p. 337): tw < 3 iff Forb(K^4) (Proposition 12.4.2).

# Relationships
## Builds Upon
- **Graph minor** — The ordering used for exclusion

## Enables
- **Kuratowski set** — The unique smallest set of forbidden minors

# Source Reference
Chapter 12, Section 12.4, pages 337-338.

# Verification Notes
- Definition from p. 337
- Confidence: HIGH — explicit definition
