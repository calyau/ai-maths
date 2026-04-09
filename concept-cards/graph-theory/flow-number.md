---
concept: Flow Number
slug: flow-number
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 157
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases:
  - "phi(G)"
prerequisites:
  - k-flow
related:
  - five-flow-conjecture
  - four-flow-conjecture
  - three-flow-conjecture
  - six-flow-theorem
  - flow-colouring-duality
answers_questions:
  - "What is the flow number of a graph?"
---

# Quick Definition
The flow number phi(G) of a multigraph G is the least integer k such that G admits a k-flow; if no k-flow exists, phi(G) = infinity.

# Core Definition
The **flow number** of G, denoted phi(G), is the least integer k >= 1 such that G admits a k-flow. If G has no k-flow for any k, we put phi(G) := infinity. A graph has finite flow number if and only if it is bridgeless. (Diestel, p. 147)

# Prerequisites
- **k-flow** — Flow number is defined in terms of k-flows

# Key Properties
1. phi(G) = infinity iff G has a bridge
2. phi(G) = 1 iff G has no edges
3. phi(G) = 2 iff all degrees are even (Proposition 6.4.1)
4. For bridgeless graphs, phi(G) <= 6 (Seymour's 6-flow theorem)
5. phi(G/e) <= phi(G) for every edge e
6. For odd n > 1: phi(K^n) = 2; phi(K^4) = 4; phi(K^n) = 3 for even n > 4

# Context & Application
Determining flow numbers leads to some of the deepest open problems in graph theory, encapsulated in Tutte's three flow conjectures: the 3-flow, 4-flow, and 5-flow conjectures.

For planar graphs, the flow-colouring duality theorem (6.5.3) states that chi(G) = phi(G*), connecting flow numbers to chromatic numbers.

# Relationships
## Builds Upon
- **k-flow** — The flow number is the minimum k for a k-flow

## Related
- **Five-flow conjecture**, **Four-flow conjecture**, **Three-flow conjecture** — Conjectures about upper bounds on flow numbers
- **Flow-colouring duality** — Connects flow number to chromatic number for planar graphs

# Source Reference
Chapter 6: Flows, Section 6.3, page 147 (pdf page 157). Flow numbers of complete graphs on p. 150.

# Verification Notes
- Confidence: HIGH — explicitly defined with explicit notation
