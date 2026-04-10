---
# === CORE IDENTIFICATION ===
concept: Lagrangian of a Graph
slug: lagrangian-of-graph

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: quadratic-forms
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 271
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjacency-matrix
extends: []
related:
  - motzkin-straus-theorem
  - graham-pollak-theorem
contrasts_with:
  - combinatorial-laplacian

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Lagrangian of a graph?"
---

# Quick Definition

The Lagrangian $f_G(x) = \langle Ax, x\rangle = \sum_{v_i \sim v_j} 2x_ix_j$ is the quadratic form of the adjacency matrix, relating eigenvalues to combinatorial properties.

# Core Definition

The Lagrangian of $G$ is $f_G(x) = \langle Ax, x\rangle = \sum_{i,j} a_{ij}x_ix_j = \sum_{v_i \sim v_j} 2x_ix_j$ (Bollobas, p. 271). Each edge $v_iv_j$ contributes $2x_ix_j$. On the simplex $S_n = \{x \in \mathbb{R}^n : \sum x_i = 1, x_i \ge 0\}$, the maximum $f(G) = \max_{x \in S} f_G(x)$ depends only on the clique number: $f(G) = (\omega(G)-1)/\omega(G)$ (Theorem 10, Motzkin-Straus).

# Prerequisites

- **Adjacency matrix** -- The Lagrangian is its quadratic form

# Key Properties

1. $f_G(x) = 0$ on subspaces spanned by independent sets
2. $f_G$ is positive definite on $W_+$ and negative definite on $W_-$
3. The number of positive/negative eigenvalues relates to independence number (Theorem 8)
4. Maximum on the simplex encodes the clique number

# Construction / Recognition

Not applicable -- this is the quadratic form of $A$.

# Context & Application

The Lagrangian connects spectral properties to combinatorial extremal problems. The Motzkin-Straus theorem gives an alternative proof of Turan's theorem, and the Graham-Pollak theorem on edge-disjoint bipartite decomposition uses inertia properties of Lagrangians.

# Examples

**Example** (p. 274): For $K_n$: $f(K_n) = (n-1)/n$, achieved at $x = (1/n, \ldots, 1/n)$.

# Relationships

## Builds Upon
- **Adjacency matrix** -- Defines the quadratic form

## Enables
- **Motzkin-Straus theorem** -- Lagrangian maximum equals $(k_0-1)/k_0$
- **Graham-Pollak theorem** -- Uses inertia of Lagrangians

## Related
- **Combinatorial Laplacian** -- Different quadratic form $\sum (x_i - x_j)^2$

## Contrasts With
- **Combinatorial Laplacian** -- Laplacian form is positive semi-definite; Lagrangian is not

# Common Errors

- **Error**: Confusing the Lagrangian with the Laplacian quadratic form
  **Correction**: The Lagrangian is $\sum 2x_ix_j$ over edges; the Laplacian form is $\sum (x_i - x_j)^2$

# Common Confusions

- **Confusion**: Thinking the Lagrangian is always non-negative
  **Clarification**: The Lagrangian can be negative (it is the quadratic form of the adjacency matrix, which has negative eigenvalues)

# Source Reference

Chapter VIII, Section VIII.2, pages 271--275.

# Verification Notes

- Definition source: Direct from p. 271
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
