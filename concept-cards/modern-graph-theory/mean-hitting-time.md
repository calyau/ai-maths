---
concept: Mean Hitting Time
slug: mean-hitting-time
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 311
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases:
  - "expected hitting time"
  - "H(x,y)"
prerequisites:
  - hitting-time
  - simple-random-walk
extends:
  - hitting-time
related:
  - mean-return-time
  - commute-time
  - effective-resistance
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
  - "What distinguishes hitting time from commute time in random walks?"
---

# Quick Definition
The mean hitting time $H(x,y)$ is the expected number of steps for a random walk starting at $x$ to first reach $y$: $H(x,y) = \mathbb{E}_x(\tau_{\{y\}}^+)$.

# Core Definition
"Denote by $H(x,y)$ the mean hitting time of $y$ from $x$, namely the expected time it takes to go from $x$ to $y$: $H(x,y) = \mathbb{E}_x(\tau_{\{y\}}^+)$" (Bollobás, p. 311). Explicitly: $H(x,y) = \sum_{k=1}^{\infty} k \mathbb{P}(X_k = y, X_i \neq y \text{ for } 1 \leq i < k \mid X_0 = x)$. "Occasionally, $H(x,y)$ is also called the hitting time of $y$ from $x$ or the access time of $y$ from $x$."

# Prerequisites
- **Hitting time** — $H(x,y)$ is the expectation of the hitting time random variable
- **Simple random walk** — The default setting for computing $H(x,y)$

# Key Properties
1. Generally not symmetric: $H(x,y) \neq H(y,x)$ in general
2. Recursive formula: $H(x,y) = 1 + \frac{1}{d(x)} \sum_{z \in \Gamma(x)} H'(z,y)$ where $H'(z,y) = H(z,y)$ for $z \neq y$ and $H'(y,y) = 0$
3. Average over adjacent pairs: $\frac{1}{2m} \sum_x \sum_{y \in \Gamma(x)} H(x,y) = n-1$ (Theorem 18)
4. Symmetry in triples: $H(s,t) + H(t,u) + H(u,s) = H(s,u) + H(u,t) + H(t,s)$ (Theorem 23)

# Construction / Recognition
## To Compute $H(x,y)$
1. Set up the system of linear equations from the recursive formula
2. $H(x,y) = 1 + \frac{1}{d(x)} \sum_{z \in \Gamma(x)} H'(z,y)$ for all $x$
3. Boundary condition: $H'(y,y) = 0$
4. Solve the linear system

# Context & Application
Mean hitting times measure how quickly different parts of a graph can be accessed from given starting points. The asymmetry of $H(x,y)$ reflects the graph structure: it is harder to reach vertices in sparse regions from dense regions.

# Examples
**Example** (p. 312): On a path $xyz$: $H(x,y) = 1$ and $H(y,x) = 3$.

**Example** (Theorem 18, p. 314): The average hitting time over all adjacent pairs is exactly $n-1$: $\frac{1}{2m}\sum_{xy \in E(G)} [H(x,y) + H(y,x)] = n-1$ (using $C(x,y) = H(x,y) + H(y,x)$).

# Relationships
## Builds Upon
- **hitting-time** — $H(x,y)$ is its expected value

## Enables
- **commute-time** — $C(x,y) = H(x,y) + H(y,x)$

## Related
- **effective-resistance** — $C(s,t) = 2m R_{\text{eff}}(s,t)$

# Common Errors
- **Error**: Assuming $H(x,y)$ is symmetric.
  **Correction**: On a path $xyz$, $H(x,y) = 1$ but $H(y,x) = 3$.

# Common Confusions
- **Confusion**: Confusing $H(x,y)$ with $H'(x,y) = \mathbb{E}_x(\tau_{\{y\}})$.
  **Clarification**: $H'(x,y) = H(x,y)$ for $x \neq y$, but $H'(x,x) = 0$ while $H(x,x) = 2m/d(x) > 0$.

# Source Reference
Chapter IX, Section IX.3, pages 311-314. Theorems 16, 18, 23.

# Verification Notes
- Definition source: Direct from p. 311
- Confidence rationale: Explicit definition with notation
- Uncertainties: None
- Cross-reference status: Verified
