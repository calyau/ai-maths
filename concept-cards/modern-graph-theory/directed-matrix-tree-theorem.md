---
concept: Directed Matrix-Tree Theorem
slug: directed-matrix-tree-theorem
category: linear-algebra-of-graphs
subcategory: graph-matrices
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.3 Vector Spaces and Matrices Associated with Graphs"
extraction_confidence: high
aliases:
  - directed Kirchhoff theorem
prerequisites:
  - matrix-tree-theorem
  - directed-graph
  - oriented-spanning-tree
  - combinatorial-laplacian
extends:
  - matrix-tree-theorem
related:
  - best-theorem
contrasts_with: []
answers_questions:
  - "How are oriented spanning trees counted in directed multigraphs?"
---

# Quick Definition

For a directed multigraph $G$, the number $t_i(G)$ of spanning trees oriented towards $v_i$ equals the first cofactor of the directed Laplacian $L$ belonging to $\ell_{ii}$.

# Core Definition

"**Theorem 14.** Let $G$ be a directed multigraph with vertex set $V(G) = \{v_1, \ldots, v_n\}$. For $1 \le i \le n$, denote by $t_i(G)$ the number of spanning trees oriented towards $v_i$. Also, let $L = (\ell_{ij})$ be the combinatorial Laplacian of $G$: for $i \ne j$, $-\ell_{ij}$ is the number of edges from $v_i$ to $v_j$, and $\ell_{ii} = \sum_{j \ne i} \ell_{ij}$. Then $t_i(G)$ is precisely the first cofactor of $L$ belonging to $\ell_{ii}$" (Bollobás, p. 66).

# Prerequisites

- **Matrix-tree theorem** — The directed version extends the undirected theorem
- **Directed graph** — Applies to directed multigraphs
- **Oriented spanning tree** — Counts oriented spanning trees
- **Combinatorial Laplacian** — Uses the directed Laplacian

# Key Properties

1. The directed Laplacian: $-\ell_{ij}$ = number of edges from $v_i$ to $v_j$; $\ell_{ii}$ = out-degree of $v_i$
2. $t_i(G)$ = cofactor of $L$ belonging to $\ell_{ii}$
3. Contains Corollary 13 as a special case (replace each undirected edge by two directed edges)
4. The proof parallels Theorem 12 using cut-and-fuse on directed edges

# Construction / Recognition

1. Form the directed Laplacian $L$
2. Delete row $i$ and column $i$
3. The determinant of the resulting matrix equals $t_i(G)$

# Context & Application

This theorem connects the BEST theorem (which uses $t_i(G)$) to matrix algebra. Together, they allow computation of the number of directed Euler circuits.

# Examples

**Example** (p. 66): The result contains the undirected case: given a multigraph, replace each edge by two directed edges and apply Theorem 14 to get Corollary 13.

# Relationships

## Builds Upon
- **Matrix-tree theorem**, **Directed graph**, **Oriented spanning tree**, **Combinatorial Laplacian**

## Enables
- Computing $t_i(G)$ for the BEST theorem

## Related
- **BEST theorem** — Uses $t_i(G)$ to count Euler circuits

# Common Errors

- **Error**: Using the undirected Laplacian for a directed graph
  **Correction**: The directed Laplacian has $-\ell_{ij}$ = number of edges from $v_i$ to $v_j$ (not symmetric)

# Common Confusions

- **Confusion**: Thinking $t_i(G)$ depends on $i$
  **Clarification**: For Eulerian directed graphs ($d^+(v) = d^-(v)$), $t_i$ is independent of $i$ (BEST theorem); in general, different roots may give different counts

# Source Reference

Chapter II: Electrical Networks, Section II.3, Theorem 14, page 66.

# Verification Notes

- Definition source: Direct theorem statement from p. 66
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
