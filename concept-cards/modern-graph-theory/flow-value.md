---
concept: Flow Value
slug: flow-value
category: network-flows
subcategory: flow-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.1 Flows in Directed Graphs"
extraction_confidence: high
aliases:
  - "value of a flow"
  - "amount of flow"
  - "v(f)"
prerequisites:
  - flow-in-directed-graph
extends: []
related:
  - capacity-of-edge
  - cut-separating-s-from-t
contrasts_with: []
answers_questions:
  - "What is the value of a flow?"
  - "How is the amount of flow measured?"
---

# Quick Definition
The flow value $v(f)$ is the net current leaving the source $s$, which equals the net current entering the sink $t$.

# Core Definition
Given a flow $f$ from $s$ to $t$ in a directed graph, the value of $f$, denoted $v(f)$, is defined as $v(f) = \sum_{y \in \Gamma^+(s)} f(s,y) - \sum_{y \in \Gamma^-(s)} f(y,s) = \sum_{y \in \Gamma^-(t)} f(y,t) - \sum_{y \in \Gamma^+(t)} f(t,y)$. The equality of these two expressions follows from summing Kirchhoff's law over all intermediate vertices (Bollobás, p. 74).

# Prerequisites
- **Flow in a directed graph** — The flow value is a property of a flow

# Key Properties
1. $v(f)$ is a single real number characterizing the "strength" of a flow
2. Net outflow at source equals net inflow at sink
3. $v(f) \le \sum_{\vec{xy} \in \vec{E}} c(x,y)$ when capacities are finite
4. The supremum of flow values over all feasible flows is always attained

# Construction / Recognition
1. Compute the total flow on edges leaving $s$ minus total flow on edges entering $s$
2. Alternatively, compute total flow entering $t$ minus total flow leaving $t$
3. Both computations yield the same result

# Context & Application
The flow value quantifies how much "material" is transported from source to sink. Maximizing the flow value subject to capacity constraints is the central optimization problem addressed by the max-flow min-cut theorem.

# Examples
**Example** (p. 74): The equality $\sum_{y \in \Gamma^+(s)} f(s,y) - \sum_{y \in \Gamma^-(s)} f(y,s) = \sum_{y \in \Gamma^-(t)} f(y,t) - \sum_{y \in \Gamma^+(t)} f(t,y)$ is derived by summing the Kirchhoff equations over all intermediate vertices.

# Relationships
## Builds Upon
- **flow-in-directed-graph** — Flow value is defined for a given flow

## Enables
- **max-flow-min-cut-theorem** — Concerns maximizing flow value

## Related
- **capacity-of-edge** — Bounds the flow value
- **cut-separating-s-from-t** — Cut capacity bounds flow value

# Common Errors
- **Error**: Computing flow value by summing flow on all edges
  **Correction**: Flow value is the *net* outflow at the source (outflow minus inflow)

# Common Confusions
- **Confusion**: Believing every flow has a unique value for given capacities
  **Clarification**: Many different flows can exist; the max-flow min-cut theorem characterizes the maximum achievable value

# Source Reference
Chapter III, Section III.1, pages 74-75.

# Verification Notes
- Definition source: Direct from p. 74
- Confidence rationale: Explicitly defined with notation
- Uncertainties: None
- Cross-reference status: Verified
