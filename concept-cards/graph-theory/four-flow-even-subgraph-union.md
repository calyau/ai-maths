---
concept: 4-Flow as Union of Even Subgraphs
slug: four-flow-even-subgraph-union
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 161
section: "6.4 k-Flows for small k"
extraction_confidence: high
aliases:
  - "Proposition 6.4.5(i)"
prerequisites:
  - four-flow
  - even-graph
  - two-flow
related:
  - cubic-four-flow-three-edge-colouring
answers_questions:
  - "When does a graph have a 4-flow in terms of even subgraphs?"
---

# Quick Definition
A graph has a 4-flow if and only if it is the union of two even subgraphs (Proposition 6.4.5(i)).

# Core Definition
**Proposition 6.4.5(i)**: A graph has a 4-flow if and only if it is the union of two even subgraphs. This follows from the observation that a Z_2^2-flow decomposes into two Z_2 components, each defining an even subgraph. (Diestel, p. 152)

# Prerequisites
- **Four-flow** — The characterization is about 4-flows
- **Even graph** — The components of the decomposition
- **Two-flow** — Each even subgraph admits a 2-flow

# Key Properties
1. Decomposes 4-flow existence into a structural condition
2. Uses the Klein four-group Z_2^2 isomorphism

# Source Reference
Chapter 6, Section 6.4, Proposition 6.4.5(i), page 152 (pdf page 162).

# Verification Notes
- Confidence: HIGH — characterization with proof
