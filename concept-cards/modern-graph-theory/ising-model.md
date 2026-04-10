---
concept: Ising Model
slug: ising-model
category: statistical-mechanics
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 351
section: "X.3 The Tutte Polynomial in Statistical Mechanics"
extraction_confidence: high
aliases: []
prerequisites:
  - potts-model
extends: []
related:
  - partition-function-potts-model
  - random-cluster-model
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial relate to statistical mechanics?"
---

# Quick Definition
The Ising model is the Potts model with $q = 2$: each vertex has spin $+1$ or $-1$, with energy penalizing disagreeing adjacent spins. Its partition function is a special case of the dichromatic polynomial.

# Core Definition
"The Potts model is a generalization of the Ising model, which is just the case $q = 2$" (Bollobás, p. 351). Spins take values in $\{1, 2\}$, and the Hamiltonian counts disagreeing edges.

# Prerequisites
- **Potts model** — The Ising model is the case $q = 2$

# Key Properties
1. Two spin states: $\omega_a \in \{+1, -1\}$ (or $\{1, 2\}$)
2. $H(\omega) = \sum_{ab \in E}(1 - \delta(\omega_a, \omega_b))$
3. Partition function: $P_G(2, \beta) = e^{-\beta|E|} Z_G(2, e^\beta - 1)$
4. The most-studied model in statistical mechanics

# Context & Application
The Ising model is the simplest nontrivial model of ferromagnetism and the prototype for all phase transition phenomena. Bollobás mentions it as the foundational special case that the Potts model generalizes.

# Relationships
## Builds Upon
- **potts-model** — Special case $q = 2$

## Related
- **partition-function-potts-model**, **random-cluster-model**

# Source Reference
Chapter X, Section X.3, page 351.

# Verification Notes
- Definition source: Direct from p. 351
- Confidence rationale: Explicit identification as $q = 2$ Potts model
- Uncertainties: None
- Cross-reference status: Verified
