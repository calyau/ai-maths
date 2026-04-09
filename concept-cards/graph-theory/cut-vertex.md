---
concept: Cut Vertex
slug: cut-vertex

category: connectivity
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 20
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "cutvertex"

prerequisites:
  - graph
  - connected-graph
  - separator
extends:
  - separator
related:
  - bridge
  - block
  - k-connected
contrasts_with:
  - bridge

answers_questions:
  - "What is a cut vertex?"
---

# Quick Definition
A cut vertex is a vertex that separates two other vertices of the same component; removing it increases the number of components.

# Core Definition
A vertex which separates two other vertices of the same component is a cutvertex (Diestel, p. 11).

# Prerequisites
- **Graph**, **connected-graph**, **separator** — a cut vertex is a separator of size 1

# Key Properties
1. A cut vertex v is a vertex whose removal disconnects some component
2. A graph is 2-connected if and only if it has no cut vertex (and has at least 3 vertices)
3. Every bridge has at least one endpoint that may be a cut vertex

# Examples
**Example** (p. 11): Fig. 1.4.2 shows a graph with cutvertices v, x, y, w and bridge e = xy.

# Relationships
## Builds Upon
- **separator** — a cut vertex is a single-vertex separator

## Related
- **bridge** — a single-edge separator
- **block** — a maximal 2-connected subgraph or bridge
- **k-connected** — 2-connected means no cut vertices

# Contrasts With
- **bridge** — a bridge is a separating edge, not a vertex

# Source Reference
Chapter 1: The Basics, Section 1.4, page 11 (pdf p. 21). See Fig. 1.4.2.

# Verification Notes
- Direct from p. 11
- Confidence: HIGH
