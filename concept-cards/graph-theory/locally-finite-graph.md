---
concept: Locally Finite Graph
slug: locally-finite-graph
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 206
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "locally finite"
prerequisites:
  - graph
  - vertex
  - infinite-graph
extends:
  - infinite-graph
related:
  - ray
  - end-of-a-graph
  - konigs-infinity-lemma
contrasts_with: []
answers_questions:
  - "What is a locally finite graph?"
  - "Why are locally finite graphs important in infinite graph theory?"
---

# Quick Definition
A graph is locally finite if all its vertices have finite degrees. Locally finite graphs are the mildest form of infinite graphs where most basic finite proof techniques can be adapted.

# Core Definition
A graph is *locally finite* if all its vertices have finite degrees (Diestel, p. 206). In the context of infinite graph theory, locally finite graphs occupy a central position: they are "only just" infinite, with countably many vertices and finitely many edges at each vertex. Many of the most typical phenomena of infinite graphs already occur in this setting.

# Prerequisites
- **Graph** — A locally finite graph is a graph with a degree constraint
- **Vertex** — Degree is measured at vertices
- **Infinite graph** — Local finiteness is primarily relevant for infinite graphs

# Key Properties
1. Every vertex has finite degree
2. A locally finite connected infinite graph is countable
3. Any locally finite connected graph has the property that |G| is compact (Proposition 8.5.1)
4. The star-comb lemma applied in locally finite graphs always yields a comb (never a star)
5. Every countable connected locally finite graph has a locally finite normal spanning tree

# Construction / Recognition
## To Recognize a Locally Finite Graph
1. Check that every vertex v satisfies d(v) < infinity
2. For infinite graphs, verify no vertex has infinite degree

# Context & Application
Locally finite graphs are the setting where infinite graph theory is most tractable. The compactness principle (via Konig's infinity lemma) works most naturally for locally finite graphs, allowing transfer of finite results. Topological properties of the end space are best behaved in the locally finite case.

# Examples
**Example 1** (p. 206): The ray is locally finite (degrees are 1 and 2).

**Example 2** (p. 208): The N x N grid is locally finite (all degrees are 2, 3, or 4) and has exactly one end, which is thick.

# Relationships
## Builds Upon
- **Infinite graph** — Locally finite graphs are a special class of infinite graphs

## Enables
- **Compactness arguments** for infinite graphs
- **Topological end space** — particularly well-behaved for locally finite graphs

## Related
- **Ray** — locally finite connected infinite graphs always contain rays
- **Konig's infinity lemma** — a key tool for locally finite graphs

# Common Errors
- **Error**: Assuming locally finite graphs must be finite
  **Correction**: A graph can have infinitely many vertices while each has finite degree

# Common Confusions
- **Confusion**: Confusing locally finite with finite
  **Clarification**: "Locally finite" means each vertex has finite degree; the graph itself may be infinite

# Source Reference
Chapter 8: Infinite Graphs, Section 8.1, page 206.

# Verification Notes
- Definition directly from p. 206
- Confidence: HIGH — explicit definition in source
