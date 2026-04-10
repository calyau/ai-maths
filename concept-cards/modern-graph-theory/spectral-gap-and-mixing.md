---
concept: Spectral Gap and Mixing
slug: spectral-gap-and-mixing
category: conductance-and-mixing
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 325
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "Cheeger inequality"
prerequisites:
  - mixing-rate
  - conductance-of-graph
extends: []
related:
  - rapid-mixing
  - lazy-random-walk
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
The spectral gap $1 - \lambda_2$ of the transition matrix governs the rate of convergence to stationarity. Corollary 31 bounds this gap: $\lambda_2 \leq 1 - \Phi_G^2$, connecting the spectral gap to the graph's expansion.

# Core Definition
Corollary 31 (p. 325): "The second eigenvalue of the SRW on a regular graph with conductance $\Phi_G$ is at most $1 - \Phi_G^2$." This means $1 - \lambda_2 \geq \Phi_G^2$, so good expansion implies a large spectral gap. Theorem 27 gives the key inequality: $d_2(t+1) \leq (1 - \Phi_G^2/4) d_2(t)$.

# Prerequisites
- **Mixing rate** — $\mu = \max\{\lambda_2, |\lambda_n|\}$
- **Conductance of a graph** — Bounds the spectral gap

# Key Properties
1. $\lambda_2 \leq 1 - \Phi_G^2$ (Corollary 31)
2. For LRW: mixing rate $\frac{1}{2}(\lambda_2 + 1) \leq 1 - \Phi_G^2/2$ (Corollary 30)
3. $d_2(t+1) \leq (1 - \Phi_G^2/4) d_2(t)$ (Theorem 27)
4. The inequality $1 - \lambda_2 \geq \Phi_G^2$ is a discrete Cheeger inequality

# Construction / Recognition
The proof of Theorem 27 uses two lemmas:
1. Lemma 28: $d_2(t+1) \leq d_2(t) - \frac{1}{2d}\sum_{ij \in E}(e_{i,t} - e_{j,t})^2$
2. Lemma 29: $\sum_{ij \in E}(x_i - x_j)^2 \geq \frac{d}{2}\Phi_G^2 \sum x_i^2$ when $\sum x_i = 0$

# Context & Application
The connection between conductance (a combinatorial quantity) and the spectral gap (an algebraic quantity) is the central result of Section IX.4. It enables proving rapid mixing via expansion properties.

# Examples
**Example**: For $Q^d$ with $\Phi_{Q^d} = 1/d$: $\lambda_2 \leq 1 - 1/d^2$. (The true value is $1 - 2/d$, which is tighter.)

# Relationships
## Builds Upon
- **mixing-rate**, **conductance-of-graph**

## Enables
- **rapid-mixing**

## Related
- **lazy-random-walk** — Main results apply to LRW

# Source Reference
Chapter IX, Section IX.4, Theorem 27, Corollaries 30-31, pages 322-325.

# Verification Notes
- Definition source: Synthesized from Theorem 27 and Corollaries 30-31
- Confidence rationale: Explicit theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
