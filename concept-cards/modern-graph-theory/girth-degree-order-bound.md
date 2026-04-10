---
concept: Girth-Degree-Order Bound
slug: girth-degree-order-bound
category: extremal-graph-theory
subcategory: extremal-bounds
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.1 Paths and Cycles"
extraction_confidence: high
aliases:
  - "Theorem 1 (Ch IV)"
  - "Moore bound"
  - "n₀(g,δ)"
prerequisites:
  - girth
extends: []
related:
  - moore-graph
contrasts_with: []
answers_questions:
  - "How does girth relate to order and minimum degree?"
---

# Quick Definition
A graph with minimum degree $\delta \ge 3$ and girth $g \ge 3$ has at least $n_0(g, \delta)$ vertices, where $n_0$ is given by explicit formulas for odd and even $g$.

# Core Definition
**Theorem 1** (Ch IV): For $g \ge 3$ and $\delta \ge 3$, define $n_0(g,\delta) = 1 + \frac{\delta}{\delta-2}((\delta-1)^{(g-1)/2}-1)$ for odd $g$, and $n_0(g,\delta) = \frac{2}{\delta-2}((\delta-1)^{g/2}-1)$ for even $g$. A graph with minimum degree $\delta$ and girth $g$ has at least $n_0(g,\delta)$ vertices (Bollobás, p. 112).

# Prerequisites
- **Girth** — The minimum cycle length being bounded

# Key Properties
1. For odd $g = 2d+1$: argument uses distances from a single vertex
2. For even $g = 2d$: argument uses distances from an adjacent pair
3. Equality defines Moore graphs
4. The bound is essentially exponential in $g$

# Construction / Recognition
1. Given $\delta$ and $g$, compute $n_0(g,\delta)$
2. Any graph with those parameters must have $\ge n_0$ vertices

# Context & Application
This is the fundamental lower bound on order for graphs with given minimum degree and girth. Moore graphs achieving equality are rare and algebraically structured.

# Examples
**Example** (p. 112, Fig. IV.1): The cases $\delta = g = 5$ and $\delta = 4, g = 6$ are illustrated.

# Relationships
## Enables
- **moore-graph** — Extremal case of equality

# Source Reference
Chapter IV, Section IV.1, pages 112-113. Theorem 1.

# Verification Notes
- Definition source: Direct theorem from p. 112
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
