---
concept: Incidence Matrix
slug: incidence-matrix
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
  - "$B(G)$"
prerequisites:
  - graph
  - directed-graph
  - vertex-space-and-edge-space
extends: []
related:
  - adjacency-matrix
  - combinatorial-laplacian
  - cycle-space
  - cut-space
contrasts_with:
  - adjacency-matrix
answers_questions:
  - "What is the incidence matrix of a graph?"
---

# Quick Definition

The incidence matrix $B = B(G)$ is the $n \times m$ matrix with $b_{ij} = 1$ if $v_i$ is the initial vertex of $e_j$, $-1$ if $v_i$ is the terminal vertex, and $0$ otherwise. It maps $C_1(G)$ to $C_0(G)$.

# Core Definition

"The incidence matrix $B = B(G) = (b_{ij})$ of $G$ is the $n \times m$ matrix defined by $b_{ij} = 1$ if $v_i$ is the initial vertex of the edge $e_j$, $-1$ if $v_i$ is the terminal vertex of the edge $e_j$, $0$ otherwise" (Bollobás, p. 62). The definition requires an orientation of the edges.

# Prerequisites

- **Graph** — The matrix represents a graph
- **Directed graph** — Requires an edge orientation
- **Vertex space and edge space** — $B: C_1(G) \to C_0(G)$

# Key Properties

1. $B$ is an $n \times m$ matrix
2. Each column has exactly one $+1$ and one $-1$ entry
3. $BB^t = D - A$ (Theorem 10) — the combinatorial Laplacian
4. $\ker(B) = Z(G)$ — the cycle space is the kernel of $B$
5. $\text{Im}(B^t) = U(G)$ — the cut space is the image of $B^t$
6. $\text{rank}(B) = n - k$ where $k$ is the number of components

# Construction / Recognition

1. Orient each edge of the graph
2. For each edge $e_j$ from $v_i$ to $v_k$: set $b_{ij} = 1$, $b_{kj} = -1$, all other entries in column $j$ to 0

# Context & Application

The incidence matrix connects the edge space to the vertex space and is the key matrix in the formulation of Kirchhoff's laws. The current law becomes $B\mathbf{w} = \mathbf{0}$, meaning the current vector lies in $\ker(B) = Z(G)$.

# Examples

**Example** (p. 62): Theorem 10 proves $BB^t = D - A$. The $(i,j)$ entry of $BB^t$ is $d(v_i)$ if $i = j$, $-1$ if $v_iv_j$ is an edge, and $0$ otherwise.

# Relationships

## Builds Upon
- **Graph**, **Directed graph**, **Vertex space and edge space**

## Enables
- **Combinatorial Laplacian** — $L = BB^t = D - A$
- **Cycle space** — $\ker(B) = Z(G)$
- **Cut space** — $\text{Im}(B^t) = U(G)$
- Kirchhoff's current law in matrix form

## Contrasts With
- **Adjacency matrix** — $A$ is $n \times n$ (vertex-vertex); $B$ is $n \times m$ (vertex-edge)

# Common Errors

- **Error**: Forgetting that $B$ depends on the chosen edge orientation
  **Correction**: Different orientations give different $B$ matrices, but $BB^t = D - A$ is orientation-independent

# Common Confusions

- **Confusion**: Confusing the unsigned incidence matrix with the signed one
  **Clarification**: The signed incidence matrix (with $\pm 1$ entries) is used here; the unsigned version has only 0 and 1 entries

# Source Reference

Chapter II: Electrical Networks, Section II.3, pages 62-63; Theorem 10, page 62.

# Verification Notes

- Definition source: Direct from p. 62
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
