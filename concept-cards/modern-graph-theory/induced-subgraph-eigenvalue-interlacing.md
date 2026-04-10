---
# === CORE IDENTIFICATION ===
concept: Induced Subgraph Eigenvalue Interlacing
slug: induced-subgraph-eigenvalue-interlacing

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
pdf_page: 269
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Cauchy interlacing for graphs

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eigenvalue-of-graph
extends: []
related:
  - chromatic-number-eigenvalue-bound
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do eigenvalues of an induced subgraph relate to those of the graph?"
---

# Quick Definition

If $H$ is an induced subgraph of $G$, then $\mu_{\min}(G) \le \mu_{\min}(H) \le \mu_{\max}(H) \le \mu_{\max}(G)$.

# Core Definition

**Theorem 5(vi)** (Bollobas, p. 269): If $H$ is an induced subgraph of $G$ then $\mu_{\min}(G) \le \mu_{\min}(H) \le \mu_{\max}(H) \le \mu_{\max}(G)$. The proof for $\mu_{\max}$: extend an eigenvector $\mathbf{y}$ of $A(H)$ to $C_0(G)$ by appending zeros; then $\langle A(G)\mathbf{x}, \mathbf{x}\rangle = \langle A(H)\mathbf{y}, \mathbf{y}\rangle = \mu_{\max}(H)$, so $\mu_{\max}(G) \ge \mu_{\max}(H)$.

# Prerequisites

- **Eigenvalue of a graph** -- The quantities being compared

# Key Properties

1. Extreme eigenvalues of induced subgraphs are sandwiched by those of the full graph
2. This is a consequence of the Cauchy interlacing theorem for hermitian matrices
3. Key ingredient in proving $\chi(G) \le \mu_{\max}(G) + 1$ (Corollary 6)

# Construction / Recognition

Not applicable -- this is an inequality.

# Context & Application

Interlacing gives a monotonicity principle for eigenvalues: removing vertices can only shrink the spectral range. This is crucial for bounding chromatic number.

# Examples

**Example**: $K_3 \subset K_5$: $\mu_{\max}(K_3) = 2 \le 4 = \mu_{\max}(K_5)$ and $\mu_{\min}(K_3) = -1 \ge -1 = \mu_{\min}(K_5)$.

# Relationships

## Builds Upon
- **Eigenvalue of a graph**

## Enables
- **Chromatic number eigenvalue bound** -- Upper bound $\chi \le \mu_{\max} + 1$

## Related
- **Chromatic number eigenvalue bound** -- Direct application

## Contrasts With
- None

# Common Errors

- **Error**: Applying interlacing to non-induced subgraphs
  **Correction**: The result requires $H$ to be an induced subgraph; removing edges as well as vertices can change eigenvalues unpredictably

# Common Confusions

- **Confusion**: Thinking interlacing applies to all eigenvalues, not just extremes
  **Clarification**: The full Cauchy interlacing theorem gives bounds on all eigenvalues, but Bollobas states only the extreme case

# Source Reference

Chapter VIII, Section VIII.2, Theorem 5(vi), page 269.

# Verification Notes

- Definition source: Direct from Theorem 5(vi)
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
