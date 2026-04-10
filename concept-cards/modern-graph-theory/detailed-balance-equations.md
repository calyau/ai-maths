---
concept: Detailed Balance Equations
slug: detailed-balance-equations
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 310
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases:
  - "time-reversibility condition"
prerequisites:
  - transition-probability-matrix
  - stationary-distribution
extends: []
related:
  - random-walk-on-electrical-network
contrasts_with: []
answers_questions:
  - "What must I know before understanding random walks on graphs?"
---

# Quick Definition
The detailed balance equations state that $\pi_x P_{xy} = \pi_y P_{yx}$ for all $x, y$, meaning that under the stationary distribution, the probability flow from $x$ to $y$ equals the flow from $y$ to $x$.

# Core Definition
A transition matrix $P$ and distribution $\pi$ satisfy the detailed balance equations if $\pi_x P_{xy} = \pi_y P_{yx}$ for all $x, y \in V$ (Bollobás, p. 310). For the SRW: $\pi_x P_{xy} = \frac{d(x)}{2m} \cdot \frac{1}{d(x)} = \frac{1}{2m} = \frac{d(y)}{2m} \cdot \frac{1}{d(y)} = \pi_y P_{yx}$.

# Prerequisites
- **Transition probability matrix** — The matrix whose balance is characterized
- **Stationary distribution** — A distribution satisfying detailed balance is stationary

# Key Properties
1. Detailed balance implies stationarity: if $\pi_x P_{xy} = \pi_y P_{yx}$ then $\pi P = \pi$
2. The converse does not hold in general; detailed balance is stronger than stationarity
3. A Markov chain satisfying detailed balance is called reversible
4. Every random walk on a weighted graph satisfies detailed balance

# Construction / Recognition
To verify detailed balance: check that $\pi_x P_{xy} = \pi_y P_{yx}$ for all pairs $x, y$.

# Context & Application
Detailed balance characterizes reversible Markov chains, which are precisely random walks on weighted graphs. "Every reversible finite Markov chain can be obtained" as a random walk on a weighted graph (p. 300).

# Examples
**Example** (p. 310): For SRW, each edge $xy$ carries probability $1/2m$ in each direction: $\pi_x P_{xy} = 1/2m = \pi_y P_{yx}$.

# Relationships
## Builds Upon
- **transition-probability-matrix**, **stationary-distribution**

## Enables
- **random-walk-on-electrical-network** — Reversibility enables the connection

# Source Reference
Chapter IX, Section IX.3, page 310.

# Verification Notes
- Definition source: Direct from p. 310
- Confidence rationale: Explicit equations
- Uncertainties: None
- Cross-reference status: Verified
