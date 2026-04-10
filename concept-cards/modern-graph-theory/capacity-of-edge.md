---
concept: Capacity of an Edge
slug: capacity-of-edge
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
  - "edge capacity"
  - "capacity function"
  - "c(x,y)"
prerequisites:
  - flow-in-directed-graph
extends: []
related:
  - flow-value
  - cut-capacity
contrasts_with:
  - vertex-capacity
answers_questions:
  - "What is the capacity of an edge in a flow network?"
---

# Quick Definition
The capacity $c(x,y)$ of a directed edge $\vec{xy}$ is a non-negative number representing the maximum flow that the edge can carry.

# Core Definition
Given a directed graph $\vec{G} = (V, \vec{E})$ with source $s$ and sink $t$, each edge $\vec{xy}$ is assigned a non-negative number $c(x,y)$, called its capacity. Any flow $f$ must satisfy $f(x,y) \le c(x,y)$ for every edge $\vec{xy}$ (Bollobás, p. 75).

# Prerequisites
- **Flow in a directed graph** — Capacities constrain flows

# Key Properties
1. Capacities are non-negative real numbers
2. Flow through an edge cannot exceed its capacity
3. Some edges may have infinite capacity
4. The capacity function may be integral (integer-valued)

# Construction / Recognition
1. Assign a non-negative number $c(x,y)$ to each directed edge $\vec{xy}$
2. A flow is feasible if $0 \le f(x,y) \le c(x,y)$ for every edge

# Context & Application
Edge capacities model real-world limitations: bandwidth of communication links, carrying capacity of roads, or throughput of pipelines. The integral capacity case is especially important because it guarantees integral maximal flows.

# Examples
**Example** (p. 75, Fig. III.1): A cut with capacity 12 is shown, where the numbers next to edges indicate their capacities.

# Relationships
## Builds Upon
- **flow-in-directed-graph** — Capacities constrain flows in the graph

## Enables
- **cut-capacity** — Capacity of a cut is the sum of capacities of its edges
- **max-flow-min-cut-theorem** — Relates maximum flow to minimum cut capacity

## Contrasts With
- **vertex-capacity** — Capacity bound placed on vertices rather than edges

# Common Errors
- **Error**: Allowing flow to exceed capacity on an edge
  **Correction**: The constraint $f(x,y) \le c(x,y)$ must hold for every edge

# Common Confusions
- **Confusion**: Thinking capacity restricts flow in both directions
  **Clarification**: Capacity $c(x,y)$ restricts flow on the directed edge $\vec{xy}$ only; the reverse edge $\vec{yx}$ (if it exists) has its own capacity

# Source Reference
Chapter III, Section III.1, page 75.

# Verification Notes
- Definition source: Direct from p. 75
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
