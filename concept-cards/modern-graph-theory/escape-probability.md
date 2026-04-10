---
concept: Escape Probability
slug: escape-probability
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 304
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases:
  - "P_esc"
  - "P_esc(s -> t)"
prerequisites:
  - random-walk-on-graph
  - effective-conductance
extends: []
related:
  - hitting-time
  - commute-time
  - sojourn-time
  - transient-random-walk
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
The escape probability $P_{\text{esc}}(s \to t)$ is the probability that, starting at $s$, a random walk reaches $t$ before returning to $s$.

# Core Definition
The probability $P_{\text{esc}} = P_{\text{esc}}(s \to t)$ of escaping from $s$ to $t$ is "the probability that, starting at $s$, we get to $t$ before we return to $s$" (Bollobás, p. 304). In terms of hitting times: $P_{\text{esc}}(s \to t) = \mathbb{P}_s(X_{\tau^+_{\{s,t\}}} = t)$.

# Prerequisites
- **Random walk on a graph** — Escape probability is defined for random walks
- **Effective conductance** — Connected via $C_{\text{eff}}(s,t) = C_s P_{\text{esc}}(s \to t)$

# Key Properties
1. $C_{\text{eff}}(s,t) = C_s P_{\text{esc}}(s \to t)$ (Theorem 8, equation (11))
2. $P_{\text{esc}}(s \to t)/P_{\text{esc}}(t \to s) = C_t/C_s$ (equation (12))
3. $P_{\text{esc}}(s \to t) = 1/S_s(s \to t)$ where $S_s$ is expected sojourn time (equation (14))
4. For SRW: $P_{\text{esc}}(s \to t) = 2m/(d(s) C(s,t))$ (Theorem 19)
5. For infinite networks: $P_{\text{esc}}(s, \infty) > 0$ characterizes transience

# Construction / Recognition
1. Start the random walk at $s$
2. Run until either $s$ or $t$ is hit (at time $\geq 1$)
3. $P_{\text{esc}}$ is the probability that $t$ is hit first

# Context & Application
Escape probability is the key quantity connecting random walks to electrical networks. Theorem 8 shows that the hitting probabilities are precisely the absolute potentials in the corresponding electrical network. This connection "greatly benefits both areas."

# Examples
**Example** (p. 315): For graph $G_0$ with $k$ edges from $s$ to $u$ and $\ell$ from $u$ to $t$: $P_{\text{esc}}(s \to t) = \ell/(k+\ell)$.

# Relationships
## Builds Upon
- **random-walk-on-graph**, **effective-conductance**

## Enables
- **commute-time** — $C(s,t) = H(s,s)/P_{\text{esc}}(s \to t)$
- **transient-random-walk** — Positive escape probability to infinity

## Related
- **sojourn-time** — $P_{\text{esc}} = 1/S_s(s \to t)$

# Common Errors
- **Error**: Computing $P_{\text{esc}}(s \to t) = P_{\text{esc}}(t \to s)$.
  **Correction**: In general these are not equal; their ratio is $C_t/C_s$.

# Common Confusions
- **Confusion**: Confusing escape probability with hitting probability from $s$ to $t$.
  **Clarification**: Escape probability requires reaching $t$ before *returning* to $s$. The hitting probability from $s$ to $t$ (eventually) is 1 on a connected finite graph.

# Source Reference
Chapter IX, Section IX.2, Theorem 8, pages 304-305. Also equation (14), p. 307.

# Verification Notes
- Definition source: Direct from p. 304
- Confidence rationale: Explicit definition and theorem
- Uncertainties: None
- Cross-reference status: Verified
