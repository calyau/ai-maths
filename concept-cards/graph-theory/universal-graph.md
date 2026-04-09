---
concept: Universal Graph
slug: universal-graph
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 223
section: "8.3 Homogeneous and universal graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - infinite-graph
extends: []
related:
  - rado-graph
  - homogeneous-graph
contrasts_with: []
answers_questions:
  - "What is a universal graph?"
---

# Quick Definition
A countable graph G* is universal in a class P (for a relation <=) if G* belongs to P and G <= G* for every countable G in P.

# Core Definition
If <= is a graph relation (such as the minor, topological minor, subgraph, or induced subgraph relation up to isomorphism), a countable graph G* is *universal* in P (for <=) if G* is in P and G <= G* for every countable graph G in P (Diestel, p. 223).

# Prerequisites
- **Infinite graph** — Universal graphs are infinite

# Key Properties
1. The Rado graph is universal in the class of all countable graphs for the induced subgraph relation
2. There is no universal planar graph for subgraphs or induced subgraphs
3. There is a universal planar graph for the minor relation (Theorem 8.3.4)
4. Most results for the induced subgraph relation are negative

# Context & Application
Universal graphs represent entire graph classes by a single specimen. From a graph-theoretic viewpoint, looking for universal graphs under weaker relations (minors) is more promising than under stronger relations (induced subgraphs).

# Examples
**Example 1** (p. 223): The Rado graph R is universal for all countable graphs.

**Example 2** (p. 226): There exists a universal planar graph for the minor relation (Diestel-Kühn 1999).

# Relationships
## Related
- **Rado graph** — Universal for countable graphs
- **Homogeneous graph** — Often also universal

# Source Reference
Chapter 8, Section 8.3, pages 223-226.

# Verification Notes
- Definition from p. 223
- Confidence: HIGH — explicit definition
