---
concept: Cut Capacity
slug: cut-capacity
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
aliases:
  - "capacity of a cut"
prerequisites:
  - cut-in-network
  - capacity-function
related:
  - max-flow-min-cut-theorem
  - total-flow-value
answers_questions:
  - "What is the capacity of a cut?"
---

# Quick Definition
The capacity of a cut (S, S-bar) in a network is c(S, S-bar), the total capacity of all directed edges from S to S-bar.

# Core Definition
For a cut (S, S-bar) in a network N = (G, s, t, c), the **capacity** of the cut is c(S, S-bar) := sum of c(e-arrow) over all e-arrow in E-arrow(S, S-bar). This provides an upper bound on the total value of any flow: |f| <= c(S, S-bar). (Diestel, p. 142)

# Prerequisites
- **Cut in network** — Capacity is a property of cuts
- **Capacity function** — Values are summed from the capacity function

# Key Properties
1. Always non-negative (capacities are non-negative integers)
2. Provides an upper bound on flow value: |f| <= c(S, S-bar) for every flow f
3. The minimum capacity over all cuts equals the maximum flow value (max-flow min-cut theorem)

# Relationships
## Builds Upon
- **Cut in network** and **Capacity function**

## Enables
- **Max-flow min-cut theorem** — The minimum cut capacity equals the maximum flow

# Source Reference
Chapter 6: Flows, Section 6.2, page 142 (pdf page 152).

# Verification Notes
- Confidence: HIGH — directly defined in the source
