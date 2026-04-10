---
# === CORE IDENTIFICATION ===
concept: Critical Window
slug: critical-window

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
aliases:
  - critical regime

# === TYPED RELATIONSHIPS ===
prerequisites:
  - phase-transition
extends: []
related:
  - subcritical-regime
  - supercritical-regime
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens at the critical point of the phase transition?"
---

# Quick Definition

At the critical point $t = \lfloor n/2 \rfloor$ (equivalently $c = 1$), the largest components of $G_t$ have order $\Theta(n^{2/3})$, intermediate between the subcritical $O(\log n)$ and supercritical $\Theta(n)$.

# Core Definition

**Theorem 17(ii)** (Bollobas, p. 247): There exist constants $0 < c_1 < c_2$ such that $c_1 n^{2/3} < L^{(i)}(G_{\lfloor n/2 \rfloor}) < c_2 n^{2/3}$ for every fixed $i$ and a.e. $G_{\lfloor n/2 \rfloor}$. Furthermore, the second largest component never exceeds $n^{2/3+\varepsilon}$ at any time.

# Prerequisites

- **Phase transition** -- The critical window is the midpoint

# Key Properties

1. Component sizes are $\Theta(n^{2/3})$ -- intermediate scaling
2. Several large components coexist (unlike the supercritical case)
3. The transition window has width $O(n^{2/3})$ around $t = n/2$
4. The second largest component never exceeds $n^{2/3+\varepsilon}$ throughout the process

# Construction / Recognition

Not applicable -- this is a regime description.

# Context & Application

The critical window was studied in detail by Bollobas (1984) and Janson-Knuth-Luczak-Pittel (1993). It is the most delicate part of the phase transition, where the component structure transitions from many small components to one giant component.

# Examples

**Example** (p. 249): For $t = n/2 + s$ with $s/n^{2/3} \to \infty$: $L^{(1)} = 4s + o(s)$, showing the giant component grows at rate 4 per edge added.

# Relationships

## Builds Upon
- **Phase transition** -- The critical point

## Enables
- Understanding of the scaling window

## Related
- **Subcritical regime** -- The phase before
- **Supercritical regime** -- The phase after

## Contrasts With
- None

# Common Errors

- **Error**: Thinking the critical window has zero width
  **Correction**: The scaling window has width $\Theta(n^{2/3})$ around the critical point

# Common Confusions

- **Confusion**: Thinking a unique giant component exists at the critical point
  **Clarification**: At $c = 1$, multiple components of size $\Theta(n^{2/3})$ coexist

# Source Reference

Chapter VII: Random Graphs, Section VII.5, Theorem 17(ii), pages 247, 249.

# Verification Notes

- Definition source: Direct from Theorem 17(ii)
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
