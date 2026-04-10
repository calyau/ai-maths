---
# === CORE IDENTIFICATION ===
concept: Bipartite Graph Eigenvalue Symmetry
slug: bipartite-graph-eigenvalue-symmetry

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eigenvalue-of-graph
extends: []
related:
  - regular-graph-eigenvalues
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What special spectral property do bipartite graphs have?"
---

# Quick Definition

If $G$ is bipartite, then $\mu$ is an eigenvalue of $G$ iff $-\mu$ is, with the same multiplicity.

# Core Definition

**Theorem 5(iv)** (Bollobas, p. 269): If $G$ is bipartite and $\mu$ is an eigenvalue of $G$ then so is $-\mu$, and $m(\mu) = m(-\mu)$. The proof defines $\mathbf{b}$ as the vector that is 1 on one vertex class and $-1$ on the other; then $\mathbf{x} \mapsto \mathbf{bx}$ gives an isomorphism between $\ker(A - \mu I)$ and $\ker(A + \mu I)$.

Additionally, **Theorem 5(iii)**: If $-\Delta$ is an eigenvalue, then $G$ is regular and bipartite.

# Prerequisites

- **Eigenvalue of a graph** -- The framework

# Key Properties

1. Spectrum is symmetric about 0
2. The map $\mathbf{x} \mapsto \mathbf{bx}$ is the key isomorphism
3. Bipartiteness is detected spectrally: $-\mu_{\max}$ is an eigenvalue iff $G$ is bipartite (for regular connected graphs)
4. For $k$-regular bipartite: eigenvalues come in pairs $(k, -k)$, $(\mu, -\mu)$, possibly with 0

# Construction / Recognition

Not applicable -- this is a spectral characterization.

# Context & Application

This symmetry is useful for determining whether a graph is bipartite from its spectrum and for simplifying computations on bipartite graphs.

# Examples

**Example** (p. 278): $K_{k,n-k}$ has eigenvalues $\pm\sqrt{k(n-k)}$ and 0, confirming the symmetry.

# Relationships

## Builds Upon
- **Eigenvalue of a graph**

## Enables
- Spectral detection of bipartiteness

## Related
- **Regular graph eigenvalues** -- Combined with regularity gives clean characterization

## Contrasts With
- None

# Common Errors

- **Error**: Concluding a graph is bipartite just because 0 is an eigenvalue
  **Correction**: 0 being an eigenvalue does not imply bipartiteness; the full symmetry of the spectrum is needed

# Common Confusions

- **Confusion**: Thinking all graphs with symmetric spectrum are bipartite
  **Clarification**: For connected graphs, symmetric spectrum implies bipartiteness, but for disconnected graphs it need not

# Source Reference

Chapter VIII, Section VIII.2, Theorem 5(iii-iv), pages 269--270.

# Verification Notes

- Definition source: Direct from Theorem 5(iv)
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
