---
# === CORE IDENTIFICATION ===
concept: Adjacency Matrix Eigenvalue Bounds
slug: adjacency-matrix-eigenvalue-bounds

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
pdf_page: 267
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
  - regular-graph-eigenvalues
  - bipartite-graph-eigenvalue-symmetry
  - induced-subgraph-eigenvalue-interlacing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What bounds do the degrees of a graph impose on its eigenvalues?"
  - "How does the adjacency matrix spectrum relate to graph properties?"
---

# Quick Definition

Theorem 5 collects the fundamental spectral bounds: $|\mu| \le \Delta$, $\delta \le \mu_{\max} \le \Delta$, with equality conditions determining regularity and bipartiteness.

# Core Definition

**Theorem 5** (Bollobas, pp. 267--269) collects six key properties: (i) $|\mu| \le \Delta$ for all eigenvalues, (ii) $\Delta$ is an eigenvalue iff $G$ is regular (then $m(\Delta)=1$ for connected $G$), (iii) $-\Delta$ is an eigenvalue implies $G$ is regular and bipartite, (iv) bipartite $\Rightarrow$ symmetric spectrum, (v) $\delta \le \mu_{\max} \le \Delta$, (vi) induced subgraph interlacing.

# Prerequisites

- **Eigenvalue of a graph** -- The spectral objects being bounded

# Key Properties

1. All eigenvalues lie in $[-\Delta, \Delta]$
2. $\mu_{\max} = \Delta$ iff $G$ is regular (for connected $G$)
3. $\mu_{\min} = -\Delta$ iff $G$ is regular and bipartite (for connected $G$)
4. $\mu_{\max} \ge \delta$ (minimum degree is a lower bound on the largest eigenvalue)
5. Average degree $\bar{d} = 2m/n \le \mu_{\max}$ (from $\langle Aj, j\rangle / n$)

# Construction / Recognition

Not applicable -- these are spectral bounds.

# Context & Application

Theorem 5 is the foundational result of spectral graph theory. It connects the most basic graph parameters (degrees) to eigenvalues and provides spectral characterizations of regularity and bipartiteness.

# Examples

**Example**: For $K_n$: $\delta = \Delta = n-1$, and $\mu_{\max} = n-1$, confirming bounds are tight.

# Relationships

## Builds Upon
- **Eigenvalue of a graph** -- The spectral data

## Enables
- **Regular graph eigenvalues** -- Detailed analysis when regular
- **Bipartite graph eigenvalue symmetry** -- Part (iv)
- **Induced subgraph eigenvalue interlacing** -- Part (vi)

## Related
- All spectral graph theory results

## Contrasts With
- None

# Common Errors

- **Error**: Assuming $\mu_{\max} = \Delta$ for non-regular graphs
  **Correction**: $\mu_{\max} \le \Delta$ with equality only for regular (connected) graphs

# Common Confusions

- **Confusion**: Thinking these bounds are tight for all graphs
  **Clarification**: The bounds are tight for regular graphs but can be loose for irregular graphs

# Source Reference

Chapter VIII, Section VIII.2, Theorem 5, pages 267--269.

# Verification Notes

- Definition source: Direct from Theorem 5
- Confidence rationale: Central theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
