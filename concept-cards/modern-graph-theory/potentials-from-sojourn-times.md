---
concept: Potentials from Sojourn Times
slug: potentials-from-sojourn-times
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 305
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases:
  - "Theorem 9"
prerequisites:
  - sojourn-time
  - absolute-potential
  - effective-resistance
extends: []
related:
  - escape-probability
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
Theorem 9 states that $V_x = S_x(s \to t)/C_x$ gives the absolute potentials for a unit current from $s$ to $t$, and the current in edge $xy$ equals the expected net traversals $E_{xy}$ in a random walk from $s$ to $t$.

# Core Definition
Theorem 9 (p. 305): Setting $V_x = S_x(s \to t)/C_x$, the distribution $(V_x)$ gives absolute potentials with $V_s = R_{\text{eff}}(s,t)$ and $V_t = 0$. The current in edge $xy$ is $E_{xy} = S_x P_{xy} - S_y P_{yx}$, the expected net traversals.

# Prerequisites
- **Sojourn time**, **absolute-potential**, **effective-resistance**

# Key Properties
1. $V_x = S_x(s \to t)/C_x$ gives potentials
2. $R_{\text{eff}}(s,t) = S_s(s \to t)/C_s$ (equation (13))
3. Current in edge = expected net traversals
4. Total current from $s$ to $t$ is exactly 1

# Relationships
## Builds Upon
- **sojourn-time**, **absolute-potential**, **effective-resistance**

## Related
- **escape-probability** — $P_{\text{esc}} = 1/S_s$

# Source Reference
Chapter IX, Section IX.2, Theorem 9, pages 305-306.

# Verification Notes
- Definition source: Direct from Theorem 9
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
