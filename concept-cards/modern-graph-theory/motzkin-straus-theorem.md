---
# === CORE IDENTIFICATION ===
concept: Motzkin-Straus Theorem
slug: motzkin-straus-theorem

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: extremal-results
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 274
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lagrangian-of-graph
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Lagrangian relate to the clique number?"
---

# Quick Definition

For a graph $G$ with clique number $k_0$, the maximum of the Lagrangian over the simplex is $f(G) = (k_0 - 1)/k_0$.

# Core Definition

**Theorem 10** (Motzkin-Straus, 1965; Bollobas, p. 274): Let $G$ have clique number $k_0$. Then $f(G) = \max_{x \in S_n} f_G(x) = (k_0 - 1)/k_0$, where $S_n$ is the standard simplex. The maximum is attained at a point whose support spans a maximum clique.

**Corollary 11**: If $G = G(n, m)$ with $m > \frac{r-2}{2(r-1)}n^2$, then $G$ contains $K_r$.

# Prerequisites

- **Lagrangian of a graph** -- The quantity being maximized

# Key Properties

1. $f(G)$ depends only on the clique number
2. The maximizer's support spans a maximum clique
3. Gives an alternative proof of a weak form of Turan's theorem
4. The proof is optimization-theoretic, not combinatorial

# Construction / Recognition

Not applicable -- this is an optimization result.

# Context & Application

The Motzkin-Straus theorem provides a continuous optimization formulation of the clique problem. It links spectral/algebraic methods to extremal graph theory.

# Examples

**Example** (p. 274): For $K_n$: $f(K_n) = \max\{1 - \sum x_i^2 : x \in S_n\} = 1 - n(1/n)^2 = (n-1)/n$.

# Relationships

## Builds Upon
- **Lagrangian of a graph**

## Enables
- Weak form of Turan's theorem (Corollary 11)

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Assuming the maximizer is unique
  **Correction**: The maximizer is unique in its support (maximum clique), but there may be multiple maximum cliques

# Common Confusions

- **Confusion**: Thinking this solves the clique problem efficiently
  **Clarification**: While the optimization formulation is continuous, finding the global maximum is still NP-hard

# Source Reference

Chapter VIII, Section VIII.2, Theorem 10 and Corollary 11, pages 274--275.

# Verification Notes

- Definition source: Direct from Theorem 10
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
