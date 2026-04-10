---
# === CORE IDENTIFICATION ===
concept: Inertia of the Adjacency Matrix
slug: inertia-of-adjacency-matrix

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
pdf_page: 272
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - positive and negative eigenvalue counts

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eigenvalue-of-graph
  - lagrangian-of-graph
extends: []
related:
  - graham-pollak-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the independence number relate to the eigenvalue distribution?"
---

# Quick Definition

The adjacency matrix of $G$ has at least $\beta(G)$ non-negative eigenvalues and at least $\beta(G)$ non-positive eigenvalues, where $\beta(G)$ is the independence number.

# Core Definition

**Theorem 8** (Bollobas, p. 273): The adjacency matrix has at least $\beta(G)$ non-negative and at least $\beta(G)$ non-positive eigenvalues, counted with multiplicity. The proof uses the fact that the Lagrangian $f_G$ is identically 0 on subspaces spanned by independent sets, hence positive semi-definite and negative semi-definite on subspaces of dimension $\beta(G)$.

# Prerequisites

- **Eigenvalue of a graph** -- The spectral data
- **Lagrangian of a graph** -- The quadratic form

# Key Properties

1. $n_+(A) \ge \beta(G)$ and $n_-(A) + n_0(A) \ge \beta(G)$
2. Similarly $n_-(A) \ge \beta(G)$ and $n_+(A) + n_0(A) \ge \beta(G)$
3. Constrains the distribution of eigenvalues via combinatorial data
4. Key ingredient in the Graham-Pollak theorem

# Construction / Recognition

Not applicable -- this is an inequality.

# Context & Application

This theorem connects the inertia (signature) of the adjacency matrix to the independence number. It is the basis of the Graham-Pollak theorem on bipartite decomposition of $K_n$.

# Examples

**Example**: For $K_n$: $\beta = 1$, and indeed $n_+ = 1$ (eigenvalue $n-1$), $n_- = n-1$ (eigenvalue $-1$), both $\ge 1$.

# Relationships

## Builds Upon
- **Eigenvalue of a graph** -- Counts positive/negative eigenvalues
- **Lagrangian of a graph** -- Key tool in the proof

## Enables
- **Graham-Pollak theorem** -- Uses the inertia bounds

## Related
- **Graham-Pollak theorem** -- Direct application

## Contrasts With
- None

# Common Errors

- **Error**: Thinking the bound is tight for all graphs
  **Correction**: The inequality can be strict; e.g., $K_n$ has $n_+ = 1$ but $\beta = 1$

# Common Confusions

- **Confusion**: Confusing $n_+$, $n_-$ with positive/negative definiteness
  **Clarification**: $n_+$ counts positive eigenvalues; positive definiteness would require $n_+ = n$

# Source Reference

Chapter VIII, Section VIII.2, Theorem 8, pages 272--273.

# Verification Notes

- Definition source: Direct from Theorem 8
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
