---
concept: Induced Subgraph
slug: induced-subgraph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "spanned subgraph"
  - "G[U]"

prerequisites:
  - graph
  - subgraph
extends:
  - subgraph
related:
  - spanning-subgraph
contrasts_with:
  - subgraph
  - spanning-subgraph

answers_questions:
  - "What is an induced subgraph?"
  - "What does G[U] mean?"
---

# Quick Definition
An induced subgraph of G is a subgraph G' that contains all the edges of G between its vertices. If U is a vertex set, G[U] denotes the subgraph induced by U.

# Core Definition
If G' is a subgraph of G and G' contains all the edges xy in E with x, y in V', then G' is an induced subgraph of G; we say that V' induces or spans G' in G, and write G' =: G[V']. Thus if U is a subset of V is any set of vertices, then G[U] denotes the graph on U whose edges are precisely the edges of G with both ends in U (Diestel, p. 4).

# Prerequisites
- **Graph** — induced subgraphs are graphs
- **Subgraph** — an induced subgraph is a special type of subgraph

# Key Properties
1. An induced subgraph is completely determined by its vertex set
2. G[U] contains exactly those edges of G that have both endpoints in U
3. Notation: G[U] for the subgraph induced by vertex set U
4. If H is a subgraph of G, G[V(H)] is abbreviated to G[H]

# Construction / Recognition
## To Construct G[U]
1. Take the vertex set U
2. Include all edges of G that have both endpoints in U
3. The result is the induced subgraph G[U]

## To Recognize
A subgraph G' of G is induced if and only if there is no edge in G between vertices of G' that is missing from G'.

# Context & Application
Induced subgraphs are important because they preserve the local structure of the original graph. Many graph properties are hereditary for induced subgraphs.

# Examples
**Example** (p. 4): Fig. 1.1.3 shows G' as an induced subgraph of G, but G'' is not induced (it omits some edges between its vertices).

# Relationships
## Builds Upon
- **subgraph** — an induced subgraph is a special subgraph

## Related
- **spanning-subgraph** — spans all vertices but may omit edges

## Contrasts With
- **subgraph** — a general subgraph may omit edges between its vertices
- **spanning-subgraph** — includes all vertices but not necessarily all edges

# Common Errors
- **Error**: Constructing G[U] but forgetting to include all edges of G between vertices of U
  **Correction**: G[U] must include every edge of G with both endpoints in U

# Source Reference
Chapter 1: The Basics, Section 1.1, page 4 (pdf p. 14). See Fig. 1.1.3.

# Verification Notes
- Direct from p. 4
- Confidence: HIGH
