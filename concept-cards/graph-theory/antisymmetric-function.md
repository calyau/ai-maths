---
concept: Antisymmetric Function
slug: antisymmetric-function
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 150
section: "6.1 Circulations"
extraction_confidence: high
aliases:
  - "condition F1"
prerequisites:
  - directed-edge
related:
  - circulation
  - flow-in-network
answers_questions:
  - "What is the antisymmetry condition for flows?"
---

# Quick Definition
A function f on directed edges is antisymmetric if f(e, x, y) = -f(e, y, x) for every edge e = xy with x != y; this is condition (F1) in the definition of circulations and flows.

# Core Definition
Condition **(F1)**: f(e, x, y) = -f(e, y, x) for all (e, x, y) in E-arrow with x != y. This ensures that the flow in one direction of an edge is the negative of the flow in the other direction. If f satisfies (F1), then f(X, X) = 0 for all X subset of V. (Diestel, p. 140)

# Prerequisites
- **Directed edge** — The function is defined on directed edges

# Key Properties
1. Ensures consistency: the two directions of an edge carry opposite flow values
2. Implies f(X, X) = 0 for all vertex subsets X
3. Shared by circulations, network flows, and all types of algebraic flows

# Relationships
## Enables
- **Circulation** — (F1) is one of two defining conditions
- **Flow in network** — (F1) is one of three defining conditions

# Source Reference
Chapter 6: Flows, Section 6.1, page 140 (pdf page 150).

# Verification Notes
- Confidence: HIGH — formal condition explicitly numbered
