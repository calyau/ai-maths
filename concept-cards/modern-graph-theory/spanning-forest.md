---
concept: Spanning Forest
slug: spanning-forest
category: tutte-polynomial
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 356
section: "X.5 A Spanning Tree Expansion of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites: []
extends:
  - spanning-subgraph
related:
  - spanning-tree-expansion
  - internal-activity
  - external-activity
contrasts_with: []
answers_questions:
  - "What must I know before understanding the Tutte polynomial?"
---

# Quick Definition
A spanning forest of a graph $G = (V, E)$ is a subforest $F$ with $V(F) = V$, the same number of components as $G$ ($k(F) = k(G)$), and no cycles ($n(F) = 0$). Equivalently, $r(F) = r(G)$ and $n(F) = 0$.

# Core Definition
"A graph $F = (V', E')$ is a spanning forest of a graph $G = (V, E)$ if $V' = V$, $E' \subset E$, and each component of $F$ is a spanning tree of a component of $G$. Equivalently, $V' = V$, $E' \subset E$, $r(F) = r(G)$ and $n(F) = 0$" (Bollobás, p. 356).

# Prerequisites
This is foundational for the spanning tree expansion.

# Key Properties
1. Same vertices and same number of components as $G$
2. No cycles: $n(F) = 0$
3. For connected $G$: a spanning forest is a spanning tree
4. $|E(F)| = r(G) = |V| - k(G)$

# Relationships
## Extends
- **spanning-subgraph** — A spanning forest is a special spanning subgraph

## Enables
- **spanning-tree-expansion** — $T_G = \sum t_{ij} x^i y^j$ sums over spanning forests

# Source Reference
Chapter X, Section X.5, page 356.

# Verification Notes
- Definition source: Direct from p. 356
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
