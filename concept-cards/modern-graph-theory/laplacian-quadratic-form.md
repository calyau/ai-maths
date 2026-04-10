---
# === CORE IDENTIFICATION ===
concept: Laplacian Quadratic Form
slug: laplacian-quadratic-form

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
pdf_page: 276
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Dirichlet form of a graph

# === TYPED RELATIONSHIPS ===
prerequisites:
  - combinatorial-laplacian
extends: []
related:
  - second-eigenvalue-laplacian
  - edge-boundary-expansion
contrasts_with:
  - lagrangian-of-graph

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the quadratic form of the graph Laplacian?"
---

# Quick Definition

The Laplacian quadratic form is $q(x) = \langle Lx, x\rangle = \sum_{v_iv_j \in E(G)} (x_i - x_j)^2$, which is always non-negative and equals zero iff $x$ is constant on each connected component.

# Core Definition

For $x = \sum x_i v_i$, the quadratic form of the Laplacian is $q(x) = \langle (D-A)x, x\rangle = \sum_{i} d(v_i)x_i^2 - \sum_{v_j \sim v_i} x_ix_j = \sum_{v_iv_j \in E(G)} (x_i - x_j)^2$ (equation (3), Bollobas, p. 276). This form emphasizes the intimate connection between the Laplacian and graph structure: it measures how much $x$ varies across edges.

# Prerequisites

- **Combinatorial Laplacian** -- The matrix whose form this is

# Key Properties

1. Always non-negative (positive semi-definite)
2. $q(x) = 0$ iff $x$ is constant on each component
3. $q(j) = 0$ where $j = (1, \ldots, 1)$
4. $\lambda_2 = \min\{q(x)/\|x\|^2 : \langle x, j\rangle = 0, x \ne 0\}$ (equation (4))
5. Each edge $v_iv_j$ contributes $(x_i - x_j)^2$ -- a measure of the "energy" of $x$ on that edge

# Construction / Recognition

Not applicable -- this is a quadratic form.

# Context & Application

The Laplacian quadratic form is the graph-theoretic analogue of the Dirichlet energy in potential theory. It measures how "smooth" a function is on the graph. The variational characterization of $\lambda_2$ via this form is the basis of spectral graph theory applications to expansion and connectivity.

# Examples

**Example**: For $K_n$ with $x = (a, b, 0, \ldots, 0)$: $q(x) = (a-b)^2 + (n-2)(a^2 + b^2)$.

# Relationships

## Builds Upon
- **Combinatorial Laplacian** -- The matrix

## Enables
- **Second eigenvalue of Laplacian** -- Variational characterization
- **Edge boundary expansion** -- Isoperimetric bounds via $q$

## Related
- **Edge boundary expansion** -- Direct application

## Contrasts With
- **Lagrangian of a graph** -- $f_G(x) = \sum 2x_ix_j$ over edges (not positive definite)

# Common Errors

- **Error**: Forgetting the factor of 2 when comparing with the Lagrangian
  **Correction**: $q(x) = \sum (x_i - x_j)^2 = \sum x_i^2 d(v_i) - f_G(x)$

# Common Confusions

- **Confusion**: Confusing the Laplacian form $\sum(x_i - x_j)^2$ with the Lagrangian $\sum 2x_ix_j$
  **Clarification**: They are related by $q(x) = x^t D x - f_G(x)$ but have very different properties

# Source Reference

Chapter VIII, Section VIII.2, equation (3), page 276.

# Verification Notes

- Definition source: Direct from equation (3)
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified
