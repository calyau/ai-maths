---
# === CORE IDENTIFICATION ===
concept: Component Gap
slug: component-gap

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
pdf_page: 249
section: "VII.5 The Phase Transition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supercritical-regime
extends: []
related:
  - giant-component
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is there a gap in component sizes in the supercritical regime?"
---

# Quick Definition

In the supercritical regime, there is a gap in component orders: no component has order between $\Theta(\log n)$ and $\Theta(n)$. Components are either "small" ($\le \alpha\log n$) or "large" ($\ge \beta n$).

# Core Definition

**Theorem 18** (Bollobas, p. 249): If $p = (1+\varepsilon)/n$ with $\varepsilon < 1/3$, then with probability at least $1 - n^{-a}$, no component has order $k$ with $\frac{8a}{\varepsilon^2}\log n \le k \le \frac{\varepsilon^2}{12}n$. This gap persists and grows as $\varepsilon$ increases, eventually separating the unique giant component from all small components.

# Prerequisites

- **Supercritical regime** -- The context for the gap

# Key Properties

1. The gap grows with $\varepsilon = c - 1$
2. Small components have $\le \alpha\log n$ vertices
3. Large components have $\ge \beta n$ vertices
4. The gap implies that adding an edge between two small components cannot create a large component
5. This structural insight leads to the uniqueness of the giant component

# Construction / Recognition

Not applicable -- this is a structural property.

# Context & Application

The component gap is the key structural insight behind the proof of Theorem 17(iii). It shows that small components cannot merge into a medium-sized component; they remain small. Large components, when they merge, form the unique giant component.

# Examples

**Example** (p. 252): For $\varepsilon_1 < \varepsilon_2 < 1/3$, there exist $\alpha, \beta > 0$ such that for $(1+\varepsilon_1)n/2 \le t \le (1+\varepsilon_2)n/2$, every component of $G_t$ is either small ($\le \alpha\log n$) or large ($\ge \beta n$).

# Relationships

## Builds Upon
- **Supercritical regime** -- The regime where the gap exists

## Enables
- Uniqueness proof for the giant component

## Related
- **Giant component** -- The large side of the gap

## Contrasts With
- None

# Common Errors

- **Error**: Thinking the gap exists at the critical point $c = 1$
  **Correction**: At $c = 1$, components have order $\Theta(n^{2/3})$, which is intermediate; the gap appears for $c > 1$

# Common Confusions

- **Confusion**: Thinking the gap means there are only two component sizes
  **Clarification**: Small components have a distribution of sizes up to $O(\log n)$; the gap is between $O(\log n)$ and $\Theta(n)$

# Source Reference

Chapter VII: Random Graphs, Section VII.5, Theorem 18, pages 249--252.

# Verification Notes

- Definition source: Direct from Theorem 18
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
