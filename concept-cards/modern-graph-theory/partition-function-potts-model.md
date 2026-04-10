---
concept: Partition Function of the Potts Model
slug: partition-function-potts-model
category: statistical-mechanics
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 350
section: "X.3 The Tutte Polynomial in Statistical Mechanics"
extraction_confidence: high
aliases:
  - "P_G(q, beta)"
prerequisites:
  - potts-model
  - dichromatic-polynomial
extends: []
related:
  - random-cluster-model
  - tutte-polynomial
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial relate to statistical mechanics?"
---

# Quick Definition
The partition function $P_G(q, \beta) = \sum_\omega e^{-\beta H(\omega)}$ normalizes the Potts measure and equals $e^{-\beta|E|} Z_G(q, e^\beta - 1)$, a simple transform of the dichromatic (and hence Tutte) polynomial.

# Core Definition
Theorem 3 (p. 350): "The partition function of the $q$-state Potts model on $G$, with inverse temperature $\beta$, is $P_G(q, \beta) = e^{-\beta|E|} Z_G(q, v)$ where $v = e^\beta - 1$."

# Prerequisites
- **Potts model** — The statistical mechanics model
- **Dichromatic polynomial** — $Z_G$ appears in the formula

# Key Properties
1. $P_G(q,\beta) = e^{-\beta|E|} Z_G(q, e^\beta - 1)$
2. Normalizes the Potts measure to a probability distribution
3. Can be expressed in terms of the Tutte polynomial
4. Encodes thermodynamic properties of the system

# Context & Application
The partition function is central to statistical mechanics: "the total measure of the space (and so our normalizing factor) is the partition function" (p. 349). Its computation reduces to evaluating the Tutte polynomial.

# Examples
**Example**: The proof rewrites $\tilde{P}_G = \sum_\omega \prod_{ab \in E}(1 + v\delta(\omega_a, \omega_b))$ and verifies the deletion-contraction recursion.

# Relationships
## Builds Upon
- **potts-model**, **dichromatic-polynomial**

## Related
- **tutte-polynomial** — Partition function is a transform of it
- **random-cluster-model** — Related partition function

# Source Reference
Chapter X, Section X.3, Theorem 3, page 350.

# Verification Notes
- Definition source: Direct from Theorem 3
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
