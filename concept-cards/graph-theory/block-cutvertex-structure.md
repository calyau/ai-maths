---
concept: Block-Cutvertex Structure
slug: block-cutvertex-structure
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
  - "block decomposition"
  - "block-cutvertex tree"
prerequisites:
  - block
  - cutvertex
  - block-graph
extends:
  - block
related:
  - two-connected-graph
contrasts_with: []
answers_questions:
  - "How is a connected graph decomposed into blocks?"
---

# Quick Definition
Every connected graph has a canonical decomposition into blocks (maximal 2-connected subgraphs, bridges, or isolated vertices) that overlap only at cutvertices, arranged in a tree structure (the block graph).

# Core Definition
The structure of G is determined by its blocks and their arrangement. Different blocks overlap in at most one vertex (a cutvertex). Every edge lies in a unique block. G is the union of its blocks. The block graph (a tree) captures the arrangement (Diestel, pp. 65-66, Proposition 3.1.2).

# Prerequisites
- **Block** — the building pieces
- **Cutvertex** — the gluing points
- **Block graph** — the tree structure

# Key Properties
1. Blocks overlap only at cutvertices
2. Every edge lies in a unique block
3. The block graph is always a tree
4. Cycles and bonds are confined to single blocks (Lemma 3.1.1)
5. Reduces structural questions to the 2-connected case

# Context & Application
The block-cutvertex decomposition is the canonical way to decompose a connected graph into 2-connected pieces. It is analogous to how tree-decompositions decompose graphs into pieces of bounded treewidth (Chapter 12).

# Examples
**Example** (p. 66, Fig. 3.1.1): A graph decomposed into blocks, with the block graph shown as a tree.

# Relationships
## Builds Upon
- **Block**, **cutvertex**, **block graph**

## Related
- **2-connected graph** — blocks are the atomic pieces

# Source Reference
Chapter 3, Section 3.1, pp. 65-66 (pdf pp. 65-66).

# Verification Notes
- Synthesized from Section 3.1 discussion
- Confidence: HIGH
