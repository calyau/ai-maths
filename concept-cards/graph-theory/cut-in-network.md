---
concept: Cut in a Network
slug: cut-in-network
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
  - "network cut"
  - "s-t cut"
prerequisites:
  - network
  - capacity-function
related:
  - flow-in-network
  - total-flow-value
  - max-flow-min-cut-theorem
  - cut-capacity
answers_questions:
  - "What is a cut in a network?"
---

# Quick Definition
A cut in a network N is a partition (S, S-bar) of the vertex set where the source s is in S and the sink t is in S-bar.

# Core Definition
Let f be a flow in a network N = (G, s, t, c). If S is a subset of V such that s is in S and t is in S-bar (= V \ S), we call the pair (S, S-bar) a **cut in N**, and c(S, S-bar) the **capacity** of this cut. (Diestel, p. 142)

# Prerequisites
- **Network** — Cuts are defined within networks
- **Capacity function** — The capacity of a cut is computed from the capacity function

# Key Properties
1. Source s must be in S, sink t must be in S-bar
2. The capacity c(S, S-bar) is the sum of capacities from S to S-bar
3. The total flow value equals f(S, S-bar) for every cut (Proposition 6.2.1)
4. |f| <= c(S, S-bar) for every cut and every flow f

# Context & Application
Cuts represent bottlenecks in a network. The minimum capacity cut determines the maximum possible flow, as stated by the max-flow min-cut theorem.

# Relationships
## Builds Upon
- **Network** — Cuts partition the vertex set of a network

## Enables
- **Max-flow min-cut theorem** — Relates minimum cuts to maximum flows
- **Cut capacity** — The capacity of a cut bounds the flow value

# Source Reference
Chapter 6: Flows, Section 6.2, page 142 (pdf page 152).

# Verification Notes
- Definition: Directly from p. 142
- Confidence: HIGH — explicit definition
