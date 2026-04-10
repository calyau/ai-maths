---
concept: Ford-Fulkerson Algorithm
slug: ford-fulkerson-algorithm
category: network-flows
subcategory: flow-algorithms
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.1 Flows in Directed Graphs"
extraction_confidence: medium
aliases:
  - "augmenting path algorithm"
  - "max-flow algorithm"
prerequisites:
  - max-flow-min-cut-theorem
  - augmenting-path
  - integrality-theorem
extends:
  - max-flow-min-cut-theorem
related:
  - flow-value
contrasts_with: []
answers_questions:
  - "How do I find a maximum flow in a network?"
---

# Quick Definition
The Ford-Fulkerson algorithm finds a maximum flow by starting from the zero flow and repeatedly augmenting along paths from source to sink until no augmenting path exists.

# Core Definition
The proof of the max-flow min-cut theorem provides an algorithm for integral capacities: start with the zero flow $f_0$, then construct an increasing sequence $f_0, f_1, f_2, \ldots$ of flows. Given $f_i$, compute the reachable set $S$ from $s$. If $t \notin S$, then $f_i$ is maximal and $\vec{E}(S, \overline{S})$ is a minimal cut. If $t \in S$, augment $f_i$ to $f_{i+1}$ by increasing flow along an augmenting path. Since each $v(f_i)$ is an integer, $v(f_{i+1}) \ge v(f_i) + 1$, so the sequence terminates in at most $\sum_{x,y} c(x,y)$ steps (Bollobás, p. 77).

# Prerequisites
- **Max-flow min-cut theorem** — The algorithm implements the proof
- **Augmenting path** — The mechanism for increasing flow
- **Integrality theorem** — Guarantees termination for integral capacities

# Key Properties
1. Terminates in at most $\sum c(x,y)$ steps for integral capacities
2. Produces both a maximal flow and a minimal cut simultaneously
3. The resulting maximal flow is integral when capacities are integral
4. The algorithm also produces a maximal acyclic flow

# Construction / Recognition
1. Initialize $f_0(x,y) = 0$ for all edges
2. Compute reachable set $S$ from $s$ (vertices reachable via residual capacity or backward flow)
3. If $t \notin S$: stop; $f$ is maximal, $\vec{E}(S, \overline{S})$ is a minimal cut
4. If $t \in S$: find augmenting path, compute bottleneck $\varepsilon$, update flow, repeat

# Context & Application
This is a constructive algorithm that simultaneously solves the maximum flow problem and finds a minimum cut. It is "a surprisingly efficient algorithm" for integral capacities (p. 77).

# Examples
**Example** (p. 77): For integral capacities, starting from the zero flow, each augmentation increases flow by at least 1. With total capacity $C = \sum c(x,y)$, the algorithm terminates in at most $C$ steps.

# Relationships
## Builds Upon
- **max-flow-min-cut-theorem** — The algorithm implements the proof
- **augmenting-path** — Used at each iteration

## Enables
- **integrality-theorem** — Demonstrated by the algorithm's construction

# Common Errors
- **Error**: Not considering backward edges when searching for augmenting paths
  **Correction**: The reachable set includes vertices reachable via backward flow reduction

# Common Confusions
- **Confusion**: Thinking the algorithm always terminates efficiently for non-integral capacities
  **Clarification**: For irrational capacities, the algorithm may not terminate; for integral capacities, it terminates in polynomial (in total capacity) steps

# Source Reference
Chapter III, Section III.1, pages 76-77.

# Verification Notes
- Definition source: Synthesized from the constructive proof of Theorem 1
- Confidence rationale: The algorithm is described explicitly but not named "Ford-Fulkerson" in the text
- Uncertainties: The name "Ford-Fulkerson" is attributed in the theorem statement
- Cross-reference status: Verified
