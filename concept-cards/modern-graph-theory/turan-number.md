---
concept: "Turán Number"
slug: turan-number
category: extremal-graph-theory
subcategory: extremal-functions
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: high
aliases:
  - "t_r(n)"
prerequisites:
  - turan-graph
extends: []
related:
  - turans-theorem
  - extremal-function
contrasts_with: []
answers_questions:
  - "What is the Turán number?"
---

# Quick Definition
The Turán number $t_r(n)$ is the number of edges in the Turán graph $T_r(n)$, equal to $ex(n; K_{r+1})$.

# Core Definition
The number of edges in $T_r(n)$ is $t_r(n)$. For fixed $r \ge 1$ and $n \to \infty$: $t_r(n) = (1 - 1/r + o(1))\binom{n}{2}$. In particular, $t_2(n) = \lfloor n^2/4 \rfloor$ (Bollobás, pp. 116-117).

# Prerequisites
- **Turán graph** — $t_r(n) = e(T_r(n))$

# Key Properties
1. $t_r(n) \ge (1-1/r)\binom{n}{2}$ (inequality (1))
2. $t_r(n) = ex(n; K_{r+1})$ by Turán's theorem
3. $t_2(n) = \lfloor n^2/4 \rfloor$

# Construction / Recognition
Compute the number of edges in $T_r(n)$: sum $n_i n_j$ over all pairs of classes.

# Context & Application
$t_r(n)$ is the threshold for containing $K_{r+1}$: more than $t_r(n)$ edges forces a $K_{r+1}$.

# Examples
**Example** (p. 117): $t_2(n) = \lfloor n^2/4 \rfloor$, so more than $\lfloor n^2/4 \rfloor$ edges guarantees a triangle.

# Relationships
## Builds Upon
- **turan-graph** — $t_r(n)$ counts its edges

## Enables
- **turans-theorem** — $ex(n; K_{r+1}) = t_r(n)$

# Source Reference
Chapter IV, Section IV.2, pages 116-117.

# Verification Notes
- Definition source: Direct from pp. 116-117
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
