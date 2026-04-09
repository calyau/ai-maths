---
concept: Block
slug: block
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 65
section: "3.1 2-Connected graphs and subgraphs"
extraction_confidence: high
aliases:
  - "block of a graph"
prerequisites:
  - graph
  - two-connected-graph
  - cutvertex
  - bridge
extends: []
related:
  - block-graph
  - two-connected-graph
contrasts_with: []
answers_questions:
  - "What is a block of a graph?"
---

# Quick Definition
A block of a graph G is a maximal connected subgraph without a cutvertex: either a maximal 2-connected subgraph, a bridge with its ends, or an isolated vertex.

# Core Definition
A maximal connected subgraph without a cutvertex is called a **block**. Thus, every block of a graph G is either a maximal 2-connected subgraph, or a bridge (with its ends), or an isolated vertex. Conversely, every such subgraph is a block. By their maximality, different blocks of G overlap in at most one vertex, which is then a cutvertex of G. Hence, every edge of G lies in a unique block, and G is the union of its blocks (Diestel, p. 65).

# Prerequisites
- **Graph** — blocks are subgraphs of a graph
- **2-connected graph** — one type of block
- **Cutvertex** — blocks have no cutvertex; blocks overlap at cutvertices
- **Bridge** — a bridge with its ends is a block

# Key Properties
1. Every block is a maximal 2-connected subgraph, a bridge (with ends), or an isolated vertex
2. Different blocks overlap in at most one vertex
3. If two blocks share a vertex, that vertex is a cutvertex of G
4. Every edge lies in a unique block
5. G is the union of its blocks
6. The cycles of G are precisely the cycles of its blocks (Lemma 3.1.1)

# Construction / Recognition
## To Identify Blocks
1. Find all cutvertices of G
2. Remove cutvertices to identify biconnected components
3. Each biconnected component, together with the cutvertices on its boundary, forms a block
4. Each bridge (with its endpoints) is a separate block
5. Each isolated vertex is a block

# Context & Application
Blocks decompose a connected graph into its 2-connected pieces. This decomposition is canonical and tree-like (the block graph is a tree, Proposition 3.1.2). Understanding blocks reduces many problems to the 2-connected case.

# Examples
**Example** (p. 66, Fig. 3.1.1): A graph is shown alongside its block graph, illustrating how blocks overlap at cutvertices.

# Relationships
## Builds Upon
- **Graph**, **2-connected graph**, **cutvertex**, **bridge**

## Enables
- **Block graph** — the tree structure of blocks and cutvertices
- Structural decomposition of graphs into 2-connected pieces

## Related
- **2-connected graph** — blocks generalize the notion

# Common Errors
- **Error**: Thinking blocks must be 2-connected
  **Correction**: A bridge with its two endpoints is also a block, even though it is not 2-connected

# Common Confusions
- **Confusion**: Confusing blocks with components
  **Clarification**: Components are maximal connected subgraphs; blocks are maximal connected subgraphs without cutvertices. A connected graph has one component but may have many blocks.

# Source Reference
Chapter 3, Section 3.1, pp. 65-66 (pdf pp. 65-66).

# Verification Notes
- Definition from p. 65
- Properties from pp. 65-66
- Confidence: HIGH — explicitly defined with full discussion
