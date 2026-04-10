---
concept: Adjacency Matrix
slug: adjacency-matrix
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
  - "$A(G)$"
prerequisites:
  - graph
  - adjacency
  - vertex-space-and-edge-space
extends: []
related:
  - incidence-matrix
  - combinatorial-laplacian
contrasts_with:
  - incidence-matrix
answers_questions:
  - "How does the adjacency matrix spectrum relate to graph properties?"
  - "What is the adjacency matrix of a graph?"
---

# Quick Definition

The adjacency matrix $A = A(G) = (a_{ij})$ is the $n \times n$ matrix with $a_{ij} = 1$ if $v_i v_j \in E(G)$ and $a_{ij} = 0$ otherwise. It is real, symmetric, and its eigenvalues encode fundamental graph properties.

# Core Definition

"The adjacency matrix $A = A(G) = (a_{ij})$ of a graph $G$ is the $n \times n$ matrix given by $a_{ij} = 1$ if $v_iv_j \in E(G)$, $0$ otherwise" (Bollobás, p. 62). It defines a linear map $A: C_0(G) \to C_0(G)$. The relationship $BB^t = D - A$ connects it to the incidence matrix $B$ and degree matrix $D$ (Theorem 10). In Chapter VIII the eigenvalues are studied in detail.

# Prerequisites

- **Graph** — The matrix represents a graph
- **Adjacency** — Matrix entries encode adjacency
- **Vertex space and edge space** — The matrix acts on $C_0(G)$

# Key Properties

1. $A$ is symmetric: $a_{ij} = a_{ji}$, so all eigenvalues are real
2. $\text{tr}(A) = 0$ since $a_{ii} = 0$ for simple graphs
3. $(A^k)_{ij}$ counts the number of walks of length $k$ from $v_i$ to $v_j$
4. $BB^t = D - A$ where $D$ is the degree matrix (Theorem 10)
5. If $G$ has at least one edge, $\mu_{\min} < 0 < \mu_{\max}$

# Construction / Recognition

## To construct $A(G)$
1. Fix an ordering $v_1, \ldots, v_n$ of vertices
2. Set $a_{ij} = 1$ if $v_iv_j \in E(G)$, and $a_{ij} = 0$ otherwise
3. The resulting matrix is symmetric with zero diagonal

# Context & Application

The adjacency matrix is the foundation of spectral graph theory (Chapter VIII). Its eigenvalues constrain chromatic number, independence number, connectivity, and expansion properties. It also appears in the electrical network equations through the Laplacian $L = D - A$.

# Examples

**Example** (p. 62): For any graph, $(BB^t)_{ij} = d(v_i)$ if $i = j$, $-1$ if $v_iv_j$ is an edge, and $0$ otherwise, giving $BB^t = D - A$.

**Example** (Ch. VIII, p. 278): $K_n$ has eigenvalues $n-1$ (multiplicity 1) and $-1$ (multiplicity $n-1$).

# Relationships

## Builds Upon
- **Graph**, **Adjacency**, **Vertex space and edge space**

## Enables
- **Combinatorial Laplacian** — $L = D - A$
- Spectral graph theory (Chapter VIII)

## Related
- **Incidence matrix** — Related via $BB^t = D - A$

## Contrasts With
- **Incidence matrix** — $A$ is $n \times n$; $B$ is $n \times m$

# Common Errors

- **Error**: Including self-loops (diagonal entries) for simple graphs
  **Correction**: For simple graphs, all diagonal entries of $A$ are 0

# Common Confusions

- **Confusion**: Confusing adjacency matrix eigenvalues with Laplacian eigenvalues
  **Clarification**: For $k$-regular graphs: Laplacian eigenvalue $= k - $ adjacency eigenvalue; otherwise the relationship is more complex

# Source Reference

Chapter II: Electrical Networks, Section II.3, page 62; Theorem 10, page 62. Also Chapter VIII, Section VIII.2, pages 266-267.

# Verification Notes

- Definition source: Direct from p. 62
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
