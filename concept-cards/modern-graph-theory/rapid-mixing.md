---
concept: Rapid Mixing
slug: rapid-mixing
category: conductance-and-mixing
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 326
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "rapidly mixing random walk"
prerequisites:
  - conductance-of-graph
  - lazy-random-walk
  - mixing-rate
extends: []
related:
  - total-variation-distance
  - spectral-gap-and-mixing
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
A sequence of graphs $(G_i)$ with $|G_i| \to \infty$ supports rapidly mixing random walks if the lazy random walk reaches within $\varepsilon$ of stationarity in polynomially many steps in $\log n_i$ (times $\log(1/\varepsilon)$).

# Core Definition
"Given a sequence $G_1, G_2, \ldots$ of graphs, with $|G_i| = n_i \to \infty$, we say that the lazy random walks on this sequence are rapidly mixing random walks if there is a polynomial $f$, depending only on the sequence $(G_i)$, such that if $0 < \varepsilon < 1$ and $t \geq f(\log n_i) \log(1/\varepsilon)$ then $d_1(\tilde{X}_i, t) \leq \varepsilon$" (Bollobás, p. 326).

# Prerequisites
- **Conductance of a graph** — Large conductance implies rapid mixing
- **Lazy random walk** — Rapid mixing is defined for LRW
- **Mixing rate** — $\mu \leq 1 - \Phi_G^2/2$

# Key Properties
1. Requires only $O(\text{poly}(\log n) \cdot \log(1/\varepsilon))$ steps to be $\varepsilon$-close to stationarity
2. Sufficient condition: $\Phi_{G_i} \geq (\log n_i)^{-k}$ for some $k$ (Theorem 32)
3. If $t \geq 8\Phi_G^{-2} \log n \cdot \log(1/\varepsilon)$ then $d_1(t) < \varepsilon$
4. "This is fast indeed: it suffices to take far fewer steps than the order of the graph" (p. 326)

# Construction / Recognition
## To Verify Rapid Mixing (Theorem 32)
1. Show $\Phi_{G_i} \geq (\log n_i)^{-k}$ for some constant $k$
2. Then $t \geq 8(\log n_i)^{2k+1} \log(1/\varepsilon)$ steps suffice

# Context & Application
"Rapidly mixing random walks have numerous algorithmic applications," including generating approximately random elements of large sets (perfect matchings, spanning trees, lattice points in convex bodies), enabling approximate counting and volume estimation (p. 327).

# Examples
**Example** (p. 326): LRW on $(K_n)$: $\Phi_{K_n} > 1/2$, so rapidly mixing.

**Example** (p. 326): LRW on $(Q^d)$: $\Phi_{Q^d} = 1/\log n$, so rapidly mixing.

**Example** (p. 327): LRW on tori $T_{2\ell}^d$ with fixed $\ell$: $\Phi = 2/(\ell d)$, so rapidly mixing as $d \to \infty$.

# Relationships
## Builds Upon
- **conductance-of-graph**, **lazy-random-walk**, **mixing-rate**

## Related
- **total-variation-distance** — Distance measure used in the definition

# Source Reference
Chapter IX, Section IX.4, Theorem 32 and Corollary 30, pages 326-327.

# Verification Notes
- Definition source: Direct from p. 326
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
