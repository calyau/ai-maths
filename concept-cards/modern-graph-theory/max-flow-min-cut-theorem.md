---
concept: Max-Flow Min-Cut Theorem
slug: max-flow-min-cut-theorem
category: network-flows
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.1 Flows in Directed Graphs"
extraction_confidence: high
aliases:
  - "Ford-Fulkerson theorem"
  - "max flow min cut"
  - "Theorem 1"
prerequisites:
  - flow-in-directed-graph
  - flow-value
  - capacity-of-edge
  - cut-separating-s-from-t
  - cut-capacity
extends: []
related:
  - integrality-theorem
  - augmenting-path
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "How does the max-flow min-cut theorem connect flows and cuts?"
  - "How do I apply the max-flow min-cut theorem?"
---

# Quick Definition
The maximal flow value from $s$ to $t$ equals the minimum capacity of a cut separating $s$ from $t$. This is the cornerstone of the theory of flows, connectivity, and matching.

# Core Definition
**Theorem 1** (Max-Flow Min-Cut Theorem, Ford and Fulkerson, 1962): The maximal flow value from $s$ to $t$ is equal to the minimum of the capacities of cuts separating $s$ from $t$. The theorem remains valid if some edges have infinite capacity but the maximal flow value is finite (Bollobás, p. 76).

# Prerequisites
- **Flow in a directed graph** — Defines what a flow is
- **Flow value** — The quantity being maximized
- **Capacity of an edge** — Constrains flow on each edge
- **Cut separating s from t** — The structure whose capacity is minimized
- **Cut capacity** — The quantity being minimized

# Key Properties
1. $\max_f v(f) = \min_S c(S, \overline{S})$ over all flows $f$ and all cuts $\vec{E}(S, \overline{S})$
2. The proof is constructive: given a maximal flow, the minimal cut is explicitly constructed
3. The theorem provides an efficient algorithm for integral capacities
4. The result implies the integrality theorem and Menger's theorem as corollaries
5. Extends to multiple sources and sinks (Theorem 3)

# Construction / Recognition
## To Find Maximum Flow and Minimum Cut
1. Start with the zero flow $f_0$
2. Define the reachable set $S$: let $s \in S$; if $x \in S$ and either $c(x,y) > f(x,y)$ or $f(y,x) > 0$, add $y$ to $S$
3. If $t \notin S$, then $f$ is maximal and $\vec{E}(S, \overline{S})$ is a minimal cut
4. If $t \in S$, find an augmenting path and increase the flow, then repeat

# Context & Application
The max-flow min-cut theorem is described as "the cornerstone of the theory to be presented in this chapter" (p. 76). It implies Menger's theorem on connectivity and Hall's marriage theorem on matchings. The proof also yields an algorithm for constructing maximum flows.

# Examples
**Example** (p. 75, Fig. III.1): A directed graph with edge capacities is shown; a cut with capacity 12 is identified. The max-flow min-cut theorem states the maximum flow equals this minimum cut capacity.

**Algorithmic example** (p. 76): For integral capacities, starting from the zero flow, successively augment along paths from $s$ to $t$. Each augmentation increases flow by at least 1, so the process terminates in at most $\sum c(x,y)$ steps.

# Relationships
## Builds Upon
- **flow-in-directed-graph** — The flow framework
- **cut-separating-s-from-t** — The dual structure

## Enables
- **mengers-theorem** — Deduced as a corollary
- **halls-theorem** — Follows from max-flow min-cut
- **integrality-theorem** — Integral capacities yield integral maximal flows
- **vertex-capacity-max-flow-min-cut** — Extension to vertex capacities

## Related
- **augmenting-path** — Used in the constructive proof

# Common Errors
- **Error**: Claiming the maximal flow or minimal cut is unique
  **Correction**: The theorem guarantees existence of optimal values, not uniqueness of the flow or cut achieving them

# Common Confusions
- **Confusion**: Thinking the theorem only applies to graphs with finite capacities
  **Clarification**: The theorem holds when some edges have infinite capacity, provided the maximal flow value is finite

# Source Reference
Chapter III, Section III.1, pages 75-77. Theorem 1.

# Verification Notes
- Definition source: Direct quote of theorem statement, p. 76
- Confidence rationale: Major theorem with full proof in source
- Uncertainties: None
- Cross-reference status: Verified
