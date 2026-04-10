---
# === CORE IDENTIFICATION ===
concept: Supercritical Regime
slug: supercritical-regime

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
  - giant-component
extends: []
related:
  - subcritical-regime
  - critical-window
  - component-gap
contrasts_with:
  - subcritical-regime

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does a random graph look like above the phase transition?"
---

# Quick Definition

In the supercritical regime ($c > 1$), the random graph $G_t$ with $t = \lfloor cn/2 \rfloor$ has a unique giant component of order $\gamma n$ and all other components have $O(\log n)$ vertices.

# Core Definition

**Theorem 17(iii)** (Bollobas, p. 248): If $c > 1$, for a.e. $G_t$: $|L^{(1)}(G_t) - \gamma n| \le \omega(n)n^{1/2}$ where $e^{-c\gamma} = 1 - \gamma$, and $L^{(i)}(G_t) \sim \frac{1}{\alpha}\log n$ for $i \ge 2$. The gap between the giant component and all others is dramatic.

# Prerequisites

- **Phase transition** -- The supercritical regime is $c > 1$
- **Giant component** -- The defining feature

# Key Properties

1. Unique giant component of order $\gamma(c) n$
2. All other components have $O(\log n)$ vertices (even smaller than subcritical)
3. As $c$ increases, $\gamma(c) \to 1$ and the graph approaches connectivity
4. The gap between $L^{(1)}$ and $L^{(2)}$ is $\Theta(n)$ vs. $\Theta(\log n)$

# Construction / Recognition

Not applicable -- this is a regime description.

# Context & Application

The supercritical regime is where network structure becomes meaningful. The giant component connects a macroscopic fraction of vertices, enabling long-range communication. This is the relevant regime for understanding real-world networks.

# Examples

**Example** (p. 248): For $c = 2$: $e^{-2\gamma} = 1 - \gamma$ gives $\gamma \approx 0.797$, so about 80% of vertices are in the giant component.

# Relationships

## Builds Upon
- **Phase transition** -- This is the $c > 1$ phase
- **Giant component** -- The central feature

## Enables
- Understanding of network connectivity

## Related
- **Component gap** -- The dramatic separation between giant and other components

## Contrasts With
- **Subcritical regime** -- No giant component exists there

# Common Errors

- **Error**: Assuming the graph is connected in the supercritical regime
  **Correction**: The graph has many small components alongside the giant component; connectivity requires $p \sim \log n / n$, not $p \sim 1/n$

# Common Confusions

- **Confusion**: Thinking $\gamma$ is the probability of connectivity
  **Clarification**: $\gamma$ is the fraction of vertices in the giant component, not a connectivity probability

# Source Reference

Chapter VII: Random Graphs, Section VII.5, Theorem 17(iii), page 248.

# Verification Notes

- Definition source: Direct from Theorem 17(iii)
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
