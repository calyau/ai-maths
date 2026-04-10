---
# === CORE IDENTIFICATION ===
concept: Laplacian Connectivity Bound
slug: laplacian-connectivity-bound

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: connectivity-bounds
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 277
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - second-eigenvalue-laplacian
extends: []
related:
  - edge-boundary-expansion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Laplacian second eigenvalue relate to connectivity?"
---

# Quick Definition

For an incomplete graph $G$, the vertex connectivity $\kappa(G) \ge \lambda_2(G)$, where $\lambda_2$ is the second smallest Laplacian eigenvalue.

# Core Definition

**Theorem 12** (Bollobas, p. 277): The vertex connectivity of an incomplete graph $G$ is at least as large as $\lambda_2(G)$. The proof constructs a vector $x$ orthogonal to $j$ with $q(x)/\|x\|^2 \le k = \kappa(G)$, using a vertex cut $S$ of size $\kappa$ separating $V'$ from $V''$.

# Prerequisites

- **Second eigenvalue of the Laplacian** -- The spectral quantity being bounded

# Key Properties

1. $\kappa(G) \ge \lambda_2(G)$ for incomplete $G$
2. For $K_n$: $\lambda_2 = n > \kappa = n - 1$ (the only exception)
3. The bound is tight for infinitely many graphs at each connectivity
4. Provides a spectral certificate for high connectivity

# Construction / Recognition

Not applicable -- this is an inequality.

# Context & Application

This theorem makes $\lambda_2$ practically useful: computing the second Laplacian eigenvalue gives a lower bound on connectivity that is often easier to obtain than the connectivity itself.

# Examples

**Example** (p. 277): The Petersen graph has $\lambda_2 = 2$ and $\kappa = 3$, so the bound is not tight here.

# Relationships

## Builds Upon
- **Second eigenvalue of the Laplacian**

## Enables
- Spectral verification of high connectivity

## Related
- **Edge boundary expansion** -- Another application of $\lambda_2$

## Contrasts With
- None

# Common Errors

- **Error**: Applying the bound to $K_n$
  **Correction**: For $K_n$, $\lambda_2 = n > n - 1 = \kappa$; the theorem requires $G$ to be incomplete

# Common Confusions

- **Confusion**: Thinking $\lambda_2 = \kappa$ always
  **Clarification**: $\lambda_2$ is a lower bound on $\kappa$; they are often not equal

# Source Reference

Chapter VIII, Section VIII.2, Theorem 12, page 277.

# Verification Notes

- Definition source: Direct from Theorem 12
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
