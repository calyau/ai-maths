---
concept: Max-Flow Min-Cut with Multiple Sources and Sinks
slug: multiple-sources-sinks-max-flow
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
  - "Theorem 3"
  - "multi-source multi-sink max-flow"
prerequisites:
  - max-flow-min-cut-theorem
extends:
  - max-flow-min-cut-theorem
related:
  - cut-separating-s-from-t
contrasts_with: []
answers_questions:
  - "How does max-flow min-cut generalize to multiple sources and sinks?"
---

# Quick Definition
The maximum flow from a set of sources to a set of sinks equals the minimum capacity of a cut separating all sources from all sinks.

# Core Definition
**Theorem 3**: The maximum of the flow value from a set of sources to a set of sinks is equal to the minimum of the capacities of cuts separating the sources from the sinks (Bollobás, p. 78). The reduction to the single-source single-sink case is achieved by adding a super-source $s$ connected to each source $s_i$ with infinite capacity, and a super-sink $t$ connected from each sink $t_j$ with infinite capacity.

# Prerequisites
- **Max-flow min-cut theorem** — The single-source case from which this is derived

# Key Properties
1. A cut must place all sources on one side and all sinks on the other
2. Reduced to single-source single-sink by adding super-source and super-sink with infinite capacity edges
3. Finite-capacity cuts in the extended graph correspond exactly to cuts in the original graph

# Construction / Recognition
1. Add new source $s$ with edges $\vec{ss_i}$ of infinite capacity to each source $s_i$
2. Add new sink $t$ with edges $\vec{t_jt}$ of infinite capacity from each sink $t_j$
3. Apply the standard max-flow min-cut theorem in the extended graph

# Context & Application
Many practical flow problems have multiple sources and sinks. This extension shows they reduce to the basic single-source single-sink case.

# Examples
**Example** (p. 78): Given sources $s_1, \ldots, s_k$ and sinks $t_1, \ldots, t_l$, add super-source $s$ and super-sink $t$. A finite-capacity cut in the extended graph cannot contain infinite-capacity edges, so it corresponds to a cut in the original graph.

# Relationships
## Builds Upon
- **max-flow-min-cut-theorem** — Extended to multiple sources/sinks

## Enables
- **mengers-theorem** — The set-to-set version

# Common Errors
- **Error**: Defining a cut that separates some but not all sources from some sinks
  **Correction**: A valid cut must have all sources on one side and all sinks on the other

# Common Confusions
- **Confusion**: Thinking multi-source multi-sink requires a fundamentally different theory
  **Clarification**: It reduces cleanly to the single-source single-sink case

# Source Reference
Chapter III, Section III.1, page 78. Theorem 3.

# Verification Notes
- Definition source: Direct theorem statement from p. 78
- Confidence rationale: Explicitly stated with proof sketch
- Uncertainties: None
- Cross-reference status: Verified
