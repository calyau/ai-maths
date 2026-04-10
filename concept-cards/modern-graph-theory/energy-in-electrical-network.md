---
# === CORE IDENTIFICATION ===
concept: Energy in an Electrical Network
slug: energy-in-electrical-network

# === CLASSIFICATION ===
category: electrical-networks
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 299
section: "IX.1 Electrical Networks Revisited"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "total energy"
  - "energy dissipation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - effective-resistance
extends: []
related:
  - thomsons-principle
  - dirichlets-principle
  - rayleighs-principle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is energy defined in an electrical network?"
---

# Quick Definition
The total energy in an electrical network is the sum $\sum_{xy \in E(G)} w_{xy}^2 r_{xy}$ over all edges, where $w_{xy}$ is the current through edge $xy$ and $r_{xy}$ is its resistance. Equivalently, it equals $\sum_{xy} (V_x - V_y)^2 / r_{xy}$.

# Core Definition
Given an edge $xy$ with resistance $r_{xy}$, potential difference $p_{xy} = V_x - V_y$, and current $w_{xy} = p_{xy}/r_{xy}$, the energy in $xy$ is $w_{xy}^2 r_{xy} = (V_x - V_y)^2/r_{xy}$. The total energy is $E = \sum_{xy \in E(G)} w_{xy}^2 r_{xy} = \sum_{xy \in E(G)} (V_x - V_y)^2/r_{xy}$ (Bollobás, p. 299, equation (5)). For a simple network (all resistances equal to 1), the total energy is the quadratic form given by the Laplacian $L = D - A$ on the vector of absolute potentials.

# Prerequisites
- **Effective resistance** — Energy is expressed in terms of resistances and currents

# Key Properties
1. Energy in a single edge: $w_{xy}^2 r_{xy} = (V_x - V_y)^2/r_{xy} = (V_x - V_y) w_{xy}$
2. Total energy equals $(V_s - V_t) w_s$ for a current from $s$ to $t$ (Corollary 4)
3. If $V_s - V_t = 1$: total energy = effective conductance $C_{\text{eff}}(s,t)$
4. If $w_s = 1$: total energy = effective resistance $R_{\text{eff}}(s,t)$
5. For simple networks: energy is the Laplacian quadratic form on potentials

# Construction / Recognition
## To Compute Total Energy
1. Determine currents $w_{xy}$ in each edge (from Kirchhoff's laws)
2. Sum $w_{xy}^2 r_{xy}$ over all edges
3. Alternatively: determine potentials $V_x$ and sum $(V_x - V_y)^2/r_{xy}$ over edges

# Context & Application
Energy is the central optimizing quantity in Thomson's and Dirichlet's principles: proper electric currents and potentials minimize total energy subject to constraints. This optimization viewpoint is "much better" (p. 298) than the static approach of simultaneously solving all three laws, as it enables proofs of the monotonicity principle.

# Examples
**Example** (p. 299): For a simple network $N = (G, 1)$, the total energy is $\sum_{xy \in E(G)} (V_x - V_y)^2$, which is the Laplacian quadratic form $\mathbf{V}^T L \mathbf{V}$.

# Relationships
## Builds Upon
- **Effective resistance** — Energy relates to resistance via $E = R_{\text{eff}} \cdot I^2$

## Enables
- **thomsons-principle** — Currents minimize energy
- **dirichlets-principle** — Potentials minimize energy
- **monotonicity-principle** — Follows from energy minimization

## Related
- **rayleighs-principle** — Conservation of energy

# Common Errors
- **Error**: Double-counting energy by summing over both orientations of each edge.
  **Correction**: Edges are oriented arbitrarily; sum once per edge. If unoriented, use $\frac{1}{2}\sum_{x,y} w_{xy}^2 r_{xy}$.

# Common Confusions
- **Confusion**: Confusing energy with current or potential difference alone.
  **Clarification**: Energy combines both: it is current squared times resistance, or potential difference squared divided by resistance.

# Source Reference
Chapter IX: Random Walks on Graphs, Section IX.1, pages 298-300. Equation (5).

# Verification Notes
- Definition source: Direct from p. 299, equation (5)
- Confidence rationale: Explicit formula with equation number
- Uncertainties: None
- Cross-reference status: Verified
