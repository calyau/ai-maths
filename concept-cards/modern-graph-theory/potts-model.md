---
concept: Potts Model
slug: potts-model
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
  - "q-state Potts model"
prerequisites:
  - tutte-polynomial
  - dichromatic-polynomial
extends: []
related:
  - ising-model
  - random-cluster-model
  - partition-function-potts-model
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial relate to statistical mechanics?"
---

# Quick Definition
The $q$-state Potts model on a multigraph $G = (V, E)$ assigns to each vertex a spin from $\{1, \ldots, q\}$, with probability proportional to $e^{-\beta H(\omega)}$, where $H(\omega) = \sum_{ab \in E}(1 - \delta(\omega_a, \omega_b))$ counts disagreeing edges and $\beta$ is inverse temperature.

# Core Definition
A state $\omega: V \to [q]$ assigns a spin $\omega_a$ to each vertex $a$. The Hamiltonian is $H(\omega) = \sum_{ab \in E}(1 - \delta(\omega_a, \omega_b))$. The Potts measure is $\mu_G^{q,\beta}(\omega) = e^{-\beta H(\omega)}$, and the partition function is $P_G(q,\beta) = \sum_{\omega} e^{-\beta H(\omega)}$ (Bollobás, pp. 349-350). By Theorem 3: $P_G(q,\beta) = e^{-\beta|E|} Z_G(q, e^\beta - 1)$.

# Prerequisites
- **Tutte polynomial** — The partition function is a transform of it
- **Dichromatic polynomial** — $P_G = e^{-\beta|E|} Z_G(q, v)$ where $v = e^\beta - 1$

# Key Properties
1. $q$ is a positive integer (number of spin states)
2. $H(\omega)$ counts edges where adjacent vertices have different spins
3. At high temperature ($\beta \to 0$): all states roughly equiprobable
4. At low temperature ($\beta \to \infty$): states minimizing $H$ dominate
5. Phase transition: structure changes suddenly at a critical temperature

# Context & Application
"In statistical mechanics we wish to study random disordered systems, especially in the neighbourhood of their phase transitions" (p. 349). The partition function is the normalizing constant for the probability measure.

# Examples
**Example**: For $q = 2$: the Ising model (special case).

# Relationships
## Builds Upon
- **tutte-polynomial**, **dichromatic-polynomial**

## Enables
- **partition-function-potts-model**

## Related
- **ising-model** — The case $q = 2$
- **random-cluster-model** — Generalization by Fortuin-Kasteleyn

# Source Reference
Chapter X, Section X.3, Theorem 3, pages 349-350.

# Verification Notes
- Definition source: Direct from pp. 349-350
- Confidence rationale: Explicit definition and theorem
- Uncertainties: None
- Cross-reference status: Verified
