---
concept: Edge-Disjoint Paths
slug: edge-disjoint-paths
category: connectivity
subcategory: path-structures
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - graph-connectivity
extends: []
related:
  - independent-paths
  - mengers-theorem
  - edge-connectivity
contrasts_with:
  - independent-paths
answers_questions:
  - "What are edge-disjoint paths?"
---

# Quick Definition
Two paths are edge-disjoint if they share no edges (but may share vertices).

# Core Definition
Two $s$-$t$ paths are edge-disjoint if they have no edge in common. The edge form of Menger's theorem states that the minimum number of edges separating $s$ from $t$ equals the maximum number of edge-disjoint $s$-$t$ paths (Bollobás, p. 82).

# Prerequisites
- **Graph connectivity** — Edge-disjoint paths arise in connectivity theory

# Key Properties
1. May share internal vertices (unlike independent paths)
2. Maximum number equals minimum edge-cut size (Menger's edge form)
3. A graph is $k$-edge-connected iff any two vertices have $k$ edge-disjoint paths

# Construction / Recognition
1. Find paths $P_1, P_2$ between $s$ and $t$
2. Check $E(P_1) \cap E(P_2) = \emptyset$

# Context & Application
Edge-disjoint paths characterize edge connectivity via the edge form of Menger's theorem (Corollary 6).

# Examples
**Example** (p. 82): In the proof of the edge form, replace each edge by two directed edges with capacity 1, then apply max-flow min-cut.

# Relationships
## Enables
- **mengers-theorem** — Edge form counts edge-disjoint paths

## Contrasts With
- **independent-paths** — Independent = vertex-disjoint; edge-disjoint allows shared vertices

# Source Reference
Chapter III, Section III.2, pages 82-83.

# Verification Notes
- Definition source: Direct from p. 82
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
