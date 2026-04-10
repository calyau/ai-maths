---
concept: Inverse Temperature
slug: inverse-temperature
category: statistical-mechanics
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 350
section: "X.3 The Tutte Polynomial in Statistical Mechanics"
extraction_confidence: high
aliases:
  - "beta"
  - "1/k_B T"
prerequisites: []
extends: []
related:
  - potts-model
  - partition-function-potts-model
  - phase-transition-statistical-mechanics
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial relate to statistical mechanics?"
---

# Quick Definition
The inverse temperature $\beta = 1/(k_B T)$ controls the Potts model: high $\beta$ (low temperature) favours ordered states; low $\beta$ (high temperature) makes all states nearly equiprobable.

# Core Definition
"$k_B$ is the Boltzmann constant ($1.38 \times 10^{-23}$ joules/Kelvin), $T$ is the temperature of the system, and $\beta$ is the inverse temperature" (Bollobás, p. 350). The Potts measure is $\mu(\omega) = e^{-\beta H(\omega)}$, and $v = e^\beta - 1$ appears in the dichromatic polynomial.

# Prerequisites
Foundational for statistical mechanics context.

# Key Properties
1. $\beta \to 0$ (high temperature): all states nearly equiprobable
2. $\beta \to \infty$ (low temperature): ground states dominate
3. $v = e^\beta - 1$ connects to the dichromatic polynomial

# Relationships
## Related
- **potts-model**, **partition-function-potts-model**, **phase-transition-statistical-mechanics**

# Source Reference
Chapter X, Section X.3, page 350.

# Verification Notes
- Definition source: Direct from p. 350
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
