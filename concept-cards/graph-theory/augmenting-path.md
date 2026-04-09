---
concept: Augmenting Path
slug: augmenting-path
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 153
section: "6.2 Flows in networks"
extraction_confidence: high
aliases:
  - "augmenting walk"
prerequisites:
  - flow-in-network
  - capacity-function
related:
  - max-flow-min-cut-theorem
answers_questions:
  - "What is an augmenting path in network flow?"
---

# Quick Definition
An augmenting path (or walk) is an s-t walk in a network along which additional flow can be sent, because every edge along the walk has residual capacity.

# Core Definition
Given an integral flow f_n in a network N = (G, s, t, c), an **augmenting path** is an s-t walk W = x_0 e_0 ... e_{l-1} x_l where f_n(e_i-arrow) < c(e_i-arrow) for all i < l (where e_i-arrow = (e_i, x_i, x_{i+1})). The **residual capacity** (or increment) is epsilon = min{ c(e_i-arrow) - f_n(e_i-arrow) | i < l } > 0. (Diestel, p. 143)

# Prerequisites
- **Flow in network** — Augmenting paths modify an existing flow
- **Capacity function** — Residual capacity is the gap between flow and capacity

# Key Properties
1. Every edge along the walk has strictly positive residual capacity
2. The increment epsilon is the minimum residual capacity along the path
3. Pushing epsilon units along the walk increases the total flow value
4. When no augmenting path exists, the current flow is maximum

# Context & Application
Augmenting paths are the mechanism by which the Ford-Fulkerson algorithm increases flow. The absence of augmenting paths certifies optimality.

# Examples
**Example** (p. 143, Fig. 6.2.2): An augmenting path W with increment epsilon = 2, for flow f_n = 0 and capacities c = 3.

# Relationships
## Builds Upon
- **Flow in network** — Augmenting paths modify flows

## Enables
- **Max-flow min-cut theorem** — The proof uses repeated augmentation along such paths

# Source Reference
Chapter 6: Flows, Section 6.2, pages 143-144 (pdf pages 153-154). See Fig. 6.2.2.

# Verification Notes
- Confidence: HIGH — clearly described in the proof of Theorem 6.2.2
