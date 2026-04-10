---
# === CORE IDENTIFICATION ===
concept: Regular Graph Eigenvalues
slug: regular-graph-eigenvalues

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: spectral-properties
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 268
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eigenvalue-of-graph
extends: []
related:
  - strongly-regular-graph
  - combinatorial-laplacian
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What special properties do eigenvalues of regular graphs have?"
---

# Quick Definition

For a connected $k$-regular graph, the maximal eigenvalue is exactly $k$ with multiplicity 1, and $\mu$ is an adjacency eigenvalue iff $k - \mu$ is a Laplacian eigenvalue.

# Core Definition

**Theorem 5(ii)** (Bollobas, p. 268): For a connected graph $G$, $\Delta(G)$ is an eigenvalue iff $G$ is regular, with $m(\Delta) = 1$. **Theorem 14** (p. 278): For a connected $k$-regular graph with distinct eigenvalues $k, \mu_1, \ldots, \mu_r$: $\prod_{i=1}^r \frac{A - \mu_i I}{k - \mu_i} = J/n$. Also, $J$ is a polynomial in $A$ iff $G$ is connected and regular. For regular graphs, $\lambda = k - \mu$ relates Laplacian and adjacency eigenvalues.

# Prerequisites

- **Eigenvalue of a graph** -- The general framework

# Key Properties

1. $k$ is the largest eigenvalue, with eigenvector $\mathbf{j} = (1, \ldots, 1)$
2. $m(k) = 1$ for connected regular graphs
3. $-k$ is an eigenvalue iff $G$ is also bipartite
4. $J/n$ is a polynomial in $A$ (Theorem 14)
5. Laplacian eigenvalues: $\lambda_i = k - \mu_i$

# Construction / Recognition

Not applicable -- these are spectral properties.

# Context & Application

Regular graphs have the most tractable spectral theory. The relationship $\lambda = k - \mu$ makes Laplacian and adjacency analyses interchangeable. Strongly regular graphs are the next level of regularity, with only 3 distinct eigenvalues.

# Examples

**Example** (p. 268): The Petersen graph is 3-regular. Its adjacency eigenvalues are 3 (mult. 1), 1 (mult. 5), $-2$ (mult. 4). Laplacian eigenvalues: 0, 2 (mult. 5), 5 (mult. 4).

# Relationships

## Builds Upon
- **Eigenvalue of a graph**

## Enables
- **Strongly regular graph** -- Further regularity conditions
- Simplified spectral analysis

## Related
- **Combinatorial Laplacian** -- Simple relationship for regular graphs

## Contrasts With
- None

# Common Errors

- **Error**: Assuming $k$ is always the largest eigenvalue for non-regular graphs
  **Correction**: For non-regular graphs, $\mu_{\max}$ is between $\delta$ and $\Delta$, not necessarily equal to either

# Common Confusions

- **Confusion**: Thinking all regular graphs are strongly regular
  **Clarification**: Regular graphs can have many distinct eigenvalues; strongly regular requires exactly 3

# Source Reference

Chapter VIII, Section VIII.2, Theorem 5(ii) and Theorem 14, pages 268, 278.

# Verification Notes

- Definition source: Direct from Theorems 5 and 14
- Confidence rationale: Explicit theorems
- Uncertainties: None
- Cross-reference status: Verified
