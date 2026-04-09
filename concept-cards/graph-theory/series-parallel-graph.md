---
concept: Series-Parallel Graph
slug: series-parallel-graph
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 201
section: "Exercises"
extraction_confidence: medium
aliases:
  - "series-parallel multigraph"
prerequisites:
  - graph
related:
  - k4-minor-free-structure
answers_questions:
  - "What is a series-parallel graph?"
---

# Quick Definition
A multigraph is series-parallel if it can be constructed from K^2 by subdividing and doubling edges. A 2-connected multigraph is series-parallel iff it has no (topological) K^4 minor.

# Core Definition
A multigraph is called **series-parallel** if it can be constructed recursively from a K^2 by the operations of subdividing and of doubling edges. Exercise 32 states: a 2-connected multigraph is series-parallel if and only if it has no (topological) K^4 minor. (Diestel, p. 193, Exercise 32)

# Prerequisites
- **Graph** — Series-parallel graphs are a class of multigraphs

# Key Properties
1. Constructed by subdivision and edge-doubling from K^2
2. Characterized by absence of K^4 minor (for 2-connected graphs)
3. Related to the K^4-minor-free structure (Proposition 7.3.1)

# Source Reference
Chapter 7, Exercise 32, page 193 (pdf page 201).

# Verification Notes
- Confidence: MEDIUM — defined in exercises, characterization left as exercise
