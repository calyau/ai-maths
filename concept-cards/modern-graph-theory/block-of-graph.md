---
concept: Block of a Graph
slug: block-of-graph
category: connectivity
subcategory: graph-decomposition
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "block"
  - "2-connected component"
prerequisites:
  - graph-connectivity
  - k-connected-graph
extends: []
related:
  - block-cutvertex-tree
  - endblock
contrasts_with:
  - component-of-graph
answers_questions:
  - "What is a block of a graph?"
---

# Quick Definition
A block of a graph $G$ is either a bridge (with its endvertices) or a maximal 2-connected subgraph of $G$.

# Core Definition
A subgraph $B$ of a graph $G$ is a block of $G$ if either it is a bridge (together with the vertices incident with the bridge) or else it is a maximal 2-connected subgraph of $G$. Any two blocks have at most one vertex in common, and every vertex belonging to at least two blocks is a cutvertex of $G$. The graph $G$ decomposes into its blocks $B_1, \ldots, B_p$ in the sense that $E(G) = \bigcup E(B_i)$ with the edge sets pairwise disjoint (Bollobás, p. 82).

# Prerequisites
- **Graph connectivity** — Blocks refine the connectivity structure
- **k-connected graph** — Blocks are maximal 2-connected subgraphs

# Key Properties
1. Every edge belongs to exactly one block
2. Any two blocks share at most one vertex
3. A shared vertex between blocks must be a cutvertex
4. Conversely, every cutvertex belongs to at least two blocks
5. $G$ is 2-connected or $K_2$ iff it has exactly one block (itself)

# Construction / Recognition
1. Find all bridges of $G$ — each is a block
2. Find all maximal 2-connected subgraphs — each is a block
3. These partition the edge set of $G$

# Context & Application
Block decomposition refines the component decomposition of a graph. Just as components decompose a graph by 0-connectivity, blocks decompose by 1-connectivity, revealing the "skeleton" structure through the block-cutvertex tree.

# Examples
**Example** (p. 82, Fig. III.4): A graph is shown with its block-cutvertex tree construction. Block $B_1$ is identified as an endblock.

# Relationships
## Builds Upon
- **k-connected-graph** — Blocks are maximal 2-connected subgraphs

## Enables
- **block-cutvertex-tree** — Tree structure of blocks and cutvertices
- **endblock** — A block containing exactly one cutvertex

## Contrasts With
- **component-of-graph** — Components decompose by 0-connectivity; blocks by 1-connectivity

# Common Errors
- **Error**: Thinking a single edge is always a block
  **Correction**: An edge is a block only if it is a bridge; otherwise it belongs to a 2-connected block

# Common Confusions
- **Confusion**: Confusing blocks with biconnected components in the computer science sense
  **Clarification**: They are the same concept; a block is precisely a maximal 2-connected subgraph or a bridge

# Source Reference
Chapter III, Section III.2, pages 81-82. Fig. III.4.

# Verification Notes
- Definition source: Direct from p. 82
- Confidence rationale: Explicitly defined with figure
- Uncertainties: None
- Cross-reference status: Verified
