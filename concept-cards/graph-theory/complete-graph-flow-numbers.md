---
concept: Flow Numbers of Complete Graphs
slug: complete-graph-flow-numbers
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 160
section: "6.4 k-Flows for small k"
extraction_confidence: high
aliases: []
prerequisites:
  - flow-number
  - k-flow
  - two-flow
  - three-flow
  - four-flow
related: []
answers_questions:
  - "What are the flow numbers of complete graphs?"
---

# Quick Definition
phi(K^n) = 2 for odd n > 1; phi(K^2) = infinity; phi(K^4) = 4; phi(K^n) = 3 for even n > 4.

# Core Definition
The flow numbers of complete graphs:
- phi(K^1) = 1 (no edges)
- phi(K^2) = infinity (has a bridge)
- phi(K^n) = 2 for odd n > 1 (all degrees even, by Proposition 6.4.1)
- phi(K^4) = 4 (the unique complete graph with flow number 4)
- phi(K^n) = 3 for all even n > 4 (Proposition 6.4.3) (Diestel, p. 150)

# Prerequisites
- **Flow number**, **k-flow** — The flow number phi(G)

# Key Properties
1. K^4 is uniquely the complete graph with flow number 4
2. All other K^n (except K^2) have flow number 2 or 3
3. The proof for even n > 4 uses induction and edge-disjoint decomposition

# Source Reference
Chapter 6, Section 6.4, page 150 (pdf page 160). Propositions 6.4.1, 6.4.3.

# Verification Notes
- Confidence: HIGH — explicit computation in text
