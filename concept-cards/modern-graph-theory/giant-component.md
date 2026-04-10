---
# === CORE IDENTIFICATION ===
concept: Giant Component
slug: giant-component

# === CLASSIFICATION ===
category: random-graphs
subcategory: component-structure
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 248
section: "VII.5 The Phase Transition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - phase-transition
extends: []
related:
  - supercritical-regime
  - branching-process-approximation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the giant component in a random graph?"
  - "How large is the giant component?"
---

# Quick Definition

In a supercritical random graph ($p = c/n$ with $c > 1$), the giant component is the unique largest component containing $\gamma n + o(n)$ vertices, where $\gamma = \gamma(c)$ satisfies $e^{-c\gamma} = 1 - \gamma$.

# Core Definition

For $t = \lfloor cn/2 \rfloor$ with $c > 1$, Theorem 17(iii) states that $|L^{(1)}(G_t) - \gamma n| \le \omega(n)n^{1/2}$ for a.e. $G_t$, where $\gamma \in (0,1)$ is the unique solution of $e^{-c\gamma} = 1 - \gamma$. All other components have $O(\log n)$ vertices. The giant component is unique and contains a constant proportion of all vertices (Bollobas, pp. 248--249).

# Prerequisites

- **Phase transition** -- The giant component emerges through the phase transition

# Key Properties

1. Emerges at $c = 1$ (the critical point)
2. For $c = 1 + \varepsilon$: $\gamma \approx 2\varepsilon$ (linear emergence near criticality)
3. The second largest component has only $O(\log n)$ vertices
4. For $t = n/2 + s$ with $s/n^{2/3} \to \infty$: $L^{(1)} \approx 4s$ (each edge adds ~4 vertices)
5. The gap between giant and second-largest is $\Omega(n) - O(\log n)$

# Construction / Recognition

## Determining $\gamma(c)$
1. Solve $e^{-c\gamma} = 1 - \gamma$ for $\gamma \in (0,1)$
2. Equivalently, find where $f_c(\gamma) = c\gamma$ intersects $g(\gamma) = -\log(1-\gamma)$
3. Near $c = 1$: $\gamma(1+\varepsilon) = 2\varepsilon - \frac{8}{3}\varepsilon^2 + \frac{28}{9}\varepsilon^3 + O(\varepsilon^4)$

# Context & Application

The giant component is the most dramatic feature of random graph evolution. Its emergence at the phase transition has deep connections to percolation theory, epidemiology (epidemic threshold), and network science (connectivity in large networks).

# Examples

**Example** (p. 249): For $t = n/2 + s$ with $s/n^{2/3} \to \infty$ and $s/n \to 0$: $L^{(1)}(G_t) = 4s + o(s)$ for a.e. $G_t$. On average, adding one edge to the random graph adds 4 vertices to the giant component.

# Relationships

## Builds Upon
- **Phase transition** -- Context for emergence

## Enables
- Understanding of network structure above criticality

## Related
- **Supercritical regime** -- The regime where the giant component exists
- **Branching process approximation** -- Determines $\gamma$

## Contrasts With
- None

# Common Errors

- **Error**: Thinking the giant component spans all vertices
  **Correction**: The giant component has $\gamma n$ vertices with $\gamma < 1$; many vertices remain in small $O(\log n)$ components

# Common Confusions

- **Confusion**: Thinking the giant component implies connectivity
  **Clarification**: The giant component emerges at $p \sim 1/n$ but the graph is not connected until $p \sim \log n / n$

# Source Reference

Chapter VII: Random Graphs, Section VII.5, Theorem 17(iii), pages 248--249.

# Verification Notes

- Definition source: Direct from Theorem 17(iii)
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
