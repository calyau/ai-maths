---
concept: Fundamental Cycle
slug: fundamental-cycle
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
  - fundamental cycle vector
prerequisites:
  - spanning-tree
  - cycle-space
extends: []
related:
  - fundamental-cut
contrasts_with:
  - fundamental-cut
answers_questions:
  - "What is a fundamental cycle with respect to a spanning tree?"
---

# Quick Definition

For a spanning tree $T$ and a chord (non-tree edge) $e_i$, the fundamental cycle $C_i$ is the unique cycle in $T + e_i$. The fundamental cycle vectors form a basis for the cycle space.

# Core Definition

"For every chord $e_i$ there is a (unique) oriented cycle $C_i$ such that $\mathbf{z}_{C_i}(e_i) = 1$ and $\mathbf{z}_{C_i}(e_j) = 0$ for every other chord $e_j$ [...] We call $C_i$ the fundamental cycle belonging to $e_i$ (with respect to $T$)" (Bollobás, p. 61).

# Prerequisites

- **Spanning tree** — Fundamental cycles are defined relative to a spanning tree
- **Cycle space** — Fundamental cycles form a basis

# Key Properties

1. Each chord contributes exactly one fundamental cycle
2. The fundamental cycle through $e_i$ uses $e_i$ and some tree edges
3. $\mathbf{z}_{C_i}(e_j) = \delta_{ij}$ for chords $e_j$ — the cycle passes through only its own chord
4. There are $m - n + 1$ fundamental cycles (for connected graphs)
5. These form a basis of the cycle space

# Construction / Recognition

1. Start with a spanning tree $T$
2. For each chord $e_i = uv$: find the unique $u$-$v$ path in $T$
3. $C_i$ is this path together with $e_i$, forming a cycle

# Context & Application

Fundamental cycles provide a canonical basis for the cycle space that is computationally convenient. In the matrix formulation of electrical networks, the fundamental cycle matrix $C$ expresses Kirchhoff's potential law.

# Examples

**Example** (p. 61): Fig. II.10 shows $\mathbf{z}_{C_9} = e_9 - e_2 + e_1 + e_4 - e_6$.

# Relationships

## Builds Upon
- **Spanning tree**, **Cycle space**

## Enables
- Matrix formulation of Kirchhoff's potential law

## Contrasts With
- **Fundamental cut** — One per tree edge; fundamental cycles are one per chord

# Common Errors

- **Error**: Thinking fundamental cycles are intrinsic to the graph
  **Correction**: They depend on the choice of spanning tree

# Common Confusions

- **Confusion**: Thinking a fundamental cycle can pass through multiple chords
  **Clarification**: Each fundamental cycle contains exactly one chord

# Source Reference

Chapter II: Electrical Networks, Section II.3, pages 61-62; Fig. II.10.

# Verification Notes

- Definition source: Direct from p. 61
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
