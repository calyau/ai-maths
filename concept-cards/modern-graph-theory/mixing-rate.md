---
concept: Mixing Rate
slug: mixing-rate
category: conductance-and-mixing
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 320
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "rate of convergence"
prerequisites:
  - stationary-distribution
  - transition-probability-matrix
extends: []
related:
  - conductance-of-graph
  - lazy-random-walk
  - spectral-gap-and-mixing
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
The mixing rate $\mu$ of a random walk on a regular graph is $\mu = \sup_{\mathbf{p}_0} \limsup_{t \to \infty} \|\mathbf{p}_t - \pi\|_2^{1/t}$, which equals $\lambda = \max\{\lambda_2, |\lambda_n|\}$, the second-largest eigenvalue in absolute value of the transition matrix.

# Core Definition
The mixing rate is $\mu = \sup_{\mathbf{p}_0} \limsup_{t \to \infty} \|\mathbf{p}_t - \pi\|_2^{1/t}$ (Bollobás, p. 320). Theorem 26 (p. 321) proves $\mu = \lambda = \max\{\lambda_2, |\lambda_n|\}$ where $\lambda_1 = 1 \geq \lambda_2 \geq \cdots \geq \lambda_n > -1$ are eigenvalues of $P$.

# Prerequisites
- **Stationary distribution** — The target of convergence
- **Transition probability matrix** — Its eigenvalues determine $\mu$

# Key Properties
1. $\mu = \max\{\lambda_2, |\lambda_n|\}$ (Theorem 26)
2. $\|\mathbf{p}_t - \pi\|_2 \leq \lambda^t$ for any initial distribution
3. For the LRW: mixing rate is $\frac{1}{2}(\lambda_2 + 1)$, always non-negative
4. $\mu \leq 1 - \Phi_G^2/2$ (Corollary 30)
5. $\lambda_2 \leq 1 - \Phi_G^2$ (Corollary 31)

# Construction / Recognition
1. Compute the eigenvalues of $P = A/d$ for a $d$-regular graph
2. $\mu = \max\{\lambda_2, |\lambda_n|\}$

# Context & Application
The mixing rate governs how quickly the random walk forgets its starting position. A small mixing rate means fast convergence; $\mu$ close to 1 means slow convergence.

# Examples
**Example** (p. 326): For $K_n$, the mixing rate of the SRW is $1/(n-1)$.

**Example** (p. 326): For the LRW on $Q^d$, the mixing rate is $1 - 1/d$.

# Relationships
## Builds Upon
- **stationary-distribution**, **transition-probability-matrix**

## Enables
- **rapid-mixing** — Rapid mixing requires $\mu$ to be bounded away from 1

## Related
- **conductance-of-graph** — Bounds $\mu$ via $\mu \leq 1 - \Phi_G^2/2$

# Source Reference
Chapter IX, Section IX.4, Theorem 26, pages 320-321.

# Verification Notes
- Definition source: Direct from p. 320
- Confidence rationale: Explicit definition with theorem
- Uncertainties: None
- Cross-reference status: Verified
