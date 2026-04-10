---
concept: Combinatorial Laplacian
slug: combinatorial-laplacian
category: linear-algebra-of-graphs
subcategory: graph-matrices
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.3 Vector Spaces and Matrices Associated with Graphs"
extraction_confidence: high
aliases:
  - Kirchhoff matrix
  - "$L = D - A$"
  - graph Laplacian
  - Laplacian matrix
prerequisites:
  - adjacency-matrix
  - incidence-matrix
extends: []
related:
  - matrix-tree-theorem
contrasts_with:
  - adjacency-matrix
answers_questions:
  - "How does the Laplacian matrix relate to spanning tree counting?"
  - "What is the combinatorial Laplacian of a graph?"
  - "How does the adjacency matrix spectrum relate to graph properties?"
---

# Quick Definition

The combinatorial Laplacian (Kirchhoff matrix) of a graph is $L = D - A = BB^t$, where $D$ is the diagonal degree matrix, $A$ is the adjacency matrix, and $B$ is the signed incidence matrix. Its cofactors count spanning trees.

# Core Definition

"The matrix $L = D - A$, the combinatorial Laplacian or Kirchhoff matrix of a graph, is of great importance in spectral graph theory" (Bollobás, p. 62). By Theorem 10, $L = BB^t$ where $B$ is the incidence matrix. All rows and columns of $L$ sum to 0, so $\det(L) = 0$ and the smallest eigenvalue is always 0. The quadratic form is $\langle Lx, x\rangle = \sum_{v_iv_j \in E} (x_i - x_j)^2$ (Ch. VIII, p. 276).

For a weighted network with conductance matrix $C$: $L = D - C$ where $D_{ii} = \sum_j c_{ij}$ (p. 65).

# Prerequisites

- **Adjacency matrix** — $L = D - A$ uses the adjacency matrix
- **Incidence matrix** — $L = BB^t$ is the Gram matrix of $B$

# Key Properties

1. $L = D - A = BB^t$
2. Positive semi-definite: all eigenvalues $\lambda_i \ge 0$
3. $\lambda_1 = 0$ with eigenvector $(1, 1, \ldots, 1)$
4. $\lambda_2 > 0$ iff $G$ is connected
5. Multiplicity of eigenvalue 0 equals the number of components
6. All first cofactors of $L$ are equal (Theorem 12)
7. For $k$-regular graphs: Laplacian eigenvalue $= k - $ adjacency eigenvalue

# Construction / Recognition

## To construct $L$
1. Form the diagonal matrix $D$ with $D_{ii} = d(v_i)$
2. Form the adjacency matrix $A$
3. Compute $L = D - A$

Equivalently: $L_{ij} = d(v_i)$ if $i = j$; $L_{ij} = -1$ if $v_iv_j \in E(G)$; $L_{ij} = 0$ otherwise.

# Context & Application

The Laplacian is central to spectral graph theory, electrical network theory, and algebraic graph theory. It connects combinatorial properties (spanning trees) to algebraic properties (cofactors) via the matrix-tree theorem. In Chapter VIII, the second eigenvalue $\lambda_2$ is shown to bound vertex connectivity, edge expansion, and random walk mixing time.

# Examples

**Example** (p. 62): For any graph, $L_{ij} = (BB^t)_{ij} = d(v_i)$ if $i = j$, $-1$ if $v_iv_j \in E(G)$, $0$ otherwise.

**Example** (Theorem 12, p. 65): The number of spanning trees equals any first cofactor of $L$.

**Example** (Ch. VIII, p. 276): For $K_n$: $L = nI - J$, eigenvalues $0$ (mult. 1) and $n$ (mult. $n-1$).

# Relationships

## Builds Upon
- **Adjacency matrix** — $L = D - A$
- **Incidence matrix** — $L = BB^t$

## Enables
- **Matrix-tree theorem** — Spanning tree count = cofactor of $L$
- Spectral analysis of graphs and connectivity bounds (Chapter VIII-IX)

## Contrasts With
- **Adjacency matrix** — $L$ incorporates degree information; $A$ does not

# Common Errors

- **Error**: Computing $\det(L)$ and expecting the number of spanning trees
  **Correction**: $\det(L) = 0$ always; use any first cofactor (delete one row and column)

# Common Confusions

- **Confusion**: Confusing Laplacian eigenvalues with adjacency eigenvalues
  **Clarification**: For $k$-regular graphs, $\lambda = k - \mu$; otherwise the relationship is more complex

# Source Reference

Chapter II: Electrical Networks, Section II.3, pages 62-65; Theorem 10, Theorem 12, Corollary 13. Also Chapter VIII, Section VIII.2, pages 275-278.

# Verification Notes

- Definition source: Direct from p. 62 (Ch. II) and p. 275 (Ch. VIII)
- Confidence rationale: Explicitly defined in both chapters
- Uncertainties: None
- Cross-reference status: Verified
