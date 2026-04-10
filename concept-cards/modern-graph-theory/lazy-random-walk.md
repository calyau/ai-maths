---
concept: Lazy Random Walk
slug: lazy-random-walk
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 322
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "LRW"
prerequisites:
  - simple-random-walk
extends:
  - simple-random-walk
related:
  - mixing-rate
  - conductance-of-graph
  - rapid-mixing
contrasts_with:
  - simple-random-walk
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
The lazy random walk (LRW) on a $d$-regular graph stays at the current vertex with probability $1/2$ and moves to a uniformly random neighbour with probability $1/(2d)$, giving transition matrix $P_L = (P_S + I)/2$.

# Core Definition
The LRW on a $d$-regular graph $G$ has transition probabilities: $P(X_{t+1} = j | X_t = i) = 1/2$ if $i = j$, $1/(2d)$ if $i \sim j$, and $0$ otherwise. "Putting it slightly differently, we attach $d$ loops to each vertex and run the simple random walk on this multigraph" (Bollobás, p. 322).

# Prerequisites
- **Simple random walk** — LRW is a slowed-down version

# Key Properties
1. $P_L = (P_S + I)/2$
2. Eigenvalues: $\frac{1}{2}(\lambda_i + 1) \geq 0$ (all non-negative)
3. Mixing rate: $\frac{1}{2}(\lambda_2 + 1)$, the second-largest eigenvalue of $P_L$
4. Eliminates negative eigenvalues, so convergence is monotone (no oscillation)
5. If $\lambda_2$ is close to 1, SRW is at most about twice as fast as LRW

# Construction / Recognition
1. Take the SRW transition matrix $P_S$
2. Set $P_L = (P_S + I)/2$
3. Equivalently: at each step, flip a coin; heads = stay, tails = take an SRW step

# Context & Application
The LRW is introduced to eliminate the issue of negative eigenvalues (which cause oscillation in bipartite graphs). With the LRW, the mixing rate is always $\frac{1}{2}(\lambda_2 + 1)$, determined solely by $\lambda_2$. This makes the conductance bound more transparent.

# Examples
**Example** (p. 326): For $K_n$: LRW mixing rate is $1/2$.

**Example** (p. 326): For $Q^d$: LRW mixing rate is $1 - 1/d$.

# Relationships
## Builds Upon
- **simple-random-walk**

## Enables
- **rapid-mixing** — Main theorem (Theorem 27) is about LRW
- **conductance-of-graph** — Conductance bounds LRW convergence

## Contrasts With
- **simple-random-walk** — SRW may have negative eigenvalues causing oscillation

# Source Reference
Chapter IX, Section IX.4, pages 322-323.

# Verification Notes
- Definition source: Direct from p. 322
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
