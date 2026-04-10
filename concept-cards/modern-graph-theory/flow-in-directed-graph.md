---
# === CORE IDENTIFICATION ===
concept: Flow in a Directed Graph
slug: flow-in-directed-graph

# === CLASSIFICATION ===
category: network-flows
subcategory: flow-definitions
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.1 Flows in Directed Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "network flow"
  - "static flow"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - directed-graph
  - kirchhoffs-current-law
  - flow-value
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a flow in a directed graph?"
  - "How is flow defined from a source to a sink?"
---

# Quick Definition
A flow in a directed graph is a non-negative function defined on the edges that satisfies Kirchhoff's current law at every intermediate vertex (neither source nor sink), meaning the total current entering equals the total current leaving.

# Core Definition
Let $\vec{G}$ be a finite directed graph with vertex set $V$ and edge set $\vec{E}$. A flow $f$ from a vertex $s$ (the source) to a vertex $t$ (the sink) is a non-negative function defined on the edges, where $f(\vec{xy})$ is the amount of flow in edge $\vec{xy}$. The flow must satisfy Kirchhoff's current law: for each $x \in V - \{s, t\}$, $\sum_{y \in \Gamma^+(x)} f(x,y) = \sum_{z \in \Gamma^-(x)} f(z,x)$, where $\Gamma^+(x)$ and $\Gamma^-(x)$ are the out-neighbourhood and in-neighbourhood of $x$ respectively (Bollobás, p. 74).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Flow values are non-negative on every edge
2. Kirchhoff's current law holds at every intermediate vertex
3. The net current leaving $s$ equals the net current flowing into $t$
4. $f(x,y) = 0$ whenever $\vec{xy} \notin \vec{E}$

# Construction / Recognition
## To Construct a Flow
1. Assign a non-negative value $f(x,y)$ to each directed edge $\vec{xy}$
2. Verify that at each vertex other than $s$ and $t$, inflow equals outflow
3. The result is a valid flow from $s$ to $t$

## To Recognize a Flow
1. Check that all edge values are non-negative
2. Verify Kirchhoff's law at every intermediate vertex
3. Confirm the function is defined on directed edges of the graph

# Context & Application
Flows in directed graphs model transport problems: shipping goods through a network, routing data through a communications network, or any scenario where quantities move along directed paths from a source to a sink. The concept is foundational to the max-flow min-cut theorem and underpins results on connectivity and matching in this chapter.

# Examples
**Example** (p. 74): Given a directed graph $\vec{G}$ with source $s$ and sink $t$, define $\Gamma^+(x) = \{y \in V : \vec{xy} \in \vec{E}\}$ and $\Gamma^-(x) = \{y \in V : \vec{yx} \in \vec{E}\}$. A flow must satisfy the balance equation at each intermediate vertex.

# Relationships
## Builds Upon
No prerequisites within this source.

## Enables
- **flow-value** — The value of a flow is defined from this concept
- **capacity-of-edge** — Capacities constrain flows
- **max-flow-min-cut-theorem** — The central theorem about flows

## Related
- **kirchhoffs-current-law** — The conservation condition for flows
- **directed-graph** — The underlying structure

## Contrasts With
No direct contrasts within this chapter.

# Common Errors
- **Error**: Allowing negative flow values on edges
  **Correction**: Flow values must be non-negative; negative flow is modeled by flow in the reverse direction

- **Error**: Forgetting to check Kirchhoff's law at all intermediate vertices
  **Correction**: The conservation law must hold at every vertex except the source and sink

# Common Confusions
- **Confusion**: Thinking flow must follow a single path from $s$ to $t$
  **Clarification**: Flow can be distributed across multiple paths simultaneously; the conservation law ensures consistency

- **Confusion**: Confusing flow in directed graphs with electrical network flow (Chapter II)
  **Clarification**: This chapter studies different aspects of flows than electrical networks — here flows are non-negative and subject to capacity constraints

# Source Reference
Chapter III: Flows, Connectivity and Matching, Section III.1 "Flows in Directed Graphs," pages 74-76.

# Verification Notes
- Definition source: Direct from source text, p. 74
- Confidence rationale: Explicit formal definition with notation
- Uncertainties: None
- Cross-reference status: Verified against chapter content
