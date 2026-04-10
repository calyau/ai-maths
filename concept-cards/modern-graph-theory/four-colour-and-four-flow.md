---
concept: Four-Colour Theorem and Four-Flow
slug: four-colour-and-four-flow
category: tutte-polynomial
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 355
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - flow-polynomial
  - flow-polynomial-chromatic-duality
extends: []
related:
  - five-flow-conjecture
  - chromatic-polynomial-from-tutte
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
The four colour theorem is equivalent to the assertion that every bridgeless planar graph has a nowhere-zero 4-flow, connecting graph colouring to flows via the Tutte polynomial and planar duality.

# Core Definition
"The four colour theorem is equivalent to the fact that every bridgeless planar graph has a nowhere-zero 4-flow" (Bollobás, p. 355). This follows from flow-chromatic duality: for a connected plane graph $G$ with dual $G^*$, $p_G(x) = q_{G^*}(x) x^{k(G)}$.

# Prerequisites
- **Flow polynomial** — Counts nowhere-zero flows
- **Flow-chromatic duality** — Connects colouring and flows

# Key Properties
1. 4-colourability of planar graphs $\Leftrightarrow$ 4-flows for bridgeless planar graphs
2. Hadwiger's conjecture (colourings) $\Leftrightarrow$ Tutte's 5-flow conjecture for general graphs
3. "It is natural to consider the flow polynomial as the dual of the chromatic polynomial" (p. 355)

# Relationships
## Builds Upon
- **flow-polynomial**, **flow-polynomial-chromatic-duality**

## Related
- **five-flow-conjecture** — Extension to non-planar graphs
- **chromatic-polynomial-from-tutte** — Dual perspective

# Source Reference
Chapter X, Section X.4, page 355. Exercise 17.

# Verification Notes
- Definition source: Direct from p. 355
- Confidence rationale: Explicit equivalence
- Uncertainties: None
- Cross-reference status: Verified
