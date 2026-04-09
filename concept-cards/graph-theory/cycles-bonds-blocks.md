---
concept: Cycles and Bonds in Blocks
slug: cycles-bonds-blocks
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
  - "Lemma 3.1.1"
prerequisites:
  - block
  - cycle
  - bond
extends: []
related:
  - block-cutvertex-structure
contrasts_with: []
answers_questions:
  - "How are cycles and bonds related to blocks?"
---

# Quick Definition
The cycles of G are precisely the cycles of its blocks. The bonds of G are precisely the minimal cuts of its blocks.

# Core Definition
**Lemma 3.1.1.** (i) The cycles of G are precisely the cycles of its blocks. (ii) The bonds of G are precisely the minimal cuts of its blocks (Diestel, p. 66).

# Prerequisites
- **Block** — the building pieces of G
- **Cycle** — confined to individual blocks
- **Bond** — minimal cuts, also confined to blocks

# Key Properties
1. Any cycle lies entirely within a single block
2. Any bond (minimal cut) arises from a single block
3. This is because cycles are connected and have no cutvertex, hence lie in a maximal such subgraph (a block)
4. For bonds: edges of a cut in a block separate vertices even in G (by maximality of blocks)

# Context & Application
This lemma shows that the local structure (cycles, bonds) of a graph is completely determined by its blocks. It justifies the reduction of structural questions to the 2-connected case.

# Examples
**Example**: If G consists of two triangles sharing a cutvertex, each triangle is a separate block. The cycles of G are exactly the cycles of each triangle (the triangles themselves).

# Relationships
## Builds Upon
- **Block**, **cycle**, **bond**

## Related
- **Block-cutvertex structure** — the global arrangement of blocks

# Source Reference
Chapter 3, Section 3.1, Lemma 3.1.1, p. 66 (pdf p. 66).

# Verification Notes
- Lemma from p. 66
- Confidence: HIGH — explicit lemma with proof
