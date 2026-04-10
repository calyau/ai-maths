---
concept: Oriented Spanning Tree
slug: oriented-spanning-tree
category: linear-algebra-of-graphs
subcategory: directed-trees
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.3 Hamilton Cycles and Euler Circuits"
extraction_confidence: high
aliases:
  - rooted spanning tree
  - arborescence
prerequisites:
  - spanning-tree
  - directed-graph
extends:
  - spanning-tree
related:
  - best-theorem
  - matrix-tree-theorem
contrasts_with: []
answers_questions:
  - "What is an oriented spanning tree?"
---

# Quick Definition

A spanning tree oriented towards vertex $v_i$ (its root) is a directed spanning tree where for every other vertex $v_j$, the unique path from $v_j$ to $v_i$ follows the edge orientations. The count $t_i(G)$ is the same for all roots.

# Core Definition

"We say that a spanning tree is oriented towards $v_i$, its root, if for every $j \neq i$ the unique path from $v_j$ to $v_i$ is oriented towards $v_i$" (Bollobás, p. 27). The BEST theorem (Theorem 13) establishes that $t_1(G) = t_2(G) = \cdots = t_n(G)$. Theorem 14 in Section II.3 shows that $t_i(G)$ equals the appropriate first cofactor of the directed Laplacian.

# Prerequisites

- **Spanning tree** — An oriented spanning tree is a directed spanning tree
- **Directed graph** — Requires directed edges

# Key Properties

1. All edges point "towards" the root
2. $t_i(G)$ is independent of the choice of root $i$ (Theorem 13)
3. $t_i(G)$ equals the first cofactor of the directed Laplacian belonging to $\ell_{ii}$ (Theorem 14)
4. Oriented spanning trees appear in the BEST theorem counting formula

# Construction / Recognition

For a directed multigraph, verify that:
1. The subgraph is a spanning tree of the underlying undirected graph
2. All edges point towards the root

# Context & Application

Oriented spanning trees bridge the BEST theorem (counting Euler circuits) and the directed matrix-tree theorem. The map $\phi_1$ in the BEST theorem proof sends each Euler trail to an oriented spanning tree via "last exit" edges.

# Examples

**Example** (p. 27): In the proof of Theorem 13, each Euler trail $S$ starting at $v_1$ determines a spanning tree oriented towards $v_1$ by taking the last edge used to exit each vertex $v_j$ ($j > 1$).

# Relationships

## Builds Upon
- **Spanning tree**, **Directed graph**

## Enables
- **BEST theorem** — Uses oriented spanning tree counts
- **Matrix-tree theorem** (directed version, Theorem 14)

# Common Errors

- **Error**: Confusing oriented spanning trees with arbitrarily oriented trees
  **Correction**: An oriented spanning tree has all edges pointing towards a specific root; arbitrary orientations do not have this property

# Common Confusions

- **Confusion**: Thinking the number of oriented trees depends on the root
  **Clarification**: $t_i(G)$ is the same for all roots $i$ (a consequence of the BEST theorem)

# Source Reference

Chapter I: Fundamentals, Section I.3, pages 27-28; Chapter II, Section II.3, Theorem 14, page 66.

# Verification Notes

- Definition source: Direct from p. 27
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
