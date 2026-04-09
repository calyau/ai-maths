---
concept: Capacity Function
slug: capacity-function
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 151
section: "6.2 Flows in networks"
extraction_confidence: high
aliases:
  - "capacity"
prerequisites:
  - network
  - directed-edge
related:
  - flow-in-network
  - cut-capacity
answers_questions:
  - "What is a capacity function in a network?"
---

# Quick Definition
A capacity function on a multigraph G is a map c: E-arrow -> N assigning a non-negative integer capacity to each directed edge, where the two directions of an edge may have different capacities.

# Core Definition
Given a multigraph G = (V, E), a **capacity function** is a map c: E-arrow -> N. It is defined independently for each direction of each edge, so c(e, x, y) and c(e, y, x) need not be equal. The capacity function is part of the definition of a network N = (G, s, t, c). (Diestel, p. 141)

# Prerequisites
- **Network** — Capacity functions are a component of networks
- **Directed edge** — Capacities are assigned to directed edges

# Key Properties
1. Values are non-negative integers
2. The two directions of an edge may have different capacities
3. Provides the upper bound constraint (F3) for network flows: f(e-arrow) <= c(e-arrow)
4. The capacity of a cut (S, S-bar) is c(S, S-bar) = sum of capacities from S to S-bar

# Context & Application
Capacity functions model the maximum throughput of each link in a network. They impose the physical constraint that no edge can carry more flow than its capacity allows.

# Relationships
## Enables
- **Flow in network** — Flows are constrained by capacity
- **Cut capacity** — Cut capacity is defined via the capacity function

# Source Reference
Chapter 6: Flows, Section 6.2, page 141 (pdf page 151).

# Verification Notes
- Definition: From p. 141
- Confidence: HIGH — explicit in the definition of a network
