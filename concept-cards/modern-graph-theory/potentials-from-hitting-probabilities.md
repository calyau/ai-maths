---
concept: Potentials from Hitting Probabilities
slug: potentials-from-hitting-probabilities
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 304
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases:
  - "Theorem 8"
prerequisites:
  - escape-probability
  - absolute-potential
  - harmonic-function-on-graph
extends: []
related:
  - potentials-from-sojourn-times
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
Theorem 8 states that $V_x = \mathbb{P}_x(\text{reaching } s \text{ before } t)$ gives absolute potentials when $s$ is set at 1 and $t$ at 0, and $C_{\text{eff}}(s,t) = C_s P_{\text{esc}}(s \to t)$.

# Core Definition
Theorem 8 (p. 304): Define $V_x = \mathbb{P}(\text{starting at } x, \text{ reaching } s \text{ before } t)$. Then $V_s = 1$, $V_t = 0$, and $(V_x)$ gives absolute potentials with $s$ at 1 and $t$ at 0. The total current is $C_{\text{eff}}(s,t) = C_s P_{\text{esc}}(s \to t)$.

# Prerequisites
- **Escape probability**, **absolute-potential**, **harmonic-function-on-graph**

# Key Properties
1. Hitting probabilities = absolute potentials
2. $C_{\text{eff}}(s,t) = C_s P_{\text{esc}}(s \to t)$ (equation (11))
3. $P_{\text{esc}}(s \to t)/P_{\text{esc}}(t \to s) = C_t/C_s$ (equation (12))

# Relationships
## Builds Upon
- **escape-probability**, **absolute-potential**, **harmonic-function-on-graph**

## Related
- **potentials-from-sojourn-times** — Alternative expression via Theorem 9

# Source Reference
Chapter IX, Section IX.2, Theorem 8, pages 304-305.

# Verification Notes
- Definition source: Direct from Theorem 8
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
