---
concept: Multiplicativity of the Tutte Polynomial
slug: multiplicativity-of-tutte-polynomial
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 344
section: "X.1 Basic Properties of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
extends: []
related:
  - rank-generating-polynomial
  - universal-polynomial-of-graphs
contrasts_with: []
answers_questions:
  - "What is the Tutte polynomial?"
---

# Quick Definition
The Tutte polynomial is multiplicative: if $G = G_1 \cup G_2$ with $G_1, G_2$ sharing at most one vertex, then $T_G = T_{G_1} \cdot T_{G_2}$.

# Core Definition
"The functions $S$ and $T$ are multiplicative in the sense that if $G = G_1 \cup G_2$ with the graphs $G_1$ and $G_2$ sharing at most one vertex, then the value on $G$ is the product of the values on $G_1$ and $G_2$" (Bollobás, p. 344). In particular, $T_G$ is determined by its values on blocks.

# Prerequisites
- **Tutte polynomial** — The property being stated

# Key Properties
1. $T_{G_1 \cup G_2} = T_{G_1} \cdot T_{G_2}$ (sharing at most one vertex)
2. $T$ is determined by multiplicativity + recursion on non-bridge/non-loop edges + values on $K_2$ and $L$
3. $T(K_1) = 1$ follows from multiplicativity
4. For blocks $B_1, \ldots, B_\ell$: $T_G = \prod T_{B_i}$ (Exercise 4)

# Context & Application
Multiplicativity reduces the computation of $T_G$ to its blocks. Combined with the deletion-contraction recursion, it fully determines the Tutte polynomial.

# Relationships
## Builds Upon
- **tutte-polynomial**

## Related
- **universal-polynomial-of-graphs** — Also multiplicative (in a weaker sense)

# Source Reference
Chapter X, Section X.1, page 344. Exercise 4.

# Verification Notes
- Definition source: Direct from p. 344
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
