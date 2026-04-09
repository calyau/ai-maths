---
concept: "Jung's Theorem"
slug: jungs-theorem
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 215
section: "8.2 Paths, trees, and ends"
extraction_confidence: high
aliases: []
prerequisites:
  - normal-spanning-tree
  - infinite-graph
extends: []
related:
  - star-comb-lemma
contrasts_with: []
answers_questions:
  - "Does every countable connected graph have a normal spanning tree?"
---

# Quick Definition
Jung's theorem (1967) states that every countable connected graph has a normal spanning tree.

# Core Definition
**Theorem 8.2.4** (Jung 1967): Every countable connected graph has a normal spanning tree (Diestel, p. 215).

# Prerequisites
- **Normal spanning tree** — The object whose existence is asserted
- **Infinite graph** — The theorem applies to countable connected graphs

# Key Properties
1. The construction follows the proof of Proposition 1.5.6 for finite graphs, extended to the infinite case
2. The normal spanning tree is built in an infinite sequence of steps
3. Each step adds one more vertex to the tree
4. The proof ensures normality is preserved at each step

# Context & Application
This is a fundamental existence result in infinite graph theory. It guarantees the availability of normal spanning trees for all countable graphs, enabling the structural analysis of their ends and separation properties. For uncountable graphs, a normal spanning tree need not exist.

# Examples
**Example 1** (p. 215-216): The proof constructs T_0, T_1, ... inductively, ensuring each T_n is a finite normal tree.

# Relationships
## Builds Upon
- **Normal spanning tree** — The theorem asserts its existence

## Enables
- All results that require a normal spanning tree for countable graphs
- Topological cycle space theory (Theorem 8.5.8)

# Source Reference
Chapter 8, Section 8.2, pages 215-216 (Theorem 8.2.4).

# Verification Notes
- Statement directly from p. 215
- Confidence: HIGH — named theorem with proof sketch
