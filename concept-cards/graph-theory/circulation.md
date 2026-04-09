---
concept: Circulation
slug: circulation
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 150
section: "6.1 Circulations"
extraction_confidence: high
aliases:
  - "H-circulation"
  - "group-valued circulation"
prerequisites:
  - graph
  - edge
  - vertex
related:
  - flow-in-network
  - h-flow
  - nowhere-zero-flow
contrasts_with:
  - flow-in-network
answers_questions:
  - "What is a circulation on a graph?"
  - "How does Diestel define the algebraic foundation for flow theory?"
---

# Quick Definition
A circulation on a multigraph G with values in an abelian group H is a function on directed edges satisfying antisymmetry (F1) and Kirchhoff's law at every vertex (F2).

# Core Definition
Let G = (V, E) be a multigraph and H an abelian group. A function f: E-arrow -> H is a **circulation** on G (an H-circulation) if it satisfies:

- **(F1)** f(e, x, y) = -f(e, y, x) for all (e, x, y) in E-arrow with x != y (antisymmetry);
- **(F2)** f(v, V) = 0 for all v in V (Kirchhoff's law: the net flow out of every vertex is zero).

(Diestel, p. 140-141, Section 6.1)

# Prerequisites
- **Graph (multigraph)** — Circulations are defined on multigraphs, requiring the notion of edges, vertices, and adjacency
- **Abelian group** — The values of a circulation live in an abelian group H; understanding group addition and inverses is needed for (F1) and (F2)

# Key Properties
1. If f satisfies (F1), then f(X, X) = 0 for all X subset of V
2. If f satisfies (F2), then f(X, V) = 0 for all X subset of V
3. The net flow across any cut is zero: f(X, X-bar) = 0 for every X subset of V (Proposition 6.1.1)
4. Circulations are always zero on bridges (Corollary 6.1.2)
5. The set of H-circulations on G forms a group under pointwise addition

# Construction / Recognition
## To Construct a Circulation
1. Choose an abelian group H for the values
2. Assign directed-edge values from H satisfying antisymmetry (F1)
3. Verify Kirchhoff's law (F2) at every vertex: the sum of outgoing flow equals zero

## To Recognize a Circulation
1. Check (F1): for every edge, the value in one direction is the negative of the value in the other
2. Check (F2): at every vertex, the total flow out sums to zero in H

# Context & Application
Diestel treats circulations as the algebraic foundation of flow theory. A circulation is the most general notion: it satisfies Kirchhoff's law at every vertex with no exceptions. Network flows (Section 6.2) relax this by allowing exceptions at a source and sink. Group-valued flows (Section 6.3) add a nowhere-zero requirement.

The algebraic treatment allows flows to take values in arbitrary abelian groups, not just integers, leading to deep connections with colouring theory.

# Examples
**Example** (p. 141): Any multigraph admits the **zero circulation** f(e-arrow) = 0 for all directed edges. This is the trivial H-circulation for any group H.

**Example** (p. 141): On a bridge e = xy, any circulation must satisfy f(e, x, y) = 0, since {x-side, y-side} forms a cut and the net flow across any cut is zero.

# Relationships
## Builds Upon
- **Graph** — Circulations are defined on multigraphs

## Enables
- **Flow in network** — Network flows are circulations with relaxed Kirchhoff's law at source and sink
- **H-flow** — An H-flow is a nowhere-zero H-circulation
- **Nowhere-zero flow** — Built on the circulation concept

## Related
- **Kirchhoffs law** — The defining condition (F2) of a circulation

## Contrasts With
- **Flow in network** — Network flows allow net flow to leave at source and enter at sink; circulations do not

# Common Errors
- **Error**: Forgetting that circulations on multigraphs require directed-edge triples (e, x, y), not just vertex pairs (x, y)
  **Correction**: In multigraphs, an edge e = xy is not uniquely identified by the pair (x, y); use the triple (e, x, y)

# Common Confusions
- **Confusion**: Thinking a circulation must have non-zero values somewhere
  **Clarification**: The zero function is always a valid circulation; the requirement of non-zero values is what distinguishes H-flows from H-circulations
- **Confusion**: Confusing "circulation" with "network flow"
  **Clarification**: A circulation satisfies Kirchhoff's law at ALL vertices; a network flow relaxes this at source and sink

# Source Reference
Chapter 6: Flows, Section 6.1 "Circulations," pages 140-141 (pdf pages 150-151). See Proposition 6.1.1 and Corollary 6.1.2.

# Verification Notes
- Definition: Directly from p. 140-141, conditions (F1) and (F2) quoted
- Key Properties: Items 1-4 explicit in source text
- Confidence: HIGH — explicit definition with formal conditions
