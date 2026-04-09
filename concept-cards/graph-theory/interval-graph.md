---
concept: Interval Graph
slug: interval-graph
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
  - chordal-graph
  - comparability-graph
contrasts_with: []
answers_questions:
  - "What is an interval graph?"
---

# Quick Definition
An interval graph is a graph where each vertex corresponds to a real interval, and two vertices are adjacent if and only if their intervals intersect.

# Core Definition
"A graph G is called an interval graph if there exists a set {I_v | v in V(G)} of real intervals such that I_u intersection I_v != empty iff uv in E(G)" (Diestel, p. 136, Exercise 39).

# Prerequisites
- **Graph**

# Key Properties
1. Every interval graph is chordal (Exercise 39(i))
2. The complement of every interval graph is a comparability graph (Exercise 39(ii))
3. A chordal graph is an interval graph iff its complement is a comparability graph (Gilmore-Hoffman 1964)
4. Interval graphs are perfect (since they are chordal)

# Relationships
## Related
- **Chordal graph** -- Interval graphs are a subclass
- **Comparability graph** -- Complement of interval graph
- **Perfect graph** -- Interval graphs are perfect

# Source Reference
Chapter 5, Section 5.5, Exercise 39, page 136.

# Verification Notes
- Definition from Exercise 39
- Confidence: MEDIUM -- defined in exercises
