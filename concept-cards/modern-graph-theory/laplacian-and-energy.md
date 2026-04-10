---
concept: Laplacian Quadratic Form and Energy
slug: laplacian-and-energy
category: electrical-networks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 299
section: "IX.1 Electrical Networks Revisited"
extraction_confidence: high
aliases: []
prerequisites:
  - energy-in-electrical-network
extends: []
related:
  - dirichlets-principle
  - spectral-gap-and-mixing
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
For a simple network (all resistances 1), the total energy is the Laplacian quadratic form $\mathbf{V}^T L \mathbf{V}$ on the vector of absolute potentials, where $L = D - A$ is the graph Laplacian.

# Core Definition
"For a simple network $N = (G, 1)$, the total energy in $N$ is the value of the quadratic form given by the Laplacian $L = D - A$ on the vector $(V_x)$ of absolute potentials" (Bollobás, p. 299). The Laplacian is $L = D - A$ where $D$ is the degree matrix and $A$ is the adjacency matrix. For general conductances, use the weighted Laplacian with $c_e = 1/r_e$.

# Prerequisites
- **Energy in an electrical network** — The quadratic form being identified

# Key Properties
1. $E = \sum_{xy \in E}(V_x - V_y)^2 = \mathbf{V}^T L \mathbf{V}$ for simple networks
2. $L = D - A$ is positive semidefinite
3. Kernel of $L$ consists of constant vectors on each component
4. For weighted networks: use weighted Laplacian with conductances

# Relationships
## Builds Upon
- **energy-in-electrical-network**

## Related
- **dirichlets-principle** — Energy minimization in terms of the Laplacian
- **spectral-gap-and-mixing** — Eigenvalues of the Laplacian relate to mixing

# Source Reference
Chapter IX, Section IX.1, page 299.

# Verification Notes
- Definition source: Direct from p. 299
- Confidence rationale: Explicit identification
- Uncertainties: None
- Cross-reference status: Verified
