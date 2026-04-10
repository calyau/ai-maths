---
# === CORE IDENTIFICATION ===
concept: Edge Boundary Expansion
slug: edge-boundary-expansion

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: expansion-properties
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
aliases:
  - isoperimetric inequality for graphs

# === TYPED RELATIONSHIPS ===
prerequisites:
  - second-eigenvalue-laplacian
extends: []
related:
  - laplacian-connectivity-bound
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Laplacian second eigenvalue bound edge expansion?"
---

# Quick Definition

For a graph $G$ of order $n$ and $U \subset V$: $|\partial U| \ge \lambda_2(G)|U||V \setminus U|/n$, where $\partial U$ is the set of edges from $U$ to $V \setminus U$.

# Core Definition

**Theorem 13** (Bollobas, p. 277): Let $G$ be a graph of order $n$. For $U \subset V$: $|\partial U| \ge \lambda_2(G)|U||V \setminus U|/n$, where $\partial U = \partial_G U$ is the edge-boundary (edges from $U$ to $V \setminus U$). The proof uses the vector $x$ with $x_i = n - k$ for $v_i \in U$ and $x_i = -k$ for $v_i \notin U$ (where $k = |U|$), giving $\langle (D-A)x, x\rangle = |\partial U|n^2$.

# Prerequisites

- **Second eigenvalue of the Laplacian** -- The spectral quantity in the bound

# Key Properties

1. Gives a lower bound on the number of edges leaving any vertex set
2. Larger $\lambda_2$ means better expansion
3. Maximized when $|U| = n/2$: $|\partial U| \ge \lambda_2 n/4$
4. This is the basic reason $\lambda_2$ is so important for expansion

# Construction / Recognition

Not applicable -- this is an isoperimetric inequality.

# Context & Application

This result is the fundamental connection between spectral properties and graph expansion. It is the basis of expander graph theory and has applications in network design, error-correcting codes, and derandomization.

# Examples

**Example**: For $K_n$ with $|U| = n/2$: $|\partial U| = (n/2)^2$ and $\lambda_2 n/4 = n^2/4$, so the bound is tight.

# Relationships

## Builds Upon
- **Second eigenvalue of the Laplacian**

## Enables
- Expander graph theory

## Related
- **Laplacian connectivity bound** -- Another consequence of $\lambda_2$

## Contrasts With
- None

# Common Errors

- **Error**: Applying the bound with the wrong normalization
  **Correction**: The bound uses $\lambda_2 |U||V \setminus U|/n$, not $\lambda_2 |U|$

# Common Confusions

- **Confusion**: Thinking edge expansion and vertex expansion are the same
  **Clarification**: Edge expansion counts boundary edges; vertex expansion counts boundary vertices

# Source Reference

Chapter VIII, Section VIII.2, Theorem 13, pages 277--278.

# Verification Notes

- Definition source: Direct from Theorem 13
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
