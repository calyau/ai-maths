---
concept: Even Graph
slug: even-graph
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 160
section: "6.4 k-Flows for small k"
extraction_confidence: high
aliases:
  - "Eulerian graph"
prerequisites:
  - graph
  - vertex
related:
  - two-flow
  - four-flow
answers_questions:
  - "What is an even graph?"
---

# Quick Definition
An even graph is a graph in which all vertex degrees are even.

# Core Definition
A graph is called **even** if all its vertex degrees are even. This is equivalent to admitting a 2-flow (Proposition 6.4.1). (Diestel, p. 150)

# Prerequisites
- **Graph** — Even graphs are a class of graphs

# Key Properties
1. All vertex degrees are even
2. Admits a 2-flow
3. A graph has a 4-flow iff it is the union of two even subgraphs

# Relationships
## Related
- **Two-flow** — Even graphs are exactly those with a 2-flow
- **Four-flow** — Union of two even subgraphs characterizes 4-flows

# Source Reference
Chapter 6: Flows, Section 6.4, page 150 (pdf page 160).

# Verification Notes
- Confidence: HIGH — directly defined
