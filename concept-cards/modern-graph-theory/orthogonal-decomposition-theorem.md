---
concept: Orthogonal Decomposition of Edge Space
slug: orthogonal-decomposition-theorem
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
aliases: []
prerequisites:
  - vertex-space-and-edge-space
  - cycle-space
  - cut-space
extends: []
related:
  - fundamental-cycle
  - fundamental-cut
  - incidence-matrix
contrasts_with: []
answers_questions:
  - "How does the edge space decompose into cycle and cut spaces?"
---

# Quick Definition

The edge space $C_1(G)$ is the orthogonal direct sum of the cycle space $Z(G)$ and the cut space $U(G)$: $C_1(G) = Z(G) \oplus U(G)$, with $\dim Z(G) = m - n + k$ and $\dim U(G) = n - k$.

# Core Definition

"**Theorem 9.** The inner product space $C_1(G)$ is the orthogonal direct sum of the cycle space $Z(G)$ and the cut space $U(G)$. If $G$ has $n$ vertices, $m$ edges and $k$ components then $\dim Z(G) = m - n + k$ and $\dim U(G) = n - k$" (Bollobás, p. 60).

# Prerequisites

- **Vertex space and edge space** — $C_1(G)$ is the ambient space
- **Cycle space** — One summand $Z(G)$
- **Cut space** — The other summand $U(G)$

# Key Properties

1. $Z(G) \perp U(G)$ — cycle and cut spaces are orthogonal
2. $C_1(G) = Z(G) \oplus U(G)$ — they span the entire edge space
3. $\dim Z(G) + \dim U(G) = m$
4. The nullity $n(G) = m - n + k$ and rank $r(G) = n - k$ are field-independent
5. The proof uses fundamental cycles and fundamental cuts as independent sets in $Z(G)$ and $U(G)$

# Construction / Recognition

The proof constructs $m - n + k$ independent cycle vectors (fundamental cycles) and $n - k$ independent cut vectors (fundamental cuts). Orthogonality follows from: each oriented cycle crosses any cut an equal number of times in each direction.

# Context & Application

This decomposition is the algebraic foundation for formulating Kirchhoff's laws. The current law says $\mathbf{w} \in Z(G)$ (kernel of $B$); the potential law says $\mathbf{p} \perp Z(G)$, i.e., $\mathbf{p} \in U(G)$.

# Examples

**Example** (pp. 61-62): Using a spanning tree $T$ with edges $e_1, \ldots, e_{n-1}$ and chords $e_n, \ldots, e_m$, the fundamental cycle vectors have $\mathbf{z}_{C_i}(e_j) = \delta_{ij}$ for $j \ge n$, and fundamental cut vectors have $\mathbf{u}_{P_i}(e_j) = \delta_{ij}$ for $j \le n-1$.

# Relationships

## Builds Upon
- **Vertex space and edge space**, **Cycle space**, **Cut space**

## Enables
- Matrix formulation of Kirchhoff's laws
- Algebraic solution of electrical network equations

## Related
- **Fundamental cycle**, **Fundamental cut** — Basis elements for the two spaces
- **Incidence matrix** — $\ker(B) = Z(G)$, $\text{Im}(B^t) = U(G)$

# Common Errors

- **Error**: Thinking cycle space and cut space can overlap
  **Correction**: They are orthogonal complements; their intersection is $\{0\}$

# Common Confusions

- **Confusion**: Thinking the decomposition depends on the field
  **Clarification**: The dimensions $m - n + k$ and $n - k$ are field-independent

# Source Reference

Chapter II: Electrical Networks, Section II.3, Theorem 9, pages 60-62.

# Verification Notes

- Definition source: Direct theorem statement from p. 60
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
