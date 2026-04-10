---
concept: Cut Separating s from t
slug: cut-separating-s-from-t
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
  - "s-t cut"
  - "edge-cut"
  - "separating cut"
prerequisites:
  - flow-in-directed-graph
extends: []
related:
  - cut-capacity
  - max-flow-min-cut-theorem
contrasts_with:
  - vertex-cut
answers_questions:
  - "What is a cut in a flow network?"
  - "How does the max-flow min-cut theorem connect flows and cuts?"
---

# Quick Definition
A cut separating $s$ from $t$ in a directed graph is the set of directed edges $\vec{E}(S, \overline{S})$ from a subset $S$ containing $s$ to its complement $\overline{S}$ containing $t$.

# Core Definition
Given a directed graph $\vec{G} = (V, \vec{E})$ with source $s$ and sink $t$, if $S$ is a subset of $V$ containing $s$ but not $t$, then $\vec{E}(S, \overline{S})$ is called a cut separating $s$ from $t$, where $\overline{S} = V - S$. Deleting the edges of a cut ensures no positive-valued flow from $s$ to $t$ can exist on the remainder. Conversely, any set of edges whose deletion prevents all positive flow from $s$ to $t$ contains a cut (Bollobás, p. 75).

# Prerequisites
- **Flow in a directed graph** — Cuts are defined in the context of flows

# Key Properties
1. A cut is determined by a partition of $V$ into $S$ (containing $s$) and $\overline{S}$ (containing $t$)
2. Only edges from $S$ to $\overline{S}$ are in the cut (not edges from $\overline{S}$ to $S$)
3. There are finitely many cuts (since $V$ is finite)
4. The capacity of a cut is at least as large as the value of any flow

# Construction / Recognition
1. Choose a subset $S \subset V$ with $s \in S$ and $t \notin S$
2. The cut is $\vec{E}(S, \overline{S}) = \{\vec{xy} \in \vec{E} : x \in S, y \in \overline{S}\}$
3. The cut capacity is $c(S, \overline{S}) = \sum c(x,y)$ over edges in the cut

# Context & Application
Cuts provide upper bounds on flow values and are dual objects to flows in the max-flow min-cut theorem. Finding a minimum capacity cut is equivalent to finding a maximum flow.

# Examples
**Example** (p. 75, Fig. III.1): A cut with capacity 12 is illustrated, where the numbers next to edges indicate their capacity.

# Relationships
## Builds Upon
- **flow-in-directed-graph** — Cuts are defined for flow networks

## Enables
- **max-flow-min-cut-theorem** — Minimum cut capacity equals maximum flow value
- **cut-capacity** — Capacity is the key measure of a cut

## Contrasts With
- **vertex-cut** — Vertex-cuts remove vertices rather than edges

# Common Errors
- **Error**: Including edges from $\overline{S}$ to $S$ in the cut
  **Correction**: A cut $\vec{E}(S, \overline{S})$ includes only edges directed from $S$ to $\overline{S}$

# Common Confusions
- **Confusion**: Thinking any set of edges whose removal disconnects $s$ from $t$ is a cut
  **Clarification**: A cut has the specific form $\vec{E}(S, \overline{S})$; an arbitrary disconnecting set contains a cut but may not be one

# Source Reference
Chapter III, Section III.1, page 75.

# Verification Notes
- Definition source: Direct from p. 75
- Confidence rationale: Explicitly defined with notation
- Uncertainties: None
- Cross-reference status: Verified
