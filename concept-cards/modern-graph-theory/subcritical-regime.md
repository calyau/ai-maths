---
# === CORE IDENTIFICATION ===
concept: Subcritical Regime
slug: subcritical-regime

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
pdf_page: 247
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
  - critical-window
  - supercritical-regime
contrasts_with:
  - supercritical-regime

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does a random graph look like below the phase transition?"
---

# Quick Definition

In the subcritical regime ($t = \lfloor cn/2 \rfloor$ with $c < 1$), all components of $G_t$ are trees of order $O(\log n)$, and the $h$ largest components all have approximately $\frac{1}{\alpha}\log n$ vertices, where $\alpha = c - 1 - \log c$.

# Core Definition

**Theorem 17(i)** (Bollobas, p. 247): If $c < 1$ then for a.e. $G_t$ with $t = \lfloor cn/2 \rfloor$: $|L^{(i)}(G_t) - \frac{1}{\alpha}(\log n - \frac{5}{2}\log\log n)| \le \omega(n)$ for every fixed $i$. All components are small and of comparable size.

# Prerequisites

- **Phase transition** -- The subcritical regime is the region $c < 1$

# Key Properties

1. All components have $O(\log n)$ vertices
2. The $h$ largest components are all approximately the same size
3. Almost all components are trees
4. $\alpha = c - 1 - \log c > 0$ for $c < 1$

# Construction / Recognition

Not applicable -- this is a regime description.

# Context & Application

The subcritical regime is the "quiet" phase of random graph evolution. The component structure grows steadily: tree components of order $k$ appear when $t \sim n^{(k-1)/k}$ (Theorem 16). No dramatic changes occur until $t$ approaches $n/2$.

# Examples

**Example** (p. 247): For $c = 0.9$, $\alpha = 0.9 - 1 - \log 0.9 \approx 0.0053$, so largest components have order about $189\log n$.

# Relationships

## Builds Upon
- **Phase transition** -- This is the subcritical phase

## Enables
- Understanding of pre-transition behavior

## Related
- **Critical window** -- The boundary at $c = 1$
- **Supercritical regime** -- The contrasting regime $c > 1$

## Contrasts With
- **Supercritical regime** -- Has a giant component; subcritical does not

# Common Errors

- **Error**: Thinking the subcritical regime has only isolated vertices
  **Correction**: Components grow to $O(\log n)$; isolated vertices disappear early

# Common Confusions

- **Confusion**: Thinking all components are exactly the same size
  **Clarification**: They are approximately equal (within $\omega(n)$ of each other), not exactly equal

# Source Reference

Chapter VII: Random Graphs, Section VII.5, Theorem 17(i), page 247.

# Verification Notes

- Definition source: Direct from Theorem 17(i)
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
