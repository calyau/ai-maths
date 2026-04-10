---
# === CORE IDENTIFICATION ===
concept: Equivalence of G(n,p) and G(n,M)
slug: equivalence-gnp-gnm

# === CLASSIFICATION ===
category: random-graphs
subcategory: model-comparison
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 236
section: "VII.2 Simple Properties of Almost All Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gnp-model
  - gnm-model
  - convex-property
extends: []
related:
  - almost-every-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When can results in G(n,p) be transferred to G(n,M) and vice versa?"
---

# Quick Definition

The models $\mathcal{G}(n, p)$ and $\mathcal{G}(n, M)$ are asymptotically interchangeable for many properties when $M \sim pN$, $M \to \infty$, and $N - M \to \infty$.

# Core Definition

**Theorem 6** (Bollobás, p. 237): Let $0 < p < 1$ with $pn^2 \to \infty$ and $(1-p)n^2 \to \infty$. (i) If for fixed $\varepsilon > 0$ and $(1-\varepsilon)pN < M < (1+\varepsilon)pN$, a.e. graph in $\mathcal{G}(n, M)$ has $Q$, then a.e. graph in $\mathcal{G}(n, p)$ has $Q$. (ii) If $Q$ is a convex property and a.e. graph in $\mathcal{G}(n, p)$ has $Q$, then a.e. graph in $\mathcal{G}(n, \lfloor pN \rfloor)$ has $Q$.

# Prerequisites

- **G(n,p) model** -- One of the two models
- **G(n,M) model** -- The other model
- **Convex property** -- Needed for the reverse direction

# Key Properties

1. Conditioning $\mathcal{G}(n, p)$ on $e(G_p) = M$ gives $\mathcal{G}(n, M)$
2. A.e. graph in $\mathcal{G}(n, p)$ has $e(G_p)$ close to $pN$ (concentration around the mean)
3. For convex properties, transfer from $\mathcal{G}(n, p)$ to $\mathcal{G}(n, M)$ works for $M = \lfloor pN \rfloor$
4. The models are "practically interchangeable in many situations"

# Construction / Recognition

Not applicable -- this is a transfer principle.

# Context & Application

This equivalence justifies working in whichever model is more convenient. Typically $\mathcal{G}(n, p)$ is preferred because edge independence simplifies calculations, but $\mathcal{G}(n, M)$ is sometimes more natural (e.g., when exact edge counts matter).

# Examples

**Example** (p. 237): A.e. graph in $\mathcal{G}(n, p)$ has between $(1-\varepsilon)pN$ and $(1+\varepsilon)pN$ edges, which is the key to the equivalence.

# Relationships

## Builds Upon
- **G(n,p) model** and **G(n,M) model**
- **Convex property** -- Required for part (ii)

## Enables
- Flexibility in choosing the more convenient model for any proof

## Related
- **Almost every graph** -- The framework for equivalence statements

## Contrasts With
- None

# Common Errors

- **Error**: Assuming equivalence holds for non-convex properties
  **Correction**: Part (ii) requires convexity; for non-convex properties, the transfer may fail

# Common Confusions

- **Confusion**: Thinking the models are identical
  **Clarification**: They are asymptotically equivalent for many properties but can differ, especially for non-convex or very delicate properties

# Source Reference

Chapter VII: Random Graphs, Section VII.2, Theorem 6, pages 236--238.

# Verification Notes

- Definition source: Direct from Theorem 6, p. 237
- Confidence rationale: Explicit theorem statement
- Uncertainties: None
- Cross-reference status: Verified
