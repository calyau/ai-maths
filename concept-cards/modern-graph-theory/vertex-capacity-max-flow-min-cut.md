---
concept: Max-Flow Min-Cut with Vertex Capacities
slug: vertex-capacity-max-flow-min-cut
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
  - "Theorem 4"
prerequisites:
  - max-flow-min-cut-theorem
  - vertex-capacity
  - vertex-cut
extends:
  - max-flow-min-cut-theorem
related:
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "How does max-flow min-cut work with vertex capacities?"
---

# Quick Definition
In a directed graph with capacity bounds on vertices (other than source and sink), the minimum vertex-cut capacity equals the maximum flow value from $s$ to $t$.

# Core Definition
**Theorem 4**: Let $\vec{G}$ be a directed graph with capacity bounds on the vertices other than the source $s$ and the sink $t$. Then the minimum of the capacity of a vertex-cut is equal to the maximum of the flow value from $s$ to $t$ (Bollobás, p. 79).

# Prerequisites
- **Max-flow min-cut theorem** — The edge-capacity version from which this is derived
- **Vertex capacity** — The constraints on vertices
- **Vertex-cut** — The dual structure to vertex-capacity flows

# Key Properties
1. Follows from the edge-capacity theorem via vertex-splitting
2. Edge-cuts of finite capacity in the split graph correspond to vertex-cuts in the original
3. Can be combined with edge capacities and multiple sources/sinks (Exercise 6)

# Construction / Recognition
1. Split each intermediate vertex $x$ into $x_-$ and $x_+$ with edge capacity $c(x)$
2. Apply the standard max-flow min-cut theorem to the split graph
3. Translate results back to the original graph

# Context & Application
This version of max-flow min-cut is the key tool for proving the vertex form of Menger's theorem, which concerns independent paths and vertex separators.

# Examples
**Example** (p. 79): The split graph $\vec{H}$ has only edges $\vec{x_-x_+}$ with finite capacities, so minimal edge-cuts in $\vec{H}$ consist entirely of such edges, corresponding to vertex-cuts in $\vec{G}$.

# Relationships
## Builds Upon
- **max-flow-min-cut-theorem** — Extended to vertex capacities

## Enables
- **mengers-theorem** — Vertex form follows directly

# Common Errors
- **Error**: Forgetting to split vertices before applying max-flow min-cut
  **Correction**: The reduction to edge capacities via vertex-splitting is essential

# Common Confusions
- **Confusion**: Thinking Theorems 1 and 4 are independent results
  **Clarification**: Theorem 4 follows from Theorem 1 via vertex-splitting; they can be combined into a single theorem

# Source Reference
Chapter III, Section III.1, page 79. Theorem 4.

# Verification Notes
- Definition source: Direct theorem statement from p. 79
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
