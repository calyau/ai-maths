---
concept: Graph Partition
slug: graph-partition
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 59
section: "2.4 Tree-packing and arboricity"
extraction_confidence: high
aliases:
  - "edge partition"
prerequisites:
  - graph
  - subgraph
extends: []
related:
  - arboricity
  - nash-williams-arboricity-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for subgraphs to partition a graph?"
---

# Quick Definition
Subgraphs G1, ..., Gk of G partition G if their edge sets form a partition of E(G).

# Core Definition
Subgraphs G1, ..., Gk of a graph G **partition** G if their edge sets form a partition of E(G) (Diestel, p. 59).

# Prerequisites
- **Graph**, **subgraph**

# Key Properties
1. Every edge belongs to exactly one of the subgraphs
2. The vertex sets may overlap
3. "Into how many connected spanning subgraphs can we partition G?" is the spanning tree packing question
4. "Into how few acyclic subgraphs?" is the arboricity question

# Context & Application
Graph partition unifies the tree packing and arboricity concepts as dual questions about edge partitions.

# Examples
**Example**: Partitioning a graph into forests: the arboricity is the minimum number of forests needed.

# Relationships
## Related
- **Arboricity** — minimum forests in a partition
- **Nash-Williams arboricity theorem** — characterizes when k forests suffice

# Source Reference
Chapter 2, Section 2.4, p. 59 (pdf p. 59).

# Verification Notes
- Definition from p. 59
- Confidence: HIGH
