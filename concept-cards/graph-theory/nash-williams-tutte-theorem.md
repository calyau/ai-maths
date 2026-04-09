---
concept: Nash-Williams-Tutte Theorem
slug: nash-williams-tutte-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 56
section: "2.4 Tree-packing and arboricity"
extraction_confidence: high
aliases:
  - "Nash-Williams 1961"
  - "Tutte 1961"
  - "tree-packing theorem"
prerequisites:
  - edge-disjoint-spanning-trees
extends: []
related:
  - arboricity
  - nash-williams-arboricity-theorem
contrasts_with: []
answers_questions:
  - "When does a graph have k edge-disjoint spanning trees?"
---

# Quick Definition
A multigraph contains k edge-disjoint spanning trees if and only if for every partition of its vertex set into r sets, it has at least k(r-1) cross-edges.

# Core Definition
**Theorem 2.4.1 (Nash-Williams 1961; Tutte 1961).** A multigraph contains k edge-disjoint spanning trees if and only if for every partition P of its vertex set it has at least k(|P|-1) cross-edges (Diestel, p. 56).

# Prerequisites
- **Edge-disjoint spanning trees** — the objects whose existence is characterized

# Key Properties
1. The condition involves all partitions of V, not just bipartitions
2. The forward direction: each spanning tree has >= r-1 cross-edges for a partition into r sets
3. The proof uses edge replacements in optimal k-tuples of spanning forests (Lemma 2.4.3)
4. Corollary 2.4.2: 2k-edge-connectivity suffices

# Construction / Recognition
## Proof Strategy
1. Consider k-tuples F = (F1, ..., Fk) of edge-disjoint spanning forests maximizing total edges
2. If some Fi is not a tree, find an edge not in any Fi
3. Use Lemma 2.4.3 to find a connected set U in all forests
4. Contract U and apply induction

# Context & Application
This theorem was proved independently by Nash-Williams and Tutte in 1961. It provides a complete characterization of when k edge-disjoint spanning trees exist, answering a fundamental question about edge-disjoint connectivity.

# Examples
**Example** (Corollary 2.4.2): A 2k-edge-connected graph G has k edge-disjoint spanning trees. Proof: any partition into r sets has at least (1/2) * r * 2k = kr >= k(r-1) cross-edges.

# Relationships
## Builds Upon
- **Edge-disjoint spanning trees**

## Related
- **Arboricity** — dual concept (edge covering by forests)
- **Nash-Williams arboricity theorem** — the covering analogue

# Common Errors
- **Error**: Checking only bipartitions instead of all partitions
  **Correction**: The condition must hold for partitions into any number r >= 2 of sets

# Common Confusions
- **Confusion**: Confusing this with the arboricity theorem
  **Clarification**: This theorem characterizes packing (edge-disjoint spanning trees); the arboricity theorem characterizes covering (partitioning edges into forests)

# Source Reference
Chapter 2, Section 2.4, Theorem 2.4.1, pp. 56-59 (pdf pp. 56-59).

# Verification Notes
- Theorem statement from p. 56
- Proof from pp. 57-59
- Confidence: HIGH — major theorem with full proof
