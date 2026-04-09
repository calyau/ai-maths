---
concept: Integral Flow
slug: integral-flow
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 152
section: "6.2 Flows in networks"
extraction_confidence: high
aliases: []
prerequisites:
  - flow-in-network
related:
  - integral-flow-theorem
  - max-flow-min-cut-theorem
answers_questions:
  - "What is an integral flow?"
---

# Quick Definition
A flow f in a network is integral if all its values f(e-arrow) are integers.

# Core Definition
A flow f in a network N is called **integral** if all its values are integers. The integral flow theorem (Corollary 6.2.3) guarantees that with integral capacities, a maximum flow can always be chosen to be integral. The Ford-Fulkerson algorithm naturally produces integral flows when started from the zero flow with integral capacities. (Diestel, p. 142)

# Prerequisites
- **Flow in network** — Integrality is a property of flows

# Key Properties
1. Integer values on all directed edges
2. Integral capacities guarantee existence of integral maximum flows
3. The total value |f| of an integral flow is an integer
4. Essential for combinatorial applications (matchings, disjoint paths)

# Source Reference
Chapter 6, Section 6.2, page 142 (pdf page 152).

# Verification Notes
- Confidence: HIGH — explicitly defined
