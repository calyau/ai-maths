---
concept: Mean Hitting Time Average
slug: mean-hitting-time-average
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 314
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases:
  - "Theorem 18"
prerequisites:
  - mean-hitting-time
  - stationary-distribution
extends: []
related:
  - commute-time
  - fosters-theorem
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
---

# Quick Definition
The average hitting time over all ordered pairs of adjacent vertices equals $n-1$: $\frac{1}{2m}\sum_x \sum_{y \in \Gamma(x)} H(x,y) = n-1$ (Theorem 18). Equivalently, the average commute time over edges is $2(n-1)$.

# Core Definition
Theorem 18 (p. 314): "Let $G$ be a connected graph of order $n$ and size $m$. The mean hitting times satisfy $\frac{1}{2m}\sum_{x \in V(G)}\sum_{y \in \Gamma(x)} H(x,y) = n-1$."

# Prerequisites
- **Mean hitting time** — The quantities being averaged
- **Stationary distribution** — Used in the proof

# Key Properties
1. $\frac{1}{2m}\sum_{xy \in E(G)} C(x,y) = n-1$ (equivalent formulation)
2. Average commute time between adjacent vertices is $2(n-1)$
3. Starting from the stationary distribution, expected return to origin in $n$ steps

# Relationships
## Builds Upon
- **mean-hitting-time**, **stationary-distribution**

## Enables
- **fosters-theorem** — Second proof combines this with $C = 2m R_{\text{eff}}$

# Source Reference
Chapter IX, Section IX.3, Theorem 18, page 314.

# Verification Notes
- Definition source: Direct from Theorem 18
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
