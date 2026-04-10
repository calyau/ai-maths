---
concept: Discrete Poincaré Inequality
slug: discrete-poincare-inequality
category: conductance-and-mixing
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 323
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "Lemma 29"
prerequisites:
  - conductance-of-graph
extends: []
related:
  - conductance-bound-on-eigenvalue
  - spectral-gap-and-mixing
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
Lemma 29 states that for a $d$-regular graph with conductance $\Phi_G$ and any function $x: V \to \mathbb{R}$ with $\sum x_i = 0$: $\sum_{ij \in E}(x_i - x_j)^2 \geq \frac{d}{2}\Phi_G^2 \sum x_i^2$.

# Core Definition
Lemma 29 (p. 323): "Let $G = (V, E)$ be a $d$-regular graph with conductance $\Phi_G$, and let $x: V \to \mathbb{R}$, $i \mapsto x_i$, be such that $\sum_{i=1}^n x_i = 0$. Then $\sum_{ij \in E}(x_i - x_j)^2 \geq \frac{d}{2}\Phi_G^2 \sum_{i=1}^n x_i^2$."

# Prerequisites
- **Conductance of a graph** — Appears in the inequality

# Key Properties
1. Links edge differences to total variance via conductance
2. Proved via Cauchy-Schwarz and definition of conductance
3. Key lemma for Theorem 27 (conductance bounds mixing rate)
4. Discrete analogue of the Poincaré inequality in analysis

# Relationships
## Builds Upon
- **conductance-of-graph**

## Enables
- **conductance-bound-on-eigenvalue** — Theorem 27

## Related
- **spectral-gap-and-mixing** — Algebraic consequence

# Source Reference
Chapter IX, Section IX.4, Lemma 29, pages 323-325.

# Verification Notes
- Definition source: Direct from Lemma 29
- Confidence rationale: Explicit lemma with proof
- Uncertainties: None
- Cross-reference status: Verified
