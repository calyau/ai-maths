---
# === CORE IDENTIFICATION ===
concept: Second Eigenvalue of the Laplacian
slug: second-eigenvalue-laplacian

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
pdf_page: 276
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - algebraic connectivity
  - Fiedler value

# === TYPED RELATIONSHIPS ===
prerequisites:
  - combinatorial-laplacian
extends: []
related:
  - laplacian-connectivity-bound
  - edge-boundary-expansion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is the second eigenvalue of the Laplacian important?"
  - "What must I know before understanding spectral graph theory?"
---

# Quick Definition

The second smallest eigenvalue $\lambda_2(G)$ of the Laplacian measures how well-connected a graph is: the larger $\lambda_2$, the harder it is to cut $G$ into pieces.

# Core Definition

$\lambda_2(G) = \min\{q(x)/\|x\|^2 : \langle x, j\rangle = 0, x \ne 0\}$ where $q(x) = \sum_{v_iv_j \in E} (x_i - x_j)^2$ (equation (4), Bollobas, p. 276). "It is difficult to overemphasize its importance. Roughly, the larger $\lambda_2(G)$ is, the more difficult it is to cut $G$ into pieces, and the more $G$ 'expands'" (p. 276).

# Prerequisites

- **Combinatorial Laplacian** -- $\lambda_2$ is its second eigenvalue

# Key Properties

1. $\lambda_2 > 0$ iff $G$ is connected
2. For $K_n$: $\lambda_2 = n$
3. For incomplete graphs: $\lambda_2 \le \kappa(G)$ (Theorem 12)
4. Edge expansion: $|\partial U| \ge \lambda_2 |U||V \setminus U|/n$ (Theorem 13)
5. Variational characterization via minimization orthogonal to $j$

# Construction / Recognition

## To Compute $\lambda_2$
1. Form the Laplacian $L = D - A$
2. Compute eigenvalues $0 = \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$
3. The second smallest is $\lambda_2$

# Context & Application

$\lambda_2$ is the key parameter in spectral graph theory for applications. It controls vertex connectivity, edge expansion, random walk mixing, and expander graph quality. It is the graph-theoretic analogue of the spectral gap in Markov chain theory.

# Examples

**Example** (p. 276): $\lambda_2(K_n) = n > \kappa(K_n) = n - 1$, but for incomplete graphs $\lambda_2 \le \kappa$.

# Relationships

## Builds Upon
- **Combinatorial Laplacian** -- Source

## Enables
- **Laplacian connectivity bound** -- $\kappa(G) \ge \lambda_2$ for incomplete $G$
- **Edge boundary expansion** -- Isoperimetric-type bound

## Related
- **Laplacian connectivity bound** -- Application of $\lambda_2$
- **Edge boundary expansion** -- Application of $\lambda_2$

## Contrasts With
- None

# Common Errors

- **Error**: Expecting $\lambda_2 \ge \kappa$ always
  **Correction**: $\lambda_2 \le \kappa$ for incomplete graphs; only $K_n$ has $\lambda_2 > \kappa$

# Common Confusions

- **Confusion**: Confusing $\lambda_2$ of the Laplacian with $\mu_2$ of the adjacency matrix
  **Clarification**: They are different; for $k$-regular graphs, $\lambda_2 = k - \mu_2$

# Source Reference

Chapter VIII, Section VIII.2, equation (4), pages 276--278.

# Verification Notes

- Definition source: Direct from equation (4), p. 276
- Confidence rationale: Explicit definition with strong endorsement of importance
- Uncertainties: None
- Cross-reference status: Verified
