---
concept: Vertex Space and Edge Space
slug: vertex-space-and-edge-space
category: linear-algebra-of-graphs
subcategory: vector-spaces
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
  - "$C_0(G)$"
  - "$C_1(G)$"
  - vertex space
  - edge space
prerequisites:
  - graph
extends: []
related:
  - cycle-space
  - cut-space
  - adjacency-matrix
  - incidence-matrix
contrasts_with: []
answers_questions:
  - "What are the vertex and edge spaces of a graph?"
---

# Quick Definition

The vertex space $C_0(G)$ is the vector space of functions from $V(G)$ to $\mathbb{C}$, with dimension $n$. The edge space $C_1(G)$ is the vector space of functions from $E(G)$ to $\mathbb{C}$, with dimension $m$.

# Core Definition

"The vertex space $C_0(G)$ of a graph $G$ is the complex vector space of all functions from $V(G)$ into $\mathbb{C}$. Similarly, the edge space $C_1(G)$ is the complex vector space of all functions from $E(G)$ into $\mathbb{C}$" (Bollobás, p. 59). With standard bases $(v_1, \ldots, v_n)$ and $(e_1, \ldots, e_m)$, these spaces are equipped with the inner product $\langle \mathbf{x}, \mathbf{y} \rangle = \sum_i x_i \overline{y}_i$.

# Prerequisites

- **Graph** — The spaces are defined for graphs

# Key Properties

1. $\dim C_0(G) = n = |V(G)|$
2. $\dim C_1(G) = m = |E(G)|$
3. Standard bases are orthonormal
4. The field can be replaced by $F_2$ or other fields
5. $C_1(G)$ decomposes as the orthogonal direct sum of cycle space and cut space

# Construction / Recognition

Elements of $C_0(G)$ are written as $\mathbf{x} = \sum x_i v_i$ or $(x_i)_1^n$. Elements of $C_1(G)$ as $\mathbf{y} = \sum y_i e_i$ or $(y_i)_1^m$.

# Context & Application

These vector spaces are the algebraic foundation for spectral graph theory and the matrix formulation of electrical network problems. The incidence matrix $B$ maps $C_1(G) \to C_0(G)$, and the adjacency matrix $A$ maps $C_0(G) \to C_0(G)$.

# Examples

**Example** (p. 59): For a graph with $n$ vertices and $m$ edges, $C_0(G) \cong \mathbb{C}^n$ and $C_1(G) \cong \mathbb{C}^m$.

# Relationships

## Builds Upon
- **Graph**

## Enables
- **Cycle space** — A subspace of $C_1(G)$
- **Cut space** — A subspace of $C_1(G)$
- **Incidence matrix** — A linear map $C_1(G) \to C_0(G)$
- **Adjacency matrix** — A linear map $C_0(G) \to C_0(G)$

# Common Errors

- **Error**: Confusing vertex space with edge space
  **Correction**: Vertex space has dimension $n$ (vertices); edge space has dimension $m$ (edges)

# Common Confusions

- **Confusion**: Thinking the vector spaces depend on the field choice
  **Clarification**: The dimensions are field-independent; the specific structure of cycle/cut spaces is also field-independent

# Source Reference

Chapter II: Electrical Networks, Section II.3, page 59.

# Verification Notes

- Definition source: Direct from p. 59
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
