---
concept: Effective Resistance
slug: effective-resistance
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
  - "R_eff"
  - "R_eff(s,t)"
prerequisites:
  - energy-in-electrical-network
extends: []
related:
  - effective-conductance
  - commute-time
  - escape-probability
  - fosters-theorem
contrasts_with:
  - effective-conductance
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
The effective resistance $R_{\text{eff}}(s,t)$ between vertices $s$ and $t$ in an electrical network is the potential difference between $s$ and $t$ needed to drive a unit current from $s$ to $t$.

# Core Definition
The effective resistance is $R_{\text{eff}}(s,t) = 1/C_{\text{eff}}(s,t)$, the reciprocal of the effective conductance. Equivalently, by Corollary 6 (p. 300): $R_{\text{eff}}(s,t) = \inf\{\sum_{xy \in E(G)} u_{xy}^2 r_{xy} : (u_{xy}) \text{ is an } s\text{-}t \text{ flow of size } 1\}$. It equals the total energy when a unit current flows from $s$ to $t$.

# Prerequisites
- **Energy in an electrical network** — Effective resistance equals the minimum energy of a unit flow

# Key Properties
1. $R_{\text{eff}}(s,t) = R_{\text{eff}}(t,s)$ (symmetric)
2. Equals the minimum total energy of a unit $s$-$t$ flow (Corollary 6)
3. Does not decrease when a wire is cut (monotonicity principle)
4. Does not increase when vertices are shorted
5. Related to commute time: $C(s,t) = 2m R_{\text{eff}}(s,t)$ (Theorem 19)
6. Related to escape probability: $R_{\text{eff}}(s,t) = 1/(d(s) P_{\text{esc}}(s \to t))$ (equation (27))

# Construction / Recognition
1. Set up the electrical network with given resistances
2. Apply a unit current from $s$ to $t$
3. Measure the resulting potential difference $V_s - V_t$; this is $R_{\text{eff}}(s,t)$
4. Alternatively: find the minimum-energy $s$-$t$ flow of size 1

# Context & Application
Effective resistance is a fundamental quantity connecting electrical networks and random walks. It determines commute times, escape probabilities, sojourn times, and appears in Foster's theorem. The monotonicity principle for effective resistance enables elegant proofs of transience/recurrence.

# Examples
**Example** (p. 315): For the graph $G_0$ with $k$ edges from $s$ to $u$ and $\ell$ edges from $u$ to $t$, $R_{\text{eff}}(s,t) = (k+\ell)/(k\ell)$.

# Relationships
## Builds Upon
- **energy-in-electrical-network**

## Enables
- **commute-time** — $C(s,t) = 2m R_{\text{eff}}(s,t)$
- **fosters-theorem** — Sum of $R_{\text{eff}}$ over edges equals $n-1$
- **transient-random-walk** — Characterized by finite $R_{\text{eff}}$ to infinity

## Contrasts With
- **effective-conductance** — $C_{\text{eff}} = 1/R_{\text{eff}}$

# Common Errors
- **Error**: Assuming effective resistance equals the resistance of a single path.
  **Correction**: Effective resistance accounts for all parallel paths; it is generally less than any single path resistance.

# Common Confusions
- **Confusion**: Thinking effective resistance is a graph-theoretic distance.
  **Clarification**: While $R_{\text{eff}}$ is a metric on graphs, it is generally different from the shortest-path distance.

# Source Reference
Chapter IX, Section IX.1, Corollaries 4-7, pages 300-301. Also Theorem 19, p. 316.

# Verification Notes
- Definition source: Direct from p. 300
- Confidence rationale: Explicit definition with multiple equivalent formulations
- Uncertainties: None
- Cross-reference status: Verified
