---
concept: Random Walk on an Electrical Network
slug: random-walk-on-electrical-network
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 303
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases: []
prerequisites:
  - random-walk-on-graph
  - effective-resistance
extends:
  - random-walk-on-graph
related:
  - harmonic-function-on-graph
  - escape-probability
  - detailed-balance-equations
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
A random walk on an electrical network $(G, c)$ uses the conductance function as edge weights: the transition probability from $x$ to $y$ is $P_{xy} = c_{xy}/C_x$ where $C_x = \sum_{z \in \Gamma(x)} c_{xz}$.

# Core Definition
"The weighted multigraphs we are especially interested in are the electrical networks $(G, c)$, with conductance function $c$: the weight of an edge $e$ is taken to be its conductance $c_e$" (Bollobás, p. 303). The transition matrix is $P_{xy} = c_{xy}/C_x$ if $xy \in E(G)$, and $0$ otherwise.

# Prerequisites
- **Random walk on a graph** — This is a special case with conductance weights
- **Effective resistance** — Key quantity connecting the walk to the network

# Key Properties
1. Transition probability proportional to edge conductance
2. Satisfies detailed balance: $\pi_x P_{xy} = \pi_y P_{yx} = c_{xy}/(2\sum_e c_e)$
3. The stationary distribution is $\pi_x = C_x / \sum_z C_z$
4. Harmonic functions for the walk correspond to potentials in the network
5. Escape probability relates to effective conductance: $C_{\text{eff}} = C_s P_{\text{esc}}$

# Context & Application
This is the central connection of Chapter IX: random walks on electrical networks establish "an intimate connection" (p. 300) that "greatly benefits both areas."

# Examples
**Example** (p. 304): If $s$ is set at potential 1 and $t$ at potential 0, then $V_x = \mathbb{P}_x(\text{reaching } s \text{ before } t)$ (Theorem 8).

# Relationships
## Builds Upon
- **random-walk-on-graph**, **effective-resistance**

## Related
- **harmonic-function-on-graph** — Potentials are harmonic functions
- **escape-probability** — $C_{\text{eff}} = C_s P_{\text{esc}}$

# Source Reference
Chapter IX, Section IX.2, pages 303-309.

# Verification Notes
- Definition source: Direct from p. 303
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
