---
concept: Fundamental Cut
slug: fundamental-cut
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
  - fundamental cocycle
  - fundamental cut vector
  - fundamental cocycle vector
prerequisites:
  - spanning-tree
  - cut-space
extends: []
related:
  - fundamental-cycle
contrasts_with:
  - fundamental-cycle
answers_questions:
  - "What is a fundamental cut with respect to a spanning tree?"
---

# Quick Definition

For a spanning tree $T$ and a tree edge $e_i$, the fundamental cut is the set of edges crossing the partition created by deleting $e_i$ from $T$. The fundamental cut vectors form a basis for the cut space.

# Core Definition

"By deleting an edge $e_i$ of $T$ the remainder of the spanning tree falls into two components. Let $V_1^i$ be the vertex set of the component containing the initial vertex of $e_i$ and let $V_2^i$ be the vertex set of the component containing the terminal vertex of $e_i$. If $P_i$ is the partition $V = V_1^i \cup V_2^i$ then clearly $\mathbf{u}_{P_i}(e_j) = \delta_{ij}$ for $1 \le j \le n-1$. The cut $E(V_1^i, V_2^i)$ is the fundamental cut, or fundamental cocycle, belonging to $e_i$" (Bollobás, p. 61).

# Prerequisites

- **Spanning tree** — Fundamental cuts are defined relative to a spanning tree
- **Cut space** — Fundamental cuts form a basis

# Key Properties

1. Each tree edge contributes one fundamental cut
2. $\mathbf{u}_{P_i}(e_j) = \delta_{ij}$ for tree edges — orthonormality on tree edges
3. There are $n - 1$ fundamental cuts (for connected graphs)
4. These form a basis of the cut space

# Construction / Recognition

1. Start with a spanning tree $T$
2. For each tree edge $e_i$: delete $e_i$ from $T$, producing components with vertex sets $V_1^i$ and $V_2^i$
3. The fundamental cut is $E(V_1^i, V_2^i)$ — all edges of $G$ crossing this partition

# Context & Application

Fundamental cuts, together with fundamental cycles, provide the dual basis structure used in the matrix formulation of Kirchhoff's laws.

# Examples

**Example** (p. 61): Fig. II.10 shows the fundamental cut vector $\mathbf{u}_{P_4} = e_4 - e_{10} - e_9$.

# Relationships

## Builds Upon
- **Spanning tree**, **Cut space**

## Enables
- Matrix formulation of electrical network equations

## Contrasts With
- **Fundamental cycle** — One per chord; fundamental cuts are one per tree edge

# Common Errors

- **Error**: Confusing the fundamental cut with just the tree edge removed
  **Correction**: The fundamental cut includes all edges of $G$ (not just tree edges) crossing the partition

# Common Confusions

- **Confusion**: Thinking fundamental cuts are independent of the spanning tree
  **Clarification**: Different spanning trees give different fundamental cuts

# Source Reference

Chapter II: Electrical Networks, Section II.3, page 61; Fig. II.10.

# Verification Notes

- Definition source: Direct from p. 61
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
