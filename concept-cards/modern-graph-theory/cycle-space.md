---
concept: Cycle Space
slug: cycle-space
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
  - "$Z(G)$"
  - nullity
  - cyclomatic number
  - corank
prerequisites:
  - vertex-space-and-edge-space
  - cycle
  - spanning-tree
extends: []
related:
  - cut-space
  - fundamental-cycle
  - incidence-matrix
contrasts_with:
  - cut-space
answers_questions:
  - "What is the cycle space of a graph?"
---

# Quick Definition

The cycle space $Z(G)$ is the subspace of the edge space $C_1(G)$ spanned by the cycle vectors $\mathbf{z}_L$, where each oriented cycle $L$ maps to a vector with $\pm 1$ entries on its edges. Its dimension is $m - n + k$.

# Core Definition

Given an oriented cycle $L$, define its cycle vector $\mathbf{z}_L \in C_1(G)$ by $\mathbf{z}_L(e_i) = 1$ if $e_i$ is oriented as $L$, $-1$ if oriented opposite, and $0$ if $e_i \notin E(L)$. "Denote by $Z(G)$ the subspace of $C_1(G)$ spanned by the vectors $\mathbf{z}_L$ as $L$ runs over the set of cycles; $Z(G)$ is the cycle space of $G$" (Bollobás, p. 60).

By Theorem 9: $\dim Z(G) = m - n + k$, where $k$ is the number of components. The cycle space is the kernel of the incidence matrix $B$. Its dimension is called the nullity or cyclomatic number of $G$.

# Prerequisites

- **Vertex space and edge space** — $Z(G)$ is a subspace of $C_1(G)$
- **Cycle** — Cycle vectors generate the cycle space
- **Spanning tree** — Fundamental cycles form a basis

# Key Properties

1. $\dim Z(G) = m - n + k$ (the nullity/cyclomatic number)
2. $Z(G) \perp U(G)$ — orthogonal to the cut space
3. $C_1(G) = Z(G) \oplus U(G)$ (orthogonal direct sum, Theorem 9)
4. $Z(G) = \ker(B)$ — the kernel of the incidence matrix
5. Fundamental cycles (one per chord of a spanning tree) form a basis

# Construction / Recognition

## To construct a basis of $Z(G)$
1. Choose a spanning tree $T$
2. For each chord $e_i$ (non-tree edge), the fundamental cycle $C_i$ through $e_i$ gives a basis vector $\mathbf{z}_{C_i}$
3. These $m - n + k$ vectors are independent and span $Z(G)$

# Context & Application

The cycle space encodes the "circular" structure of the graph. In electrical networks, Kirchhoff's potential law states that the potential vector is orthogonal to the cycle space: $C^t \mathbf{p} = \mathbf{0}$.

# Examples

**Example** (p. 60): Fig. II.9 shows a cycle $L$ oriented anti-clockwise with cycle vector $\mathbf{z}_L = (-1, 1, 1, -1, 0, \ldots, 0)$.

**Example** (p. 61): Fig. II.10 shows a fundamental cycle vector $\mathbf{z}_{C_9} = e_9 - e_2 + e_1 + e_4 - e_6$.

# Relationships

## Builds Upon
- **Vertex space and edge space**, **Cycle**, **Spanning tree**

## Enables
- Formulation of Kirchhoff's potential law in matrix form
- **Fundamental cycle** — Basis elements of the cycle space

## Contrasts With
- **Cut space** — The orthogonal complement of the cycle space

# Common Errors

- **Error**: Confusing the cycle space with the set of cycles
  **Correction**: The cycle space is a vector space; it contains all linear combinations of cycle vectors, not just individual cycles

# Common Confusions

- **Confusion**: Thinking the cycle space depends on the choice of spanning tree
  **Clarification**: The cycle space itself is unique; only the basis depends on the spanning tree choice

# Source Reference

Chapter II: Electrical Networks, Section II.3, Theorem 9, pages 59-62.

# Verification Notes

- Definition source: Direct from p. 60
- Confidence rationale: Explicitly defined with basis construction
- Uncertainties: None
- Cross-reference status: Verified
