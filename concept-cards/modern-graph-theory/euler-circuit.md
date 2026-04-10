---
concept: Euler Circuit
slug: euler-circuit
category: paths-and-cycles
subcategory: hamilton-euler
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.3 Hamilton Cycles and Euler Circuits"
extraction_confidence: high
aliases:
  - Eulerian circuit
  - Euler cycle
prerequisites:
  - graph
  - circuit
  - connected-graph
  - vertex-degree
extends:
  - circuit
related:
  - euler-trail
  - eulerian-graph
  - hamilton-cycle
contrasts_with:
  - hamilton-cycle
answers_questions:
  - "What is an Euler circuit?"
  - "What distinguishes Hamilton cycles from Euler circuits?"
---

# Quick Definition

An Euler circuit is a circuit containing all edges of a graph. A non-trivial connected graph has an Euler circuit iff every vertex has even degree.

# Core Definition

"A circuit in a graph $G$ containing all the edges is said to be an Euler circuit of $G$" (Bollobás, p. 25). "**Theorem 12.** A non-trivial connected graph has an Euler circuit iff each vertex has even degree" (p. 25). Named after Euler, who in 1736 solved the Königsberg bridge problem using this concept.

# Prerequisites

- **Graph** — Euler circuits are defined within graphs
- **Circuit** — An Euler circuit is a circuit
- **Connected graph** — The graph must be connected
- **Vertex degree** — The characterization uses degree parity

# Key Properties

1. Traverses every edge exactly once, returning to the starting vertex
2. Exists iff the graph is connected and every vertex has even degree (Theorem 12)
3. Theorem 12 is equivalent to Theorem 1 (cycle partition)
4. Also valid for multigraphs and directed multigraphs
5. The directed version requires $d^+(v) = d^-(v)$ for all vertices

# Construction / Recognition

## To determine existence
1. Verify the graph is connected
2. Verify every vertex has even degree

## To construct (implicit from Theorem 1)
1. Find a cycle
2. Remove its edges; find another cycle in the remaining graph
3. Concatenate cycles into a single Euler circuit

# Context & Application

Euler circuits originated from the Königsberg bridge problem (1736): can one walk through the city crossing each bridge exactly once? Euler proved this is impossible since the associated multigraph has four vertices of odd degree. Euler circuits also appear in the BEST theorem counting formula and in the Amitsur-Levitzki theorem.

# Examples

**Example** (pp. 25-26): The Königsberg bridges (Fig. I.14, I.15) have a multigraph with all vertices of odd degree, so no Euler trail exists.

**Example** (p. 25): For odd $n \ge 3$, $K_n$ has an Euler circuit since it is $(n-1)$-regular with $n-1$ even.

# Relationships

## Builds Upon
- **Circuit** — An Euler circuit is a specific circuit

## Enables
- **BEST theorem** — Counts Euler circuits
- **Amitsur-Levitzki theorem** — Uses Euler trails in its proof

## Related
- **Euler trail** — An open version (different start and end)
- **Eulerian graph** — A graph possessing an Euler circuit

## Contrasts With
- **Hamilton cycle** — Visits every vertex; Euler circuit traverses every edge

# Common Errors

- **Error**: Confusing Euler circuit (all edges) with Hamilton cycle (all vertices)
  **Correction**: Euler = edges, Hamilton = vertices

# Common Confusions

- **Confusion**: Thinking an Euler circuit must visit every vertex exactly once
  **Clarification**: An Euler circuit visits every vertex at least once but may visit vertices multiple times (at vertices of degree $> 2$)

# Source Reference

Chapter I: Fundamentals, Section I.3, Theorem 12, pages 25-26.

# Verification Notes

- Definition source: Direct from p. 25
- Confidence rationale: Explicitly defined with characterization theorem
- Uncertainties: None
- Cross-reference status: Verified
