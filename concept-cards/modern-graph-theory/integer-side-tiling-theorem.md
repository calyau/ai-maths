---
concept: Integer Side Tiling Theorem
slug: integer-side-tiling-theorem
category: electrical-networks
subcategory: squaring
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.2 Squaring the Square"
extraction_confidence: high
aliases:
  - "de Bruijn's tiling theorem"
prerequisites:
  - graph
  - bipartite-graph
extends: []
related:
  - dehns-theorem
  - squared-rectangle
contrasts_with: []
answers_questions:
  - "If each tile in a rectangle tiling has an integer side, must the rectangle?"
---

# Quick Definition

If a rectangle is tiled with rectangles each having at least one integer side, then the outer rectangle itself must have an integer side. Four elegant proofs are given (graph-theoretic, analytic, checkerboard, and perturbation).

# Core Definition

"**Theorem 6.** Let a rectangle $T$ be tiled with rectangles $T_1, \ldots, T_\ell$. If each $T_i$ has an integer side then so does $T$" (Bollobás, p. 57). The first proof constructs a bipartite graph $G$ with lattice points on one side and tiling rectangles on the other, using parity of edge count. Theorem 7 generalizes to $n$-dimensional boxes: "If each $B_i$ has at least $k$ integer sides, then $B$ itself has at least $k$ integer sides."

# Prerequisites

- **Graph** — The first proof uses a bipartite graph construction
- **Bipartite graph** — The graph has lattice points and rectangles as vertex classes

# Key Properties

1. Four independent proofs: graph-theoretic, analytic ($\sin 2\pi x \sin 2\pi y$), checkerboard, perturbation
2. Generalizes to $n$ dimensions (Theorem 7)
3. Theorem 8 gives divisibility conditions for brick-tiling of boxes
4. The graph proof uses the parity of $e(G)$ and the fact that corner $(0,0)$ has degree 1

# Construction / Recognition

**Graph proof sketch**: Lattice points in the rectangle form one vertex class $L$; tiling rectangles form the other class $R$. A lattice point is joined to a tile if it is a corner of that tile. Since each tile has an integer side, each tile has degree 0, 2, or 4 (even). So $e(G)$ is even. But corner $(0,0)$ has degree 1, forcing at least one other rectangle corner to be a lattice point.

# Context & Application

These theorems, due to de Bruijn (1969), beautifully combine graph theory, analysis, and combinatorics. They extend Dehn's classical result to general rectangle tilings.

# Examples

**Example** (pp. 57-58): Four complete proofs of Theorem 6 are presented, each using a different technique.

# Relationships

## Builds Upon
- **Graph**, **Bipartite graph**

## Related
- **Dehn's theorem** — Special case for square tilings
- **Squared rectangle** — Context of tiling problems

# Common Errors

- **Error**: Thinking the theorem requires all tiles to be squares
  **Correction**: The tiles are general rectangles, each with at least one integer side

# Common Confusions

- **Confusion**: Thinking all sides must be integer
  **Clarification**: Only one side of each tile needs to be integer; the conclusion is that one side of the outer rectangle is integer

# Source Reference

Chapter II: Electrical Networks, Section II.2, Theorems 6-8, pages 57-59.

# Verification Notes

- Definition source: Direct theorem statement from p. 57
- Confidence rationale: Explicitly stated with four proofs
- Uncertainties: None
- Cross-reference status: Verified
