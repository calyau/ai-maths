---
concept: Augmenting Path
slug: augmenting-path
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
  - "flow-augmenting path"
prerequisites:
  - flow-in-directed-graph
  - capacity-of-edge
  - max-flow-min-cut-theorem
extends: []
related:
  - integrality-theorem
  - ford-fulkerson-algorithm
contrasts_with: []
answers_questions:
  - "How do I find a maximum flow in a network?"
---

# Quick Definition
An augmenting path is a sequence of vertices $x_0 = s, x_1, \ldots, x_\ell = t$ along which the flow can be increased, either by pushing more flow forward on under-capacity edges or by reducing flow backward on positive-flow edges.

# Core Definition
In the proof of the max-flow min-cut theorem, if $t$ belongs to the reachable set $S$ from $s$, there exist vertices $x_0 = s, x_1, \ldots, x_\ell = t$ such that $\varepsilon_i = \max\{c(x_i, x_{i+1}) - f(x_i, x_{i+1}), f(x_{i+1}, x_i)\} > 0$ for every $i$. Setting $\varepsilon = \min_i \varepsilon_i$, the flow can be augmented: increase forward flow by $\varepsilon$ where residual capacity exists, or decrease backward flow by $\varepsilon$ where positive backward flow exists. The new flow $f^*$ has value $v(f^*) = v(f) + \varepsilon$ (Bollobás, p. 76).

# Prerequisites
- **Flow in a directed graph** — The flow being augmented
- **Capacity of an edge** — Determines residual capacity
- **Max-flow min-cut theorem** — Augmenting paths arise in the proof

# Key Properties
1. An augmenting path exists if and only if the current flow is not maximal
2. Each augmentation strictly increases the flow value
3. For integral capacities, each augmentation increases flow by at least 1
4. The path may use edges in both forward and backward directions

# Construction / Recognition
1. Build the reachable set $S$ from $s$: add $y$ to $S$ if $c(x,y) > f(x,y)$ or $f(y,x) > 0$ for some $x \in S$
2. If $t \in S$, trace back through the construction to find the path
3. Compute $\varepsilon = \min_i \varepsilon_i$ along the path
4. Update flow values along the path

# Context & Application
Augmenting paths form the basis of the Ford-Fulkerson algorithm for computing maximum flows. The concept is central to converting the existence proof of the max-flow min-cut theorem into a practical algorithm.

# Examples
**Example** (p. 76): Starting from the zero flow with integral capacities, repeatedly find augmenting paths and increase flow. The process terminates in at most $\sum c(x,y)$ steps since each step increases the integral flow by at least 1.

# Relationships
## Builds Upon
- **flow-in-directed-graph** — Augmenting a flow
- **max-flow-min-cut-theorem** — Augmenting paths arise in the proof

## Enables
- **ford-fulkerson-algorithm** — Based on repeated augmentation
- **integrality-theorem** — Integral augmentations preserve integrality

# Common Errors
- **Error**: Only considering forward edges for augmentation
  **Correction**: Backward edges with positive flow can also be used to reroute flow

# Common Confusions
- **Confusion**: Thinking an augmenting path must be a directed path in the original graph
  **Clarification**: An augmenting path can traverse edges backward (reducing flow) as well as forward (increasing flow)

# Source Reference
Chapter III, Section III.1, pages 76-77.

# Verification Notes
- Definition source: Synthesized from proof of Theorem 1
- Confidence rationale: The concept is described in the proof but not given a formal standalone definition
- Uncertainties: The term "augmenting path" is used implicitly rather than formally defined
- Cross-reference status: Verified
