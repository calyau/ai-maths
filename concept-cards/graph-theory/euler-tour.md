---
concept: Euler Tour
slug: euler-tour

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 31
section: "1.8 Euler tours"

extraction_confidence: high

aliases:
  - "Eulerian"
  - "Eulerian graph"
  - "Euler circuit"

prerequisites:
  - graph
  - walk
  - connected-graph
  - degree
extends: []
related:
  - handshaking-lemma
  - hamilton-cycle
contrasts_with:
  - hamilton-cycle

answers_questions:
  - "What is an Euler tour?"
  - "How do I find an Euler tour in a graph?"
  - "When is a graph Eulerian?"
  - "What distinguishes a Hamilton cycle from an Euler tour?"
---

# Quick Definition
An Euler tour is a closed walk that traverses every edge of the graph exactly once. A graph is Eulerian if it admits an Euler tour.

# Core Definition
Let us call a closed walk in a graph an Euler tour if it traverses every edge of the graph exactly once. A graph is Eulerian if it admits an Euler tour (Diestel, p. 22).

Theorem 1.8.1 (Euler 1736): A connected graph is Eulerian if and only if every vertex has even degree (Diestel, p. 22).

# Prerequisites
- **Graph** — Euler tours exist in graphs
- **Walk** — an Euler tour is a closed walk
- **Connected graph** — the graph must be connected
- **Degree** — the characterization uses degree parity

# Key Properties
1. An Euler tour visits every edge exactly once
2. An Euler tour visits every vertex at least once
3. A connected graph is Eulerian iff every vertex has even degree (Theorem 1.8.1)
4. The degree condition is necessary: a vertex appearing k times contributes degree 2k
5. An Euler tour is NOT required to visit every vertex exactly once

# Construction / Recognition
## To Determine if a Graph is Eulerian
1. Check that the graph is connected
2. Check that every vertex has even degree
3. If both conditions hold, the graph is Eulerian

## To Find an Euler Tour (from the proof)
1. Start with a longest walk W using no edge more than once
2. W must be closed (since all degrees are even)
3. If W misses an edge e incident with a vertex of W, extend W to include e
4. Repeat until all edges are covered

# Context & Application
The Euler tour problem is historically the first graph theory problem, originating from the Konigsberg bridge problem (1736). It contrasts with the Hamilton cycle problem, which seeks to visit every vertex exactly once.

# Examples
**Example** (p. 22): Fig. 1.8.1 shows the bridges of Konigsberg. Fig. 1.8.2 shows the corresponding graph, which is not Eulerian because some vertices have odd degree.

# Relationships
## Builds Upon
- **walk**, **connected-graph**, **degree**

## Related
- **handshaking-lemma** — the even-degree condition relates to edge counting

## Contrasts With
- **hamilton-cycle** — visits every vertex exactly once (not every edge)

# Common Confusions
- **Confusion**: Confusing Euler tour (every edge once) with Hamilton cycle (every vertex once)
  **Clarification**: An Euler tour traverses every edge exactly once but may revisit vertices. A Hamilton cycle visits every vertex exactly once but need not use every edge.

- **Confusion**: Thinking an Euler tour is a cycle
  **Clarification**: An Euler tour is a closed walk, not a cycle (it may revisit vertices)

# Source Reference
Chapter 1: The Basics, Section 1.8, pages 21-22 (pdf pp. 31-32). Theorem 1.8.1. See Figs. 1.8.1, 1.8.2.

# Verification Notes
- Definition and theorem directly from pp. 21-22
- Confidence: HIGH — classic result with explicit proof
