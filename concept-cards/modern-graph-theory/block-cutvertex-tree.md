---
concept: Block-Cutvertex Tree
slug: block-cutvertex-tree
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
  - "bc(G)"
  - "block-cut tree"
  - "BC-tree"
prerequisites:
  - block-of-graph
extends:
  - block-of-graph
related:
  - endblock
contrasts_with: []
answers_questions:
  - "How is a connected graph decomposed into blocks?"
---

# Quick Definition
The block-cutvertex tree $bc(G)$ of a nontrivial connected graph $G$ is a tree whose vertices are the blocks and cutvertices of $G$, with edges joining each cutvertex to the blocks containing it.

# Core Definition
If $G$ is a nontrivial connected graph, let $bc(G)$ be the graph whose vertices are the blocks and cutvertices of $G$ and whose edges join cutvertices to blocks: each cutvertex is joined to the blocks containing it. Then $bc(G)$ is a tree. Each endvertex of $bc(G)$ is a block of $G$, called an endblock (Bollobás, p. 82).

# Prerequisites
- **Block of a graph** — The blocks are vertices of the tree

# Key Properties
1. $bc(G)$ is always a tree
2. Endvertices of $bc(G)$ are blocks (endblocks)
3. If $G$ is 2-connected or is $K_2$, then $bc(G)$ has one vertex
4. Otherwise, $G$ has at least two endblocks
5. A block is an endblock iff it contains exactly one cutvertex

# Construction / Recognition
1. Identify all blocks $B_1, \ldots, B_p$ of $G$
2. Identify all cutvertices $v_1, \ldots, v_q$
3. Create a bipartite graph with blocks on one side, cutvertices on the other
4. Connect each cutvertex to the blocks that contain it
5. The result is a tree

# Context & Application
The block-cutvertex tree reveals the global structure of a connected graph through its blocks and cutvertices. It provides a tree decomposition that is useful for structural arguments.

# Examples
**Example** (p. 82, Fig. III.4): The construction of $bc(G)$ from a graph $G$ is illustrated, showing endblock $B_1$.

# Relationships
## Builds Upon
- **block-of-graph** — Blocks are the fundamental components

## Enables
- **endblock** — Endvertex blocks of the tree

# Common Errors
- **Error**: Including non-cutvertices as vertices of $bc(G)$
  **Correction**: Only blocks and cutvertices are vertices of the block-cutvertex tree

# Common Confusions
- **Confusion**: Thinking $bc(G)$ can have cycles
  **Clarification**: $bc(G)$ is always a tree

# Source Reference
Chapter III, Section III.2, page 82. Fig. III.4.

# Verification Notes
- Definition source: Direct from p. 82
- Confidence rationale: Explicitly defined with figure
- Uncertainties: None
- Cross-reference status: Verified
