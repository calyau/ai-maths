---
concept: Absolute Potential
slug: absolute-potential
category: electrical-networks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 298
section: "IX.1 Electrical Networks Revisited"
extraction_confidence: high
aliases:
  - "V_x"
  - "potential function"
prerequisites:
  - effective-resistance
extends: []
related:
  - harmonic-function-on-graph
  - dirichlets-principle
  - escape-probability
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
The absolute potential $V_x$ at vertex $x$ in an electrical network is a function satisfying $p_{xy} = V_x - V_y$ (potential difference) for each edge $xy$, well-defined whenever Kirchhoff's potential law holds.

# Core Definition
"KPL is equivalent to the possibility of defining an absolute potential $V_x$ for every vertex $x$ such that $p_{xy} = V_x - V_y$ for each edge $xy$" (Bollobás, p. 298). The potential function is harmonic at non-outlet vertices (equation (4)): $C_x V_x = \sum_{y \in \Gamma(x)} c_{xy} V_y$.

# Prerequisites
- **Effective resistance** — Potentials determine and are determined by resistances

# Key Properties
1. $p_{xy} = V_x - V_y$ for every edge $xy$
2. Harmonic at non-outlet vertices: $V_x = \frac{1}{C_x}\sum c_{xy} V_y$
3. By Theorem 8: $V_x = \mathbb{P}_x(\text{reaching } s \text{ before } t)$ when $V_s = 1, V_t = 0$
4. By Theorem 9: $V_x = S_x(s \to t)/C_x$ for unit current

# Relationships
## Builds Upon
- **effective-resistance**

## Related
- **harmonic-function-on-graph** — Potentials are harmonic
- **escape-probability** — Potentials equal hitting probabilities

# Source Reference
Chapter IX, Section IX.1, pages 298-299. Theorems 8-9.

# Verification Notes
- Definition source: Direct from p. 298
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
