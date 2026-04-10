---
concept: "Kuratowski's Theorem"
slug: kuratowskis-theorem
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases:
  - Kuratowski planarity criterion
prerequisites:
  - planar-graph
  - complete-graph
  - complete-bipartite-graph
  - subdivision
extends: []
related:
  - wagners-theorem
  - graph-minor
contrasts_with: []
answers_questions:
  - "How can planarity be characterized?"
  - "What is Kuratowski's theorem?"
---

# Quick Definition

Kuratowski's theorem (1930) states that a graph is planar if and only if it contains no subdivision of $K_5$ or $K_{3,3}$.

# Core Definition

"**Theorem 17.** A graph is planar iff it does not contain a subdivision of $K_5$ or $K_{3,3}$" (Bollobás, p. 32). This provides a complete characterization of planarity in terms of forbidden substructures.

# Prerequisites

- **Planar graph** — The property being characterized
- **Complete graph** — $K_5$ is one forbidden subdivision
- **Complete bipartite graph** — $K_{3,3}$ is the other
- **Subdivision** — The theorem uses subdivisions

# Key Properties

1. Two forbidden subdivisions suffice to characterize planarity
2. $K_5$ and $K_{3,3}$ are the minimal nonplanar graphs (in the subdivision sense)
3. Equivalent to Wagner's theorem (which uses minors instead of subdivisions)

# Construction / Recognition

## To test planarity using Kuratowski's theorem
1. Search for a subgraph that is a subdivision of $K_5$
2. Search for a subgraph that is a subdivision of $K_{3,3}$
3. The graph is planar iff neither is found

# Context & Application

Kuratowski's theorem is one of the most celebrated results in graph theory. It reduces planarity testing to a combinatorial condition. Wagner's equivalent formulation using minors (Theorem 18) led to the Robertson-Seymour graph minor theory.

# Examples

**Example** (p. 32): Fig. I.20 shows a graph $G$ containing $TK_5$ and a graph $H$ containing $TK_{3,3}$, both nonplanar.

# Relationships

## Builds Upon
- **Planar graph**, **Complete graph**, **Complete bipartite graph**, **Subdivision**

## Enables
- Planarity testing algorithms
- Foundation for graph minor theory

## Related
- **Wagner's theorem** — Equivalent formulation using minors

# Common Errors

- **Error**: Checking only for $K_5$ as a subgraph rather than $TK_5$ as a subgraph
  **Correction**: Must check for subdivisions of $K_5$ and $K_{3,3}$, not just the graphs themselves

# Common Confusions

- **Confusion**: Thinking Kuratowski's theorem requires both $TK_5$ and $TK_{3,3}$
  **Clarification**: A graph is nonplanar if it contains either $TK_5$ or $TK_{3,3}$ (or both)

# Source Reference

Chapter I: Fundamentals, Section I.4, Theorem 17, page 32.

# Verification Notes

- Definition source: Direct theorem statement from p. 32
- Confidence rationale: Explicitly stated (proof deferred)
- Uncertainties: None
- Cross-reference status: Verified
