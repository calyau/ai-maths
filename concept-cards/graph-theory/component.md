---
concept: Component
slug: component

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 20
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "connected component"

prerequisites:
  - graph
  - connected-graph
  - subgraph
extends: []
related:
  - separator
contrasts_with: []

answers_questions:
  - "What is a component of a graph?"
---

# Quick Definition
A component of a graph G is a maximal connected subgraph. Components are always non-empty; the empty graph has no components.

# Core Definition
A maximal connected subgraph of G is called a component of G. Note that a component, being connected, is always non-empty; the empty graph, therefore, has no components (Diestel, p. 11).

# Prerequisites
- **Graph** — components partition the vertex set of a graph
- **Connected graph** — components are maximal connected subgraphs
- **Subgraph** — components are subgraphs

# Key Properties
1. The components of G partition V(G) (Exercise 9)
2. A graph is connected if and only if it has exactly one component
3. Components are non-empty by definition
4. Each vertex belongs to exactly one component

# Context & Application
Components decompose a disconnected graph into its connected pieces.

# Examples
**Example** (p. 11): Fig. 1.4.1 shows a graph with three components.

# Relationships
## Builds Upon
- **connected-graph**, **subgraph**

# Source Reference
Chapter 1: The Basics, Section 1.4, page 11 (pdf p. 21). See Fig. 1.4.1.

# Verification Notes
- Direct from p. 11
- Confidence: HIGH
