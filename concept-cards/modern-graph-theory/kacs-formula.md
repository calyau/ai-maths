---
concept: Kac's Formula
slug: kacs-formula
category: random-walks
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 314
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases: []
prerequisites:
  - stationary-distribution
  - mean-return-time
extends:
  - mean-return-time
related:
  - hitting-time
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
---

# Quick Definition
Kac's formula generalizes the mean return time result: for any set $S$ of states in an ergodic Markov chain, $\pi(S) \mathbb{E}_{\pi_S}(\tau_S^+) = 1$, where $\pi_S$ is the stationary distribution conditioned on $S$.

# Core Definition
Equation (22), p. 314: $\pi(S)\mathbb{E}_{\pi_S}(\tau_S^+) = 1$, where $\pi_S$ is $\pi$ conditioned on $S$ and $\tau_S^+$ is the first return time to $S$. For $S = \{x\}$, this reduces to $\pi_x H(x,x) = 1$, i.e., $H(x,x) = 1/\pi_x$.

# Prerequisites
- **Stationary distribution** — $\pi$ and $\pi_S$ appear in the formula
- **Mean return time** — Kac's formula generalizes $H(x,x) = 1/\pi_x$

# Key Properties
1. Generalizes $H(x,x) = 1/\pi_x$ to arbitrary subsets $S$
2. Starting from $\pi_S$ (stationary distribution restricted to $S$), the expected return to $S$ is $1/\pi(S)$
3. Holds for any ergodic finite Markov chain

# Construction / Recognition
Two proofs are sketched: (1) repeat the argument of Theorem 16; (2) use stationarity to show $\sum_{k=1}^{\infty} \mathbb{P}_\pi(\tau_S^+ = k) = \pi(S) \sum_{k=1}^{\infty} \mathbb{P}_{\pi_S}(\tau_S^+ \geq k) = \pi(S) \mathbb{E}_{\pi_S}(\tau_S^+) = 1$.

# Context & Application
Kac's formula is useful when analyzing the expected time for a random walk to return to a set of states, not just a single state.

# Examples
**Example**: For $S = \{x\}$: $\pi_x \cdot H(x,x) = 1$, giving $H(x,x) = 2m/d(x)$ for SRW.

# Relationships
## Builds Upon
- **stationary-distribution**, **mean-return-time**

## Enables
General return time calculations for sets of states

# Source Reference
Chapter IX, Section IX.3, equation (22), page 314.

# Verification Notes
- Definition source: Direct from equation (22), p. 314
- Confidence rationale: Explicit formula with proof sketch
- Uncertainties: None
- Cross-reference status: Verified
