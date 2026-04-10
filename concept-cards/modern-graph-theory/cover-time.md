---
concept: Cover Time
slug: cover-time
category: random-walks
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 335
section: "IX.5 Exercises"
extraction_confidence: medium
aliases:
  - "mean cover time"
  - "C(s)"
prerequisites:
  - simple-random-walk
  - effective-resistance
  - commute-time
extends: []
related:
  - rapid-mixing
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
---

# Quick Definition
The cover time $C(s)$ from vertex $s$ is the expected number of steps for the SRW starting at $s$ to visit every vertex. Exercise 33 shows $C(s) \leq 2m R(T)$ for any spanning tree $T$, implying $C(s) \leq n(n-1)^2$.

# Core Definition
Exercise 33 (p. 335): "The mean cover time, or simply cover time, $C(s)$ is the expected number of steps taken by the SRW on $G$ started at $s$ to visit all vertices of $G$." Upper bound: $C(s) \leq 2m R(T)$ where $R(T) = \sum_{xy \in E(T)} R_{\text{eff}}(x,y)$.

# Prerequisites
- **Simple random walk** — The walk being analyzed
- **Effective resistance** — Appears in the bound
- **Commute time** — Related parameter

# Key Properties
1. $C(s) \leq 2m R(T)$ for any spanning tree $T$ (Exercise 33)
2. $C(s) \leq n(n-1)^2$ (using $R(T) \leq (n-1)^2/2$)
3. For $K_n$: $C(s) = (n-1)\sum_{k=1}^{n-1} 1/k$ (coupon collector, Exercise 44)
4. For path $P_n$ from endpoint: $C(0) = n^2$ (Exercise 40)

# Relationships
## Builds Upon
- **simple-random-walk**, **effective-resistance**, **commute-time**

## Related
- **rapid-mixing** — Cover time bounds are algorithmic applications

# Source Reference
Chapter IX, Exercises 33, 40, 42, 44, pages 335-336.

# Verification Notes
- Definition source: From Exercise 33
- Confidence rationale: Medium -- defined in exercises, not main text
- Uncertainties: None
- Cross-reference status: Verified
