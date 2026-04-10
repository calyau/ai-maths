---
concept: Component
slug: component
category: graph-fundamentals
subcategory: connectivity
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
  - connected component
prerequisites:
  - graph
  - connected-graph
extends: []
related:
  - cutvertex
  - bridge
contrasts_with: []
answers_questions:
  - "What is a component of a graph?"
---

# Quick Definition

A component of a graph is a maximal connected subgraph. Every graph is the vertex-disjoint union of its components.

# Core Definition

"A maximal connected subgraph is a component of the graph" (Bollobás, p. 14). Theorem 3 establishes that components correspond to equivalence classes under the reachability relation, and every vertex belongs to exactly one component.

# Prerequisites

- **Graph** — Components are defined for graphs
- **Connected graph** — A component is a maximal connected subgraph

# Key Properties

1. Every vertex belongs to exactly one component
2. Every graph is the vertex-disjoint union of its components
3. A graph is connected iff it has exactly one component
4. An edge is a bridge iff its deletion increases the number of components
5. A vertex is a cutvertex iff its deletion increases the number of components

# Construction / Recognition

Use Theorem 3: for any vertex $x$, the component containing $x$ is $W = \{y \in G : d(x, y) < \infty\}$.

# Context & Application

Components partition a graph into its connected pieces. Many graph-theoretic results can be proved by first considering the connected case and then extending to general graphs by treating each component separately.

# Examples

**Example** (p. 14): A forest consists of multiple components, each of which is a tree.

# Relationships

## Builds Upon
- **Graph**, **Connected graph**

## Enables
- **Cutvertex** — Deletion increases component count
- **Bridge** — Deletion increases component count
- **Forest** — Each component is a tree

# Common Errors

- **Error**: Thinking components can share vertices
  **Correction**: Components are vertex-disjoint by definition

# Common Confusions

- **Confusion**: Confusing component with subgraph
  **Clarification**: A component is a maximal connected subgraph; not every subgraph is a component

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, pages 14-15; Theorem 3, page 16.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
