---
concept: Mean Return Time
slug: mean-return-time
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 312
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases:
  - "H(x,x)"
  - "expected return time"
prerequisites:
  - mean-hitting-time
  - stationary-distribution
extends:
  - mean-hitting-time
related:
  - kacs-formula
  - commute-time
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
---

# Quick Definition
The mean return time to vertex $x$ is $H(x,x) = \mathbb{E}_x(\tau_{\{x\}}^+)$, the expected number of steps for a random walk starting at $x$ to first return to $x$. For the SRW on a connected graph: $H(x,x) = 2m/d(x)$.

# Core Definition
Theorem 16 (p. 312): "The mean return time to a vertex $x$ in a connected graph is $H(x,x) = 2m/d(x)$." This equals the reciprocal of the stationary probability: $H(x,x) = 1/\pi_x$ where $\pi_x = d(x)/2m$.

# Prerequisites
- **Mean hitting time** — Return time is the special case $H(x,x)$
- **Stationary distribution** — $H(x,x) = 1/\pi_x$

# Key Properties
1. $H(x,x) = 2m/d(x)$ for the SRW (Theorem 16)
2. $H(x,x) = 1/\pi_x$ where $\pi$ is the stationary distribution (equation (21))
3. More generally, Kac's formula: $\pi(S)\mathbb{E}_{\pi_S}(\tau_S^+) = 1$ for any set $S$ (equation (22))
4. Independent of graph structure beyond $d(x)$ and $m$

# Construction / Recognition
The mean return time to $x$ is simply $2m/d(x)$; no computation beyond knowing the degree and number of edges is needed.

# Context & Application
The mean return time formula is "perhaps the most basic result about random walks on graphs" and has a beautifully simple form. It generalizes to Kac's formula for ergodic Markov chains.

# Examples
**Example** (p. 312): On a complete graph $K_n$, each vertex has degree $n-1$ and $m = \binom{n}{2}$, so $H(x,x) = 2\binom{n}{2}/(n-1) = n$.

# Relationships
## Builds Upon
- **mean-hitting-time**, **stationary-distribution**

## Enables
- **commute-time** — Uses return time relation: $C(s,t) = H(s,s)/P_{\text{esc}}(s \to t)$
- **kacs-formula** — Generalization to sets

# Common Errors
- **Error**: Thinking mean return time depends on global graph structure beyond degree and size.
  **Correction**: $H(x,x) = 2m/d(x)$ depends only on the degree of $x$ and the total number of edges.

# Source Reference
Chapter IX, Section IX.3, Theorem 16, page 312. Also equation (21), p. 314.

# Verification Notes
- Definition source: Direct from Theorem 16
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
