---
concept: Hitting Time
slug: hitting-time
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
  - "first passage time"
  - "access time"
  - "tau_S"
prerequisites:
  - random-walk-on-graph
extends: []
related:
  - mean-hitting-time
  - mean-return-time
  - commute-time
  - escape-probability
contrasts_with:
  - commute-time
answers_questions:
  - "How do I compute hitting times for a random walk?"
  - "What distinguishes hitting time from commute time in random walks?"
---

# Quick Definition
The hitting time of a set $S$ is the first time the random walk visits a state in $S$. Two variants exist: $\tau_S = \min\{t \geq 0 : X_t \in S\}$ and $\tau_S^+ = \min\{t \geq 1 : X_t \in S\}$.

# Core Definition
"For a set $S$ of states, we define two hitting times: $\tau_S = \min\{t \geq 0 : X_t \in S\}$ and $\tau_S^+ = \min\{t \geq 1 : X_t \in S\}$. As we frequently start our RW at a state $x$ in $S$, it is important to distinguish between the two hitting times" (Bollobás, p. 304).

# Prerequisites
- **Random walk on a graph** — Hitting times are parameters of random walks

# Key Properties
1. $\tau_S = 0$ if $X_0 \in S$; $\tau_S^+$ requires at least one step
2. For $x \notin S$: $\tau_S = \tau_S^+$ when started from $x$
3. The distinction matters when $X_0 \in S$ (e.g., for return times)
4. Hitting times are random variables, not constants
5. The mean hitting time $H(x,y) = \mathbb{E}_x(\tau_{\{y\}}^+)$ is generally not symmetric

# Construction / Recognition
## To Compute a Hitting Time
1. Start the random walk at $X_0 = x$
2. Run the walk step by step
3. Record the first time $t$ such that $X_t \in S$ (for $\tau_S$) or $t \geq 1$ with $X_t \in S$ (for $\tau_S^+$)

# Context & Application
Hitting times are fundamental parameters of random walks, quantifying how quickly a walk reaches target states. They appear in algorithmic applications (how long to explore a graph), in the connection to electrical networks, and in Foster's theorem.

# Examples
**Example** (p. 312): For a path $xyz$, $H(x,y) = 1$ (one step from $x$ to its neighbour $y$) but $H(y,x) = 3$ (from $y$, we go to either $x$ or $z$ with equal probability; if $z$, we must return).

# Relationships
## Builds Upon
- **random-walk-on-graph**

## Enables
- **mean-hitting-time** — Expected value of hitting time
- **commute-time** — Sum of hitting times in both directions
- **mean-return-time** — Special case $H(x,x)$

## Contrasts With
- **commute-time** — Round-trip time vs. one-way time

# Common Errors
- **Error**: Using $\tau_S$ when $\tau_S^+$ is needed (e.g., for return times).
  **Correction**: When starting at $x \in S$, always use $\tau_S^+$ (which requires at least one step).

# Common Confusions
- **Confusion**: Expecting hitting times to be symmetric: $H(x,y) = H(y,x)$.
  **Clarification**: Hitting times are generally not symmetric. On a path $xyz$: $H(x,y) = 1$ but $H(y,x) = 3$.

# Source Reference
Chapter IX, Section IX.2, page 304. Also Section IX.3, page 311.

# Verification Notes
- Definition source: Direct quote from p. 304
- Confidence rationale: Explicit definition with two variants
- Uncertainties: None
- Cross-reference status: Verified
