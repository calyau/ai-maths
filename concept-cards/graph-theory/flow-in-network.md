---
concept: Flow in a Network
slug: flow-in-network
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 151
section: "6.2 Flows in networks"
extraction_confidence: high
aliases:
  - "network flow"
  - "flow"
prerequisites:
  - network
  - capacity-function
  - kirchhoffs-law
  - circulation
extends:
  - circulation
related:
  - total-flow-value
  - cut-in-network
  - max-flow-min-cut-theorem
contrasts_with:
  - circulation
answers_questions:
  - "What is a flow in a network?"
  - "How does a network flow differ from a circulation?"
---

# Quick Definition
A flow in a network N = (G, s, t, c) is a real-valued function on directed edges satisfying antisymmetry, Kirchhoff's law at all vertices except source and sink, and a capacity constraint.

# Core Definition
A function f: E-arrow -> R is a **flow** in N = (G, s, t, c) if it satisfies:

- **(F1)** f(e, x, y) = -f(e, y, x) for all (e, x, y) in E-arrow with x != y (antisymmetry);
- **(F2')** f(v, V) = 0 for all v in V \ {s, t} (Kirchhoff's law except at source and sink);
- **(F3)** f(e-arrow) <= c(e-arrow) for all e-arrow in E-arrow (capacity constraint).

The flow is called **integral** if all its values are integers. (Diestel, p. 141-142)

# Prerequisites
- **Network** — A flow is defined within a network N = (G, s, t, c)
- **Capacity function** — Provides the upper bound constraint (F3)
- **Kirchhoff's law** — The conservation condition (F2') is a modified form
- **Circulation** — A flow generalizes/relaxes a circulation by allowing exceptions at s and t

# Key Properties
1. Satisfies antisymmetry (F1) like a circulation
2. Satisfies Kirchhoff's law everywhere except at source s and sink t
3. Respects capacity constraints on every directed edge
4. The total value |f| = f(s, V) is the same for every cut (Proposition 6.2.1)
5. |f| may formally be negative; swapping s and t changes the sign

# Construction / Recognition
## To Construct a Flow
1. Start with the zero flow f_0 = 0 on all edges
2. Find an augmenting path from s to t with available capacity
3. Push flow along this path up to the minimum residual capacity
4. Repeat until no augmenting path exists (Ford-Fulkerson algorithm)

# Context & Application
Network flows model transportation, communication, and resource allocation problems. The concept unifies results in matching, connectivity, and combinatorial optimization. Diestel notes that the max-flow min-cut theorem alone implies Menger's theorem, indicating the natural power of the approach.

# Examples
**Example** (p. 142, Fig. 6.2.1): A network flow in short notation showing a flow of total value 3, with values indicated in the forward direction on each edge.

**Example** (p. 143, Fig. 6.2.2): An augmenting path W with increment epsilon = 2, for constant flow f_n = 0 and capacities c = 3.

# Relationships
## Builds Upon
- **Circulation** — A flow is like a circulation but with Kirchhoff's law relaxed at s and t
- **Network** — Flows exist within networks

## Enables
- **Total flow value** — Defined as f(s, V)
- **Max-flow min-cut theorem** — Characterizes maximum flows
- **Integral flow theorem** — Integral capacity implies integral maximum flow

## Contrasts With
- **Circulation** — A circulation satisfies Kirchhoff's law at ALL vertices; a flow allows exceptions

# Common Errors
- **Error**: Assuming flow values must be non-negative
  **Correction**: By antisymmetry (F1), if f(e, x, y) > 0 then f(e, y, x) < 0; flow can be "negative" in a direction

# Common Confusions
- **Confusion**: Conflating a "flow" (network flow with source/sink) with a "circulation" (flow satisfying Kirchhoff's law everywhere)
  **Clarification**: In Diestel's terminology, a flow allows exceptions at s and t; a circulation does not

# Source Reference
Chapter 6: Flows, Section 6.2 "Flows in networks," pages 141-142 (pdf pages 151-152).

# Verification Notes
- Definition: Directly from p. 141-142, conditions (F1), (F2'), (F3) quoted
- Confidence: HIGH — explicit formal definition with conditions numbered
