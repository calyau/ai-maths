---
# === CORE IDENTIFICATION ===
concept: Dirichlet's Principle
slug: dirichlets-principle

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
  - "Theorem 1 (Dirichlet's principle)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - energy-in-electrical-network
extends: []
related:
  - thomsons-principle
  - monotonicity-principle
  - effective-conductance
contrasts_with:
  - thomsons-principle

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
Dirichlet's principle states that, given fixed potentials at outlets $s_1, \ldots, s_k$, the distribution of potentials at all other vertices that minimizes total energy $E = \sum (V_x - V_y)^2/r_{xy}$ is the one that gives the proper electric current.

# Core Definition
Let $N = (G, r)$ be an electrical network with outlets $s_1, \ldots, s_k$ set at potentials $V_{s_1}, \ldots, V_{s_k}$. Theorem 1 (p. 299) states there exist absolute potentials $V_x$ for $x \in V(G) \setminus \{s_1, \ldots, s_k\}$ minimizing $E((V_x)) = \sum_{xy \in E(G)} (V_x - V_y)^2/r_{xy}$. This distribution gives a proper electric current with no outlet other than the $s_i$, and the minimum of $E$ equals the total energy.

# Prerequisites
- **Energy in an electrical network** — Dirichlet's principle minimizes energy over potentials

# Key Properties
1. Fixes potentials at outlets, minimizes energy over potentials at other vertices
2. At the minimum, $\partial E/\partial V_x = 0$ gives KCL at each non-outlet vertex
3. Combined with Corollary 4, gives effective conductance (Corollary 5)
4. $C_{\text{eff}}(s,t) = \inf\{\sum (V_x - V_y)^2/r_{xy} : V_s = 1, V_t = 0\}$

# Construction / Recognition
## To Apply Dirichlet's Principle
1. Fix potentials $V_{s_i}$ at outlet vertices
2. Choose potentials at all other vertices to minimize $\sum (V_x - V_y)^2/r_{xy}$
3. The minimizing potentials define the proper electric current via Ohm's law
4. KCL is automatically satisfied at non-outlet vertices

# Context & Application
Dirichlet's principle is the "potential approach" complementing Thomson's "flow approach." It is particularly useful for bounding effective conductance from above, since any assignment of potentials gives an upper bound.

# Examples
**Example** (p. 300): The effective conductance $C_{\text{eff}}(s,t) = \inf\{\sum (V_x - V_y)^2/r_{xy} : V_s = 1, V_t = 0\}$ (Corollary 5).

# Relationships
## Builds Upon
- **energy-in-electrical-network**

## Enables
- **effective-conductance** — Expressed as minimum energy
- **monotonicity-principle** — Follows from either Thomson's or Dirichlet's principle

## Contrasts With
- **thomsons-principle** — Minimizes over flows rather than potentials

# Common Errors
- **Error**: Forgetting to fix the boundary potentials before minimizing.
  **Correction**: Potentials at outlets must be prescribed; only non-outlet potentials are free variables.

# Common Confusions
- **Confusion**: Thinking Dirichlet's and Thomson's principles give different results.
  **Clarification**: Both yield the same proper electric current; they differ only in the optimization approach (potentials vs. flows).

# Source Reference
Chapter IX: Random Walks on Graphs, Section IX.1, Theorem 1, page 299.

# Verification Notes
- Definition source: Direct from Theorem 1, p. 299
- Confidence rationale: Named theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
