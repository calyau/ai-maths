---
concept: Forest
slug: forest
category: paths-and-cycles
subcategory: trees-and-forests
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases:
  - acyclic graph
prerequisites:
  - graph
  - cycle
extends: []
related:
  - tree
  - component
contrasts_with: []
answers_questions:
  - "What is a forest?"
---

# Quick Definition

A forest is a graph without any cycles (an acyclic graph). A forest is a disjoint union of trees — each component of a forest is a tree.

# Core Definition

"A graph without any cycles is a forest, or an acyclic graph" (Bollobás, p. 14). A forest of order $n$ with $k$ components has size $n - k$ (Corollary 8). For every pair of distinct vertices, a forest contains at most one path between them (Theorem 5).

# Prerequisites

- **Graph** — A forest is a graph
- **Cycle** — A forest has no cycles

# Key Properties

1. No cycles
2. Each component is a tree
3. A forest of order $n$ with $k$ components has exactly $n - k$ edges (Corollary 8)
4. Between any two vertices, there is at most one path (Theorem 5)
5. A connected forest is a tree

# Construction / Recognition

## To recognize a forest
1. Verify there are no cycles
2. Equivalently, verify $e(G) = n - k$ where $k$ is the number of components

# Context & Application

Forests arise naturally as acyclic subgraphs. The forest in Fig. I.5 illustrates a bipartite graph that is a disjoint union of trees.

# Examples

**Example** (p. 14): Fig. I.5 shows a forest (which is also bipartite).

# Relationships

## Builds Upon
- **Graph**, **Cycle**

## Enables
- **Tree** — A connected forest

## Related
- **Component** — Each component of a forest is a tree

# Common Errors

- **Error**: Assuming a forest must be connected
  **Correction**: A forest may be disconnected; a connected forest is called a tree

# Common Confusions

- **Confusion**: Thinking "forest" means "collection of disjoint trees with at least two components"
  **Clarification**: A single tree is also a forest (a forest with one component)

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 14; Corollary 8, page 19.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
