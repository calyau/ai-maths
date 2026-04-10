---
concept: Conductance Bound on the Second Eigenvalue
slug: conductance-bound-on-eigenvalue
category: conductance-and-mixing
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 322
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "Theorem 27"
  - "discrete Cheeger inequality"
prerequisites:
  - conductance-of-graph
  - lazy-random-walk
extends: []
related:
  - spectral-gap-and-mixing
  - rapid-mixing
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
Theorem 27 states that for every LRW on a $d$-regular graph with conductance $\Phi_G$: $d_2(t+1) \leq (1 - \Phi_G^2/4) \, d_2(t)$, giving exponential convergence at rate $1 - \Phi_G^2/4$.

# Core Definition
Theorem 27 (p. 322): "Let $G$ be a non-trivial regular graph with conductance $\Phi_G$. Then every LRW on $G$ is such that $d_2(t+1) \leq (1 - \frac{1}{4}\Phi_G^2) d_2(t)$." This is proved using Lemma 28 (bounding $d_2$ decrease by edge differences) and Lemma 29 (discrete Poincare inequality linking edge differences to total variance via $\Phi_G$).

# Prerequisites
- **Conductance of a graph** — The expansion parameter bounding convergence
- **Lazy random walk** — The walk to which the theorem applies

# Key Properties
1. $d_2(t+1) \leq (1 - \Phi_G^2/4) d_2(t)$ (Theorem 27)
2. Implies $\mu \leq (1 - \Phi_G^2/4)^{1/2}$ (Corollary 30)
3. Implies $\lambda_2 \leq 1 - \Phi_G^2$ for SRW (Corollary 31)
4. Proved via Cauchy-Schwarz and the definition of conductance

# Context & Application
This is the "main result of this section" (p. 322), establishing a close relationship between conductance and convergence speed. It is a discrete analogue of the Cheeger inequality.

# Relationships
## Builds Upon
- **conductance-of-graph**, **lazy-random-walk**

## Enables
- **rapid-mixing** — Theorem 32 follows from this bound
- **spectral-gap-and-mixing** — Corollary 31

# Source Reference
Chapter IX, Section IX.4, Theorem 27, Lemmas 28-29, pages 322-325.

# Verification Notes
- Definition source: Direct from Theorem 27
- Confidence rationale: Central theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
