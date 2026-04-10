---
concept: Network Solution Theorem
slug: network-solution-theorem
category: electrical-networks
subcategory: network-theory
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.3 Vector Spaces and Matrices Associated with Graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - electrical-network
  - incidence-matrix
  - cycle-space
  - cut-space
  - combinatorial-laplacian
extends: []
related:
  - kirchhoffs-theorem-spanning-trees
  - matrix-tree-theorem
contrasts_with: []
answers_questions:
  - "How are electrical network equations solved in matrix form?"
---

# Quick Definition

The current vector in an electrical network is given by $\mathbf{w} = -C(C^tRC)^{-1}C^t\mathbf{g}$, where $C$ is the fundamental cycle matrix, $R$ is the resistance matrix, and $\mathbf{g}$ is the voltage generator vector.

# Core Definition

"**Theorem 11.** The electric current $\mathbf{w}$ satisfying $\mathbf{p} = R\mathbf{w} + \mathbf{g}$ is given by $\mathbf{w} = -C(C^tRC)^{-1}C^t\mathbf{g}$" (Bollobás, p. 65). The proof uses three matrix equations:
1. Kirchhoff's current law: $B\mathbf{w} = \mathbf{0}$
2. Kirchhoff's potential law: $C^t\mathbf{p} = \mathbf{0}$
3. Ohm's law with generator: $\mathbf{p} = R\mathbf{w} + \mathbf{g}$

The splitting $C_1(G) = E_T + E_N$ (tree edges and chords) gives $\mathbf{w} = C\mathbf{w}_N$ and $(C^tRC)\mathbf{w}_N = -C^t\mathbf{g}$.

# Prerequisites

- **Electrical network** — The theorem solves network equations
- **Incidence matrix** — $B$ appears in the current law
- **Cycle space** — The current vector lies in the cycle space
- **Cut space** — The potential vector lies in the cut space
- **Combinatorial Laplacian** — Related to the network solution

# Key Properties

1. The current vector $\mathbf{w}$ lies in the cycle space ($B\mathbf{w} = \mathbf{0}$)
2. The potential vector $\mathbf{p}$ lies in the cut space ($C^t\mathbf{p} = \mathbf{0}$)
3. $C^tRC$ is invertible (since $R$ is positive definite on non-zero-resistance edges)
4. The solution is unique
5. Valid for multigraphs with the same definitions

# Construction / Recognition

1. Choose a spanning tree; split edges into tree edges and chords
2. Construct the fundamental cycle matrix $C$
3. Solve $(C^tRC)\mathbf{w}_N = -C^t\mathbf{g}$ for $\mathbf{w}_N$
4. Recover full current: $\mathbf{w} = C\mathbf{w}_N$

# Context & Application

This theorem provides the complete algebraic solution to the electrical network problem, unifying Kirchhoff's laws and Ohm's law into a single matrix equation. It was Kirchhoff who first realized the applicability of matrix algebra to graph theory, in this very context.

# Examples

**Example** (p. 65): The proof shows that $C_T = -B_T^{-1}B_N$ relates the tree and chord parts of the cycle matrix, and $B_T$ is invertible iff the tree edges form a spanning tree.

# Relationships

## Builds Upon
- **Electrical network**, **Incidence matrix**, **Cycle space**, **Cut space**, **Combinatorial Laplacian**

## Related
- **Kirchhoff's theorem on spanning trees** — Gives current in terms of spanning tree counts
- **Matrix-tree theorem** — Counts spanning trees via the Laplacian

# Common Errors

- **Error**: Forgetting that $R$ must be positive definite on non-zero-resistance edges
  **Correction**: Zero-resistance edges (shorts) require special handling and must form a connected subgraph

# Common Confusions

- **Confusion**: Thinking the solution depends on the choice of spanning tree
  **Clarification**: The final current $\mathbf{w}$ is independent of the spanning tree choice; only the intermediate computation differs

# Source Reference

Chapter II: Electrical Networks, Section II.3, Theorem 11, pages 64-65.

# Verification Notes

- Definition source: Direct theorem statement from p. 65
- Confidence rationale: Explicitly stated with derivation
- Uncertainties: None
- Cross-reference status: Verified
