---
# === CORE IDENTIFICATION ===
concept: Phase Transition
slug: phase-transition

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
pdf_page: 246
section: "VII.5 The Phase Transition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Erdos-Renyi phase transition
  - double jump

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gnp-model
  - threshold-function
  - giant-component
extends: []
related:
  - subcritical-regime
  - critical-window
  - supercritical-regime
  - branching-process-approximation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the phase transition in random graphs?"
  - "What must I know before understanding random graph phase transitions?"
---

# Quick Definition

The phase transition is the sudden qualitative change in the component structure of $G_{n,t}$ around $t = n/2$: before this time, all components have $O(\log n)$ vertices; after, a unique giant component of order $\Theta(n)$ emerges while all others remain $O(\log n)$.

# Core Definition

**Theorem 17** (Bollobas, p. 247): Let $c > 0$ and $t = \lfloor cn/2 \rfloor$. (i) If $c < 1$ (subcritical): $L^{(i)}(G_t) \sim \frac{1}{\alpha}\log n$ for all $i$, where $\alpha = c - 1 - \log c$. (ii) If $c = 1$ (critical): $L^{(i)} = \Theta(n^{2/3})$. (iii) If $c > 1$ (supercritical): $L^{(1)}(G_t) \sim \gamma n$ where $e^{-c\gamma} = 1 - \gamma$, and $L^{(i)} \sim \frac{1}{\alpha}\log n$ for $i \ge 2$.

# Prerequisites

- **G(n,p) model** -- The probability space, with $p = c/n$
- **Threshold function** -- Phase transition as a threshold phenomenon
- **Giant component** -- The emergent structure

# Key Properties

1. The critical point is $t = n/2$ (equivalently $p = 1/n$)
2. Subcritical ($c < 1$): all components have $O(\log n)$ vertices
3. Critical ($c = 1$): largest components have order $\Theta(n^{2/3})$
4. Supercritical ($c > 1$): unique giant component of order $\gamma n$; all others $O(\log n)$
5. The function $\gamma(c)$ satisfies $e^{-c\gamma} = 1 - \gamma$ and $\gamma(1+\varepsilon) = 2\varepsilon - \frac{8}{3}\varepsilon^2 + O(\varepsilon^3)$

# Construction / Recognition

## To Observe the Phase Transition
1. Consider $G_{n,t}$ with $t = \lfloor cn/2 \rfloor$
2. For $c < 1$: measure $L^{(1)}$; it is $O(\log n)$
3. Increase $c$ through 1
4. For $c > 1$: $L^{(1)} = \gamma(c) n + o(n)$ while $L^{(2)} = O(\log n)$

# Context & Application

The phase transition is "the most dramatic example of a phase transition discovered by Erdos and Renyi" (p. 221). The terminology is borrowed from physics. The sudden emergence of the giant component has profound implications for network science, percolation theory, and epidemiology.

# Examples

**Example** (p. 248): If $c$ increases from $c < 1$ to $c' > 1$ (even slightly, e.g., $c' = \frac{100}{99}c$), then $L^{(1)}$ jumps from $O(\log n)$ to $\Theta(n)$.

# Relationships

## Builds Upon
- **G(n,p) model** -- With $p = c/n$
- **Threshold function** -- The transition is a threshold phenomenon
- **Giant component** -- The object that emerges

## Enables
- Understanding of network resilience and percolation

## Related
- **Subcritical regime** -- $c < 1$
- **Critical window** -- $c = 1$
- **Supercritical regime** -- $c > 1$
- **Branching process approximation** -- Determines $\gamma$

## Contrasts With
- None

# Common Errors

- **Error**: Thinking the phase transition happens at a single edge addition
  **Correction**: The transition is a window; the giant component grows from 0 to $\Theta(n)$ over $O(n)$ edge additions around $t = n/2$

# Common Confusions

- **Confusion**: Confusing the phase transition ($p \sim 1/n$) with the connectivity threshold ($p \sim \log n/n$)
  **Clarification**: The giant component emerges well before the graph becomes connected

# Source Reference

Chapter VII: Random Graphs, Section VII.5, Theorem 17, pages 246--250.

# Verification Notes

- Definition source: Direct from Theorem 17, pp. 247--248
- Confidence rationale: Central theorem with detailed statement
- Uncertainties: None
- Cross-reference status: Verified
