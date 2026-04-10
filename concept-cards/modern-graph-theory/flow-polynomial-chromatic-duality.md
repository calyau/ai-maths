---
concept: Flow-Chromatic Duality
slug: flow-polynomial-chromatic-duality
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
  - chromatic-polynomial-from-tutte
extends: []
related:
  - five-flow-conjecture
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
For a connected plane graph $G$ with dual $G^*$: $p_G(x) = q_{G^*}(x) \cdot x^{k(G)}$ and $T_{G^*}(x,y) = T_G(y,x)$. The flow polynomial is the "dual of the chromatic polynomial."

# Core Definition
"It is natural to consider the flow polynomial as the dual of the chromatic polynomial" (Bollobás, p. 355). For plane graphs: $p_G(x) = q_{G^*}(x) x^{k(G)}$ (Exercise 16) and $T_{G^*}(x,y) = T_G(y,x)$ (Exercise 15). The four colour theorem is equivalent to every bridgeless planar graph having a nowhere-zero 4-flow.

# Prerequisites
- **Flow polynomial** — One side of the duality
- **Chromatic polynomial from Tutte** — The other side

# Key Properties
1. $T_{G^*}(x,y) = T_G(y,x)$ for plane graph $G$ with dual $G^*$
2. $p_G(x) = q_{G^*}(x) x^{k(G)}$ for connected plane $G$
3. Four colour theorem $\Leftrightarrow$ every bridgeless planar graph has nowhere-zero 4-flow

# Relationships
## Builds Upon
- **flow-polynomial**, **chromatic-polynomial-from-tutte**

## Related
- **five-flow-conjecture** — Extends duality beyond planar graphs

# Source Reference
Chapter X, Section X.4, page 355. Exercises 15-17.

# Verification Notes
- Definition source: Direct from p. 355 and Exercises 15-16
- Confidence rationale: Explicit statement with exercises
- Uncertainties: None
- Cross-reference status: Verified
