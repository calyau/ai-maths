---
concept: Eulerian Graph
slug: eulerian-graph
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
  - Euler graph
prerequisites:
  - graph
  - euler-circuit
  - connected-graph
  - vertex-degree
extends: []
related:
  - euler-trail
  - randomly-eulerian-graph
contrasts_with: []
answers_questions:
  - "What is an Eulerian graph?"
---

# Quick Definition

A graph is Eulerian if it has an Euler circuit. Equivalently, a non-trivial connected graph is Eulerian iff every vertex has even degree.

# Core Definition

"A graph is Eulerian if it has an Euler circuit" (Bollobás, p. 25). By Theorem 12, this is equivalent to being connected with every vertex having even degree. The directed analogue requires $d^+(v) = d^-(v)$ for all vertices.

# Prerequisites

- **Graph** — Eulerian is a property of graphs
- **Euler circuit** — An Eulerian graph has an Euler circuit
- **Connected graph** — Must be connected
- **Vertex degree** — All degrees must be even

# Key Properties

1. Connected and every vertex has even degree
2. Edge set can be partitioned into cycles (Theorem 1)
3. For odd $n$, $K_n$ is Eulerian
4. For directed multigraphs: Eulerian iff connected and $d^+(v) = d^-(v)$ for all $v$

# Construction / Recognition

Check: (1) connected, and (2) every vertex has even degree.

# Context & Application

Eulerian graphs are those admitting a closed tour traversing every edge exactly once. They arise in circuit design, route planning, and the theoretical study of graph decompositions.

# Examples

**Example** (p. 25): For odd $n \ge 3$, $K_n$ is Eulerian since every vertex has degree $n - 1$ (even).

# Relationships

## Builds Upon
- **Euler circuit**, **Connected graph**, **Vertex degree**

## Enables
- **BEST theorem** — Counting Euler circuits in Eulerian digraphs

## Related
- **Randomly Eulerian graph** — An Eulerian graph where any greedy traversal succeeds

# Common Errors

- **Error**: Claiming a disconnected graph with all even degrees is Eulerian
  **Correction**: Connectivity is required; isolated components prevent a single circuit

# Common Confusions

- **Confusion**: Confusing "Eulerian" with "having an Euler trail"
  **Clarification**: Eulerian means having an Euler circuit (closed); graphs with exactly 2 odd-degree vertices have an Euler trail but are not Eulerian

# Source Reference

Chapter I: Fundamentals, Section I.3, Theorem 12, page 25.

# Verification Notes

- Definition source: Direct from p. 25
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
