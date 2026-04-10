---
concept: Phase Transition in Statistical Mechanics
slug: phase-transition-statistical-mechanics
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
extraction_confidence: medium
aliases: []
prerequisites:
  - potts-model
  - partition-function-potts-model
extends: []
related:
  - random-cluster-model
  - phase-transition
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial relate to statistical mechanics?"
---

# Quick Definition
In the Potts model, a phase transition occurs when the structure of a typical configuration changes suddenly at a critical temperature, analogous to the emergence of the giant component in random graphs.

# Core Definition
"Much of our interest in the system is due to the fact that the structure of a 'typical' system changes suddenly as the temperature passes through a certain critical value. This phase transition is reminiscent of the phenomenon in the evolution of random graphs" (Bollobás, p. 350).

# Prerequisites
- **Potts model** — The model exhibiting phase transitions
- **Partition function of the Potts model** — Encodes thermodynamic behaviour

# Key Properties
1. High temperature ($\beta \to 0$): all states approximately equiprobable
2. Low temperature ($\beta \to \infty$): states minimizing $H$ dominate
3. Critical temperature: sharp change in typical behaviour
4. Analogous to giant component threshold in random graphs

# Relationships
## Builds Upon
- **potts-model**, **partition-function-potts-model**

## Related
- **random-cluster-model**, **phase-transition** (random graphs analogue)

# Source Reference
Chapter X, Section X.3, page 350.

# Verification Notes
- Definition source: Direct from p. 350
- Confidence rationale: Medium -- informal description
- Uncertainties: No rigorous definition of critical temperature given
- Cross-reference status: Verified
