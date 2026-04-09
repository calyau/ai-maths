---
concept: Density of a Pair
slug: density-of-pair
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 186
section: "7.4 Szemeredi's regularity lemma"
extraction_confidence: high
aliases:
  - "d(X,Y)"
  - "pair density"
prerequisites:
  - graph
  - edge
related:
  - epsilon-regular-pair
  - regularity-lemma
  - proportional-edge-density
answers_questions:
  - "What is the density of a pair of vertex sets?"
---

# Quick Definition
The density of a pair (X, Y) of disjoint vertex sets is d(X, Y) = ||X, Y|| / (|X| * |Y|), the proportion of possible X-Y edges that actually exist.

# Core Definition
Let G = (V, E) be a graph, and X, Y disjoint subsets of V. The **density** of the pair (X, Y) is d(X, Y) := ||X, Y|| / (|X| * |Y|), where ||X, Y|| is the number of X-Y edges. This is a real number between 0 and 1. (Diestel, p. 176)

# Prerequisites
- **Graph**, **Edge** — Density counts edges between vertex sets

# Key Properties
1. A real number in [0, 1]
2. d(X, Y) = 1 means complete bipartite between X and Y
3. d(X, Y) = 0 means no edges between X and Y
4. The key quantity in the definition of epsilon-regular pairs

# Relationships
## Enables
- **Epsilon-regular pair** — Regularity is defined in terms of density deviations

# Source Reference
Chapter 7, Section 7.4, page 176 (pdf page 186).

# Verification Notes
- Confidence: HIGH — explicitly defined with notation
