---
concept: Sojourn Time
slug: sojourn-time
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 305
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases:
  - "expected sojourn time"
  - "S_x(s -> t)"
prerequisites:
  - random-walk-on-graph
  - hitting-time
extends: []
related:
  - escape-probability
  - effective-resistance
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
---

# Quick Definition
The expected sojourn time $S_x(s \to t)$ at vertex $x$ is the expected number of times the random walk visits $x$ when started at $s$ and stopped upon reaching $t$.

# Core Definition
$S_x(s \to t) = \mathbb{E}_s(|\{i < \tau_{\{t\}} : X_i = x\}|)$ (Bollobás, p. 305). The sojourn time counts visits to $x$ before reaching $t$. Note $S_t(s \to t) = 0$ and $S_s(s \to t) \geq 1$ since the walk starts at $s$.

# Prerequisites
- **Random walk on a graph** — Sojourn time is a random walk parameter
- **Hitting time** — Sojourn time counts visits before a hitting time

# Key Properties
1. $S_t(s \to t) = 0$ always
2. $P_{\text{esc}}(s \to t) = 1/S_s(s \to t)$ (equation (14))
3. $R_{\text{eff}}(s,t) = S_s(s \to t)/C_s$ (equation (13), Theorem 9)
4. The function $V_x = S_x(s \to t)/C_x$ gives absolute potentials (Theorem 9)
5. Reciprocity: $d(s) S_x(s \to t) = d(x) S_s(x \to t)$ (Theorem 24)

# Construction / Recognition
1. Start the walk at $s$
2. Count visits to $x$ until the walk first reaches $t$
3. Average over many trials to estimate $S_x(s \to t)$

# Context & Application
Sojourn times link random walks to electrical networks: the ratio $S_x(s \to t)/C_x$ gives absolute potentials (Theorem 9), and the current through an edge equals the expected difference of traversal counts in opposite directions.

# Examples
**Example** (p. 305): If the network has just vertices $s$ and $t$ joined by one edge, then $S_s(s \to t) = 1$.

# Relationships
## Builds Upon
- **random-walk-on-graph**, **hitting-time**

## Enables
- **effective-resistance** — $R_{\text{eff}} = S_s(s \to t)/C_s$
- **escape-probability** — $P_{\text{esc}} = 1/S_s(s \to t)$

# Common Errors
- **Error**: Including visits to $t$ in the sojourn count.
  **Correction**: The sojourn time counts visits strictly before reaching $t$.

# Source Reference
Chapter IX, Section IX.2, Theorem 9, pages 305-306.

# Verification Notes
- Definition source: Direct from p. 305
- Confidence rationale: Explicit definition with formula
- Uncertainties: None
- Cross-reference status: Verified
