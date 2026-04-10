---
concept: Random Walk on the Torus
slug: torus-random-walk
category: conductance-and-mixing
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 327
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases: []
prerequisites:
  - rapid-mixing
  - conductance-of-graph
extends: []
related:
  - hypercube-random-walk
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
The torus $T_\ell^d$ (product of $d$ cycles of length $\ell$) has $\ell^d$ vertices, is $2d$-regular, and has conductance $\Phi_{T_{2\ell}^d} = 2/(\ell d)$. For fixed $\ell$, lazy random walks on $(T_{2\ell}^d)_d$ are rapidly mixing.

# Core Definition
$T_\ell^d$ is the product of $d$ cycles each of length $\ell$. "One can show that for $G = T_{2\ell}^d$ we have $\Phi_G = 2/(\ell d)$" (Bollobás, p. 327). Since $T_4^d = Q^{2d}$ (the $2d$-dimensional cube), this extends the hypercube result.

# Prerequisites
- **Rapid mixing**, **conductance-of-graph**

# Key Properties
1. $T_\ell^d$ has $\ell^d$ vertices, is $2d$-regular
2. $\Phi_{T_{2\ell}^d} = 2/(\ell d)$
3. For fixed $\ell$: rapidly mixing as $d \to \infty$
4. $T_4^d = Q^{2d}$

# Relationships
## Builds Upon
- **rapid-mixing**, **conductance-of-graph**

## Related
- **hypercube-random-walk** — Special case $T_4^d = Q^{2d}$

# Source Reference
Chapter IX, Section IX.4, page 327.

# Verification Notes
- Definition source: Direct from p. 327
- Confidence rationale: Explicit computation
- Uncertainties: None
- Cross-reference status: Verified
