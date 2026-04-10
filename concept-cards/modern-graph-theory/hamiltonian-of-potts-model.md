---
concept: Hamiltonian of the Potts Model
slug: hamiltonian-of-potts-model
category: statistical-mechanics
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 349
section: "X.3 The Tutte Polynomial in Statistical Mechanics"
extraction_confidence: high
aliases:
  - "H(omega)"
  - "energy function"
prerequisites:
  - potts-model
extends: []
related:
  - partition-function-potts-model
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial relate to statistical mechanics?"
---

# Quick Definition
The Hamiltonian $H(\omega) = \sum_{ab \in E}(1 - \delta(\omega_a, \omega_b))$ of a state $\omega$ in the Potts model counts the number of edges whose endpoints have different spins.

# Core Definition
"The Hamiltonian $H(\omega)$ of a state $\omega$: $H(\omega) = \sum_{ab \in E}(1 - \delta(\omega_a, \omega_b))$" (Bollobás, p. 349). The Potts measure is $\mu(\omega) = e^{-\beta H(\omega)}$, so states with lower Hamiltonian (more agreement) have higher probability.

# Prerequisites
- **Potts model** — The Hamiltonian is part of its definition

# Key Properties
1. $H(\omega) \geq 0$ always
2. $H(\omega) = 0$ iff all spins agree (all vertices same colour)
3. $H(\omega) = |E|$ iff no adjacent vertices agree
4. For proper colourings: $H(\omega) = |E|$

# Relationships
## Builds Upon
- **potts-model**

## Enables
- **partition-function-potts-model** — $P_G = \sum_\omega e^{-\beta H(\omega)}$

# Source Reference
Chapter X, Section X.3, page 349.

# Verification Notes
- Definition source: Direct from p. 349
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified
