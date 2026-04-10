---
concept: Vertex Capacity
slug: vertex-capacity
category: network-flows
subcategory: flow-definitions
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
  - "vertex capacity restriction"
  - "capacity bound on vertices"
prerequisites:
  - flow-in-directed-graph
  - capacity-of-edge
extends: []
related:
  - vertex-cut
  - vertex-capacity-max-flow-min-cut
contrasts_with:
  - capacity-of-edge
answers_questions:
  - "How are vertex capacity constraints handled in flow networks?"
---

# Quick Definition
A vertex capacity $c(x)$ bounds the total flow passing through an intermediate vertex $x$, constraining $\sum_{y \in \Gamma^+(x)} f(x,y) \le c(x)$.

# Core Definition
Given a directed graph with capacity restrictions on the vertices (except source and sink), each vertex $x \in V - \{s,t\}$ has a capacity $c(x) \ge 0$ such that the total flow through $x$ satisfies $\sum_{y \in \Gamma^+(x)} f(x,y) = \sum_{z \in \Gamma^-(x)} f(z,x) \le c(x)$. This can be reduced to edge capacities by splitting each vertex $x$ into $x_-$ (receiving incoming edges) and $x_+$ (sending outgoing edges), connected by an edge $\vec{x_- x_+}$ with capacity $c(x)$ (Bollobás, p. 78).

# Prerequisites
- **Flow in a directed graph** — Vertex capacities constrain flows
- **Capacity of an edge** — Vertex capacities reduce to edge capacities

# Key Properties
1. Vertex capacity restricts total throughput at a vertex
2. The vertex-splitting reduction preserves all flow properties
3. A vertex-cut corresponds to an edge-cut in the split graph
4. Source and sink are exempt from capacity restrictions

# Construction / Recognition
## Vertex Splitting Reduction
1. Replace each $x \in V - \{s,t\}$ by two vertices $x_-$ and $x_+$
2. Redirect incoming edges to $x_-$ and outgoing edges from $x_+$
3. Add edge $\vec{x_- x_+}$ with capacity $c(x)$
4. Apply the standard max-flow min-cut theorem to the new graph

# Context & Application
Vertex capacities model situations where nodes have limited processing capacity. The vertex-splitting technique is a standard reduction that enables applying edge-based theorems.

# Examples
**Example** (p. 78, Fig. III.2): A graph $\vec{G}$ with vertex capacity restrictions is transformed into a graph $\vec{H}$ with edge capacity restrictions by splitting each vertex.

# Relationships
## Builds Upon
- **capacity-of-edge** — Vertex capacities reduce to edge capacities

## Enables
- **vertex-capacity-max-flow-min-cut** — Theorem 4
- **mengers-theorem** — Vertex form uses vertex capacities

## Contrasts With
- **capacity-of-edge** — Edge vs. vertex constraints

# Common Errors
- **Error**: Applying vertex splitting to the source or sink
  **Correction**: Only intermediate vertices are split; source and sink have no capacity restriction

# Common Confusions
- **Confusion**: Thinking vertex and edge capacities require different theoretical frameworks
  **Clarification**: Vertex capacities reduce to edge capacities via vertex splitting

# Source Reference
Chapter III, Section III.1, pages 78-79. Fig. III.2.

# Verification Notes
- Definition source: Direct from p. 78
- Confidence rationale: Explicitly defined with figure
- Uncertainties: None
- Cross-reference status: Verified
