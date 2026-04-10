---
concept: Commute Time
slug: commute-time
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
  - "mean commute time"
  - "C(x,y)"
prerequisites:
  - mean-hitting-time
  - effective-resistance
extends: []
related:
  - escape-probability
  - fosters-theorem
contrasts_with:
  - mean-hitting-time
answers_questions:
  - "What distinguishes hitting time from commute time in random walks?"
---

# Quick Definition
The mean commute time $C(x,y)$ between vertices $x$ and $y$ is the expected number of steps in a round-trip from $x$ to $y$ and back: $C(x,y) = H(x,y) + H(y,x)$.

# Core Definition
"For vertices $x \neq y$, the mean commute time between $x$ and $y$, denoted by $C(x,y)$, is the expected number of steps in a round-trip, in a walk from $x$ to $y$ and then back to $x$. Thus $C(x,y) = H(x,y) + H(y,x)$" (Bollobás, p. 314).

# Prerequisites
- **Mean hitting time** — Commute time is the sum of two hitting times
- **Effective resistance** — Commute time equals $2m R_{\text{eff}}(s,t)$

# Key Properties
1. $C(x,y) = H(x,y) + H(y,x)$ (definition)
2. $C(s,t) = 2m R_{\text{eff}}(s,t)$ (Theorem 19, equation (26))
3. Symmetric: $C(x,y) = C(y,x)$
4. Average over edges: $\frac{1}{2m}\sum_{xy \in E(G)} C(x,y) = n-1$ (equation (24))
5. $P_{\text{esc}}(s \to t) = H(s,s)/C(s,t) = 2m/(d(s)C(s,t))$ (Theorem 19)

# Construction / Recognition
1. Compute $H(x,y)$ and $H(y,x)$ (from linear equations or electrical network methods)
2. $C(x,y) = H(x,y) + H(y,x)$
3. Alternatively: $C(x,y) = 2m R_{\text{eff}}(x,y)$

# Context & Application
Commute time is the symmetrized version of hitting time and has the elegant property of being proportional to effective resistance. This connection makes commute times computable via electrical network methods.

# Examples
**Example** (p. 314): The average commute time between adjacent vertices is $2(n-1)$: $\frac{1}{m}\sum_{xy \in E(G)} C(x,y) = 2(n-1)$.

# Relationships
## Builds Upon
- **mean-hitting-time** — Commute time sums two hitting times
- **effective-resistance** — Commute time is $2m$ times effective resistance

## Enables
- **fosters-theorem** — Uses $C(s,t) = 2m R_{\text{eff}}(s,t)$

## Contrasts With
- **mean-hitting-time** — Commute time is symmetric; hitting time generally is not

# Common Errors
- **Error**: Thinking $C(x,y) = 2 H(x,y)$.
  **Correction**: $C(x,y) = H(x,y) + H(y,x)$, and generally $H(x,y) \neq H(y,x)$.

# Common Confusions
- **Confusion**: Confusing commute time with twice the hitting time.
  **Clarification**: Commute time symmetrizes the hitting time, but it is not simply $2H(x,y)$ unless $H(x,y) = H(y,x)$.

# Source Reference
Chapter IX, Section IX.3, Theorem 19, pages 314-316. Equation (24).

# Verification Notes
- Definition source: Direct from p. 314
- Confidence rationale: Explicit definition and fundamental theorem
- Uncertainties: None
- Cross-reference status: Verified
