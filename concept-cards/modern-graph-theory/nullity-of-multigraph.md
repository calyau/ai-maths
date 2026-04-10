---
concept: Nullity of a Multigraph
slug: nullity-of-multigraph
category: tutte-polynomial
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 342
section: "X.1 Basic Properties of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "n(G)"
  - "cycle rank"
  - "circuit rank"
prerequisites: []
extends: []
related:
  - rank-of-multigraph
  - rank-generating-polynomial
contrasts_with:
  - rank-of-multigraph
answers_questions:
  - "What must I know before understanding the Tutte polynomial?"
---

# Quick Definition
The nullity of a multigraph $G = (V, E)$ is $n(G) = |E| - |V| + k(G)$, the number of independent cycles.

# Core Definition
$n(G) = |E| - |V| + k(G) = |E| - r(G)$ (Bollobás, p. 342). It equals the dimension of the cycle space. $\deg_y T_G = n(G)$.

# Prerequisites
This is a foundational concept with no prerequisites.

# Key Properties
1. $n(G) = |E| - |V| + k(G) = |E| - r(G)$
2. $n(G) = 0$ iff $G$ is a forest
3. $n(G) \geq 0$ always
4. $\deg_y T_G = n(G)$
5. For spanning subgraph $(V, F)$: $n(F) = |F| - |V| + k(F)$

# Context & Application
Nullity appears as the exponent of $(y-1)$ in the Tutte polynomial definition and measures the number of independent cycles.

# Examples
**Example**: $n(C_n) = 1$ (one cycle). $n(K_n) = \binom{n}{2} - n + 1$.

# Relationships
## Enables
- **tutte-polynomial**, **rank-generating-polynomial**

## Contrasts With
- **rank-of-multigraph**

# Source Reference
Chapter X, Section X.1, page 342.

# Verification Notes
- Definition source: Direct from p. 342
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
