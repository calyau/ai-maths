---
concept: Effective Conductance
slug: effective-conductance
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
  - "C_eff"
  - "C_eff(s,t)"
prerequisites:
  - energy-in-electrical-network
extends: []
related:
  - effective-resistance
  - escape-probability
  - dirichlets-principle
contrasts_with:
  - effective-resistance
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
The effective conductance $C_{\text{eff}}(s,t)$ between vertices $s$ and $t$ is the current flowing from $s$ to $t$ when $s$ and $t$ are set at potential difference 1.

# Core Definition
"The effective conductance $C_{\text{eff}} = C_{\text{eff}}(s,t)$ of an electrical network from $s$ to $t$ is the value of the current from $s$ to $t$ if $s$ and $t$ are set at potential difference 1" (Bollobás, p. 300). By Corollary 5: $C_{\text{eff}}(s,t) = \inf\{\sum_{xy \in E(G)} (V_x - V_y)^2/r_{xy} : V_s = 1, V_t = 0\}$.

# Prerequisites
- **Energy in an electrical network** — Effective conductance equals the minimum energy at unit potential difference

# Key Properties
1. $C_{\text{eff}}(s,t) = 1/R_{\text{eff}}(s,t)$
2. Equals the infimum of $\sum (V_x - V_y)^2/r_{xy}$ over potentials with $V_s = 1, V_t = 0$ (Corollary 5)
3. $C_{\text{eff}}(s,t) = C_s P_{\text{esc}}(s \to t)$ where $C_s$ is total conductance at $s$ (Theorem 8, equation (11))
4. Does not increase when a wire is cut
5. Symmetric: $C_{\text{eff}}(s,t) = C_{\text{eff}}(t,s)$

# Construction / Recognition
1. Set $s$ at potential 1, $t$ at potential 0
2. Find the potential distribution minimizing total energy
3. The total current leaving $s$ equals $C_{\text{eff}}(s,t)$

# Context & Application
Effective conductance directly links to escape probability: $C_{\text{eff}}(s,t) = C_s P_{\text{esc}}(s \to t)$ (Theorem 8). For infinite networks, $C_{\text{eff}}^{(\infty)} > 0$ characterizes transience.

# Examples
**Example** (p. 315): For graph $G_0$ with $k$ edges from $s$ to $u$ and $\ell$ from $u$ to $t$: $C_{\text{eff}}(s,t) = k\ell/(k+\ell)$.

# Relationships
## Builds Upon
- **energy-in-electrical-network**

## Enables
- **escape-probability** — $P_{\text{esc}} = C_{\text{eff}}/C_s$
- **transient-random-walk** — Characterized by positive $C_{\text{eff}}^{(\infty)}$

## Contrasts With
- **effective-resistance** — Reciprocal quantities

# Common Errors
- **Error**: Confusing effective conductance with the conductance of a single edge.
  **Correction**: Effective conductance accounts for all paths in the network.

# Common Confusions
- **Confusion**: Thinking effective conductance depends on the direction of current.
  **Clarification**: $C_{\text{eff}}(s,t) = C_{\text{eff}}(t,s)$ always.

# Source Reference
Chapter IX, Section IX.1, Corollary 5, page 300. Also Theorem 8, p. 304.

# Verification Notes
- Definition source: Direct from p. 300
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
