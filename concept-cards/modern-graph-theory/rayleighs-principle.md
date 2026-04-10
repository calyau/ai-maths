---
concept: Rayleigh's Principle
slug: rayleighs-principle
category: electrical-networks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 300
section: "IX.1 Electrical Networks Revisited"
extraction_confidence: high
aliases:
  - "conservation of energy principle"
prerequisites:
  - energy-in-electrical-network
extends: []
related:
  - thomsons-principle
  - dirichlets-principle
  - effective-resistance
  - effective-conductance
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
Rayleigh's principle (Theorem 3) states that for any flow $u$ from $s$ to $t$ satisfying KCL and any function $(V_x)$ on the vertices: $(V_s - V_t)u_s = \sum_{xy \in E(G)} (V_x - V_y) u_{xy}$.

# Core Definition
Theorem 3 (p. 300): Let $u = (u_{xy})$ be a flow from $s$ to $t$ satisfying KCL at every vertex other than $s$ and $t$, with value $u_s$. Let $(V_x)$ be any function on the vertices. Then $(V_s - V_t)u_s = \sum_{xy \in E(G)} (V_x - V_y) u_{xy}$.

# Prerequisites
- **Energy in an electrical network** — Rayleigh's principle connects flow and potential energy

# Key Properties
1. The total energy in a current from $s$ to $t$ is $(V_s - V_t)w_s$ (Corollary 4)
2. If $V_s - V_t = 1$: total energy = total current = effective conductance
3. If $w_s = 1$: total energy = potential difference = effective resistance

# Context & Application
Rayleigh's principle "implies that if we replace a network with a source $s$ and a sink $t$ with a single wire whose resistance is the effective resistance of the network, then the total energy in the system does not change" (p. 300).

# Examples
**Example** (Corollary 4): With unit potential difference ($V_s - V_t = 1$), the total energy equals $C_{\text{eff}}(s,t)$.

# Relationships
## Builds Upon
- **energy-in-electrical-network**

## Enables
- **effective-resistance** — Expressed via Rayleigh's principle
- **effective-conductance** — Expressed via Rayleigh's principle

# Source Reference
Chapter IX, Section IX.1, Theorem 3 and Corollary 4, page 300.

# Verification Notes
- Definition source: Direct from Theorem 3
- Confidence rationale: Named theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
