---
concept: Vertex-Cut
slug: vertex-cut
category: connectivity
subcategory: separating-sets
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
  - "vertex cut"
  - "separating set"
prerequisites:
  - flow-in-directed-graph
extends: []
related:
  - cut-separating-s-from-t
  - vertex-connectivity
contrasts_with:
  - cut-separating-s-from-t
answers_questions:
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
A vertex-cut is a subset $S$ of vertices (excluding source and sink) whose removal disconnects the graph so that no positive-valued flow from $s$ to $t$ exists on $G - S$.

# Core Definition
In a directed graph with vertex capacity restrictions, a vertex-cut is a subset $S$ of $V - \{s,t\}$ such that no positive-valued flow from $s$ to $t$ can be defined on $G - S$. The capacity of a vertex-cut $S$ is $\sum_{x \in S} c(x)$ (Bollobás, p. 79).

# Prerequisites
- **Flow in a directed graph** — Vertex-cuts are defined in the context of flows

# Key Properties
1. A vertex-cut removes vertices, not edges
2. Source and sink cannot be in the vertex-cut
3. Via vertex-splitting, vertex-cuts correspond to edge-cuts
4. The minimum vertex-cut capacity equals the maximum flow with vertex capacities (Theorem 4)

# Construction / Recognition
1. Find a subset $S \subset V - \{s,t\}$
2. Check that $G - S$ has no path from $s$ to $t$
3. The capacity is $\sum_{x \in S} c(x)$

# Context & Application
Vertex-cuts are the natural dual to vertex connectivity. They connect to Menger's theorem: the minimum number of vertices separating two non-adjacent vertices equals the maximum number of independent paths between them.

# Examples
**Example** (p. 79, Fig. III.2): After vertex-splitting, vertex-cuts in $\vec{G}$ correspond to edge-cuts of finite capacity in $\vec{H}$, since only the edges $\vec{x_-x_+}$ have finite capacities.

# Relationships
## Builds Upon
- **flow-in-directed-graph** — Context for vertex-cuts

## Enables
- **vertex-connectivity** — Minimum vertex-cut size defines connectivity
- **mengers-theorem** — Vertex form concerns vertex-cuts

## Contrasts With
- **cut-separating-s-from-t** — Edge-cut vs. vertex-cut

# Common Errors
- **Error**: Including the source or sink in a vertex-cut
  **Correction**: Vertex-cuts are subsets of $V - \{s,t\}$

# Common Confusions
- **Confusion**: Confusing the number of vertices removed with the capacity of the cut
  **Clarification**: When all vertex capacities are 1, the capacity equals the number of vertices; in general, capacity is the sum of individual vertex capacities

# Source Reference
Chapter III, Section III.1, pages 78-79.

# Verification Notes
- Definition source: Direct from p. 79
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
