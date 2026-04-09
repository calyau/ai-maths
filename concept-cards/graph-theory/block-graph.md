---
concept: Block Graph
slug: block-graph
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 66
section: "3.1 2-Connected graphs and subgraphs"
extraction_confidence: high
aliases:
  - "block-cutvertex tree"
prerequisites:
  - block
  - cutvertex
extends:
  - block
related:
  - tree
contrasts_with: []
answers_questions:
  - "How are blocks arranged in a graph?"
---

# Quick Definition
The block graph of a connected graph G is the bipartite graph on the set A of cutvertices and set B of blocks, with edges aB whenever cutvertex a belongs to block B. It is always a tree.

# Core Definition
Let A denote the set of cutvertices of G, and B the set of its blocks. The natural bipartite graph on A union B formed by the edges aB with a in B is the **block graph** of G (Diestel, p. 66).

**Proposition 3.1.2.** The block graph of a connected graph is a tree (Diestel, p. 66).

# Prerequisites
- **Block** — the blocks are one vertex class
- **Cutvertex** — the cutvertices are the other vertex class

# Key Properties
1. The block graph is bipartite: one class is cutvertices, the other is blocks
2. It is always a tree (for connected graphs)
3. It captures the "coarse structure" of G as viewed from a distance
4. Leaves in the block graph correspond to end-blocks (blocks with at most one cutvertex)

# Context & Application
The block graph provides a tree-like view of the structure of a connected graph. It reduces structural questions about G to questions about its blocks (which are 2-connected, bridges, or isolated vertices) arranged in a tree pattern.

# Examples
**Example** (p. 66, Fig. 3.1.1): A graph with several blocks connected through cutvertices, and its block graph shown as a tree.

# Relationships
## Builds Upon
- **Block**, **cutvertex**

## Related
- **Tree** — the block graph is always a tree

# Source Reference
Chapter 3, Section 3.1, Proposition 3.1.2, p. 66 (pdf p. 66).

# Verification Notes
- Definition and proposition from p. 66
- Confidence: HIGH — explicitly defined with illustration
