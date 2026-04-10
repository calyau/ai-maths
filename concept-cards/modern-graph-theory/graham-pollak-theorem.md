---
# === CORE IDENTIFICATION ===
concept: Graham-Pollak Theorem
slug: graham-pollak-theorem

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: decomposition-results
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 278
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lagrangian-of-graph
  - eigenvalue-of-graph
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the minimum number of complete bipartite graphs needed to partition the edges of K_n?"
---

# Quick Definition

$K_n$ cannot be the edge-disjoint union of fewer than $n-1$ complete bipartite graphs.

# Core Definition

**Theorem 9** (Graham-Pollak; Bollobas, p. 278): The complete graph $K_n$ is not the edge-disjoint union of $n-2$ complete bipartite graphs. The proof uses the Lagrangian: each bipartite graph's Lagrangian is positive semi-definite on a subspace of dimension $n-1$, so $n-2$ such graphs give positive semi-definiteness on a subspace of dimension $\ge 2$, contradicting the fact that $f_{K_n}$ is not positive semi-definite on any 2-dimensional subspace.

# Prerequisites

- **Lagrangian of a graph** -- The quadratic form used in the proof
- **Eigenvalue of a graph** -- Inertia properties

# Key Properties

1. The minimum is exactly $n-1$ (achievable by star decomposition)
2. The proof is purely linear algebraic
3. Generalizes: if $G$ is the edge-disjoint union of $n-r$ complete bipartite graphs, then $f_G$ is positive semi-definite on some $r$-dimensional subspace

# Construction / Recognition

Not applicable -- this is an existence/non-existence result.

# Context & Application

A beautiful application of spectral methods to a combinatorial problem. The proof is notably short yet the result seems hard to prove otherwise.

# Examples

**Example**: $K_4$ needs at least 3 complete bipartite graphs: $K_{1,3}$, $K_{1,2}$, and $K_{1,1}$ (a star decomposition).

# Relationships

## Builds Upon
- **Lagrangian of a graph**
- **Eigenvalue of a graph**

## Enables
- Understanding of bipartite decompositions

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Thinking the lower bound $n-1$ is trivial
  **Correction**: The lower bound requires the spectral argument; simple counting arguments do not suffice

# Common Confusions

- **Confusion**: Thinking the theorem concerns arbitrary bipartite subgraphs
  **Clarification**: The decomposition requires edge-disjoint complete bipartite graphs, not arbitrary bipartite graphs

# Source Reference

Chapter VIII, Section VIII.2, Theorem 9, pages 278--279.

# Verification Notes

- Definition source: Direct from Theorem 9
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
