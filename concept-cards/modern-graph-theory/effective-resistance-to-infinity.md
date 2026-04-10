---
concept: Effective Resistance to Infinity
slug: effective-resistance-to-infinity
category: electrical-networks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 306
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases:
  - "R_eff(s, infinity)"
prerequisites:
  - effective-resistance
  - monotonicity-principle
extends:
  - effective-resistance
related:
  - transient-random-walk
  - recurrent-random-walk
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
For an infinite electrical network, the effective resistance from a vertex $s$ to infinity is $R_{\text{eff}}^{(\infty)} = \lim_{\ell \to \infty} R_{\text{eff}}^{(\ell)}$, where $R_{\text{eff}}^{(\ell)}$ is the effective resistance from $s$ to the shorted boundary at distance $\ell$.

# Core Definition
Fix a vertex $s$ and for $\ell \in \mathbb{N}$, let $N_\ell$ be the network obtained by shorting all vertices at distance $\geq \ell$ to a vertex $t_\ell$. By the monotonicity principle, $R_{\text{eff}}^{(\ell)}$ is increasing, so $R_{\text{eff}}^{(\infty)} = \lim R_{\text{eff}}^{(\ell)}$ is well-defined (possibly infinite). Theorem 10 (p. 306): the RW is transient iff $R_{\text{eff}}^{(\infty)} < \infty$.

# Prerequisites
- **Effective resistance** — Extended to infinite networks
- **Monotonicity principle** — Ensures the limit exists

# Key Properties
1. $R_{\text{eff}}^{(\ell)}$ is increasing in $\ell$
2. $R_{\text{eff}}^{(\infty)} < \infty$ iff the random walk is transient
3. $R_{\text{eff}}^{(\infty)} = \infty$ iff the random walk is recurrent

# Relationships
## Builds Upon
- **effective-resistance**, **monotonicity-principle**

## Enables
- **transient-random-walk** — $R_{\text{eff}}^{(\infty)} < \infty$
- **recurrent-random-walk** — $R_{\text{eff}}^{(\infty)} = \infty$

# Source Reference
Chapter IX, Section IX.2, Theorem 10, pages 306-307.

# Verification Notes
- Definition source: Synthesized from p. 306-307
- Confidence rationale: Clear construction with theorem
- Uncertainties: None
- Cross-reference status: Verified
