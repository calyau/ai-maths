---
# === CORE IDENTIFICATION ===
concept: Eigenvalue of a Graph
slug: eigenvalue-of-graph

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: spectral-properties
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 267
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - graph eigenvalue
  - adjacency eigenvalue

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjacency-matrix
extends: []
related:
  - adjacency-matrix-eigenvalue-bounds
  - chromatic-number-eigenvalue-bound
  - spectrum-of-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the eigenvalues of a graph?"
  - "How does the adjacency matrix spectrum relate to graph properties?"
---

# Quick Definition

An eigenvalue of a graph $G$ is an eigenvalue of its adjacency matrix $A(G)$. The eigenvalues are real and satisfy $|\mu| \le \Delta(G)$, with $\mu_{\max} \ge \delta(G)$.

# Core Definition

An eigenvalue of the adjacency matrix $A$ is called an eigenvalue of $G$. Writing $\mu_1 > \mu_2 > \cdots > \mu_t$ for the distinct eigenvalues with multiplicities $m(\mu_1), \ldots, m(\mu_t)$: $\sum m(\mu_i) = n$ and $\sum m(\mu_i)\mu_i = 0$ (since $\text{tr}(A) = 0$). We write $\mu_{\max}(G) = \mu_1$ and $\mu_{\min}(G) = \mu_t$ (Bollobas, p. 267).

# Prerequisites

- **Adjacency matrix** -- Eigenvalues are defined via $A(G)$

# Key Properties (Theorem 5)

1. Every eigenvalue $\mu$ satisfies $|\mu| \le \Delta(G)$
2. $\Delta$ is an eigenvalue iff $G$ is regular; then $m(\Delta) = 1$ (for connected $G$)
3. $-\Delta$ is an eigenvalue iff $G$ is regular and bipartite
4. If $G$ is bipartite: $\mu$ is an eigenvalue iff $-\mu$ is, with equal multiplicity
5. $\delta(G) \le \mu_{\max}(G) \le \Delta(G)$
6. For induced subgraph $H$: $\mu_{\min}(G) \le \mu_{\min}(H) \le \mu_{\max}(H) \le \mu_{\max}(G)$

# Construction / Recognition

## To Find Eigenvalues
1. Construct the adjacency matrix $A$
2. Solve the characteristic equation $\det(A - \mu I) = 0$
3. For highly regular graphs, use the collapsed adjacency matrix (Theorem 15)

# Context & Application

Graph eigenvalues encode structural information. The maximal eigenvalue relates to degrees, the eigenvalue ratio bounds the chromatic number, the multiplicity structure constrains independence numbers, and bipartite graphs have symmetric spectra.

# Examples

**Example 1** (p. 278): $E_n$ has eigenvalue 0 with multiplicity $n$.

**Example 2** (p. 278): $K_n$ has eigenvalues $n-1$ (mult. 1) and $-1$ (mult. $n-1$).

**Example 3** (p. 278): $K_{k,n-k}$ has eigenvalues $\pm\sqrt{k(n-k)}$ (mult. 1 each) and 0 (mult. $n-2$).

# Relationships

## Builds Upon
- **Adjacency matrix** -- Eigenvalues are of this matrix

## Enables
- **Adjacency matrix eigenvalue bounds** -- Bounds on eigenvalues
- **Chromatic number eigenvalue bound** -- $\chi \ge 1 - \mu_{\max}/\mu_{\min}$
- **Strongly regular graph** -- Characterized by having exactly 3 distinct eigenvalues

## Related
- **Spectrum of a graph** -- The full list of eigenvalues with multiplicities

## Contrasts With
- None

# Common Errors

- **Error**: Assuming all eigenvalues are non-negative
  **Correction**: Since $\text{tr}(A) = 0$, negative eigenvalues must exist if positive ones do

# Common Confusions

- **Confusion**: Confusing eigenvalues of $A$ with eigenvalues of the Laplacian $L$
  **Clarification**: For $k$-regular graphs, $\lambda_i = k - \mu_i$; for non-regular graphs, the relationship is indirect

# Source Reference

Chapter VIII: Graphs, Groups and Matrices, Section VIII.2, Theorem 5, pages 267--269.

# Verification Notes

- Definition source: Direct from p. 267
- Confidence rationale: Explicit definition with full theorem
- Uncertainties: None
- Cross-reference status: Verified
