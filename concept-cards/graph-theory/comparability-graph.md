---
concept: Comparability Graph
slug: comparability-graph
category: graph-colouring
subcategory: perfect-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.5 Perfect graphs"
extraction_confidence: medium
aliases: []
prerequisites:
  - graph
extends: []
related:
  - perfect-graph
  - interval-graph
  - chordal-graph
contrasts_with: []
answers_questions:
  - "What is a comparability graph?"
---

# Quick Definition
A comparability graph is a graph whose vertices can be partially ordered so that two vertices are adjacent if and only if they are comparable in the partial order.

# Core Definition
"A graph is called a comparability graph if there exists a partial ordering of its vertex set such that two vertices are adjacent if and only if they are comparable" (Diestel, p. 136, Exercise 38).

# Prerequisites
- **Graph**

# Key Properties
1. Every comparability graph is perfect (Exercise 38)
2. The complement of any interval graph is a comparability graph (Exercise 39)

# Context & Application
Comparability graphs arise in scheduling and order theory. Their perfection follows from Dilworth's theorem on partial orders.

# Relationships
## Related
- **Perfect graph** -- Comparability graphs are perfect
- **Interval graph** -- Complement of interval graph is a comparability graph

# Source Reference
Chapter 5, Section 5.5, Exercise 38, page 136.

# Verification Notes
- Definition from Exercise 38
- Confidence: MEDIUM -- defined in exercises, not main text
