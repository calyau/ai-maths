---
concept: Endblock
slug: endblock
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
  - "end block"
prerequisites:
  - block-of-graph
  - block-cutvertex-tree
extends:
  - block-of-graph
related: []
contrasts_with: []
answers_questions:
  - "What is an endblock?"
---

# Quick Definition
An endblock is a block containing exactly one cutvertex; it corresponds to an endvertex (leaf) of the block-cutvertex tree.

# Core Definition
Each endvertex of $bc(G)$ is a block of $G$, called an endblock of $G$. A block is an endblock iff it contains exactly one cutvertex. If $G$ is not 2-connected and is not $K_2$, it has at least two endblocks (Bollobás, p. 82).

# Prerequisites
- **Block of a graph** — Endblocks are special blocks
- **Block-cutvertex tree** — Endblocks are leaf nodes

# Key Properties
1. Contains exactly one cutvertex
2. At least two endblocks in any non-2-connected graph with $\ge 3$ vertices
3. Corresponds to leaves of $bc(G)$

# Context & Application
Endblocks are useful in structural arguments: they are "peripheral" parts of the graph that can be analyzed independently.

# Examples
**Example** (p. 82, Fig. III.4): Block $B_1$ is shown as an endblock.

# Relationships
## Builds Upon
- **block-of-graph** — Endblocks are special blocks

# Source Reference
Chapter III, Section III.2, page 82.

# Verification Notes
- Definition source: Direct from p. 82
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
