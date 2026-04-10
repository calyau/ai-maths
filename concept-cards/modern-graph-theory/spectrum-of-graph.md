---
# === CORE IDENTIFICATION ===
concept: Spectrum of a Graph
slug: spectrum-of-graph

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
pdf_page: 278
section: "VIII.2 The Adjacency Matrix and the Laplacian"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - adjacency spectrum

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eigenvalue-of-graph
extends: []
related:
  - strongly-regular-graph
  - chromatic-number-eigenvalue-bound
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the spectrum of a graph?"
---

# Quick Definition

The spectrum of a graph is the multiset of eigenvalues of its adjacency matrix, consisting of all eigenvalues with their multiplicities.

# Core Definition

The spectrum of a graph is the set of all eigenvalues and their multiplicities: $\{\mu_1^{m(\mu_1)}, \mu_2^{m(\mu_2)}, \ldots, \mu_t^{m(\mu_t)}\}$ where $\mu_1 > \mu_2 > \cdots > \mu_t$ are distinct eigenvalues. For the complete graph $K_n$: spectrum is $\{(n-1)^1, (-1)^{n-1}\}$. For the complete bipartite graph $K_{k,n-k}$: $\{\sqrt{k(n-k)}^1, 0^{n-2}, (-\sqrt{k(n-k)})^1\}$ (Bollobas, p. 278).

# Prerequisites

- **Eigenvalue of a graph** -- The individual components

# Key Properties

1. Sum of all eigenvalues (with multiplicity) = $\text{tr}(A) = 0$
2. Total multiplicity = $n$ (the order of the graph)
3. Bipartite graphs have symmetric spectra: $\mu$ iff $-\mu$
4. Determining the entire spectrum is computationally hard in general
5. Two non-isomorphic graphs can have the same spectrum (cospectral graphs)

# Construction / Recognition

## Known Spectra
- $E_n$: $\{0^n\}$
- $K_n$: $\{(n-1)^1, (-1)^{n-1}\}$
- $K_{k,n-k}$: $\{(\sqrt{k(n-k)})^1, 0^{n-2}, (-\sqrt{k(n-k)})^1\}$
- Strongly regular with $(k,a,b)$: 3 distinct eigenvalues

# Context & Application

The spectrum encodes extensive graph information: degree bounds, chromatic number bounds, bipartiteness, and more. Two cospectral non-isomorphic graphs show the spectrum does not determine a graph uniquely.

# Examples

**Example** (p. 278): $K_n$ has eigenvalues $n-1$ (mult. 1) and $-1$ (mult. $n-1$). Since $\text{tr}(A) = 0$: $(n-1) + (n-1)(-1) = 0$.

# Relationships

## Builds Upon
- **Eigenvalue of a graph** -- Components of the spectrum

## Enables
- **Strongly regular graph** -- Characterized by 3 distinct eigenvalues
- **Chromatic number eigenvalue bound** -- Uses extreme eigenvalues

## Related
- **Strongly regular graph** -- Small number of distinct eigenvalues
- **Chromatic number eigenvalue bound** -- Application

## Contrasts With
- None

# Common Errors

- **Error**: Assuming the spectrum determines the graph
  **Correction**: Cospectral non-isomorphic graphs exist

# Common Confusions

- **Confusion**: Confusing adjacency spectrum with Laplacian spectrum
  **Clarification**: They are different; for regular graphs they are simply related, otherwise not

# Source Reference

Chapter VIII, Section VIII.2, page 278.

# Verification Notes

- Definition source: Direct from p. 278
- Confidence rationale: Explicit examples
- Uncertainties: None
- Cross-reference status: Verified
