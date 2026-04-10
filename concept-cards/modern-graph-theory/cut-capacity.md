---
concept: Cut Capacity
slug: cut-capacity
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
  - "capacity of a cut"
prerequisites:
  - cut-separating-s-from-t
  - capacity-of-edge
extends: []
related:
  - max-flow-min-cut-theorem
  - flow-value
contrasts_with: []
answers_questions:
  - "What is the capacity of a cut?"
---

# Quick Definition
The capacity of a cut $\vec{E}(S, \overline{S})$ is the sum $c(S, \overline{S})$ of the capacities of all edges directed from $S$ to $\overline{S}$.

# Core Definition
Given a cut $\vec{E}(S, \overline{S})$ separating $s$ from $t$ in a directed graph with capacity function $c$, the capacity of the cut is $c(S, \overline{S}) = \sum_{\vec{xy} \in \vec{E}(S,\overline{S})} c(x,y)$. The capacity of every cut is at least as large as the value of any flow (Bollobás, p. 75).

# Prerequisites
- **Cut separating s from t** — The cut whose capacity is being measured
- **Capacity of an edge** — Individual edge capacities are summed

# Key Properties
1. Cut capacity is always at least as large as any flow value
2. The minimum cut capacity equals the maximum flow value (max-flow min-cut theorem)
3. Since there are finitely many cuts, a minimum capacity cut always exists
4. A cut with infinite capacity edges can still have finite capacity if only finitely many edges cross

# Construction / Recognition
1. Identify the cut $\vec{E}(S, \overline{S})$
2. Sum $c(x,y)$ over all directed edges from $S$ to $\overline{S}$

# Context & Application
Cut capacity provides the upper bound that matches flow value in the max-flow min-cut theorem. Finding the minimum cut capacity is equivalent to solving the maximum flow problem.

# Examples
**Example** (p. 75, Fig. III.1): A cut with capacity 12 is shown in the figure.

# Relationships
## Builds Upon
- **cut-separating-s-from-t** — The cut being measured
- **capacity-of-edge** — Summed to get cut capacity

## Enables
- **max-flow-min-cut-theorem** — Minimum cut capacity equals maximum flow

## Related
- **flow-value** — Bounded above by every cut capacity

# Common Errors
- **Error**: Including reverse-direction edge capacities in the cut capacity
  **Correction**: Only sum capacities of edges directed from $S$ to $\overline{S}$

# Common Confusions
- **Confusion**: Thinking cut capacity is the total capacity of all edges incident to the cut
  **Clarification**: Only edges crossing from $S$ to $\overline{S}$ contribute; edges from $\overline{S}$ to $S$ do not

# Source Reference
Chapter III, Section III.1, page 75.

# Verification Notes
- Definition source: Direct from p. 75
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
