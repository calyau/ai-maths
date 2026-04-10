---
# === CORE IDENTIFICATION ===
concept: Chromatic Number Eigenvalue Bound
slug: chromatic-number-eigenvalue-bound

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: chromatic-bounds
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 270
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Hoffman bound on chromatic number

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eigenvalue-of-graph
extends: []
related:
  - adjacency-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the adjacency matrix spectrum relate to graph properties?"
---

# Quick Definition

The chromatic number of a non-empty graph satisfies $\chi(G) \ge 1 - \mu_{\max}(G)/\mu_{\min}(G)$ and $\chi(G) \le \mu_{\max}(G) + 1$.

# Core Definition

**Corollary 6** (p. 270): $\chi(G) \le \mu_{\max}(G) + 1$, since $\delta(H) \le \mu_{\max}(H) \le \mu_{\max}(G)$ for every induced subgraph $H$. **Theorem 7** (p. 270): For non-empty $G$, $\chi(G) \ge 1 - \mu_{\max}(G)/\mu_{\min}(G)$. The proof uses the colour spaces $U_i$ and the fact that $\langle Au, u\rangle = 0$ for $u \in U_i$, giving $\mu_{\max} + (k-1)\mu_{\min} \le 0$ where $k = \chi(G)$.

# Prerequisites

- **Eigenvalue of a graph** -- Need $\mu_{\max}$ and $\mu_{\min}$

# Key Properties

1. Upper bound: $\chi(G) \le \mu_{\max} + 1$ (via greedy argument on subgraphs)
2. Lower bound: $\chi(G) \ge 1 - \mu_{\max}/\mu_{\min}$ (algebraic)
3. Both bounds are tight for some graphs (e.g., strongly regular)
4. The lower bound uses the orthogonal decomposition by colour classes

# Construction / Recognition

Not applicable -- these are algebraic bounds.

# Context & Application

These bounds connect the algebraic (eigenvalue) and combinatorial (coloring) structure of graphs. They are especially powerful for highly regular graphs where eigenvalues can be computed explicitly.

# Examples

**Example** (p. 278): For $K_n$: $\mu_{\max} = n-1$, $\mu_{\min} = -1$, so $\chi \ge 1 - (n-1)/(-1) = n$. Both bounds are tight.

# Relationships

## Builds Upon
- **Eigenvalue of a graph** -- The spectral data

## Enables
- Algebraic approaches to coloring

## Related
- **Adjacency matrix** -- Source of eigenvalues

## Contrasts With
- None

# Common Errors

- **Error**: Applying the lower bound to graphs with $\mu_{\min} = 0$
  **Correction**: The bound requires $\mu_{\min} < 0$, which holds for any graph with at least one edge

# Common Confusions

- **Confusion**: Thinking the eigenvalue lower bound is always tight
  **Clarification**: It can be far from tight for non-regular graphs

# Source Reference

Chapter VIII, Section VIII.2, Corollary 6 and Theorem 7, pages 270--271.

# Verification Notes

- Definition source: Direct from Corollary 6 and Theorem 7
- Confidence rationale: Explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
