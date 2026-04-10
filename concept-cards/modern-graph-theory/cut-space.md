---
concept: Cut Space
slug: cut-space
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
  - "$U(G)$"
  - cocycle space
  - rank of a graph
prerequisites:
  - vertex-space-and-edge-space
  - spanning-tree
extends: []
related:
  - cycle-space
  - fundamental-cut
  - incidence-matrix
contrasts_with:
  - cycle-space
answers_questions:
  - "What is the cut space of a graph?"
---

# Quick Definition

The cut space $U(G)$ is the subspace of $C_1(G)$ spanned by cut vectors $\mathbf{u}_P$, where $P$ is a vertex partition $V = V_1 \cup V_2$. Its dimension is $n - k$ (the rank of the graph).

# Core Definition

Given a partition $V = V_1 \cup V_2$, the cut $E(V_1, V_2)$ is the set of edges between $V_1$ and $V_2$. The cut vector $\mathbf{u}_P(e_i) = 1$ if $e_i$ goes from $V_1$ to $V_2$, $-1$ if from $V_2$ to $V_1$, and $0$ otherwise. "$U(G)$ [is] the subspace of the edge space $C_1(G)$ spanned by all the cut vectors $\mathbf{u}_P$, and we call it the cut (or cocycle) space of $G$" (Bollobás, p. 60).

By Theorem 9: $\dim U(G) = n - k$. The cut space is the image of $B^t$ and the orthogonal complement of the cycle space.

# Prerequisites

- **Vertex space and edge space** — $U(G)$ is a subspace of $C_1(G)$
- **Spanning tree** — Fundamental cuts form a basis

# Key Properties

1. $\dim U(G) = n - k$ (the rank of $G$)
2. $U(G) \perp Z(G)$ — orthogonal to the cycle space
3. $C_1(G) = Z(G) \oplus U(G)$ (Theorem 9)
4. $U(G) = \text{Im}(B^t)$ — the image of the transpose of the incidence matrix
5. Fundamental cuts (one per tree edge) form a basis

# Construction / Recognition

## To construct a basis of $U(G)$
1. Choose a spanning tree $T$ with edges $e_1, \ldots, e_{n-1}$
2. Deleting tree edge $e_i$ splits $T$ into two components with vertex sets $V_1^i, V_2^i$
3. The fundamental cut vector $\mathbf{u}_{P_i}$ has $\mathbf{u}_{P_i}(e_j) = \delta_{ij}$ for tree edges
4. These $n - k$ vectors form a basis

# Context & Application

The cut space encodes the "connectivity structure" of the graph. In electrical networks, Kirchhoff's current law states that the current vector lies in the cycle space (orthogonal complement of cuts).

# Examples

**Example** (p. 61): Fig. II.10 shows a fundamental cut vector $\mathbf{u}_{P_4} = e_4 - e_{10} - e_9$.

# Relationships

## Builds Upon
- **Vertex space and edge space**, **Spanning tree**

## Enables
- **Fundamental cut** — Basis elements of the cut space
- Kirchhoff's current law formulation

## Contrasts With
- **Cycle space** — Orthogonal complement

# Common Errors

- **Error**: Thinking every partition gives a "cut" regardless of connectivity
  **Correction**: A cut $E(V_1, V_2)$ may be empty if no edges cross the partition

# Common Confusions

- **Confusion**: Confusing "cut" with "edge cut" (minimum edge set disconnecting the graph)
  **Clarification**: Here "cut" means any edge set $E(V_1, V_2)$ for a vertex partition, not necessarily a minimum disconnecting set

# Source Reference

Chapter II: Electrical Networks, Section II.3, Theorem 9, pages 60-62.

# Verification Notes

- Definition source: Direct from p. 60
- Confidence rationale: Explicitly defined with basis construction
- Uncertainties: None
- Cross-reference status: Verified
